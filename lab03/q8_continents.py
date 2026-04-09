import requests

BASE = "https://re.jrc.ec.europa.eu/api/v5_3/MRcalc"

locations = [
    # Ameryka Północna
    ("Phoenix (US)",      "Ameryka",    33.4,-112.1),
    ("Las Vegas (US)",    "Ameryka",    36.2,-115.1),
    ("Miami (US)",        "Ameryka",    25.8, -80.2),
    ("New York (US)",     "Ameryka",    40.7, -74.0),
    ("Mexico City (MX)",  "Ameryka",    19.4,-99.1),
    ("Tromso (NO)",       "Ameryka",    69.7,  19.0),
    # Ameryka Południowa
    ("Santiago (CL)",     "Ameryka",   -33.4, -70.6),
    ("Lima (PE)",         "Ameryka",   -12.1, -77.0),
    ("Sao Paulo (BR)",    "Ameryka",   -23.6, -46.6),
    ("Manaus (BR)",       "Ameryka",    -3.1, -60.0),
    ("Buenos Aires (AR)", "Ameryka",   -34.6, -58.4),

    # Europa
    ("Reykjavik (IS)",    "Europa",     64.1, -21.9),
    ("Oslo (NO)",         "Europa",     59.9,  10.7),
    ("Helsinki (FI)",     "Europa",     60.2,  25.0),
    ("Stockholm (SE)",    "Europa",     59.3,  18.1),
    ("Warsaw (PL)",       "Europa",     52.2,  21.0),
    ("London (GB)",       "Europa",     51.5,  -0.1),
    ("Berlin (DE)",       "Europa",     52.5,  13.4),
    ("Prague (CZ)",       "Europa",     50.1,  14.4),
    ("Vienna (AT)",       "Europa",     48.2,  16.4),
    ("Madrid (ES)",       "Europa",     40.4,  -3.7),
    ("Seville (ES)",      "Europa",     37.4,  -5.9),
    ("Lisbon (PT)",       "Europa",     38.7,  -9.1),
    ("Rome (IT)",         "Europa",     41.9,  12.5),
    ("Athens (GR)",       "Europa",     37.9,  23.7),
    ("Palermo (IT)",      "Europa",     38.1,  13.4),

    # Afryka
    ("Cairo (EG)",        "Afryka",     30.0,  31.2),
    ("Marrakesh (MA)",    "Afryka",     31.6,  -8.0),
    ("Tripoli (LY)",      "Afryka",     32.9,  13.2),
    ("Nairobi (KE)",      "Afryka",     -1.3,  36.8),
    ("Lagos (NG)",        "Afryka",      6.5,   3.4),
    ("Kinshasa (CD)",     "Afryka",     -4.3,  15.3),
    ("Cape Town (ZA)",    "Afryka",    -33.9,  18.4),
    ("Johannesburg (ZA)", "Afryka",    -26.2,  28.0),

    # Azja
    ("Riyadh (SA)",       "Azja",       24.7,  46.7),
    ("Dubai (AE)",        "Azja",       25.3,  55.3),
    ("Tehran (IR)",       "Azja",       35.7,  51.4),
    ("New Delhi (IN)",    "Azja",       28.6,  77.2),
    ("Mumbai (IN)",       "Azja",       19.1,  72.9),
    ("Colombo (LK)",      "Azja",        6.9,  80.6),
    ("Beijing (CN)",      "Azja",       39.9, 116.4),
    ("Shanghai (CN)",     "Azja",       31.2, 121.5),
    ("Tokyo (JP)",        "Azja",       35.7, 139.7),
    ("Singapore (SG)",    "Azja",        1.3, 103.8),
    ("Bangkok (TH)",      "Azja",       13.7, 100.5),
    ("Jakarta (ID)",      "Azja",       -6.2, 106.8),

    # Australia i Oceania
    ("Perth (AU)",        "Australia/Oceania", -31.9, 115.9),
    ("Sydney (AU)",       "Australia/Oceania", -33.9, 151.2),
    ("Melbourne (AU)",    "Australia/Oceania", -37.8, 144.9),
]

def annual_ghi(lat, lon):
    r = requests.get(BASE, params=dict(
        lat=lat, lon=lon,
        horirrad=1,
        outputformat="json"
    ))
    monthly = r.json()["outputs"]["monthly"]
    return sum(m["H(h)_m"] for m in monthly)

print(f"{'Lokalizacja':<22} {'Kontynent':<22} {'GHI roczne [kWh/m²/rok]':>25}")
print("-" * 72)

results = []
for name, region, lat, lon in locations:
    ghi = annual_ghi(lat, lon)
    results.append((name, region, ghi))
    print(f"{name:<22} {region:<14} {ghi:>20.1f}")

# Statystyka po kontynentach
print("\n" + "="*80)
print("PODSUMOWANIE STATYSTYCZNE PO KONTYNENTACH")
print("="*80)

continents = {}
for name, continent, ghi in results:
    if continent not in continents:
        continents[continent] = []
    continents[continent].append(ghi)

for continent in sorted(continents.keys()):
    values = continents[continent]
    mean = sum(values) / len(values)
    min_val = min(values)
    max_val = max(values)
    spread = max_val - min_val
    variance = sum((x - mean)**2 for x in values) / len(values)
    std_dev = variance ** 0.5

    print(f"\n{continent:<22} | N={len(values):2d} | Śr={mean:7.1f} | Min={min_val:7.1f} | Max={max_val:7.1f} | σ={std_dev:6.1f} | Rozstęp={spread:7.1f} [kWh/m²/rok]")

# Ogólne statystyki
print("\n" + "-"*80)
all_values = [ghi for _, _, ghi in results]
all_mean = sum(all_values) / len(all_values)
all_min = min(all_values)
all_max = max(all_values)
all_std = (sum((x - all_mean)**2 for x in all_values) / len(all_values)) ** 0.5

print(f"ŚWIAT (razem)        | N={len(all_values):2d} | Śr={all_mean:7.1f} | Min={all_min:7.1f} | Max={all_max:7.1f} | σ={all_std:6.1f} | Rozstęp={all_max-all_min:7.1f} [kWh/m²/rok]")
