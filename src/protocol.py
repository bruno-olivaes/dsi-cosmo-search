"""Protocolo radix-agnostic v2.1 — 3 estágios com BIC e bootstrap correto."""
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import lombscargle
from .likelihood import gaussian_loglike


def _detrend_polynomial(u, y, deg=3):
    coeffs = np.polyfit(u, y, deg)
    return y - np.polyval(coeffs, u)


def stage1_detection(k, residuals):
    u = np.log(k); u = u - u.mean()
    y = residuals - residuals.mean()
    u_span = u.max() - u.min()
    omega_min = 2.0 * np.pi / u_span
    du_med = np.median(np.diff(np.sort(u)))
    omega_max = 2.0 * np.pi / (10.0 * du_med)
    omega_grid = np.logspace(np.log10(omega_min), np.log10(omega_max), 5000)
    power = lombscargle(u, y, omega_grid, normalize=True)
    idx = int(np.argmax(power))
    return float(omega_grid[idx]), float(power[idx])


def _sinusoid(u, amp, omega, phi):
    return amp * np.cos(omega * u + phi)


def stage2_refinement(k, residuals, omega_peak):
    u = np.log(k); u = u - u.mean()
    y = residuals - residuals.mean()
    p0 = [np.std(y), omega_peak, 0.0]
    bounds = ([0.0, omega_peak * 0.5, -np.pi], [np.inf, omega_peak * 1.5, np.pi])
    try:
        popt, pcov = curve_fit(_sinusoid, u, y, p0=p0, bounds=bounds, maxfev=20000)
    except Exception:
        return None
    amp, omega, phi = popt
    perr = np.sqrt(np.diag(pcov))
    sigma_omega = float(perr[1])
    ln_lambda_hat = 2.0 * np.pi / omega
    sigma_ln_lambda = ln_lambda_hat * sigma_omega / omega
    lambda_hat = float(np.exp(ln_lambda_hat))
    return {
        'amp': float(amp), 'omega': float(omega), 'phi': float(phi),
        'sigma_omega': sigma_omega,
        'lambda_hat': lambda_hat,
        'sigma_lambda': float(lambda_hat * sigma_ln_lambda),
        'rel_err_lambda': float(sigma_ln_lambda),
    }


def _scramble_phases(u, y, rng):
    u_grid = np.linspace(u.min(), u.max(), len(u))
    y_uniform = np.interp(u_grid, u, y)
    F = np.fft.rfft(y_uniform)
    phases = rng.uniform(0.0, 2.0 * np.pi, len(F))
    F_scram = np.abs(F) * np.exp(1j * phases)
    y_scram_uniform = np.fft.irfft(F_scram, n=len(u_grid))
    return np.interp(u, u_grid, y_scram_uniform)


def stage3_certify(k, residuals, stage2, n_bootstrap=1000, rng=None):
    if rng is None:
        rng = np.random.default_rng(42)
    u = np.log(k); u = u - u.mean()
    u_span = u.max() - u.min()
    omega = stage2['omega']

    gate_resolvable = bool(omega >= 2.0 * np.pi / u_span)

    y = residuals - residuals.mean()
    noise = float(np.std(y))
    gate_amplitude = bool(abs(stage2['amp']) >= noise)
    gate_precision = bool(stage2['rel_err_lambda'] < 0.10)

    max_powers = np.zeros(n_bootstrap)
    for i in range(n_bootstrap):
        y_scram = _scramble_phases(u, y, rng)
        omega_grid = np.linspace(omega * 0.5, omega * 1.5, 500)
        max_powers[i] = float(np.max(
            lombscargle(u, y_scram - y_scram.mean(), omega_grid, normalize=True)
        ))
    power_obs = float(np.atleast_1d(lombscargle(u, y, np.array([omega]), normalize=True))[0])
    p_corrected = float(np.mean(max_powers >= power_obs))
    gate_plevel = bool(p_corrected < 0.05)

    return {
        'gate_resolvable': gate_resolvable,
        'gate_amplitude': gate_amplitude,
        'gate_precision': gate_precision,
        'gate_plevel': gate_plevel,
        'power_observed': power_obs,
        'p_corrected': p_corrected,
    }


def _bic_gate(k, residuals, stage2, cov):
    u = np.log(k); u = u - u.mean()
    y = residuals - residuals.mean()
    null_model = np.zeros_like(y)
    dsi_model = stage2['amp'] * np.cos(stage2['omega'] * u + stage2['phi'])
    ll_null = gaussian_loglike(null_model, y, cov)
    ll_dsi = gaussian_loglike(dsi_model, y, cov)
    n = len(k)
    bic_null = -2.0 * ll_null + 0 * np.log(n)
    bic_dsi = -2.0 * ll_dsi + 3 * np.log(n)
    delta_bic = float(bic_null - bic_dsi)
    return delta_bic, bool(delta_bic > 10.0)


def run_protocol(k, residuals, cov=None, seed=42):
    rng = np.random.default_rng(seed)
    u = np.log(k)
    resid_dt = _detrend_polynomial(u, residuals, deg=3)

    omega_peak, power_peak = stage1_detection(k, resid_dt)
    s2 = stage2_refinement(k, resid_dt, omega_peak)
    if s2 is None:
        return {'certified': False, 'reason': 'stage2_failed',
                'stage1': {'omega_peak': omega_peak, 'power_peak': power_peak}}

    s3 = stage3_certify(k, resid_dt, s2, rng=rng)

    if cov is not None and s3['gate_resolvable'] and s3['gate_amplitude'] and s3['gate_precision']:
        delta_bic, gate_bic = _bic_gate(k, resid_dt, s2, cov)
    else:
        delta_bic, gate_bic = float('nan'), False

    s3['delta_bic'] = delta_bic
    s3['gate_bic'] = gate_bic
    certified = bool(
        s3['gate_resolvable'] and s3['gate_amplitude']
        and s3['gate_precision'] and s3['gate_plevel'] and s3['gate_bic']
    )
    s3['certified'] = certified

    return {
        'stage1': {'omega_peak': omega_peak, 'power_peak': power_peak},
        'stage2': s2,
        'stage3': s3,
        'certified': certified,
    }

