import requests
import os

BASE_PVCALC = "https://re.jrc.ec.europa.eu/api/v5_3/PVcalc"

LAT = 50.062
LON = 19.937
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(OUT_DIR, exist_ok=True)

MONTHS_PL = ["Sty", "Lut", "Mar", "Kwi", "Maj", "Cze",
             "Lip", "Sie", "Wrz", "Paź", "Lis", "Gru"]

# Task 13: custom horizon file
# N→E→S (azimuths 0°–170°): 10°  |  S→W→N (azimuths 180°–350°): 20°
HORIZON_HEIGHTS = [10] * 18 + [20] * 18   # 36 values, every 10°

def write_horizon_csv():
    path = os.path.join(OUT_DIR, "horizon_krakow.csv")
    with open(path, "w") as f:
        for i, h in enumerate(HORIZON_HEIGHTS):
            azimuth = i * 10
            f.write(f"{azimuth},{h}\n")
    print(f"Zapisano plik horyzontu: horizon_krakow.csv ({len(HORIZON_HEIGHTS)} wierszy)")
    print("Format: azymut[°], wysokość_horyzontu[°]")
    print()
    print("Zawartość pliku horyzontu:")
    for i, h in enumerate(HORIZON_HEIGHTS):
        print(f"  {i*10:>4}°  →  {h}°")
    print()

def extract_angles(data):
    mount = data.get("inputs", {}).get("mounting_system", {}).get("fixed", {})
    angle = mount.get("slope", {}).get("value", "N/A")
    aspect = mount.get("azimuth", {}).get("value", "N/A")
    return angle, aspect

def get_pvcalc(optimalangles=1, userhorizon=None):
    params = dict(
        lat=LAT, lon=LON,
        raddatabase="PVGIS-SARAH3",
        peakpower=1, loss=14,
        aspect=0,
        outputformat="json",
        browser=0,
    )
    if optimalangles:
        params["optimalangles"] = 1
    if userhorizon is not None:
        params["usehorizon"] = 1
        params["userhorizon"] = ",".join(str(h) for h in userhorizon)
    else:
        params["usehorizon"] = 0

    r = requests.get(BASE_PVCALC, params=params)
    r.raise_for_status()
    return r.json()

print("=== Zadanie 13: Plik obrysu horyzontu ===\n")
write_horizon_csv()

print("=== Zadanie 14: Symulacja z niestandardowym horyzontem vs bez horyzontu ===\n")
print(f"Lokalizacja: Kraków ({LAT}°N, {LON}°E)")
print(f"Baza danych: PVGIS-SARAH3, moc systemu: 1 kWp\n")

print("Pobieranie wyników BEZ horyzontu (referencja — zadanie 12)...")
data_no_hor = get_pvcalc(optimalangles=1, userhorizon=None)
totals_no = data_no_hor["outputs"]["totals"]["fixed"]
monthly_no = data_no_hor["outputs"]["monthly"]["fixed"]
angle_no, aspect_no = extract_angles(data_no_hor)
ey_no = totals_no["E_y"]
print(f"  Kąt optymalny: {angle_no}°, Azymut: {aspect_no}°")
print(f"  Roczna produkcja E_y = {ey_no:.1f} kWh/kWp\n")

print("Pobieranie wyników Z niestandardowym horyzontem (zadanie 14)...")
data_hor = get_pvcalc(optimalangles=1, userhorizon=HORIZON_HEIGHTS)
totals_hor = data_hor["outputs"]["totals"]["fixed"]
monthly_hor = data_hor["outputs"]["monthly"]["fixed"]
angle_hor, aspect_hor = extract_angles(data_hor)
ey_hor = totals_hor["E_y"]
print(f"  Kąt optymalny (z horyzontem): {angle_hor}°, Azymut: {aspect_hor}°")
print(f"  Roczna produkcja E_y = {ey_hor:.1f} kWh/kWp\n")

diff_annual = (ey_hor - ey_no) / ey_no * 100
print(f"=== Porównanie roczne ===")
print(f"  Bez horyzontu:    {ey_no:>8.1f} kWh/kWp  (kąt {angle_no}°)")
print(f"  Z horyzontem:     {ey_hor:>8.1f} kWh/kWp  (kąt {angle_hor}°)")
print(f"  Zmiana:           {diff_annual:>+8.1f}%\n")

print(f"{'Miesiąc':>8} | {'Bez horyzontu [kWh]':>20} | {'Z horyzontem [kWh]':>20} | {'Zmiana [%]':>12}")
print("-" * 70)
for i, (mn, mh) in enumerate(zip(monthly_no, monthly_hor)):
    en = mn["E_m"]
    eh = mh["E_m"]
    diff = (eh - en) / en * 100 if en > 0 else 0
    print(f"{MONTHS_PL[i]:>8} | {en:>20.2f} | {eh:>20.2f} | {diff:>11.1f}%")

print()
print("=== Analiza wpływu horyzontu ===")
print(f"Strona południowa (180–350°): horyzont 20° blokuje promieniowanie bezpośrednie")
print(f"  przy niskim kącie elewacji Słońca — najsilniejszy efekt zimą (grudzień–luty).")
print(f"Strona północna (0–170°): horyzont 10° — mniejszy wpływ na produkcję,")
print(f"  gdyż Słońce w Polsce nigdy nie wschodzi od północy.")
print(f"Zmiana optymalnego kąta nachylenia: z {angle_no}° na {angle_hor}° —")
if str(angle_hor) != str(angle_no):
    print(f"  PVGIS dostosował kąt uwzględniając zacienienie od południa.")
else:
    print(f"  kąt pozostał niezmieniony (horyzont nie wpłynął na optymalizację).")
