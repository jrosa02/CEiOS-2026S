import requests
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from collections import defaultdict

BASE = "https://re.jrc.ec.europa.eu/api/v5_3/seriescalc"

LAT = 50.062
LON = 19.937
TARGET_MONTHS = {6: "Czerwiec", 9: "Wrzesień", 12: "Grudzień"}
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imgs")
os.makedirs(OUT_DIR, exist_ok=True)


def parse_time(t):
    t = str(t)
    date_part, time_part = t.split(":")
    return int(date_part[4:6]), int(date_part[6:8]), int(time_part[:2])


def gi(h):
    return h.get("Gb(i)", 0) + h.get("Gd(i)", 0) + h.get("Gr(i)", 0)


def fetch_pv_hourly(trackingtype=None, angle=None):
    """Fetch hourly PV output [W] — works correctly with trackingtype."""
    params = dict(
        lat=LAT, lon=LON,
        raddatabase="PVGIS-SARAH3",
        peakpower=1, loss=14,
        pvcalculation=1,
        startyear=2023, endyear=2023,
        outputformat="json", browser=0,
    )
    if trackingtype is not None:
        params["trackingtype"] = trackingtype
    if angle is not None:
        params["angle"] = angle
        params["aspect"] = 0
    r = requests.get(BASE, params=params)
    r.raise_for_status()
    return r.json()["outputs"]["hourly"]


def fetch_irradiance_hourly(angle):
    """Fetch hourly irradiance components [W/m²] for fixed plane."""
    params = dict(
        lat=LAT, lon=LON,
        raddatabase="PVGIS-SARAH3",
        pvcalculation=0, components=1,
        angle=angle, aspect=0,
        startyear=2023, endyear=2023,
        outputformat="json", browser=0,
    )
    r = requests.get(BASE, params=params)
    r.raise_for_status()
    return r.json()["outputs"]["hourly"]


def avg_hourly_profile(hourly, value_fn):
    """Average value per hour-of-day for each target month.
    Returns {month: {hour: avg_value}}"""
    acc = defaultdict(lambda: defaultdict(list))
    for h in hourly:
        month, _, hour = parse_time(h["time"])
        acc[month][hour].append(value_fn(h))
    return {m: {hr: np.mean(vals) for hr, vals in hrs.items()}
            for m, hrs in acc.items()}


print("Pobieranie danych godzinowych z PVGIS-SARAH3 dla Krakowa (2023)...")
print(f"Lokalizacja: lat={LAT}, lon={LON}\n")

# PV power output for charts (trackingtype works correctly here)
hourly_35_pv  = fetch_pv_hourly(angle=35)
hourly_2ax_pv = fetch_pv_hourly(trackingtype=4)

# Irradiance components for tasks 5 & 6 (Kd analysis, fixed plane only)
hourly_35_irr = fetch_irradiance_hourly(angle=35)

profiles_35  = avg_hourly_profile(hourly_35_pv,  lambda h: h.get("P", 0))
profiles_2ax = avg_hourly_profile(hourly_2ax_pv, lambda h: h.get("P", 0))

# ── Task 4: charts ─────────────────────────────────────────────────────────
print("=== Zadanie 4: Wykresy średnich dobowych profili promieniowania ===\n")

fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=False)
fig.suptitle(
    "Średni dobowy profil promieniowania słonecznego — Kraków 2023\n"
    "PVGIS-SARAH3 | stacjonarny 35° (S) vs. układ nadążny 2-osiowy",
    fontsize=11,
)

for ax, (month_num, month_name) in zip(axes, TARGET_MONTHS.items()):
    p35  = profiles_35.get(month_num, {})
    p2ax = profiles_2ax.get(month_num, {})
    hrs = sorted(set(p35) | set(p2ax))

    ax.plot(hrs, [p35.get(h, 0)  for h in hrs], label="Stacjonarny 35°, S",
            color="#e07b00", linewidth=2)
    ax.plot(hrs, [p2ax.get(h, 0) for h in hrs], label="Śledzenie 2-osiowe",
            color="#1a6faf", linewidth=2, linestyle="--")

    ax.set_title(month_name, fontsize=12)
    ax.set_xlabel("Godzina")
    ax.set_ylabel("Średnia moc PV [W/kWp]")
    ax.set_xlim(0, 23)
    ax.set_ylim(bottom=0)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(4))
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8)

