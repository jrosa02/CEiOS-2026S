import requests
import os

BASE = "https://re.jrc.ec.europa.eu/api/v5_3/tmy"

LAT = 50.062
LON = 19.937
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(OUT_DIR, exist_ok=True)

FORMATS = [
    ("json",  "tmy_krakow.json"),
    ("csv",   "tmy_krakow.csv"),
    ("epw",   "tmy_krakow.epw"),
    ("basic", "tmy_krakow_basic.csv"),
]

print("=== Zadanie 11: Pobieranie plików TMY dla Krakowa ===")
print(f"Lokalizacja: lat={LAT}, lon={LON}")
print(f"Baza danych: PVGIS-SARAH3\n")

for fmt, filename in FORMATS:
    params = dict(
        lat=LAT, lon=LON,
        raddatabase="PVGIS-SARAH3",
        outputformat=fmt,
        browser=0,
    )
    print(f"Pobieranie formatu '{fmt}'...")
    r = requests.get(BASE, params=params)
    if r.status_code != 200:
        print(f"  BŁĄD {r.status_code}: {r.text[:200]}")
        continue

    path = os.path.join(OUT_DIR, filename)
    with open(path, "wb") as f:
        f.write(r.content)
    size = os.path.getsize(path)
    print(f"  Zapisano: {filename} ({size} bajtów)")

print()
print("=== Zadanie 10: Zawartość pliku TMY (nagłówek i pierwsze wiersze) ===")

csv_path = os.path.join(OUT_DIR, "tmy_krakow.csv")
if os.path.exists(csv_path):
    with open(csv_path, encoding="utf-8", errors="replace") as f:
        lines = f.readlines()

    print(f"\nPlik CSV — łączna liczba wierszy: {len(lines)}")
    print("\n--- Nagłówek (pierwsze 20 wierszy) ---")
    for i, line in enumerate(lines[:20]):
        print(f"{i+1:>3}: {line}", end="")

    print("\n--- Fragment danych (wiersze z nagłówkami kolumn i pierwsze 5 rekordów) ---")
    data_start = next((i for i, l in enumerate(lines) if l.startswith("time") or l.startswith("T2m")), None)
    if data_start is not None:
        for line in lines[data_start:data_start + 6]:
            print(line, end="")
    print()

print("\n=== Zadanie 10: Opis kolumn i rozdzielczość czasowa ===")
print("""
Plik TMY zawiera 8760 rekordów godzinowych (1 rok x 8760 godzin).
Każdy rekord odpowiada 1 godzinie czasu słonecznego.

Kolumny (typowe dla PVGIS TMY):
  T2m      — temperatura powietrza na wysokości 2 m [°C]
  RH       — wilgotność względna [%]
  G(h)     — globalne promieniowanie poziome GHI [W/m²]
  Gb(n)    — promieniowanie bezpośrednie normalne DNI [W/m²]
  Gd(h)    — promieniowanie rozproszone poziome DHI [W/m²]
  IR(h)    — promieniowanie podczerwone poziome [W/m²]
  WS10m    — prędkość wiatru na 10 m [m/s]
  WD10m    — kierunek wiatru [°]
  SP       — ciśnienie powierzchniowe [Pa]

Zakres czasowy: PVGIS-SARAH3 obejmuje lata 2005–2023.
TMY jest plikiem syntetycznym — każdy miesiąc pochodzi z innego roku,
wybranego jako najbardziej typowy metodą statystyczną (Finkelstein-Schafer).
""")
