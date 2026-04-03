"""
AASB: Orion Belt sky chart comparison
Earth (Giza, 30°N) vs Mars Pathfinder site (19.13°N)
Two epochs: ~2560 BCE (Khufu) and ~10,500 BCE (Bauval alignment)

Uses manual precession + Alt/Az calculation to support BCE dates beyond
astropy's ERFA limits. Precession via Lieske (1979) rotation angles.
Note: accuracy degrades beyond ~5 centuries from J2000; 10,500 BCE is
illustrative — shows general belt orientation, not arcsecond precision.

Author: Eric D. Martin (code generated 2026-04-03 for aasb repo)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# ---------------------------------------------------------------------------
# Orion's Belt stars — J2000 ICRS (RA, Dec in degrees)
# Approximate distances for legend
# ---------------------------------------------------------------------------
belt_stars = {
    'Alnitak':  (85.1896, -1.9426, '~800 ly'),
    'Alnilam':  (84.0534, -1.2019, '~1300 ly'),
    'Mintaka':  (83.0016, -0.2991, '~900 ly'),
}

orion_context = {
    'Betelgeuse': (88.7929,  7.4071),
    'Rigel':      (78.6345, -8.2016),
    'Bellatrix':  (81.2828,  6.3497),
    'Saiph':      (86.9391, -9.6697),
}

# ---------------------------------------------------------------------------
# JD calculation (proleptic Julian calendar)
# ---------------------------------------------------------------------------
def date_to_jd(astro_year, month, day, hour_ut=12):
    """Julian Day Number from astronomical year/month/day."""
    y, m = astro_year, month
    if m <= 2:
        y -= 1
        m += 12
    # Proleptic Julian calendar (B=0)
    jd = (int(365.25 * (y + 4716)) + int(30.6001 * (m + 1))
          + day - 1524.5 + hour_ut / 24.0)
    return jd

# ---------------------------------------------------------------------------
# Precession: Lieske (1979) rotation angles, valid ~J2000 ± few centuries
# Extended here to ~125 centuries for illustration; accuracy ~few degrees
# ---------------------------------------------------------------------------
def precess_j2000_to_epoch(ra0, dec0, T):
    """
    Precess (ra0, dec0) in J2000 degrees to epoch T Julian centuries from J2000.
    Returns (ra_prec, dec_prec) in degrees.
    """
    ra = np.radians(ra0)
    dec = np.radians(dec0)

    # Lieske 1979 precession angles in arcseconds
    zeta_A = ((2306.2181 + 1.39656*T - 0.000139*T**2)*T
              + (0.30188 - 0.000344*T)*T**2 + 0.017998*T**3)
    z_A    = ((2306.2181 + 1.39656*T - 0.000139*T**2)*T
              + (1.09468 + 0.000066*T)*T**2 + 0.018203*T**3)
    theta_A = ((2004.3109 - 0.85330*T - 0.000217*T**2)*T
               - (0.42665 + 0.000217*T)*T**2 - 0.041775*T**3)

    z_r   = np.radians(zeta_A  / 3600)
    zA_r  = np.radians(z_A     / 3600)
    th_r  = np.radians(theta_A / 3600)

    A = np.cos(dec) * np.sin(ra + z_r)
    B = (np.cos(th_r) * np.cos(dec) * np.cos(ra + z_r)
         - np.sin(th_r) * np.sin(dec))
    C = (np.sin(th_r) * np.cos(dec) * np.cos(ra + z_r)
         + np.cos(th_r) * np.sin(dec))

    ra_prec  = (np.degrees(np.arctan2(A, B)) + np.degrees(zA_r)) % 360
    dec_prec = np.degrees(np.arcsin(np.clip(C, -1, 1)))
    return ra_prec, dec_prec

# ---------------------------------------------------------------------------
# Greenwich Mean Sidereal Time (degrees) for a JD
# ---------------------------------------------------------------------------
def gmst_deg(jd):
    T = (jd - 2451545.0) / 36525.0
    theta = (280.46061837
             + 360.98564736629 * (jd - 2451545.0)
             + 0.000387933 * T**2
             - T**3 / 38710000.0)
    return theta % 360

# ---------------------------------------------------------------------------
# Alt/Az from precessed RA/Dec, observer lat/lon, JD
# ---------------------------------------------------------------------------
def altaz(ra_prec, dec_prec, lat_deg, lon_deg, jd):
    lst = (gmst_deg(jd) + lon_deg) % 360
    ha_r  = np.radians((lst - ra_prec) % 360)
    dec_r = np.radians(dec_prec)
    lat_r = np.radians(lat_deg)

    sin_alt = (np.sin(dec_r)*np.sin(lat_r)
               + np.cos(dec_r)*np.cos(lat_r)*np.cos(ha_r))
    alt = np.degrees(np.arcsin(np.clip(sin_alt, -1, 1)))

    cos_az = ((np.sin(dec_r) - np.sin(np.radians(alt))*np.sin(lat_r))
              / (np.cos(np.radians(alt))*np.cos(lat_r) + 1e-12))
    az = np.degrees(np.arccos(np.clip(cos_az, -1, 1)))
    if np.sin(ha_r) > 0:
        az = 360 - az

    return alt, az

# ---------------------------------------------------------------------------
# Scenarios
# ---------------------------------------------------------------------------
JD_2560       = date_to_jd(-2559,  12, 21, hour_ut=22)  # 2560 BCE Dec 21 22h
JD_10500_giza = date_to_jd(-10499,  3, 21, hour_ut=10)  # 10500 BCE transit from Giza: max alt 6.6° (barely visible)
JD_10500_mars = date_to_jd(-10499,  3, 21, hour_ut=14)  # 10500 BCE transit from Mars site: max alt 17.4°

scenarios = [
    {
        'label': 'Giza, Egypt  ~2560 BCE\n(Khufu pyramid era)',
        'lat': 30.0, 'lon': 31.13, 'jd': JD_2560,
        'T': (JD_2560-2451545)/36525,
        'planet': 'Earth',
        'note': 'Belt ~31° above horizon'
    },
    {
        'label': 'Mars Pathfinder Site  ~2560 BCE\n(19.13°N, 326.83°E)',
        'lat': 19.13, 'lon': 326.83, 'jd': JD_2560,
        'T': (JD_2560-2451545)/36525,
        'planet': 'Mars',
        'note': 'Belt ~47° above horizon'
    },
    {
        'label': 'Giza, Egypt  ~10,500 BCE\n(Bauval / Orion Correlation era)\nat belt transit: barely visible, Alt ~7°',
        'lat': 30.0, 'lon': 31.13, 'jd': JD_10500_giza,
        'T': (JD_10500_giza-2451545)/36525,
        'planet': 'Earth',
        'note': 'Belt max 6.6° — southern horizon\n(Bauval: belt was at min height, mirroring pyramids)'
    },
    {
        'label': 'Mars Pathfinder Site  ~10,500 BCE\n(19.13°N) at belt transit: Alt ~17°',
        'lat': 19.13, 'lon': 326.83, 'jd': JD_10500_mars,
        'T': (JD_10500_mars-2451545)/36525,
        'planet': 'Mars',
        'note': 'Belt max 17.4° — much higher from Mars\n(lower lat = better view of belt at this epoch)'
    },
]

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(16, 14))
fig.patch.set_facecolor('#07070f')

belt_colors = {'Alnitak': '#99ccff', 'Alnilam': '#ffffff', 'Mintaka': '#ffcc88'}
ctx_color   = '#2a4a6a'

for ax, sc in zip(axes.flat, scenarios):
    ax.set_facecolor('#040408')
    lat, lon, jd, T = sc['lat'], sc['lon'], sc['jd'], sc['T']

    # Context stars
    for name, (ra0, dec0) in orion_context.items():
        rp, dp = precess_j2000_to_epoch(ra0, dec0, T)
        alt, az = altaz(rp, dp, lat, lon, jd)
        if alt > 2:
            ax.plot(az, alt, 'o', color=ctx_color, markersize=6, alpha=0.7)
            ax.annotate(name, (az, alt), color='#3a6080', fontsize=7.5,
                        xytext=(5, 4), textcoords='offset points')

    # Belt stars
    bp = {}
    for name, (ra0, dec0, dist_label) in belt_stars.items():
        rp, dp = precess_j2000_to_epoch(ra0, dec0, T)
        alt, az = altaz(rp, dp, lat, lon, jd)
        bp[name] = (az, alt)
        ax.plot(az, alt, '*', color=belt_colors[name],
                markersize=22, markeredgecolor='white', markeredgewidth=0.5, zorder=5)
        ax.annotate(f"{name}\n({dist_label})", (az, alt),
                    color=belt_colors[name], fontsize=8.5, fontweight='bold',
                    xytext=(8, 6), textcoords='offset points')

    # Belt line
    order = ['Mintaka', 'Alnilam', 'Alnitak']
    azs  = [bp[n][0] for n in order]
    alts = [bp[n][1] for n in order]
    ax.plot(azs, alts, '-', color='#aaaaff', linewidth=2, alpha=0.7, zorder=3)

    # Meridian (S = 180°)
    ax.axvline(180, color='#ff4444', linewidth=0.8, linestyle='--', alpha=0.5, label='S meridian')

    # Horizon
    ax.axhline(0, color='#334455', linewidth=1)
    ax.fill_between([0, 360], [0, 0], [-5, -5], color='#0a1520', alpha=0.8)

    # Center view on belt
    az_c  = np.mean(azs)
    alt_c = np.mean(alts)
    ax.set_xlim(az_c - 20, az_c + 20)
    ax.set_ylim(max(alt_c - 18, 0), alt_c + 18)

    belt_tilt = np.degrees(np.arctan2(alts[-1]-alts[0], azs[-1]-azs[0]))

    ax.set_title(sc['label'], color='white', fontsize=10.5, pad=8, fontweight='bold')
    ax.set_xlabel('Azimuth (°)  — S = 180°', color='#8899aa', fontsize=9)
    ax.set_ylabel('Altitude (°)', color='#8899aa', fontsize=9)
    ax.tick_params(colors='#556677', labelsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor('#1a2a3a')

    info = (f"Belt center:  Alt {alt_c:.1f}°  Az {az_c:.1f}°\n"
            f"Belt tilt:    {belt_tilt:.1f}° from horizontal\n"
            f"Lat:          {lat:.2f}°N")
    ax.text(0.02, 0.97, info, transform=ax.transAxes, color='#88aacc',
            fontsize=8, va='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='#05050f', alpha=0.8))

    planet_color = '#ff7733' if sc['planet'] == 'Mars' else '#33aaff'
    ax.text(0.98, 0.97, sc['planet'], transform=ax.transAxes, color=planet_color,
            fontsize=12, va='top', ha='right', fontweight='bold')

plt.suptitle(
    "Orion's Belt: Earth (Giza 30°N) vs Mars Pathfinder Site (19.13°N)\n"
    "Epochs: ~2560 BCE (Khufu) and ~10,500 BCE (Bauval Orion Correlation)\n"
    "Angular pattern identical from both planets — latitude shifts altitude above horizon\n"
    "Precession via Lieske (1979); 10,500 BCE is illustrative (±few degrees accuracy)",
    color='#ccddee', fontsize=11, y=1.01
)

plt.tight_layout()
out = '/scratch/repos/aasb/images/orion_comparison.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='#07070f')
print(f"Saved: {out}")
print(f"JD 2560 BCE:       {JD_2560:.1f}")
print(f"JD 10500 BCE Giza: {JD_10500_giza:.1f}")
print(f"JD 10500 BCE Mars: {JD_10500_mars:.1f}")
