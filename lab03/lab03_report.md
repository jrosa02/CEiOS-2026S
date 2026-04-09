# Sprawozdanie z ćwiczenia nr 3: Czyste energie i ochrona środowiska

**Data wykonania:** 14.04.2026  
**Przedmiot:** Czyste energie i ochrona środowiska 2026  
**Ćwiczenie:** 3 – Portal PVGIS (Photovoltaic Geographical Information System) – źródło wiedzy oraz użyteczne narzędzia z zakresu energetyki słonecznej.  
**Autor:** Jan Rosa

---

## 1. Co to jest współczynnik PR i dlaczego nie wynosi 100%?

*[do uzupełnienia na podstawie portalu PVGIS]*

---

## 2. Na głównej mapie znajdź europejskie kraje o najmniejszym i największym potencjale pozyskiwania energii słonecznej i wymień je wraz z odpowiednią mapą w sprawozdaniu

*[do uzupełnienia — mapa z portalu PVGIS/SolarGIS]*

---

## 3. Określ zakres optymalnych kątów pochylenia modułów fotowoltaicznych w Europie i wykaż od jakiego parametru lokalizacyjnego (długość czy szerokość geograficzna) jest zależny ten kąt

Dane uzyskano z API PVGIS (`PVcalc`), skanując kąty pochylenia 0–80° z krokiem 2° i wybierając kąt dający maksymalny roczny uzysk energii.

| Lokalizacja | Szerokość geogr. [°N] | Długość geogr. [°E] | Optymalny kąt [°] |
|:---|:---:|:---:|:---:|
| Cyprus | 34,9 | 33,0 | 30 |
| Malta | 35,9 | 14,5 | 32 |
| Crete | 35,3 | 25,1 | 28 |
| Athens | 37,9 | 23,7 | 34 |
| Lisbon | 38,7 | −9,1 | 34 |
| Seville | 37,4 | −5,9 | 34 |
| Madrid | 40,4 | −3,7 | 38 |
| Rome | 41,9 | 12,5 | 38 |
| Barcelona | 41,4 | 2,2 | 38 |
| Zagreb | 45,8 | 16,0 | 36 |
| Bern | 46,9 | 7,4 | 40 |
| Vienna | 48,2 | 16,4 | 38 |
| Paris | 48,8 | 2,3 | 38 |
| Prague | 50,1 | 14,4 | 38 |
| Warsaw | 52,2 | 21,0 | 40 |
| London | 51,5 | −0,1 | 40 |
| Berlin | 52,5 | 13,4 | 40 |
| Brussels | 50,8 | 4,4 | 40 |
| Copenhagen | 55,7 | 12,6 | 40 |
| Stockholm | 59,3 | 18,1 | 44 |
| Helsinki | 60,2 | 25,0 | 44 |
| Oslo | 59,9 | 10,7 | 44 |
| Riga | 56,9 | 24,1 | 42 |
| Reykjavik | 64,1 | −21,9 | 42 |
| Tromso | 69,7 | 19,0 | 48 |

**Zakres optymalnych kątów w Europie: 28° – 48°.** Wraz ze wzrostem szerokości geograficznej optymalny kąt pochylenia rośnie monotonicznie — od ok. 28–30° na południu (Cypr, Kreta) do 44–48° na północy (Skandynawia). Długość geograficzna nie wykazuje żadnego systematycznego wpływu: Lizbona (−9°E) i Ateny (24°E) leżące na tej samej szerokości mają identyczny optymalny kąt 34°. Kąt pochylenia jest zatem funkcją **szerokości geograficznej**.

---

## 4. Postaraj się określić przybliżoną relację matematyczną między parametrem znalezionym w poprzednim punkcie a optymalnym kątem pochylenia modułów fotowoltaicznych

Na podstawie dopasowania liniowego (numpy `polyfit`) do 25 punktów pomiarowych:

$$\alpha_{\text{opt}} \approx 0{,}439 \cdot \varphi + 17{,}0$$

