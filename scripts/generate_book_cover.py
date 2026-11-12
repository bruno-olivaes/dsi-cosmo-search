"""
Generate Official Book Cover for The Matrioska Protocol
Bruno Luçardo Olivaes
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# Output paths
paths = [
    r"C:\Users\bruno\projects\bruno-olivaes.github.io\assets\book_cover.png",
    r"C:\Users\bruno\Desktop\Publicacao_Artigos_Academia\book_cover.png",
    r"C:\Users\bruno\projects\dsi-cosmo-search\book_cover.png"
]

width = 1600
height = 2400

# Create base figure with matplotlib
fig = plt.figure(figsize=(width/200, height/200), dpi=200, facecolor='#060913')
ax = fig.add_axes([0, 0, 1, 1])
ax.set_facecolor('#060913')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.8, 1.8)
ax.axis('off')

# 1. Subtle Log-Periodic Nested Spirals & Concentric Geometric Rings (Matrioska Concept)
theta = np.linspace(0, 10 * np.pi, 2000)
# Log-periodic dilation factor lambda = 3
r = 0.05 * np.exp(0.11 * theta)
mask = r < 1.4
theta = theta[mask]
r = r[mask]

# Draw dual golden-cyan log spirals
x1 = r * np.cos(theta)
y1 = r * np.sin(theta) * 0.95 - 0.1
ax.plot(x1, y1, color='#1e3a8a', alpha=0.35, lw=1.8)
ax.plot(-x1, -y1, color='#0284c7', alpha=0.25, lw=1.2)

# Nested concentric scale circles (Matrioska scales)
radii = [0.15, 0.28, 0.48, 0.78, 1.15]
for idx, rad in enumerate(radii):
    circle = plt.Circle((0, -0.1), rad, color='#38bdf8', fill=False, lw=1.0, alpha=0.15 + idx*0.05, ls='--' if idx % 2 == 1 else '-')
    ax.add_patch(circle)

# Background subtle wave
x_wave = np.linspace(-1.2, 1.2, 500)
for w_idx in range(5):
    y_wave = -1.2 + 0.08 * w_idx + 0.03 * np.cos(15 * x_wave + w_idx)
    ax.plot(x_wave, y_wave, color='#1d4ed8', alpha=0.15, lw=1)

# Subtle particle dots / cosmological perturbation seeds
np.random.seed(42)
n_stars = 180
star_x = np.random.uniform(-1.1, 1.1, n_stars)
star_y = np.random.uniform(-1.7, 1.7, n_stars)
star_alpha = np.random.uniform(0.1, 0.6, n_stars)
star_s = np.random.uniform(0.5, 4.0, n_stars)
ax.scatter(star_x, star_y, s=star_s, c='#93c5fd', alpha=star_alpha, edgecolors='none')

# Border frame
rect = plt.Rectangle((-1.12, -1.72), 2.24, 3.44, fill=False, color='#2563eb', lw=2.0, alpha=0.6)
ax.add_patch(rect)
inner_rect = plt.Rectangle((-1.09, -1.69), 2.18, 3.38, fill=False, color='#fbbf24', lw=0.8, alpha=0.3)
ax.add_patch(inner_rect)

# Save temporary canvas
temp_path = r"C:\Users\bruno\projects\dsi-cosmo-search\temp_cover_bg.png"
fig.savefig(temp_path, dpi=200, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)

# Open in Pillow for premium typography overlay
img = Image.open(temp_path).convert("RGBA")
draw = ImageDraw.Draw(img)

# Try loading system font, fallback to default
try:
    font_cat = ImageFont.truetype("arialbd.ttf", 46)
    font_title = ImageFont.truetype("georgiab.ttf", 84)
    font_sub = ImageFont.truetype("arial.ttf", 48)
    font_tag = ImageFont.truetype("ariali.ttf", 38)
    font_author = ImageFont.truetype("arialbd.ttf", 64)
    font_meta = ImageFont.truetype("arial.ttf", 36)
    font_doi = ImageFont.truetype("courbd.ttf", 38)
except:
    font_cat = ImageFont.load_default()
    font_title = font_cat
    font_sub = font_cat
    font_tag = font_cat
    font_author = font_cat
    font_meta = font_cat
    font_doi = font_cat

# Helper to draw centered text
def draw_centered(text, y, font, color, tracking=0):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    x = (width - w) // 2
    draw.text((x, y), text, font=font, fill=color)

# 1. Top Category & Series
draw_centered("MONOGRAPH SYNTHESIS · CDD 500 → 530.1", 160, font_cat, "#38bdf8")
draw_centered("NATURAL SCIENCES & THEORETICAL PHYSICS", 220, font_meta, "#94a3b8")

# Horizontal decorative line
draw.line([(width//2 - 250, 280), (width//2 + 250, 280)], fill="#3b82f6", width=2)
draw.line([(width//2 - 120, 286), (width//2 + 120, 286)], fill="#fbbf24", width=1)

# 2. Main Title
draw_centered("THE MATRIOSKA", 380, font_title, "#ffffff")
draw_centered("PROTOCOL", 480, font_title, "#ffffff")

# 3. Subtitle
draw_centered("From Primordial Discrete Scale Invariance", 620, font_sub, "#93c5fd")
draw_centered("to Post-Quantum Agility", 685, font_sub, "#93c5fd")

# 4. Scope tag
draw_centered("A Unified 3-Stage Metrological Architecture", 780, font_tag, "#cbd5e1")
draw_centered("Enforcing Anti-Hallucination Bounds Across 18 Orders of Scale", 830, font_tag, "#94a3b8")

# Decorative central emblem circle
center_y = 1380
badge_box = [(width//2 - 180, center_y - 45), (width//2 + 180, center_y + 45)]
draw.rounded_rectangle(badge_box, radius=24, outline="#38bdf8", width=2, fill="#0b1329")
draw_centered("7 PAPERS · 1 FRAMEWORK", center_y - 18, font_cat, "#fbbf24")

# 5. Author
draw_centered("BRUNO LUÇARDO OLIVAES", 1880, font_author, "#ffffff")
draw_centered("Independent Researcher · Brazil", 1960, font_meta, "#94a3b8")
draw_centered("ORCID: 0009-0003-8857-7945", 2010, font_meta, "#60a5fa")

# 6. Bottom CERN / Zenodo Archive Box
box_top = 2110
box_bot = 2240
box_left = 180
box_right = width - 180
draw.rounded_rectangle([(box_left, box_top), (box_right, box_bot)], radius=16, outline="#2563eb", width=2, fill="#0f172a")

draw_centered("PERMANENT CERN / ZENODO ARCHIVE", box_top + 22, font_meta, "#cbd5e1")
draw_centered("DOI: 10.5281/zenodo.24124702", box_top + 68, font_doi, "#fbbf24")

# Save to all target paths
for p in paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    img.save(p, "PNG")
    print(f"Cover saved successfully to: {p}")

if os.path.exists(temp_path):
    os.remove(temp_path)

