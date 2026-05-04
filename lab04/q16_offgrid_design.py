import requests
import time

BASE = "https://re.jrc.ec.europa.eu/api/v5_3/SHScalc"

LAT = 50.062
LON = 19.937

# System requirements (task 16)
CONSUMER_POWER_W = 42
CONSUMPTION_DAY_WH = CONSUMER_POWER_W * 24       # 1008 Wh/day
AUTONOMY_DAYS = 7
USABLE_BATTERY_WH = CONSUMPTION_DAY_WH * AUTONOMY_DAYS  # 7056 Wh
CUTOFF_PCT = 40
NOMINAL_BATTERY_WH = int(USABLE_BATTERY_WH / (1 - CUTOFF_PCT / 100))  # 11760 Wh

MONTHS_PL = ["Sty", "Lut", "Mar", "Kwi", "Maj", "Cze",
             "Lip", "Sie", "Wrz", "Paź", "Lis", "Gru"]

# Uniform 24h consumption profile (constant 42W throughout the day)
HOUR_CONSUMPTION = ",".join([f"{1/24:.6f}"] * 24)

def call_shscalc(peakpower, angle):
    params = dict(
        lat=LAT, lon=LON,
        raddatabase="PVGIS-SARAH3",
        peakpower=peakpower,
        batterysize=NOMINAL_BATTERY_WH,
        cutoff=CUTOFF_PCT,
        consumptionday=CONSUMPTION_DAY_WH,
        hourconsumption=HOUR_CONSUMPTION,
        angle=angle,
        aspect=0,
        outputformat="json",
        browser=0,
    )
    r = requests.get(BASE, params=params)
    if r.status_code == 429 or r.status_code == 529:
        time.sleep(2)
        r = requests.get(BASE, params=params)
    r.raise_for_status()
    return r.json()

def max_fe(data):
    monthly = data["outputs"]["monthly"]
    return max(m.get("f_e", 0) for m in monthly)

def worst_month_fe(data):
    monthly = data["outputs"]["monthly"]
    worst = max(monthly, key=lambda m: m.get("f_e", 0))
    idx = monthly.index(worst)
    return MONTHS_PL[idx], worst.get("f_e", 0)

print("=== Zadanie 16: Projekt wyspowego systemu fotowoltaicznego ===\n")
print(f"Lokalizacja: Kraków ({LAT}°N, {LON}°E)")
print(f"Baza danych: PVGIS-SARAH3")
print(f"Odbiornik: {CONSUMER_POWER_W} W, ciągły pobór mocy (24h/dobę)")
print(f"Zapotrzebowanie: {CONSUMPTION_DAY_WH} Wh/dobę")
print(f"Wymagana autonomia: {AUTONOMY_DAYS} dni")
print(f"Pojemność użytkowa akumulatora: {USABLE_BATTERY_WH} Wh")
print(f"Poziom odcięcia: {CUTOFF_PCT}%")
print(f"Pojemność nominalna akumulatora: {NOMINAL_BATTERY_WH} Wh\n")

# Phase 1: grid search to find minimum peakpower
PEAKPOWERS = [500, 750, 1000, 1250, 1500, 1750, 2000, 2500, 3000]
ANGLES = [50, 55, 60, 65, 70]

print("--- Faza 1: Przeszukiwanie siatki (peakpower × kąt nachylenia) ---")
print(f"Kryterium: f_e = 0% we wszystkich miesiącach (brak dni bez zasilania)\n")

header = f"{'Moc[Wp]':>9}" + "".join(f" | kąt {a:>2}° (f_e%)" for a in ANGLES)
print(header)
print("-" * len(header))

best_peakpower = None
best_angle = None
grid_results = {}

for pp in PEAKPOWERS:
    row = f"{pp:>9}"
    for angle in ANGLES:
        data = call_shscalc(pp, angle)
        fe_max = max_fe(data)
        grid_results[(pp, angle)] = (fe_max, data)
        marker = " ✓" if fe_max == 0 else ""
        row += f" | {fe_max:>12.1f}{marker}"
        if fe_max == 0 and best_peakpower is None:
            best_peakpower = pp
            best_angle = angle
    print(row)

print()

if best_peakpower is None:
    print("UWAGA: Żadna kombinacja nie osiągnęła f_e=0% — rozszerz zakres mocy!")
else:
    print(f"=== Rekomendacja projektowa ===")
    print(f"  Minimalna moc PV: {best_peakpower} Wp")
    print(f"  Optymalny kąt nachylenia: {best_angle}°")
    print(f"  Azymut: 0° (południe)")
    print(f"  Pojemność nominalna akumulatora: {NOMINAL_BATTERY_WH} Wh")
    print(f"  Pojemność użytkowa: {USABLE_BATTERY_WH} Wh (autonomia {AUTONOMY_DAYS} dni)")
    print()

    _, best_data = grid_results[(best_peakpower, best_angle)]
    monthly = best_data["outputs"]["monthly"]
    totals = best_data["outputs"]["totals"]

    print(f"--- Miesięczny bilans energetyczny (moc={best_peakpower} Wp, kąt={best_angle}°) ---")
    print(f"{'Miesiąc':>8} | {'Produkcja[Wh/d]':>16} | {'Zapotrzeb.[Wh/d]':>17} | {'Nadwyżka[Wh/d]':>15} | {'f_e[%]':>8} | {'f_f[%]':>8}")
    print("-" * 85)

    for i, m in enumerate(monthly):
        e_d = m.get("E_d", 0)
        e_lost = m.get("E_lost_d", 0)
        fe = m.get("f_e", 0)
        ff = m.get("f_f", 0)
        surplus = e_d - CONSUMPTION_DAY_WH
        print(f"{MONTHS_PL[i]:>8} | {e_d:>16.1f} | {CONSUMPTION_DAY_WH:>17.1f} | {surplus:>+15.1f} | {fe:>8.1f} | {ff:>8.1f}")

    print()
    e_miss_annual = totals.get("E_miss", 0)
    e_lost_annual = totals.get("E_lost", 0)
    ff_annual = totals.get("f_f", 0)
    fe_annual = totals.get("f_e", 0)
    print(f"=== Podsumowanie roczne ===")
    print(f"  Średni dzienny deficyt energii:   {e_miss_annual:.1f} Wh/d")
    print(f"  Średnia dzienna nadwyżka (straty): {e_lost_annual:.1f} Wh/d")
    print(f"  % dni z pełnym akumulatorem:       {ff_annual:.1f}%")
    print(f"  % dni z pustym akumulatorem:       {fe_annual:.1f}%")
    print()
    print("=== Wnioski ===")
    print(f"Zaprojektowany system: {best_peakpower} Wp modułów PV + {NOMINAL_BATTERY_WH} Wh akumulatorów")
    print(f"Kąt nachylenia {best_angle}° (stromszy niż optymalny roczny ~38°) optymalizuje")
    print(f"produkcję zimową, gdy Słońce jest nisko nad horyzontem.")
    print(f"Latem system generuje znaczne nadwyżki (akumulator pełny {ff_annual:.0f}% dni),")
    print(f"co jest typowe dla systemów wyspowych projektowanych na pokrycie zimy.")
    print(f"Pojemność akumulatora {NOMINAL_BATTERY_WH} Wh zapewnia {AUTONOMY_DAYS}-dniową")
    print(f"autonomię przy poborze {CONSUMER_POWER_W} W bez nasłonecznienia.")