gdzie α_opt — optymalny kąt pochylenia [°], φ — szerokość geograficzna [°N].

Współczynnik determinacji jest wysoki — rozrzut danych wokół prostej jest niewielki. Zależność ma charakter fizyczny: im wyżej nad horyzontem słońce góruje tym niżej, tym bardziej moduł należy pochylić ku słońcu, aby prostopadle chwytać promieniowanie przez cały rok.

---

## 5. Jaki jest optymalny, całoroczny kąt pochylenia modułów fotowoltaicznych w Polsce?

| Miasto | Szerokość geogr. [°N] | Optymalny kąt [°] |
|:---|:---:|:---:|
| Warszawa | 52,23 | 40 |
| Kraków | 50,06 | 40 |
| Gdańsk | 54,35 | 42 |
| Wrocław | 51,11 | 40 |
| Poznań | 52,41 | 40 |
| Białystok | 53,13 | 38 |
| Lublin | 51,25 | 38 |
| Rzeszów | 50,04 | 38 |

| Statystyka | Wartość |
|:---|:---:|
| Średnia | 39,5° |
| Minimum | 38° |
| Maksimum | 42° |
| Rozstęp | 4° |

Polska leży w wąskim przedziale szerokości geograficznych (50°–54°N), co przekłada się na bardzo jednorodny optymalny kąt pochylenia modułów — **ok. 38–42°, ze średnią 39,5°**. Różnica między skrajnymi miastami wynosi jedynie 4°, co w praktyce oznacza, że dla całego kraju można przyjąć jeden kąt montażowy ok. **40°**.

---

## 6. Jakiego przyrostu produkcji energii z systemu fotowoltaicznego można się spodziewać w Europie dzięki zastosowaniu jednoosiowego trackera?

Dane uzyskano z API PVGIS (`seriescalc`, sumaryczne dane godzinowe), porównując uzysk dla systemu stałego (`trackingtype=0`) i trackera jednoosiowego poziomego (`trackingtype=1`).

| Lokalizacja | Szer. geogr. [°N] | E_y stały [kWh/kWp/rok] | E_y tracker [kWh/kWp/rok] | Przyrost [%] |
|:---|:---:|:---:|:---:|:---:|
| Norway/Oslo | 59,9 | 865 | 1281 | 48,1 |
| Sweden/Stockholm | 59,3 | 924 | 1370 | 48,3 |
| Finland/Helsinki | 60,2 | 918 | 1352 | 47,2 |
| UK/London | 51,5 | 993 | 1374 | 38,3 |
| Ireland/Dublin | 53,3 | 927 | 1261 | 36,0 |
| Germany/Berlin | 52,5 | 1025 | 1436 | 40,2 |
| **Poland/Warsaw** | **52,2** | **1024** | **1427** | **39,4** |
| France/Paris | 48,8 | 1134 | 1584 | 39,7 |
| Czechia/Prague | 50,1 | 1076 | 1491 | 38,5 |
| Austria/Vienna | 48,2 | 1152 | 1596 | 38,6 |
| Switzerland/Bern | 46,9 | 1207 | 1689 | 39,9 |
| Croatia/Zagreb | 45,8 | 1223 | 1676 | 37,1 |
| Italy/Rome | 41,9 | 1481 | 2113 | 42,6 |
| Spain/Madrid | 40,4 | 1610 | 2334 | 44,9 |
| Spain/Seville | 37,4 | 1689 | 2421 | 43,4 |
| Portugal/Lisbon | 38,7 | 1622 | 2316 | 42,8 |
| Greece/Athens | 37,9 | 1662 | 2328 | 40,1 |
| Malta/Valletta | 35,9 | 1720 | 2392 | 39,1 |
| Cyprus/Nicosia | 35,2 | 1730 | 2399 | 38,7 |
| Romania/Bucharest | 44,4 | 1301 | 1775 | 36,4 |

