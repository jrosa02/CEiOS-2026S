import requests
import os

BASE = "https://re.jrc.ec.europa.eu/api/v5_3/MRcalc"

LAT = 50.062
LON = 19.937
YEAR = 2022
ANGLE = 40  # chosen tilt angle

MONTHS_PL = ["Sty", "Lut", "Mar", "Kwi", "Maj", "Cze",
             "Lip", "Sie", "Wrz", "Paź", "Lis", "Gru"]

params = dict(
    lat=LAT, lon=LON,
    raddatabase="PVGIS-SARAH3",
    startyear=YEAR, endyear=YEAR,
    horirrad=1,    # H(h) — horizontal irradiation
    optrad=1,      # H(i_opt) — optimal angle irradiation
    selectrad=1,   # H(i) — irradiation at chosen angle
    angle=ANGLE,
    mr_dni=1,      # Gb(n) — direct normal irradiation
    d2g=1,         # Kd — diffuse/global ratio
    outputformat="json", browser=0,
)

print(f"=== Zadanie 2: Miesięczne nasłonecznienie — Kraków {YEAR} ===")
print(f"Lokalizacja: lat={LAT}, lon={LON}")
print(f"Baza danych: PVGIS-SARAH3, kąt wybrany: {ANGLE}°\n")

r = requests.get(BASE, params=params)
r.raise_for_status()
data = r.json()

rows = data["outputs"]["monthly"]

print(f"{'Miesiąc':>8} | {'H(h)':>10} | {'H(i_opt)':>10} | {'H(i=40°)':>10} | {'Gb(n)':>10} | {'Kd':>6}")
print(f"{'':>8} | {'[kWh/m²]':>10} | {'[kWh/m²]':>10} | {'[kWh/m²]':>10} | {'[kWh/m²]':>10} | {'[-]':>6}")
print("-" * 70)

for i, row in enumerate(rows):
    hh   = row["H(h)_m"]
    hopt = row["H(i_opt)_m"]
    hsel = row["H(i)_m"]
    dni  = row["Hb(n)_m"]
    kd   = row["Kd"]
    print(f"{MONTHS_PL[i]:>8} | {hh:>10.1f} | {hopt:>10.1f} | {hsel:>10.1f} | {dni:>10.1f} | {kd:>6.2f}")

hh_y   = sum(r["H(h)_m"]     for r in rows)
hopt_y = sum(r["H(i_opt)_m"] for r in rows)
hsel_y = sum(r["H(i)_m"]     for r in rows)
dni_y  = sum(r["Hb(n)_m"]    for r in rows)
print("-" * 70)
print(f"{'Rok':>8} | {hh_y:>10.1f} | {hopt_y:>10.1f} | {hsel_y:>10.1f} | {dni_y:>10.1f} | {'—':>6}")

# Key figures
jun = rows[5]
dec = rows[11]
jan = rows[0]
print(f"\n=== Kluczowe wartości ===")
print(f"Maksimum H(h): czerwiec {YEAR} = {jun['H(h)_m']:.1f} kWh/m²")
print(f"Minimum H(h):  grudzień {YEAR} = {dec['H(h)_m']:.1f} kWh/m²")
gain_jan = (jan["H(i_opt)_m"] - jan["H(h)_m"]) / jan["H(h)_m"] * 100
print(f"Wzrost H(i_opt) vs H(h) w styczniu: +{gain_jan:.1f}%")
