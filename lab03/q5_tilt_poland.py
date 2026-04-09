import requests

BASE = "https://re.jrc.ec.europa.eu/api/v5_3/PVcalc"

cities = [
    ("Warszawa",   52.23, 21.01),
    ("Kraków",     50.06, 19.94),
    ("Gdańsk",     54.35, 18.65),
    ("Wrocław",    51.11, 17.04),
    ("Poznań",     52.41, 16.93),
    ("Białystok",  53.13, 23.16),
    ("Lublin",     51.25, 22.57),
    ("Rzeszów",    50.04, 22.00),
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

angles = []
print(f"{'Miasto':<12} {'Lat':>6} {'Optymalny kąt':>15}")
print("-" * 36)

for name, lat, lon in cities:
    angle = find_optimal_angle(lat, lon)
    angles.append(angle)
    print(f"{name:<12} {lat:>6.2f} {angle:>13.1f}°")

mean = sum(angles) / len(angles)
spread = max(angles) - min(angles)
print(f"\nŚrednia: {mean:.1f}°  |  Rozstęp: {spread:.1f}°  |  Min: {min(angles):.1f}°  Max: {max(angles):.1f}°")