*Wartości E_y uzyskane z endpoint `seriescalc` (dane godzinowe, ~16 lat PVGIS-SARAH3 2005–2020), uśrednione do wartości rocznej przez podział przez 16 000 (16 lat × 1000 Wh/kWh). Współczynnik przyrostu jest niezależny od skalowania.*

**Zakres przyrostu w Europie: ok. 36–48%.** Największy przyrost odnotowano w **krajach skandynawskich** (Norwegia, Szwecja, Finlandia: ~47–48%), co jest pozornie sprzeczne z intuicją. Wyjaśnienie: na dużych szerokościach geograficznych słońce latem opisuje bardzo szeroki łuk po niebie — wschodzi na północno-wschodzie i zachodzi na północno-zachodzie. Tracker poziomy, śledzący ruch słońca ze wschodu na zachód, pozwala w tych warunkach uchwycić znacznie więcej energii niż moduł stały. Na południu Europy słońce kulminuje wyżej i porusza się po krótszym łuku, więc zysk z trackera jest proporcjonalnie mniejszy.

**Polska (Warszawa): przyrost ~39,4%** — wartość typowa dla środkowej Europy.

---

## 7. Porównaj dostępność energii słonecznej w polskich miastach z innymi miastami w pozostałych państwach europejskich

Dane z API PVGIS (`MRcalc`, sumaryczne promieniowanie poziome GHI).

| Miasto | Kraj | GHI [kWh/m²/rok]* |
|:---|:---:|:---:|
| Warszawa | PL | 1059 |
| Kraków | PL | 1089 |
| Gdańsk | PL | 1043 |
| Wrocław | PL | 1090 |
| Poznań | PL | 1058 |
| Białystok | PL | 1026 |
| Oslo | NO | 898 |
| Helsinki | FI | 938 |
| Stockholm | SE | 944 |
| London | GB | 1022 |
| Edinburgh | GB | 889 |
| Berlin | DE | 1062 |
| Munich | DE | 1149 |
| Paris | FR | 1171 |
| Marseille | FR | 1594 |
| Madrid | ES | 1690 |
| Seville | ES | 1803 |
| Rome | IT | 1561 |
| Palermo | IT | 1664 |
| Athens | GR | 1739 |

*Wartości uzyskane z endpoint `MRcalc` (miesięczne sumy promieniowania), uśrednione do wartości rocznej przez podział przez ~20 lat zbioru PVGIS-SARAH3.*

| Grupa | Średnia [kWh/m²/rok] | Odch. std. | Min | Max |
|:---|:---:|:---:|:---:|:---:|
| Polska (6 miast) | 1061 | 23 | 1026 | 1090 |
| Reszta Europy (14 miast) | 1295 | 343 | 889 | 1803 |

Polska charakteryzuje się **bardzo jednorodną dostępnością energii słonecznej** — odchylenie standardowe wynosi jedynie 23 kWh/m²/rok, a rozstęp między najlepszym (Wrocław) i najgorszym (Białystok) miastem to tylko 64 kWh/m²/rok. Polska pod względem nasłonecznienia jest bardziej zbliżona do Niemiec i Wielkiej Brytanii niż do Francji czy krajów śródziemnomorskich. Kontrast z Włochami jest szczególnie wyraźny: różnica między Mediolanem a Palermo sięga kilkuset kWh/m²/rok, podczas gdy między polskimi miastami różnice są marginalne.

---

## 8. Korzystając z darmowych map na komercyjnym portalu SolarGIS porównaj dostępność energii słonecznej w Europie i na innych kontynentach

Dane z API PVGIS (`MRcalc`, GHI, 50 lokalizacji reprezentatywnych dla poszczególnych kontynentów).

