# Sprawozdanie z ćwiczenia nr 3: Czyste energie i ochrona środowiska

**Data wykonania:** 14.04.2026  
**Przedmiot:** Czyste energie i ochrona środowiska 2026  
**Ćwiczenie:** 3 – Portal PVGIS (Photovoltaic Geographical Information System) – źródło wiedzy oraz użyteczne narzędzia
z zakresu energetyki słonecznej.
**Autor:** Jan Rosa

---

## Pytania

1. Co to jest współczynnik PR i dlaczego nie wynosi 100%.
2. Na głównej mapie znajdź europejskie kraje o najmniejszym i największym potencjale
pozyskiwania energii słonecznej i wymień je wraz z odpowiednią mapą w sprawozdaniu.
3. Określ zakres optymalnych kątów pochylenia modułów fotowoltaicznych w Europie i wykaż od
jakiego parametru lokalizacyjnego (długość czy szerokość geograficzna) jest zależny ten kąt.
4. Postaraj się określić przybliżoną relację matematyczną między parametrem znalezionym w
poprzednim punkcie a optymalnym kątem pochylenia modułów fotowoltaicznych.
5. Jaki jest optymalny, całoroczny kąt pochylenia modułów fotowoltaicznych w Polsce?
6. Jakiego przyrostu produkcji energii z systemu fotowoltaicznego można się spodziewać w Europie
dzięki zastosowaniu jednoosiowego trackera ? Podaj zakres tego przyrostu. Wskaż kraje, w
których jest on największy i spróbuj wyjaśnić, dlaczego. Jaki przyrost produkcji energii
elektrycznej da zastosowanie jednoosiowego trackera w Polsce?
7. Porównaj dostępność energii słonecznej w Polskich miastach z innymi miastami w pozostałych
państwach europejskich. Porównanie ma dotyczyć zarówno wartości średniej jak i różnic dla
poszczególnych miast. Porównanie ma wykazać czy Polska charakteryzuje się w miarę jednakową
dostępnością energii słonecznej we wszystkich miastach czy też występują u nas zarówno
obszary o bardzo dobrych jak i o bardzo słabych warunkach słonecznych (np. jak we Włoszech
lub w UK).
8. Korzystając z darmowych map na komercyjnym portalu SolarGIS
(https://solargis.com/resources/free-maps-and-gis-data) porównaj dostępność energii
słonecznej w Europie i na innych kontynentach. Wnioski umieść w sprawozdaniu.
9. Wypełnij tabelę danymi z map wskazanych krajów.
10. Spróbuj wyjaśnić, dlaczego te same stawki taryf gwarantowanych (kwoty uzyskiwane za energię
wyprodukowaną w PV i wprowadzoną do publicznej sieci elektroenergetycznej ) w Niemczech
stymulowały równomierny rozwój branży a w Hiszpanii doprowadziły do lawinowego wzrostu
budowy farm PV i niemal spowodowały krach na rynku energii. Aby zrozumieć to zjawisko
sprawdź jaka jest istota taryf gwarantowanych (Feed-In Tariff) szczególnie w zakresie
fotowoltaiki, jaka była relacja ich stawek do cen energii sieciowej w na początku systemowego
rozwoju fotowoltaiki w danym kraju (np. Niemcy 2006, UK 2010) oraz kto tak naprawdę ponosi
koszty finansowania systemu taryf gwarantowanych?

---

## 1. Co to jest współczynnik PR i dlaczego nie wynosi 100%?

## 2. Na głównej mapie znajdź europejskie kraje o najmniejszym i największym potencjale pozyskiwania energii słonecznej i wymień je wraz z odpowiednią mapą w sprawozdaniu

## 3. Określ zakres optymalnych kątów pochylenia modułów fotowoltaicznych w Europie i wykaż od jakiego parametru lokalizacyjnego (długość czy szerokość geograficzna) jest zależny ten kąt

Location          Lat     Lon   OptAngle
------------------------------------------
Cyprus           34.9    33.0       30.0°
Malta            35.9    14.5       32.0°
Crete            35.3    25.1       28.0°
Athens           37.9    23.7       34.0°
Lisbon           38.7    -9.1       34.0°
Seville          37.4    -5.9       34.0°
Madrid           40.4    -3.7       38.0°
Rome             41.9    12.5       38.0°
Barcelona        41.4     2.2       38.0°
Zagreb           45.8    16.0       36.0°
Bern             46.9     7.4       40.0°
Vienna           48.2    16.4       38.0°
Paris            48.8     2.3       38.0°
Prague           50.1    14.4       38.0°
Warsaw           52.2    21.0       40.0°
London           51.5    -0.1       40.0°
Berlin           52.5    13.4       40.0°
Brussels         50.8     4.4       40.0°
Copenhagen       55.7    12.6       40.0°
Stockholm        59.3    18.1       44.0°
Helsinki         60.2    25.0       44.0°
Oslo             59.9    10.7       44.0°
Riga             56.9    24.1       42.0°
Reykjavik        64.1   -21.9       42.0°
Tromso           69.7    19.0       48.0°

## 4. Postaraj się określić przybliżoną relację matematyczną między parametrem znalezionym w poprzednim punkcie a optymalnym kątem pochylenia modułów fotowoltaicznych

Linear fit: optimal_angle ≈ 0.439 × lat + (17.02)
Angle range: 28.0° – 48.0°

## 5. Jaki jest optymalny, całoroczny kąt pochylenia modułów fotowoltaicznych w Polsce?

Miasto          Lat   Optymalny kąt
------------------------------------
Warszawa      52.23          40.0°
Kraków        50.06          40.0°
Gdańsk        54.35          42.0°
Wrocław       51.11          40.0°
Poznań        52.41          40.0°
Białystok     53.13          38.0°
Lublin        51.25          38.0°
Rzeszów       50.04          38.0°

Średnia: 39.5°  |  Rozstęp: 4.0°  |  Min: 38.0°  Max: 42.0°

## 6. Jakiego przyrostu produkcji energii z systemu fotowoltaicznego można się spodziewać w Europie dzięki zastosowaniu jednoosiowego trackera? Podaj zakres tego przyrostu. Wskaż kraje, w których jest on największy i spróbuj wyjaśnić, dlaczego. Jaki przyrost produkcji energii elektrycznej da zastosowanie jednoosiowego trackera w Polsce?

Lokalizacja                Lat   E_y stały  E_y tracker   Przyrost
-------------------------------------------------------------------
Norway/Oslo               59.9 13844532.3   20497476.1       48.1%
Sweden/Stockholm          59.3 14785608.8   21920448.5       48.3%
Finland/Helsinki          60.2 14693393.1   21629823.2       47.2%
UK/London                 51.5 15894818.8   21983570.0       38.3%
Ireland/Dublin            53.3 14835028.8   20172961.3       36.0%
Germany/Berlin            52.5 16399211.7   22984252.7       40.2%
Poland/Warsaw             52.2 16387988.6   22838456.1       39.4%
France/Paris              48.8 18145532.7   25341298.1       39.7%
Czechia/Prague            50.1 17218119.6   23849371.6       38.5%
Austria/Vienna            48.2 18431093.2   25542569.2       38.6%
Switzerland/Bern          46.9 19316657.7   27028846.3       39.9%
Croatia/Zagreb            45.8 19566773.1   26823177.3       37.1%
Italy/Rome                41.9 23702238.0   33799696.2       42.6%
Spain/Madrid              40.4 25762201.2   37341352.1       44.9%
Spain/Seville             37.4 27023395.5   38740149.1       43.4%
Portugal/Lisbon           38.7 25950059.0   37062134.3       42.8%
Greece/Athens             37.9 26597714.5   37251685.6       40.1%
Malta/Valletta            35.9 27523849.2   38272813.3       39.1%
Cyprus/Nicosia            35.2 27672051.9   38388827.6       38.7%
Romania/Bucharest         44.4 20816172.5   28398416.2       36.4%

## 7. Porównaj dostępność energii słonecznej w polskich miastach z innymi miastami w pozostałych państwach europejskich

Miasto         Kraj    GHI roczne [kWh/m²]
------------------------------------------
Warszawa         PL              21186.8
Kraków           PL              21778.1
Gdańsk           PL              20861.2
Wrocław          PL              21793.0
Poznań           PL              21161.6
Białystok        PL              20523.3
Oslo             NO              17968.9
Helsinki         FI              18764.5
Stockholm        SE              18883.6
London           GB              20434.8
Edinburgh        GB              17772.6
Berlin           DE              21249.6
Munich           DE              22975.6
Paris            FR              23415.4
Marseille        FR              31878.2
Madrid           ES              33809.9
Seville          ES              36055.8
Rome             IT              31220.8
Palermo          IT              33286.2
Athens           GR              34774.3

Polska  — średnia: 21217.3  odch.std: 458.0  min: 20523.3  max: 21793.0
Reszta EU — średnia: 25892.2  odch.std: 6857.7  min: 17772.6  max: 36055.8

## 8. Korzystając z darmowych map na komercyjnym portalu SolarGIS porównaj dostępność energii słonecznej w Europie i na innych kontynentach

Lokalizacja            Kontynent                GHI roczne [kWh/m²/rok]
------------------------------------------------------------------------
Phoenix (US)           Ameryka                     40763.2
Las Vegas (US)         Ameryka                     40417.5
Miami (US)             Ameryka                     35256.7
New York (US)          Ameryka                     28542.2
Mexico City (MX)       Ameryka                     39971.2
Tromso (NO)            Ameryka                     13577.6
Santiago (CL)          Ameryka                     40083.3
Lima (PE)              Ameryka                     42005.4
Sao Paulo (BR)         Ameryka                     31197.9
Manaus (BR)            Ameryka                     33747.0
Buenos Aires (AR)      Ameryka                     32451.7
Reykjavik (IS)         Europa                      14130.1
Oslo (NO)              Europa                      17968.9
Helsinki (FI)          Europa                      18764.5
Stockholm (SE)         Europa                      18883.6
Warsaw (PL)            Europa                      21186.9
London (GB)            Europa                      20434.8
Berlin (DE)            Europa                      21249.6
Prague (CZ)            Europa                      22271.6
Vienna (AT)            Europa                      23837.7
Madrid (ES)            Europa                      33809.9
Seville (ES)           Europa                      36055.8
Lisbon (PT)            Europa                      33403.1
Rome (IT)              Europa                      31220.8
Athens (GR)            Europa                      34774.3
Palermo (IT)           Europa                      33286.2
Cairo (EG)             Afryka                      41611.9
Marrakesh (MA)         Afryka                      39477.2
Tripoli (LY)           Afryka                      37300.3
Nairobi (KE)           Afryka                      37345.9
Lagos (NG)             Afryka                      35837.0
Kinshasa (CD)          Afryka                      34506.9
Cape Town (ZA)         Afryka                      36175.5
Johannesburg (ZA)      Afryka                      38183.3
Riyadh (SA)            Azja                        42793.1
Dubai (AE)             Azja                        40678.2
Tehran (IR)            Azja                        35769.7
New Delhi (IN)         Azja                        36200.0
Mumbai (IN)            Azja                        35516.8
Colombo (LK)           Azja                        35297.9
Beijing (CN)           Azja                        30143.6
Shanghai (CN)          Azja                        28634.7
Tokyo (JP)             Azja                        26424.8
Singapore (SG)         Azja                        34392.0
Bangkok (TH)           Azja                        35643.1
Jakarta (ID)           Azja                        37242.4
Perth (AU)             Australia/Oceania              37440.5
Sydney (AU)            Australia/Oceania              32730.3
Melbourne (AU)         Australia/Oceania              30664.3

================================================================================
PODSUMOWANIE STATYSTYCZNE PO KONTYNENTACH
================================================================================

Afryka                 | N= 8 | Śr=37554.8 | Min=34506.9 | Max=41611.9 | σ=2085.7 | Rozstęp= 7105.0 [kWh/m²/rok]

Ameryka                | N=11 | Śr=34364.9 | Min=13577.6 | Max=42005.4 | σ=7868.0 | Rozstęp=28427.7 [kWh/m²/rok]

Australia/Oceania      | N= 3 | Śr=33611.7 | Min=30664.3 | Max=37440.5 | σ=2835.7 | Rozstęp= 6776.2 [kWh/m²/rok]

Azja                   | N=12 | Śr=34894.7 | Min=26424.8 | Max=42793.1 | σ=4459.8 | Rozstęp=16368.3 [kWh/m²/rok]

Europa                 | N=15 | Śr=25418.5 | Min=14130.1 | Max=36055.8 | σ=7178.0 | Rozstęp=21925.8 [kWh/m²/rok]

--------------------------------------------------------------------------------
ŚWIAT (razem)        | N=49 | Śr=32230.6 | Min=13577.6 | Max=42793.1 | σ=7579.9 | Rozstęp=29215.4 [kWh/m²/rok]

## 9. Wypełnij tabelę danymi z map wskazanych krajów

## 10. Spróbuj wyjaśnić, dlaczego te same stawki taryf gwarantowanych w Niemczech stymulowały równomierny rozwój branży a w Hiszpanii doprowadziły do lawinowego wzrostu budowy farm PV i niemal spowodowały krach na rynku energii

**Feed-In Tariff (FiT)** to system gwarantowanego odkupu energii z OZE po stałej, z góry ustalonej cenie przez 20–25 lat, niezależnie od ceny rynkowej. Różnicę między stawką FiT a ceną rynkową pokrywają **wszyscy odbiorcy energii elektrycznej** poprzez dodatkową opłatę w rachunku (Niemcy: *EEG-Umlage*). W przypadku braku pełnego przeniesienia tych kosztów na odbiorców różnicę pokrywa budżet państwa, co prowadzi do narastania długu publicznego.

| Parametr | Niemcy (2006) | Hiszpania (2007–2008) |
|:---|:---|:---|
| FiT dla PV | ~0,51 €/kWh | ~0,44 €/kWh |
| Cena detaliczna energii | ~0,19 €/kWh | ~0,11 €/kWh |
| Relacja FiT / cena rynkowa | ~2,5× | ~4× |
| Nasłonecznienie | ~1 000 kWh/kWp/rok | ~1 600 kWh/kWp/rok |
| Roczna degresja stawek | ~5% | brak |
| Limit rocznych instalacji | brak (degresja jako hamulec) | brak |
| Finansowanie dopłat | EEG-Umlage (odbiorcy) | deficyt taryfowy (dług państwa) |

W Niemczech mechanizm **automatycznej degresji** — im więcej instalacji, tym niższe stawki dla kolejnych — tworzył naturalny hamulec wzrostu i utrzymywał rentowność inwestycji na umiarkowanym poziomie. W Hiszpanii brak degresji i brak limitu mocy, w połączeniu z dwukrotnie wyższym nasłonecznieniem, spowodowały, że rentowność inwestycji PV była wyjątkowo wysoka i atrakcyjna spekulacyjnie. W 2008 r. zainstalowano ~2,7 GW (cel: 400 MW), co wygenerowało wieloletnie zobowiązania finansowe państwa. Deficyt taryfowy (*déficit tarifario*) przekroczył do 2012 r. **26 mld €**, zmuszając rząd do retroaktywnego obcięcia stawek w 2013 r. i wywołując falę procesów arbitrażowych.

Zasadnicza różnica między oboma krajami leżała nie w wysokości samej taryfy, lecz w **konstrukcji systemu**: brak mechanizmu korekty i lepsze warunki słoneczne przekształciły instrument wsparcia OZE w narzędzie spekulacji inwestycyjnej.