plt.tight_layout()
out_path = os.path.join(OUT_DIR, "q4_daily_profiles.png")
plt.savefig(out_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Zapisano wykres: {out_path}\n")

# ── Task 4: monthly summary table ──────────────────────────────────────────
print(f"{'Miesiąc':>10} | {'H(35°) [kWh/m²/d]':>20} | {'H(2ax) [kWh/m²/d]':>20} | {'Zysk [%]':>10}")
print("-" * 68)
for month_num, month_name in TARGET_MONTHS.items():
    p35  = profiles_35.get(month_num, {})
    p2ax = profiles_2ax.get(month_num, {})
    # W → kWh/day (each value is avg W per hour, sum over 24h / 1000)
    s35  = sum(p35.values())  / 1000
    s2ax = sum(p2ax.values()) / 1000
    gain = (s2ax - s35) / s35 * 100 if s35 > 0 else 0
    print(f"{month_name:>10} | {s35:>20.3f} | {s2ax:>20.3f} | {gain:>9.1f}%")

# ── Tasks 5 & 6: noon-hour analysis (using irradiance components) ──────────
print("\n=== Zadania 5 i 6: Promieniowanie w okolicach południa słonecznego ===\n")
print(f"{'Miesiąc':>10} | {'G(35°) [W/m²]':>15} | {'G(2ax) [W]':>12} | {'Kd(35°)':>9} | {'Abs. chmur [%]':>15} | {'Zysk 2ax [%]':>13}")
print("-" * 85)

NOON_HOURS = (11, 12, 13)

for month_num, month_name in TARGET_MONTHS.items():
    noon_irr = [h for h in hourly_35_irr
                if parse_time(h["time"])[0] == month_num
                and parse_time(h["time"])[2] in NOON_HOURS
                and gi(h) > 10]
    noon_2ax = [h for h in hourly_2ax_pv
                if parse_time(h["time"])[0] == month_num
                and parse_time(h["time"])[2] in NOON_HOURS
                and h.get("P", 0) > 5]
    noon_35p = [h for h in hourly_35_pv
                if parse_time(h["time"])[0] == month_num
                and parse_time(h["time"])[2] in NOON_HOURS
                and h.get("P", 0) > 5]

    if not noon_irr:
        continue

    avg_gi   = sum(gi(h) for h in noon_irr) / len(noon_irr)
    avg_2ax  = sum(h["P"] for h in noon_2ax) / len(noon_2ax) if noon_2ax else 0
    avg_35p  = sum(h["P"] for h in noon_35p) / len(noon_35p) if noon_35p else 0

    kd_vals = [h.get("Gd(i)", 0) / gi(h) for h in noon_irr]
    avg_kd  = sum(kd_vals) / len(kd_vals)

    # Cloud absorption: (1 - actual/clearsky). Approximate clearsky as actual/(1-kd_clear)
    # Simpler: use Kd as proxy — fraction of radiation that is diffuse (cloud-scattered)
    # Conservative estimate: cloud absorption ≈ max(0, Kd - 0.15) / (1 - 0.15) * 100
    # where 0.15 is typical clear-sky diffuse fraction
    cloud_abs = max(0.0, (avg_kd - 0.15) / 0.85) * 100

    gain_2ax = (avg_2ax - avg_35p) / avg_35p * 100 if avg_35p > 0 else 0

    print(f"{month_name:>10} | {avg_gi:>15.1f} | {avg_2ax:>12.1f} | {avg_kd:>9.3f} | {cloud_abs:>14.1f}% | {gain_2ax:>12.1f}%")

print()
print("Legenda:")
print("  G(35°) — średnia irradiancja na płaszczyźnie 35°/S w godzinach południowych [W/m²]")
print("  G(2ax) — średnia moc PV układu 2-osiowego w godzinach południowych [W/kWp]")
print("  Kd     — wskaźnik rozproszenia (0=czyste niebo, 1=całkowite zachmurzenie)")
print("  Abs. chmur — szacunkowy udział pochłoniętego przez chmury promieniowania")
print("  Zysk 2ax — wzrost mocy układu nadążnego względem stacjonarnego 35°")
print()
print("Wniosek (zadanie 5):")
print("  Grudzień: najwyższy Kd → chmury pochłaniają największy % promieniowania południowego.")
print("  Czerwiec: niższy Kd, mimo możliwych burz konwekcyjnych po południu.")
print()
print("Wniosek (zadanie 6):")
print("  W godzinach południowych zysk z 2-osiowego śledzenia jest stosunkowo mały —")
print("  Słońce jest wtedy najwyżej i panel 35° jest do niego dobrze skierowany.")
print("  Największy zysk z śledzenia pochodzi z godzin porannych i popołudniowych,")
print("  szczególnie latem gdy Słońce przesuwa się po szerokim łuku.")