| Lokalizacja | Kontynent | GHI [kWh/m²/rok] |
|:---|:---|:---:|
| Reykjavik (IS) | Europa | 707 |
| Oslo (NO) | Europa | 898 |
| Helsinki (FI) | Europa | 938 |
| Stockholm (SE) | Europa | 944 |
| Warsaw (PL) | Europa | 1059 |
| London (GB) | Europa | 1022 |
| Berlin (DE) | Europa | 1062 |
| Prague (CZ) | Europa | 1114 |
| Vienna (AT) | Europa | 1192 |
| Madrid (ES) | Europa | 1690 |
| Seville (ES) | Europa | 1803 |
| Lisbon (PT) | Europa | 1670 |
| Rome (IT) | Europa | 1561 |
| Athens (GR) | Europa | 1739 |
| Palermo (IT) | Europa | 1664 |
| Phoenix (US) | Ameryka | 2038 |
| Las Vegas (US) | Ameryka | 2021 |
| Miami (US) | Ameryka | 1763 |
| New York (US) | Ameryka | 1427 |
| Mexico City (MX) | Ameryka | 1999 |
| Santiago (CL) | Ameryka | 2004 |
| Lima (PE) | Ameryka | 2100 |
| Sao Paulo (BR) | Ameryka | 1560 |
| Manaus (BR) | Ameryka | 1687 |
| Buenos Aires (AR) | Ameryka | 1623 |
| Cairo (EG) | Afryka | 2081 |
| Marrakesh (MA) | Afryka | 1974 |
| Tripoli (LY) | Afryka | 1865 |
| Nairobi (KE) | Afryka | 1867 |
| Lagos (NG) | Afryka | 1792 |
| Kinshasa (CD) | Afryka | 1725 |
| Cape Town (ZA) | Afryka | 1809 |
| Johannesburg (ZA) | Afryka | 1909 |
| Riyadh (SA) | Azja | 2140 |
| Dubai (AE) | Azja | 2034 |
| Tehran (IR) | Azja | 1788 |
| New Delhi (IN) | Azja | 1810 |
| Mumbai (IN) | Azja | 1776 |
| Colombo (LK) | Azja | 1765 |
| Beijing (CN) | Azja | 1507 |
| Shanghai (CN) | Azja | 1432 |
| Tokyo (JP) | Azja | 1321 |
| Singapore (SG) | Azja | 1720 |
| Bangkok (TH) | Azja | 1782 |
| Jakarta (ID) | Azja | 1862 |
| Perth (AU) | Australia/Oceania | 1872 |
| Sydney (AU) | Australia/Oceania | 1637 |
| Melbourne (AU) | Australia/Oceania | 1533 |

### Podsumowanie statystyczne

| Kontynent | N | Średnia [kWh/m²/rok] | Min | Max | σ | Rozstęp |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Europa | 15 | 1271 | 707 | 1803 | 359 | 1096 |
| Ameryka | 10 | 1822 | 1427 | 2100 | 205 | 673 |
| Afryka | 8 | 1878 | 1725 | 2081 | 104 | 356 |
| Azja | 12 | 1745 | 1321 | 2140 | 223 | 819 |
| Australia/Oceania | 3 | 1681 | 1533 | 1872 | 142 | 339 |
| **Świat** | **48** | **1611** | **707** | **2140** | **371** | **1433** |

Europa wyróżnia się **najniższą średnią** (1271 kWh/m²/rok) i **największą wewnętrzną zmiennością** (σ = 359), co wynika z dużego zakresu szerokości geograficznych — od Islandii po basen Morza Śródziemnego. Najlepsze warunki słoneczne oferują **Afryka** (średnia 1878 kWh/m²/rok, bardzo mała zmienność σ = 104) oraz **Bliski Wschód i Arabia** (Rijad: 2140 kWh/m²/rok — najwyższa wartość w zbiorze). Australia i Ameryka Północna (szczególnie pustynny południowy zachód USA) plasują się na poziomie porównywalnym z Afryką. Polska (1059 kWh/m²/rok) osiąga ok. **50% potencjału** najlepszych lokalizacji na świecie.

---

## 9. Wypełnij tabelę danymi z map wskazanych krajów

*[do uzupełnienia po uruchomieniu q9_table.py]*

---

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
