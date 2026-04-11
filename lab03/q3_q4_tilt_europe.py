import requests
import numpy as np

BASE = "https://re.jrc.ec.europa.eu/api/v5_3/PVcalc"

locations = [
    ("Cyprus",      34.9, 33.0),
    ("Malta",       35.9, 14.5),
    ("Crete",       35.3, 25.1),
    ("Athens",      37.9, 23.7),
    ("Lisbon",      38.7, -9.1),
    ("Seville",     37.4, -5.9),
    ("Madrid",      40.4, -3.7),
    ("Rome",        41.9, 12.5),
    ("Barcelona",   41.4,  2.2),
    ("Zagreb",      45.8, 16.0),
    ("Bern",        46.9,  7.4),
    ("Vienna",      48.2, 16.4),
    ("Paris",       48.8,  2.3),
    ("Prague",      50.1, 14.4),
    ("Warsaw",      52.2, 21.0),
    ("London",      51.5, -0.1),
    ("Berlin",      52.5, 13.4),
    ("Brussels",    50.8,  4.4),
    ("Copenhagen",  55.7, 12.6),
    ("Stockholm",   59.3, 18.1),
    ("Helsinki",    60.2, 25.0),
    ("Oslo",        59.9, 10.7),
    ("Riga",        56.9, 24.1),
    ("Reykjavik",   64.1,-21.9),
    ("Tromso",      69.7, 19.0),
]

def find_optimal_angle(lat, lon):
    """Scan angles 0-80° and find max annual yield"""
    max_e_y = 0
    opt_angle = 0
    for angle in range(0, 81, 2):
        r = requests.get(BASE, params=dict(
            lat=lat, lon=lon,
            peakpower=1, loss=14,
            angle=angle,
            outputformat="json"
        ))
        data = r.json()
        e_y = data["outputs"]["totals"]["fixed"]["E_y"]
        if e_y > max_e_y:
            max_e_y = e_y
            opt_angle = angle
    return opt_angle

results = []
print(f"{'Location':<14} {'Lat':>6} {'Lon':>7} {'OptAngle':>10}")
print("-" * 42)

for name, lat, lon in locations:
    angle = find_optimal_angle(lat, lon)
    results.append((name, lat, lon, angle))
    print(f"{name:<14} {lat:>6.1f} {lon:>7.1f} {angle:>10.1f}°")

lats = np.array([r[1] for r in results])
angles = np.array([r[3] for r in results])
coeffs = np.polyfit(lats, angles, 1)
predicted = np.polyval(coeffs, lats)
ss_res = np.sum((angles - predicted) ** 2)
ss_tot = np.sum((angles - angles.mean()) ** 2)
r2 = 1 - ss_res / ss_tot
print(f"\nLinear fit: optimal_angle ≈ {coeffs[0]:.3f} × lat + ({coeffs[1]:.2f})")
print(f"R² = {r2:.4f}")
print(f"Angle range: {angles.min():.1f}° – {angles.max():.1f}°")
