import requests

BASE = "https://re.jrc.ec.europa.eu/api/v5_3/PVcalc"

LAT = 50.062
LON = 19.937

MONTHS_PL = ["Sty", "Lut", "Mar", "Kwi", "Maj", "Cze",
             "Lip", "Sie", "Wrz", "Paź", "Lis", "Gru"]

def extract_angles(data):
    mount = data.get("inputs", {}).get("mounting_system", {}).get("fixed", {})
    angle = mount.get("slope", {}).get("value", "N/A")
    aspect = mount.get("azimuth", {}).get("value", "N/A")
    return angle, aspect

def get_pv_output(angle, aspect=0, optimalangles=0):
    params = dict(
        lat=LAT, lon=LON,
        raddatabase="PVGIS-SARAH3",
        peakpower=1,
        loss=14,
        angle=angle,
        aspect=aspect,
        outputformat="json",
        browser=0,
    )
    if optimalangles:
        params["optimalangles"] = 1
    r = requests.get(BASE, params=params)
    r.raise_for_status()
    return r.json()

print("=== Zadanie 12: System 1 kWp — wolnostojący vs. BIPV ===")
print(f"Lokalizacja: Kraków ({LAT}°N, {LON}°E)")
print(f"Baza danych: PVGIS-SARAH3\n")

print("Pobieranie wyników dla systemu wolnostojącego (kąt optymalny)...")
data_free = get_pv_output(angle=0, optimalangles=1)
totals_free = data_free["outputs"]["totals"]["fixed"]
monthly_free = data_free["outputs"]["monthly"]["fixed"]

opt_angle, opt_aspect = extract_angles(data_free)
e_y_free = totals_free["E_y"]

print(f"  Kąt optymalny: {opt_angle}°, Azymut: {opt_aspect}°")
print(f"  Roczna produkcja E_y = {e_y_free:.1f} kWh/kWp\n")

print("Pobieranie wyników dla BIPV (kąt=90°, fasada południowa)...")
data_bipv = get_pv_output(angle=90, aspect=0)
totals_bipv = data_bipv["outputs"]["totals"]["fixed"]
monthly_bipv = data_bipv["outputs"]["monthly"]["fixed"]
e_y_bipv = totals_bipv["E_y"]

spadek = (e_y_free - e_y_bipv) / e_y_free * 100
print(f"  Kąt: 90° (pionowa fasada), Azymut: 0° (południe)")
print(f"  Roczna produkcja E_y = {e_y_bipv:.1f} kWh/kWp\n")

print(f"=== Porównanie roczne ===")
print(f"  Wolnostojący (optymalny):   {e_y_free:>8.1f} kWh/kWp")
print(f"  BIPV (90°, południe):        {e_y_bipv:>8.1f} kWh/kWp")
print(f"  Spadek produkcji BIPV:       {spadek:>8.1f}%")
print()
print(f"{'Miesiąc':>8} | {'Wolnostojący [kWh]':>20} | {'BIPV 90° [kWh]':>16} | {'Różnica [%]':>12}")
print("-" * 65)

for i, (mf, mb) in enumerate(zip(monthly_free, monthly_bipv)):
    ef = mf["E_m"]
    eb = mb["E_m"]
    diff = (ef - eb) / ef * 100 if ef > 0 else 0
    print(f"{MONTHS_PL[i]:>8} | {ef:>20.2f} | {eb:>16.2f} | {diff:>11.1f}%")

print()
print("Wniosek: Główna przyczyna spadku produkcji BIPV to pionowe zamontowanie modułów (90°).")
print("Promieniowanie bezpośrednie pada pod dużym kątem padania przez większość roku,")
print("szczególnie latem gdy Słońce jest wysoko — moduły pionowe 'patrzą w bok' od Słońca.")
