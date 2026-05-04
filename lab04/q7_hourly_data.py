import requests

BASE = "https://re.jrc.ec.europa.eu/api/v5_3/seriescalc"

LAT = 50.062
LON = 19.937

print("=== Zadanie 7: Godzinowe dane promieniowania słonecznego — Kraków 2023 ===")
print(f"Lokalizacja: lat={LAT}, lon={LON}")
print(f"Baza danych: PVGIS-SARAH3, rok: 2023\n")

params = dict(
    lat=LAT, lon=LON,
    raddatabase="PVGIS-SARAH3",
    startyear=2023, endyear=2023,
    pvcalculation=0,
    components=1,
    angle=0,
    aspect=0,
    outputformat="json",
    browser=0,
)

print("Pobieranie danych...")
r = requests.get(BASE, params=params)
r.raise_for_status()
data = r.json()

hourly = data["outputs"]["hourly"]
meta = data.get("meta", {})

print(f"Liczba rekordów: {len(hourly)}")
print()

if hourly:
    keys = list(hourly[0].keys())
    print("=== Nagłówki kolumn ===")
    col_descriptions = {
        "time":  "Czas (format: YYYYMMDDhhmm, UTC)",
        "G(h)":  "Globalne promieniowanie poziome GHI [W/m²]",
        "Gb(n)": "Promieniowanie bezpośrednie normalne DNI [W/m²]",
        "Gd(h)": "Promieniowanie rozproszone poziome DHI [W/m²]",
        "G(i)":  "Globalne promieniowanie na płaszczyźnie pochylonej [W/m²]",
        "Gb(i)": "Promieniowanie bezpośrednie poziome (angle=0°) [W/m²]",
        "Gd(i)": "Promieniowanie rozproszone poziome DHI [W/m²]",
        "Gr(i)": "Promieniowanie odbite od podłoża [W/m²] (=0 dla poziomu)",
        "H_sun": "Wysokość Słońca nad horyzontem [°]",
        "T2m":   "Temperatura powietrza 2 m n.p.g. [°C]",
        "WS10m": "Prędkość wiatru 10 m n.p.g. [m/s]",
        "Int":   "Wskaźnik rekonstrukcji danych [1=rekonstruowane]",
    }

    header_parts = []
    for k in keys:
        desc = col_descriptions.get(k, k)
        header_parts.append(f"  {k:<10} — {desc}")
        print(f"  {k:<10} — {desc}")

    print()
    print(f"=== Pierwsze 10 rekordów ===")
    header = " | ".join(f"{k:>10}" for k in keys)
    print(header)
    print("-" * len(header))
    for row in hourly[:10]:
        print(" | ".join(f"{str(row.get(k, ''))[:10]:>10}" for k in keys))

    print()
    print("=== Statystyki roczne ===")
    def col_stats(col):
        vals = [h[col] for h in hourly if col in h and h[col] is not None]
        if not vals:
            return None
        return min(vals), max(vals), sum(vals) / len(vals)

    for col in ["Gb(i)", "Gd(i)", "H_sun", "T2m", "WS10m"]:
        s = col_stats(col)
        if s:
            print(f"  {col:<8}: min={s[0]:.1f}, max={s[1]:.1f}, avg={s[2]:.1f}")

    ghi_annual = sum(h.get("Gb(i)", 0) + h.get("Gd(i)", 0) for h in hourly) / 1000
    print(f"\n  Suma roczna GHI (Gb+Gd): {ghi_annual:.1f} kWh/m²")
