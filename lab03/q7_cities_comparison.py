import requests

BASE = "https://re.jrc.ec.europa.eu/api/v5_3/MRcalc"

cities = [
    # Polskie miasta
    ("Warszawa",    "PL", 52.23, 21.01),
    ("Kraków",      "PL", 50.06, 19.94),
    ("Gdańsk",      "PL", 54.35, 18.65),
    ("Wrocław",     "PL", 51.11, 17.04),
    ("Poznań",      "PL", 52.41, 16.93),
    ("Białystok",   "PL", 53.13, 23.16),
    # Pozostałe kraje europejskie
    ("Oslo",        "NO", 59.9,  10.7),
    ("Helsinki",    "FI", 60.2,  25.0),
    ("Stockholm",   "SE", 59.3,  18.1),
    ("London",      "GB", 51.5,  -0.1),
    ("Edinburgh",   "GB", 55.9,  -3.2),
    ("Berlin",      "DE", 52.5,  13.4),
    ("Munich",      "DE", 48.1,  11.6),
    ("Paris",       "FR", 48.8,   2.3),
    ("Marseille",   "FR", 43.3,   5.4),
    ("Madrid",      "ES", 40.4,  -3.7),
    ("Seville",     "ES", 37.4,  -5.9),
    ("Rome",        "IT", 41.9,  12.5),
    ("Palermo",     "IT", 38.1,  13.4),
    ("Athens",      "GR", 37.9,  23.7),
]

def annual_ghi(lat, lon):
    r = requests.get(BASE, params=dict(
        lat=lat, lon=lon,
        horirrad=1,
        outputformat="json"
    ))
    monthly = r.json()["outputs"]["monthly"]
    return sum(m["H(h)_m"] for m in monthly)

results = []
print(f"{'Miasto':<14} {'Kraj':>4} {'GHI roczne [kWh/m²]':>22}")
print("-" * 42)

for name, country, lat, lon in cities:
    ghi = annual_ghi(lat, lon)
    results.append((name, country, ghi))
    print(f"{name:<14} {country:>4} {ghi:>20.1f}")

pl = [ghi for _, c, ghi in results if c == "PL"]
eu = [ghi for _, c, ghi in results if c != "PL"]

def mean(xs): return sum(xs) / len(xs)
def std(xs):
    m = mean(xs)
    return (sum((x - m)**2 for x in xs) / len(xs)) ** 0.5

print(f"\nPolska  — średnia: {mean(pl):.1f}  odch.std: {std(pl):.1f}  min: {min(pl):.1f}  max: {max(pl):.1f}")
print(f"Reszta EU — średnia: {mean(eu):.1f}  odch.std: {std(eu):.1f}  min: {min(eu):.1f}  max: {max(eu):.1f}")
