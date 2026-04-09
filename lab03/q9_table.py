import requests

BASE = "https://re.jrc.ec.europa.eu/api/v5_3/PVcalc"

# Representative locations (capital or geographic center) per country
countries = [
    ("Polska",       "PL", 52.23, 21.01),
    ("Niemcy",       "DE", 52.52, 13.40),
    ("Hiszpania",    "ES", 40.42, -3.70),
    ("Portugalia",   "PT", 38.72, -9.14),
    ("Francja",      "FR", 48.85,  2.35),
    ("Włochy",       "IT", 41.90, 12.49),
    ("Grecja",       "GR", 37.98, 23.73),
    ("Wielka Brytania","GB",51.51, -0.13),
    ("Szwecja",      "SE", 59.33, 18.07),
    ("Norwegia",     "NO", 59.91, 10.75),
    ("Finlandia",    "FI", 60.17, 24.94),
    ("Cypr",         "CY", 35.17, 33.37),
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
    return opt_angle, max_e_y

print(f"| {'Kraj':<20} | {'Lat':>5} | {'E_y [kWh/kWp/rok]':>20} | {'H_i_opt [kWh/m²/rok]':>23} | {'Kąt optymalny':>15} |")
print("|" + "-"*22 + "|" + "-"*7 + "|" + "-"*22 + "|" + "-"*25 + "|" + "-"*17 + "|")

for name, code, lat, lon in countries:
    angle, e_y = find_optimal_angle(lat, lon)
    r = requests.get(BASE, params=dict(
        lat=lat, lon=lon,
        peakpower=1, loss=14,
        angle=angle,
        outputformat="json"
    ))
    data = r.json()
    h_i_opt = data["outputs"]["totals"]["fixed"].get("H(i)_y") or data["outputs"]["totals"]["fixed"].get("H(i_opt)_y", 0)
    print(f"| {name:<20} | {lat:>5.1f} | {e_y:>20.1f} | {h_i_opt:>23.1f} | {angle:>13.1f}° |")
