import requests

BASE_SERIES = "https://re.jrc.ec.europa.eu/api/v5_3/seriescalc"

locations = [
    ("Norway/Oslo",       59.9, 10.7),
    ("Sweden/Stockholm",  59.3, 18.1),
    ("Finland/Helsinki",  60.2, 25.0),
    ("UK/London",         51.5, -0.1),
    ("Ireland/Dublin",    53.3, -6.3),
    ("Germany/Berlin",    52.5, 13.4),
    ("Poland/Warsaw",     52.2, 21.0),
    ("France/Paris",      48.8,  2.3),
    ("Czechia/Prague",    50.1, 14.4),
    ("Austria/Vienna",    48.2, 16.4),
    ("Switzerland/Bern",  46.9,  7.4),
    ("Croatia/Zagreb",    45.8, 16.0),
    ("Italy/Rome",        41.9, 12.5),
    ("Spain/Madrid",      40.4, -3.7),
    ("Spain/Seville",     37.4, -5.9),
    ("Portugal/Lisbon",   38.7, -9.1),
    ("Greece/Athens",     37.9, 23.7),
    ("Malta/Valletta",    35.9, 14.5),
    ("Cyprus/Nicosia",    35.2, 33.4),
    ("Romania/Bucharest", 44.4, 26.1),
]

def get_annual_yield(lat, lon, trackingtype=0, optimalinclination=0):
    """Get annual PV yield using seriescalc with tracking option"""
    params = dict(
        lat=lat, lon=lon,
        peakpower=1, loss=14,
        pvcalculation=1,
        trackingtype=trackingtype,
        outputformat="json"
    )
    if optimalinclination:
        params["optimalinclination"] = 1
    r = requests.get(BASE_SERIES, params=params)
    data = r.json()
    hourly = data["outputs"]["hourly"]
    return sum(h["P"] for h in hourly if "P" in h)

print(f"{'Lokalizacja':<24} {'Lat':>5} {'E_y stały':>11} {'E_y tracker':>12} {'Przyrost':>10}")
print("-" * 67)

for name, lat, lon in locations:
    e_fixed   = get_annual_yield(lat, lon, trackingtype=0)
    e_tracker = get_annual_yield(lat, lon, trackingtype=4, optimalinclination=1)
    gain = (e_tracker - e_fixed) / e_fixed * 100 if e_fixed > 0 else 0
    print(f"{name:<24} {lat:>5.1f} {e_fixed:>9.1f}   {e_tracker:>10.1f}   {gain:>8.1f}%")
