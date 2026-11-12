"""
Generate 4 Instagram Arts (1080x1080) for Scientific Launch
Bruno Luçardo Olivaes
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

out_dirs = [
    r"C:\Users\bruno\projects\dsi-cosmo-search\instagram_assets",
    r"C:\Users\bruno\Desktop\Publicacao_Artigos_Academia\instagram_assets",
    r"C:\Users\bruno\projects\bruno-olivaes.github.io\assets\instagram"
]

for d in out_dirs:
    os.makedirs(d, exist_ok=True)

# Common styling
BG_DARK = "#090d16"
ACCENT_BLUE = "#3b82f6"
ACCENT_CYAN = "#38bdf8"
ACCENT_GOLD = "#fbbf24"
ACCENT_RED = "#f87171"
TEXT_WHITE = "#ffffff"
TEXT_MUTED = "#94a3b8"

# -------------------------------------------------------------------------
# ARTE 1: Paper 7 (LHC NSBI - 9.5x mais sensível)
# -------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.2, 7.2), dpi=150, facecolor=BG_DARK)
ax.set_facecolor(BG_DARK)

# Background grid lines
for g in np.linspace(0, 1, 11):
    ax.axhline(g, color='#1e293b', lw=0.8, alpha=0.5, zorder=1)
    ax.axvline(g, color='#1e293b', lw=0.8, alpha=0.5, zorder=1)

# Bars
methods = ['Tradicional\n(Lomb-Scargle Binned)', 'Neural SBI\n(Unbinned PyTorch)']
limits = [0.552, 0.058]
colors = ['#ef4444', '#06b6d4']

bars = ax.bar([0.32, 0.68], limits, width=0.22, color=colors, edgecolor=['#f87171', '#38bdf8'], lw=2.5, zorder=3)

# Bar labels
ax.text(0.32, 0.552 + 0.03, r'$\varepsilon_{95} \leq 0.552$', ha='center', va='bottom', color='#fca5a5', fontsize=15, fontweight='bold')
ax.text(0.68, 0.058 + 0.03, r'$\varepsilon_{95} \leq 0.058$', ha='center', va='bottom', color='#67e8f9', fontsize=15, fontweight='bold')

# Multiplier callout badge
ax.annotate('9.5x MAIS\nSENSÍVEL', xy=(0.68, 0.16), xytext=(0.50, 0.38),
            arrowprops=dict(arrowstyle="->", color=ACCENT_GOLD, lw=2.5, connectionstyle="arc3,rad=-0.2"),
            bbox=dict(boxstyle="round,pad=0.5", facecolor="#1e1b4b", edgecolor=ACCENT_GOLD, lw=2),
            ha='center', va='center', color=ACCENT_GOLD, fontsize=14, fontweight='bold', zorder=4)

ax.set_xlim(0.1, 0.9)
ax.set_ylim(0, 0.72)
ax.set_xticks([0.32, 0.68])
ax.set_xticklabels(methods, fontsize=12, color=TEXT_WHITE, fontweight='bold')
ax.tick_params(colors=TEXT_MUTED, labelsize=11)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#334155')
ax.spines['bottom'].set_color('#334155')

# Title & Subtitle inside plot
plt.title("QUEBRANDO A BARREIRA DO ZEPTOVERSO\nLimite Superior DSI no LHC (CERN Open Data CMS)",
          fontsize=14, color=TEXT_WHITE, fontweight='bold', pad=18)

# Footer note
plt.figtext(0.5, 0.03, "Paper 7 · Inferência Não-Binada · Zero Falsos Alarmes (ΔBIC = -23.2)",
            ha="center", fontsize=9, color=TEXT_MUTED, fontweight='semibold')

plt.tight_layout()
temp1 = r"C:\Users\bruno\projects\dsi-cosmo-search\temp_art1.png"
fig.savefig(temp1, dpi=150, facecolor=BG_DARK)
plt.close(fig)

# -------------------------------------------------------------------------
# ARTE 2: Paper 2 (Casimir AFM - O Fantasma de 583.5 nm)
# -------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.2, 7.2), dpi=150, facecolor=BG_DARK)
ax.set_facecolor(BG_DARK)

z = np.linspace(200, 1000, 300)
# Physical monotonic curve
p_true = 20 * (200/z)**4
# Spurious Runge wave
p_ghost = p_true + 1.8 * np.sin(2 * np.pi * (z - 200) / 383.5) * np.exp(-(z-400)**2 / (2*180**2))

ax.plot(z, p_true, color='#10b981', lw=3.0, label='Base Física Real: {1, z⁻⁴, z⁻⁵} (Ruído Branco)', zorder=3)
ax.plot(z, p_ghost, color='#f43f5e', lw=2.2, ls='--', label='Polinômio Cúbico / Spline (Runge Artifact)', zorder=2)

# Ghost annotation
ax.annotate('FALSO PICO ESPÚRIO\n"O Fantasma de 583.5 nm"\n(FAP ~ 10⁻⁴⁵ artificial)',
            xy=(420, 9.8), xytext=(650, 15.0),
            arrowprops=dict(arrowstyle="->", color='#f43f5e', lw=2.2),
            bbox=dict(boxstyle="round,pad=0.5", facecolor="#271018", edgecolor='#f43f5e', lw=1.8),
            ha='center', va='center', color='#fecdd3', fontsize=11, fontweight='bold')

ax.set_xlim(180, 1020)
ax.set_ylim(-2, 22)
ax.set_xlabel('Distância de Separação z (nm)', fontsize=12, color=TEXT_WHITE, fontweight='bold')
ax.set_ylabel('Pressão de Casimir Residual (mPa)', fontsize=12, color=TEXT_WHITE, fontweight='bold')
ax.tick_params(colors=TEXT_MUTED, labelsize=10)
ax.legend(loc='upper right', facecolor='#111827', edgecolor='#374151', labelcolor=TEXT_WHITE, fontsize=10)
for sp in ax.spines.values():
    sp.set_color('#334155')

plt.title("METROLOGIA EM FORÇAS DE VÁCUO (AFM / KPFM)\nComo Splines e Polinômios Criam Sinais Fantasmas",
          fontsize=14, color=TEXT_WHITE, fontweight='bold', pad=18)

plt.figtext(0.5, 0.03, "Paper 2 · Eliminação de Artefatos Metrológicos · Review of Scientific Instruments",
            ha="center", fontsize=9, color=TEXT_MUTED, fontweight='semibold')

plt.tight_layout()
temp2 = r"C:\Users\bruno\projects\dsi-cosmo-search\temp_art2.png"
fig.savefig(temp2, dpi=150, facecolor=BG_DARK)
plt.close(fig)

# -------------------------------------------------------------------------
# ARTE 3: Paper 3 (ESA Euclid - Quebra de Degenerescência)
# -------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.2, 7.2), dpi=150, facecolor=BG_DARK)
ax.set_facecolor(BG_DARK)

z_arr = np.linspace(0, 3.0, 300)
# CPL model w(z) = w0 + wa * z/(1+z)
w_cpl = -0.867 - 0.547 * (z_arr / (1 + z_arr))
# Oscillatory model
w_osc = -1.0 + 0.218 * np.sin((2*np.pi / 3.09) * np.log(1 / (1 + z_arr)) + 0.592)

ax.plot(z_arr, w_cpl, color='#38bdf8', lw=2.5, label='Modelo Linear CPL (w₀, wₐ)', zorder=3)
ax.plot(z_arr, w_osc, color='#a855f7', lw=2.5, label='Modelo Log-Oscilatório', zorder=3)
ax.axhline(-1, color='#64748b', lw=1.2, ls=':', label='Constante Cosmológica (ΛCDM: w = -1)')

# Degeneracy zone (low z)
ax.axvspan(0, 0.8, color='#334155', alpha=0.35, label='Zona Degenerada (Pantheon+ / DESI Hoje)')
# Euclid Breaking Zone
ax.axvspan(1.2, 2.5, color='#1e3a8a', alpha=0.45, label='Janela Euclid (Quebra a ≥ 3σ)')

ax.annotate('PONTO DE QUEBRA EUCLID\nΔw = +0.104 detectável\n(Precisão σ_H/H ~ 1.3%)',
            xy=(1.8, -1.22), xytext=(2.0, -0.65),
            arrowprops=dict(arrowstyle="->", color=ACCENT_GOLD, lw=2.0),
            bbox=dict(boxstyle="round,pad=0.5", facecolor="#1e1b4b", edgecolor=ACCENT_GOLD, lw=1.8),
            ha='center', va='center', color=ACCENT_GOLD, fontsize=11, fontweight='bold')

ax.set_xlim(0, 3.0)
ax.set_ylim(-1.6, -0.4)
ax.set_xlabel('Redshift Cosmológico z (Passado do Universo)', fontsize=12, color=TEXT_WHITE, fontweight='bold')
ax.set_ylabel('Equação de Estado da Energia Escura w(z)', fontsize=12, color=TEXT_WHITE, fontweight='bold')
ax.tick_params(colors=TEXT_MUTED, labelsize=10)
ax.legend(loc='lower left', facecolor='#111827', edgecolor='#374151', labelcolor=TEXT_WHITE, fontsize=9)
for sp in ax.spines.values():
    sp.set_color('#334155')

plt.title("ENERGIA ESCURA OSCILATÓRIA & ESA EUCLID\nA Quebra da Degenerescência Cósmica em 3 Anos",
          fontsize=14, color=TEXT_WHITE, fontweight='bold', pad=18)

plt.figtext(0.5, 0.03, "Paper 3 · Solução Exata de Friedmann & Matriz de Fisher · DOI: 10.5281/zenodo.24121691",
            ha="center", fontsize=9, color=TEXT_MUTED, fontweight='semibold')

plt.tight_layout()
temp3 = r"C:\Users\bruno\projects\dsi-cosmo-search\temp_art3.png"
fig.savefig(temp3, dpi=150, facecolor=BG_DARK)
plt.close(fig)

# -------------------------------------------------------------------------
# ARTE 4: Livro (Monografia Master) - Com capa renderizada
# -------------------------------------------------------------------------
cover_img_path = r"C:\Users\bruno\projects\dsi-cosmo-search\book_cover.png"
if os.path.exists(cover_img_path):
    cover = Image.open(cover_img_path)
    # Target 1080x1080
    art4 = Image.new("RGBA", (1080, 1080), BG_DARK)
    draw4 = ImageDraw.Draw(art4)

    # Resize cover to fit nicely
    cov_w, cov_h = 420, 630
    cover_resized = cover.resize((cov_w, cov_h), Image.Resampling.LANCZOS)
    
    # Position cover in upper-middle
    pos_x = (1080 - cov_w) // 2
    pos_y = 190
    
    # Outer glow / shadow
    shadow_box = [(pos_x - 12, pos_y - 12), (pos_x + cov_w + 12, pos_y + cov_h + 12)]
    draw4.rounded_rectangle(shadow_box, radius=16, outline="#3b82f6", width=3, fill="#0b1329")
    
    art4.paste(cover_resized, (pos_x, pos_y))
    
    try:
        f_top = ImageFont.truetype("arialbd.ttf", 40)
        f_sub = ImageFont.truetype("arial.ttf", 26)
        f_badge = ImageFont.truetype("arialbd.ttf", 30)
        f_doi = ImageFont.truetype("courbd.ttf", 28)
    except:
        f_top = ImageFont.load_default()
        f_sub = f_top
        f_badge = f_top
        f_doi = f_top

    def draw_c(d, txt, y, f, col):
        bb = d.textbbox((0, 0), txt, font=f)
        w = bb[2] - bb[0]
        d.text(((1080 - w)//2, y), txt, font=f, fill=col)

    draw_c(draw4, "A MONOGRAFIA MASTER UNIFICADA", 50, f_top, "#ffffff")
    draw_c(draw4, "The Matrioska Protocol · A Jornada Completa em 34 Páginas", 115, f_sub, "#93c5fd")
    
    draw_c(draw4, "7 ARTIGOS · 1 ARQUITETURA METROLÓGICA", 855, f_badge, "#fbbf24")
    
    # DOI Box
    draw4.rounded_rectangle([(180, 915), (900, 985)], radius=12, outline="#38bdf8", width=2, fill="#0f172a")
    draw_c(draw4, "DOI CERN / ZENODO: 10.5281/zenodo.24124702", 935, f_doi, "#38bdf8")
    
    draw_c(draw4, "Acesse a vitrine oficial: bruno-olivaes.github.io", 1015, f_sub, "#94a3b8")
    
    temp4 = r"C:\Users\bruno\projects\dsi-cosmo-search\temp_art4.png"
    art4.save(temp4, "PNG")

# Now resize & save all 4 to 1080x1080 in all destination folders
temp_files = [
    (temp1, "01_instagram_paper7_nsbi_9.5x.png"),
    (temp2, "02_instagram_paper2_casimir_fantasma.png"),
    (temp3, "03_instagram_paper3_euclid_degenerescencia.png"),
    (temp4, "04_instagram_livro_matrioska_protocol.png")
]

for src, name in temp_files:
    if os.path.exists(src):
        im = Image.open(src).convert("RGB")
        im_1080 = im.resize((1080, 1080), Image.Resampling.LANCZOS)
        for target_dir in out_dirs:
            dest = os.path.join(target_dir, name)
            im_1080.save(dest, "PNG", quality=95)
            print(f"Saved: {dest}")
        os.remove(src)

print("All Instagram assets generated successfully!")
