import requests
import os

BASE = "https://re.jrc.ec.europa.eu/api/v5_3/seriescalc"

LAT = 50.062
LON = 19.937
YEAR = 2023
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(OUT_DIR, exist_ok=True)

print("=== Zadanie 7: Godzinowe dane promieniowania słonecznego — Kraków 2023 ===")
print(f"Lokalizacja: lat={LAT}, lon={LON}")
print(f"Baza danych: PVGIS-SARAH3, rok: {YEAR}\n")

params = dict(
    lat=LAT, lon=LON,
    raddatabase="PVGIS-SARAH3",
    startyear=YEAR, endyear=YEAR,
    pvcalculation=0,
    components=1,
    angle=0,
    aspect=0,
    outputformat="csv",
    browser=0,
)

print("Pobieranie pliku CSV...")
r = requests.get(BASE, params=params)
r.raise_for_status()

csv_path = os.path.join(OUT_DIR, f"hourly_krakow_{YEAR}.csv")
with open(csv_path, "wb") as f:
    f.write(r.content)
print(f"Zapisano: {csv_path} ({len(r.content)} bajtów)\n")

# Parse and display the file
lines = r.content.decode("utf-8", errors="replace").splitlines()
print(f"Łączna liczba wierszy w pliku: {len(lines)}\n")

# Find metadata header and data header
data_start = next(
    (i for i, l in enumerate(lines) if l.startswith("time") or l.startswith("Lat")),
    None,
)

print("--- Nagłówek pliku (pierwsze wiersze metadanych) ---")
for line in lines[:8]:
    print(line)

# Find the data column header row
col_header_idx = next(
    (i for i, l in enumerate(lines) if l.startswith("time")), None
)

if col_header_idx is not None:
    print(f"\n--- Nagłówek kolumn (wiersz {col_header_idx + 1}) ---")
    print(lines[col_header_idx])
    print()
    print("--- Pierwsze 5 rekordów danych ---")
    for line in lines[col_header_idx + 1 : col_header_idx + 6]:
        print(line)

print()
print("=== Opis kolumn ===")
col_descriptions = {
    "time":   "Czas UTC (format YYYYMMDD:HHmm)",
    "Gb(i)":  "Promieniowanie bezpośrednie na płaszczyźnie poziomej [W/m²]",
    "Gd(i)":  "Promieniowanie rozproszone na płaszczyźnie poziomej DHI [W/m²]",
    "Gr(i)":  "Promieniowanie odbite od podłoża [W/m²] (≈0 dla kąta 0°)",
    "H_sun":  "Wysokość Słońca nad horyzontem [°]",
    "T2m":    "Temperatura powietrza na wysokości 2 m [°C]",
    "WS10m":  "Prędkość wiatru na wysokości 10 m [m/s]",
    "Int":    "Flaga rekonstrukcji danych (1 = dane interpolowane)",
}
for col, desc in col_descriptions.items():
    print(f"  {col:<8} — {desc}")

# Annual stats from JSON for verification
print("\nWeryfikacja: pobieranie sum rocznych z API (JSON)...")
params_json = dict(params)
params_json["outputformat"] = "json"
rj = requests.get(BASE, params=params_json)
rj.raise_for_status()
hourly = rj.json()["outputs"]["hourly"]
ghi = sum(h.get("Gb(i)", 0) + h.get("Gd(i)", 0) for h in hourly) / 1000
print(f"  Suma roczna GHI = Gb(i) + Gd(i): {ghi:.1f} kWh/m²")
print(f"  Liczba rekordów godzinowych: {len(hourly)}")
