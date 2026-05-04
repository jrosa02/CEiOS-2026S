import requests
from collections import defaultdict

BASE = "https://re.jrc.ec.europa.eu/api/v5_3/seriescalc"

LAT = 50.062
LON = 19.937
TARGET_MONTHS = {6: "Czerwiec", 9: "Wrzesień", 12: "Grudzień"}

def fetch_hourly(angle):
    params = dict(
        lat=LAT, lon=LON,
        raddatabase="PVGIS-SARAH3",
        peakpower=1, loss=14,
        angle=angle,
        aspect=0,
        pvcalculation=0,
        components=1,
        startyear=2023, endyear=2023,
        outputformat="json",
        browser=0,
    )
    r = requests.get(BASE, params=params)
    r.raise_for_status()
    return r.json()["outputs"]["hourly"]

def parse_time(t):
    """Parse PVGIS time string 'YYYYMMDD:HHMM' → (month, day, hour)"""
    t = str(t)
    date_part, time_part = t.split(":")
    month = int(date_part[4:6])
    day = int(date_part[6:8])
    hour = int(time_part[:2])
    return month, day, hour

def gi(h):
    """Total irradiance on plane = Gb(i) + Gd(i) + Gr(i)"""
    return h.get("Gb(i)", 0) + h.get("Gd(i)", 0) + h.get("Gr(i)", 0)

def group_by_month_day(hourly):
    by_month = defaultdict(lambda: defaultdict(list))
    for h in hourly:
        month, day, _ = parse_time(h["time"])
        by_month[month][day].append(h)
    return by_month

print("Pobieranie danych godzinowych z PVGIS-SARAH3 dla Krakowa (2023)...")
print(f"Lokalizacja: lat={LAT}, lon={LON}\n")

hourly_35 = fetch_hourly(angle=35)
hourly_horiz = fetch_hourly(angle=0)

by_month_35 = group_by_month_day(hourly_35)
by_month_horiz = group_by_month_day(hourly_horiz)

print("=== Zadanie 4: Dzienna dostępność promieniowania słonecznego ===\n")

for month_num, month_name in TARGET_MONTHS.items():
    print(f"--- {month_name} (miesiąc {month_num}) ---")
    print(f"{'Dzień':>5} | {'H(i) 35° [kWh/m²]':>20} | {'H(h) 0° [kWh/m²]':>20} | {'Zysk [%]':>10}")
    print("-" * 65)

    days_35 = by_month_35.get(month_num, {})
    days_h = by_month_horiz.get(month_num, {})
    monthly_sum_35 = 0
    monthly_sum_h = 0

    for day in sorted(set(days_35.keys()) | set(days_h.keys())):
        g_i = sum(gi(h) for h in days_35.get(day, [])) / 1000
        g_h = sum(gi(h) for h in days_h.get(day, [])) / 1000
        zysk = (g_i - g_h) / g_h * 100 if g_h > 0 else 0
        print(f"{day:>5} | {g_i:>20.3f} | {g_h:>20.3f} | {zysk:>9.1f}%")
        monthly_sum_35 += g_i
        monthly_sum_h += g_h

    total_gain = (monthly_sum_35 - monthly_sum_h) / monthly_sum_h * 100 if monthly_sum_h > 0 else 0
    print(f"{'SUMA':>5} | {monthly_sum_35:>20.3f} | {monthly_sum_h:>20.3f} | {total_gain:>9.1f}%")
    print()

print("=== Zadanie 5 i 6: Analiza promieniowania w okolicach południa słonecznego ===\n")

print(f"{'Miesiąc':>10} | {'Śr. G(i) 35° [W/m²]':>22} | {'Śr. G(h) [W/m²]':>18} | {'Śr. Kd':>8} | {'Opis zachmurzenia':>20}")
print("-" * 90)

for month_num, month_name in TARGET_MONTHS.items():
    days_35 = by_month_35.get(month_num, {})
    days_h = by_month_horiz.get(month_num, {})

    noon_35 = [h for day in days_35.values() for h in day if parse_time(h["time"])[2] in (11, 12, 13)]
    noon_h = [h for day in days_h.values() for h in day if parse_time(h["time"])[2] in (11, 12, 13)]

    if not noon_35:
        continue

    avg_gi = sum(gi(h) for h in noon_35) / len(noon_35)
    avg_gh = sum(gi(h) for h in noon_h) / len(noon_h) if noon_h else 0

    kd_vals = [h.get("Gd(i)", 0) / gi(h) for h in noon_35 if gi(h) > 10]
    avg_kd = sum(kd_vals) / len(kd_vals) if kd_vals else 0

    if avg_kd > 0.7:
        cloud_desc = "silne zachmurzenie"
    elif avg_kd > 0.4:
        cloud_desc = "umiarkowane"
    else:
        cloud_desc = "czyste niebo"

    print(f"{month_name:>10} | {avg_gi:>22.1f} | {avg_gh:>18.1f} | {avg_kd:>8.3f} | {cloud_desc:>20}")

print()
print("Wniosek (zadanie 5): Kd → 1 oznacza dominację promieniowania rozproszonego (zachmurzenie).")
print("  Grudzień: niskie Słońce, krótki dzień → największy udział rozproszenia.")
print("  Czerwiec: możliwe czyste niebo, ale też zachmurzenie konwekcyjne.")
print()
print("Wniosek (zadanie 6): Zysk z nachylenia 35° największy w grudniu,")
print("  gdyż Słońce jest nisko (kąt elewacji ~17°), a płaszczyzna 35° jest do niego prostopadła.")
print("  W czerwcu Słońce jest wysoko (~63°), więc zysk z pochylenia jest mniejszy.")
