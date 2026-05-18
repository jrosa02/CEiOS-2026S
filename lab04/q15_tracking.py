import requests
from collections import defaultdict

BASE = "https://re.jrc.ec.europa.eu/api/v5_3/seriescalc"

LAT = 50.062
LON = 19.937

# PVGIS seriescalc trackingtype mapping:
#   0 = fixed
#   1 = inclined axis (single horizontal axis N-S, tracks elevation)
#   2 = two-axis (full tracking)
#   3 = vertical axis (tracks azimuth, inclination fixed → needs optimalinclination=1)
TRACKING_MODES = [
    (0, "Stacjonarny (optymalny kąt)", True),
    (1, "Inclined axis (oś pozioma N-S)", False),
    (2, "Two-axis (dwuosiowy)",          False),
    (3, "Vertical axis (oś pionowa)",    True),
]

MONTHS_PL = ["Sty", "Lut", "Mar", "Kwi", "Maj", "Cze",
             "Lip", "Sie", "Wrz", "Paź", "Lis", "Gru"]

def get_tracking_yield(trackingtype, optimalinclination=False):
    params = dict(
        lat=LAT, lon=LON,
        raddatabase="PVGIS-SARAH3",
        peakpower=1, loss=14,
        pvcalculation=1,
        trackingtype=trackingtype,
        startyear=2023, endyear=2023,
        outputformat="json",
        browser=0,
    )
    if optimalinclination:
        params["optimalinclination"] = 1
    r = requests.get(BASE, params=params)
    r.raise_for_status()
    data = r.json()
    hourly = data["outputs"]["hourly"]
    annual = sum(h.get("P", 0) for h in hourly) / 1000
    return annual, hourly

def monthly_totals(hourly):
    by_month = defaultdict(float)
    for h in hourly:
        t = str(h["time"])
        month = int(t[4:6])
        by_month[month] += h.get("P", 0) / 1000
    return [by_month[m] for m in range(1, 13)]

print("=== Zadanie 15: Porównanie systemów nadążnych 1 kWp — Kraków ===")
print(f"Lokalizacja: lat={LAT}, lon={LON}")
print(f"Baza danych: PVGIS-SARAH3, rok 2023\n")

results = []
for ttype, name, opt in TRACKING_MODES:
    print(f"Pobieranie: {name} (trackingtype={ttype})...")
    e_y, hourly = get_tracking_yield(ttype, optimalinclination=opt)
    results.append((name, e_y, hourly))
    print(f"  E_y = {e_y:.1f} kWh/rok")

e_fixed = results[0][1]
print()
print(f"{'System':>36} | {'E_y [kWh/rok]':>14} | {'Przyrost vs stacjonarny':>24}")
print("-" * 82)
for name, e_y, _ in results:
    gain = (e_y - e_fixed) / e_fixed * 100
    marker = "" if gain == 0 else f"(+{gain:.1f}%)" if gain > 0 else f"({gain:.1f}%)"
    print(f"{name:>36} | {e_y:>14.1f} | {marker:>24}")

print()
print("--- Miesięczna produkcja energii [kWh] ---")
print(f"{'Miesiąc':>8}", end="")
for name, _, _ in results:
    short = name.split("(")[0].strip()[:16]
    print(f" | {short:>16}", end="")
print()
print("-" * (9 + len(results) * 19))

monthly_data = [monthly_totals(r[2]) for r in results]
for i in range(12):
    print(f"{MONTHS_PL[i]:>8}", end="")
    for md in monthly_data:
        print(f" | {md[i]:>16.2f}", end="")
    print()
