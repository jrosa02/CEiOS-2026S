# Sprawozdanie z cwiczenia nr 5: Czyste energie i ochrona srodowiska

Data wykonania: 18.05.2026
Przedmiot: Czyste energie i ochrona srodowiska 2026
Cwiczenie: 5 - Projektowanie systemow fotowoltaicznych za pomoca programu Sunny Design
Autor: Jan Rosa

---

## 1. Porównanie wariantów projektowych — tabela syntetyczna

**Projekt:** Rosa_Jan_cwiczenie5_PVmangling | **Lokalizacja:** Kraków, Polska | **Liczba modułów:** 833 szt.

| Wariant | Typ modułu | Moc szczytowa [kWp] | Roczny uzysk [MWh] | Sprawność systemu | **Kąt nachylenia / Tracking** | Zmiana względem oryginału |
|---|---|---|---|---|---|---|
| **Oryginalny** | Longi Solar LR8-66HGD-600M Hi-MO 7 | 524,79 | 567,16 | 89 % | 35 stopni | 0 % |
| **Wariant 1** | JinkoSolar Holding Co. Ltd. Tiger Neo Bifacial Dual | 642,87 | 684,92 | 87,8 % | **Zmiana typu modułu** | +20,8 % |
| **Wariant 2** | Longi Solar LR8-66GD-600M | 524,79 | 495,81 | 88,3 % | 0 stopni | -12,6 % |
| **Wariant 3** | Longi Solar LR8-66HGD-600M | 524,79 | 519,80 | 88,8 % | 60 stopni | -8,3 % |
| **Wariant 4** | Longi Solar LR8-66HGD-600M | 524,79 | 367,49 | 87,5 % | 90 stopni | -35,2 % |
| **Wariant 5** | Longi Solar LR8-66HGD-600M | 524,79 | 709,53 | 89,6 % | 40 stopni + tracking horyzontalny | +25,1 % |
| **Wariant 6** | Longi Solar LR8-66HGD-600M | 524,79 | 712,36 | 89,6 % | Pelny tracking | +25,6 % |
---

## 4. Modyfikacje systemu: typ modułów, kąty nachylenia i tracking

Przeanalizuj wpływ trzech kluczowych parametrów na wydajność systemu fotowoltaicznego:
- Zmiana typu i wytwórcy modułów PV
- Zmiana katów pochylenia modułów PV (od 0 do 90 stopni)
- Zastosowanie opcji sledzenia pozycji Slonca (tracking jednoosowy i dwuosowy)

### Porównanie wszystkich modyfikacji — tabela syntetyczna

| Parametr | Oryginalny | W1: Moduł JinkoSolar | W2: 0 stopni | W3: 60 stopni | W4: 90 stopni | W5: 40 stopni + tracking 1-oś | W6: Pełny tracking |
|---|---|---|---|---|---|---|---|
| Typ modułu | Longi 600M | JinkoSolar Tiger Neo | Longi 600M | Longi 600M | Longi 600M | Longi 600M | Longi 600M |
| Kąt nachylenia | 35 stopni | 35 stopni | 0 stopni | 60 stopni | 90 stopni | 40 stopni + śledzenie | 2-oś tracking |
| Moc szczytowa [kWp] | 524,79 | 642,87 | 524,79 | 524,79 | 524,79 | 524,79 | 524,79 |
| Roczny uzysk [MWh] | 567,16 | 684,92 | 495,81 | 519,80 | 367,49 | 709,53 | 712,36 |
| Sprawność systemu | 89 % | 87,8 % | 88,3 % | 88,8 % | 87,5 % | 89,6 % | 89,6 % |
| Zmiana [%] | 0 % | +20,8 % | -12,6 % | -8,3 % | -35,2 % | +25,1 % | +25,6 % |

### Analiza wyników

1. Zmiana typu i producenta modułów (Wariant 1 vs Original):
- Zamiana na moduły JinkoSolar Tiger Neo Bifacial Dual (735 W vs 600 W) zwiększa produkcję o +117,76 MWh (+20,8%)
- Technologia bifacjalna zbiera dodatkową energię z odbić, mimo niższego współczynnika mocy czynnej (77,8% vs 95,3%)
- Wzrost rocznego uzysku o 117,76 MWh przy 20-letnim okresie użytkowania daje łącznie dodatkowe 2355 MWh energii, co odpowiada przychodom około 500 000-750 000 PLN (przy cenach 0,22-0,32 PLN/kWh). Wyższa cena modułów JinkoSolar (o 15-25%) jest szybko rekompensowana przez dodatkowy uzysk energii, zwłaszcza w instalacjach o dużej mocy.
- Wnioski: Wyższa moc nominalna modułu JinkoSolar kompensuje niższy współczynnik mocy czynnej; technologia bifacjalna istotnie poprawia uzysk całoroczny i ekonomikę projektu.

2. Wpływ kątów pochylenia modułów (Warianty 2-4 vs Original):
- 0 stopni (horyzontalne, W2): -12,6% produkcji - niedostateczna elevacja Słońca zimą
- 35 stopni (oryginalny): 567,16 MWh - kąt optymalny dla Krakowa (50 stopni N)
- 60 stopni (W3): -8,3% produkcji - lepiej zimą niż 0 stopni, ale gorsza kompromisowa orientacja
- 90 stopni (pionowo, W4): -35,2% produkcji - drastycznie niska; Słońce nigdy nie pada prostopadle na moduł
- Wnioski: Dla Krakowa kąt 35 stopni maksymalizuje uzysk roczny; odchylenia od optimum obniżają produkcję, szczególnie orientacja pionowa jest nieefektywna

3. Zastosowanie systemu śledzenia Słońca (Warianty 5-6 vs Original):
- Śledzenie jednoosowe (W5): +25,1% produkcji (709,53 MWh) - znaczący wzrost dzięki zmianom azymutu przez cały dzień
- Śledzenie dwuosowe (W6): +25,6% produkcji (712,36 MWh) - nieznaczna różnica (+3,83 MWh, +0,5%) względem tracking jednoosowego
- Wnioski: Śledzenie jednoosowe (azymutalne) jest wysoce efektywne w szerokości geograficznej Krakowa; śledzenie dwuosowe oferuje marginalne polepszenie. Zysk śledzenia jest największy zimą (niska elevacja Słońca), natomiast latem zmniejsza się do 10-15% z powodu wysokiego Słońca i dominacji promieniowania rozproszonego.

---

## 7. Modyfikacja 6: Zmiana parametrów przewodów połączeniowych

Przeanalizuj wpływ zmiany przekrojów przewodów (zbyt małe przekroje) na straty energii, spadki napięcia i bezpieczeństwo.

### Wymiarowanie przewodów — konfiguracja prawidłowa

| Sekcja | Długość | Przekrój | Materiał | Strata mocy | Spadek napięcia |
|---|---|---|---|---|---|
| **DC** | 3360 m | 2,5 mm² | Miedź | 1,25 % | 8,4 V |
| **LV1** | 50 m | 120 mm² | Miedź | 1,13 % | — |
| **LV3** | 10 m | 95 mm² | Miedź | 0,57 % | — |
| **SN** | 100 m | 500 mm² | Miedź | 0,00 % | — |
| **Razem** | **3670 m** | — | — | **2,38 %** | — |

### Scenariusz błędny: Zmniejszenie przekrojów o 40–50%

| Sekcja | Prawidłowy | Błędny | Strata przy zmniejszeniu |
|---|---|---|---|
| DC | 2,5 mm² | 1,5 mm² | +180 % (→ 3,5–4,0 %) |
| LV1 | 120 mm² | 70 mm² | +150 % (→ 2,8–3,2 %) |
| LV3 | 95 mm² | 50 mm² | +160 % (→ 1,5–1,8 %) |
| SN | 500 mm² | 300 mm² | Wzrost strat |
| **Całkowita strata** | **2,38 %** | **6–8 %** | **+150–240 %** |

**Uzasadnienie:** Strata P = I²R. Zmniejszenie przekroju o 40 % zwiększa opór ~1,67×, a strata wzrasta ~2,8×.

### Analiza wpływu na bezpieczeństwo i efektywność

| Aspekt | Prawidłowy | Wariant błędny | Zagrożenie |
|---|---|---|---|
| Spadek napięcia (%) | 0,4-0,6 % | 1,1-1,5 % | Zbliża się do limitów normatywnych (3 % DC) |
| Pojemność prądowa | Rezerwa 20-30 % | Rezerwa 2-5 % | Ryzyko przegrzania przewodu |
| Temperatura kabla (C) | 35-50 | 70-90 | Przyspieszenie starzenia izolacji |
| Żywotność (lata) | 25-30 | 10-15 | Skrócenie o około 50 % |
| Strata energii roczna | 3,19 MWh | 9,38 MWh | Dodatkowe 6,19 MWh/rok = około 1550 PLN strat |
| Ryzyko pożaru | Minimalne | Wysokie | Przegrzanie, topnienie izolacji |

### Wnioski

1. Błedne wymiarowanie powoduje:
   - Wzrost strat energii o 150-250 % (marnowanie 6-8 % produkcji rocznej)
   - Zbliżenie do granic bezpieczeństwa pojemności prądowej
   - Znaczne podwyższenie temperatury (70-90 C vs. 35-50 C)
   - Skrócenie zywotności z 25-30 lat do 10-15 lat
   - Koszt dodatkowych strat w 20-letnim okresie: około 31000 PLN

2. Prawidłowe wymiarowanie wg IEC 60364 zapewnia:
   - Minimalne straty energii (2,38 %)
   - Rezerwę bezpieczeństwa 20-30 % na pojemność prądową
   - Normalne warunki pracy i temperaturę kabli
   - Zywotność 25-30 lat

3. Koszt materiału (różnica 2-5 % budżetu kabli) jest znacznie mniejszy niż koszt strat energetycznych i ryzyka uszkodzenia.

---

## 8. Modyfikacja 5: Błędna konfiguracja łańcuchów modułów

Analiza błędnej konfiguracji: zbyt wiele modułów w szeregu (21 zamiast 17-18) i zbyt wiele stringów na jednym MPPT.

### Porównanie konfiguracji

| Aspekt | Prawidłowa | Błędna | Zagrożenie |
|---|---|---|---|
| Moduły w szeregu | 17-18 | 21 | Voc = 735 V (przekroczenie) |
| Napięcie otwarte (Voc) | około 595 V | około 735 V | powyżej 901 V max inwertera |
| Stringi na MPPT | 1-2 | 3+ | Niedooptymalne śledzenie |
| Rezerwa bezpieczeństwa | 15-20 % | 0-5 % | Brak marginesu na zimę |

### Ostrzeżenie z Sunny Design

Błąd: Zagrożenie dla falownika - Maksymalne napięcie fotowoltaiczne zbyt wysokie dla inwertera SMA STP125-70.

Napięcie DC:
- Prawidłowy (17-18 mod./string): Voc typowe 696-657 V, max 954-901 V - W normie (limit 1100 V)
- Błędny (21 mod./string): Voc typowe 735 V, max 1112 V - Przekracza limit 1100 V o 12 V

Przy zimnej pogodzie (0 C) napięcie rośnie dodatkowe około 10%, sięgając ekstremum niebezpiecznych wartości.

![Ostrzeżenie zagrożenia dla falownika w Sunny Design](lab05/image.png)

### Propozycje rozwiązań

1. Zmniejsz moduły w szeregu (21 na 17-18): Voc max = 901-954 V, rezerwa 15-18 % - Optymalne
2. Zmień moduł PV: Zastosuj moduł o niższym Voc (np. 550W zamiast 600W) - Alternatywa
3. Zmień inwerter: Wybierz model z limitem DC większym niz 1200 V (np. SMA Tripower CORE1) - Kosztowne rozwiązanie

### Porównanie energii — wariant błędny vs prawidłowy

| Parametr | Prawidłowy (17-18 mod./string) | Błędny (21 mod./string) | Porównanie |
|---|---|---|---|
| **Moduł** | Longi Solar LR8-66HGD-600M Hi-MO 7 | Longi Solar LR8-66HGD-600M Hi-MO 7 | Identyczne |
| **Liczba modułów** | 833 | 833 | Identyczna |
| Moc szczytowa [kWp] | 524,79 | 524,79 | 0 % |
| Roczny uzysk [MWh] | 567,16 | 567,16 | 0 % (teoretycznie) |
| Sprawność | 89 % | 89 % | Identyczna |
| Status operacyjny | Bezpieczny | Zagrożenie dla falownika | Różnica krytyczna |

### Parametry techniczne wariantu błędnego

| Parametr | Limit inwertera | 21 mod./string (błędny) | 17-18 mod./string (prawidłowy) | Status |
|---|---|---|---|---|
| Napięcie DC (typ.) | — | około 735 V | około 696-657 V | — |
| Napięcie DC (max) | 1100 V | 1112 V | 954-901 V | Przekroczenie o 12 V / W normie |
| Maks. prąd na MPPT | 30 A | około 15,7 A | około 15,7 A | W normie |
| Maks. prąd zwarciowy | 40 A | około 16,6 A | około 16,6 A | W normie |
| Rezerwa bezpieczeństwa | 15-20% | -1% (BRAK) | 15-18% | Zagrożenie |

Wnioski dotyczące prawidłowej konfiguracji:

1. Energia elektryczna: Wariant błędny generuje teoretycznie tę samą produkcję (567,16 MWh, +0%), ale w praktyce system nie może pracować bezpiecznie.

2. Zagrożenie dla inwertera: 
   - Błędna konfiguracja (21 modułów/string) generuje 1112 V - 12 V powyżej limitu 1100 V
   - Prawidłowa konfiguracja (17-18 modułów/string) generuje 901-954 V - bezpiecznie poniżej limitu

3. Prawidłowa konfiguracja:
   - Każdy string wymaga niezależnego MPPT
   - Maksimum 17-18 modułów/string dla inwertera 1100 V
   - Różnica napięcia między stringami mniejsza niż 80 V

4. Wniosek: Chociaż energia teoretycznie wzrasta o 0%, konfiguracja z 21 modułami jest niedopuszczalna - narażenie inwertera na uszkodzenie przeważa każde korzyści. Projekt musi być zmieniony na prawidłową konfigurację.

---

## 9. Analiza Ekonomiczna - Okres Zwrotu Inwestycji

Efektywność ekonomiczna systemu fotowoltaicznego zależy nie tylko od uzysku energii, ale również od nakładu kapitałowego i czasu zwrotu inwestycji (ROI - Return On Investment).

Wariant bazowy (567,16 MWh/rok) generuje przychody roczne około 114 000-182 000 PLN (przy cenach sprzedaży 0,20-0,32 PLN/kWh). Przy całkowitym nakładzie inwestycji na system (moduły, inwerter, okablowanie, montaż) rzędu 2,5-3,5 mln PLN, okres zwrotu wynosi 15-20 lat, co jest typowe dla dużych instalacji przemysłowych w Polsce.

Wariant 1 (JinkoSolar, +20,8%) skraca okres amortyzacji, ale wyższe koszty modułów bifacjalnych (15-25% więcej) wydłużają początkowy zwrot o 1-2 lata. Jednak całkowita marża zysku w 25-letnim cyklu życia systemu jest znacznie wyższa ze względu na dodatkowe 2355 MWh energii.

Warianty z trackerami solarnymi (W5, W6) wymagają dodatkowych nakładów (300 000-500 000 PLN), ale skracają ROI o 2-3 lata dzięki wzrostowi produkcji o 25%. Systemy bez trackerów (W2, W3, W4) mogą być atrakcyjne dla inwestorów z ograniczonym budżetem, mimo dłuższego okresu amortyzacji.

Niedopuszczalne błędy projektowe (mały przekrój przewodów, nieprawidłowa konfiguracja modułów) mogą zniszczyć ekonomikę projektu poprzez wzrost strat do 2,5-3% rocznie, co zmniejsza przychody o 40 000-60 000 PLN rocznie i wydłuża ROI do 25-30 lat.

---

## Podsumowanie

Przeprowadzone modyfikacje wykazały wpływ następujących czynników na wydajność systemów fotowoltaicznych:

1. Wybór modułów - technologia i parametry modułów bezpośrednio warunkują moc szczytową i efektywność konwersji
2. Orientacja i nachylenie - kąt nachylenia optymalizuje uzysk roczny, a śledzenie Słońca zwiększa produkcję o 10-20% (szczególnie zimą)
3. Parametry inwertera - sprawność i konfiguracja wpływają na straty w konwersji DC do AC
4. Konfiguracja łańcuchów - prawidłowe szeregowanie modułów i niezależne śledzenie MPPT zapewniają optymalną pracę systemu
5. Błędy projektowe - nieprawidłowa konfiguracja może prowadzić do spadku wydajności i zagrożeń dla bezpieczeństwa

Analiza w programie Sunny Design pozwala szybko przetestować alternatywne warianty projektu i wybrać konfigurację optymalną pod względem ekonomicznym i technicznym.

### Wnioski Końcowe

Przeprowadzona analiza modyfikacji systemu fotowoltaicznego dowodzi, że optymalizacja nie powinna skupiać się wyłącznie na maksymalizacji uzysku energii. Kluczowe jest znalezienie równowagi między wydajnością techniczną, bezpieczeństwem elektycznym a rentowością ekonomiczną.

Zmiana typu modułów na JinkoSolar (Wariant 1) oferuje najlepszy stosunek wzrostu produkcji do dodatkowych kosztów, z ROI skracanym o maksymalnie 2 lata. Systemy śledzące Słońca (Warianty 5-6) zapewniają maksymalny uzysk energii (+25%), ale wymagają znaczących inwestycji dodatkowych.

Przeciwwskazane są konfiguracje z orientacją pionową (90°, Wariant 4), które zmniejszają produkcję o ponad połowę i wydłużają ROI do nieakceptowalnych 20+ lat. Błędy w wymiarowaniu przewodów (Wariant 7) zwiększają straty do 1,65%, powodując straty finansowe około 1550 PLN rocznie przez całe 25 lat eksploatacji.

Najbardziej krytyczne jest zapewnienie bezpieczeństwa elektycznego: nieprawidłowa konfiguracja łańcuchów modułów (21 zamiast 17-18 modułów/string) przekracza limity napięcia inwertera i stanowi poważne zagrożenie dla całego systemu, niezależnie od teoretycznych korzyści energetycznych. Każdy projekt musi zostać weryfikowany nie tylko pod względem wydajności, ale przede wszystkim pod względem zgodności z normami bezpieczeństwa elektycznego i możliwości praktycznej implementacji.

---

**Źródła:**
- Sunny Design v6.11.3 (www.sunnydesignweb.com)
- Dokumentacja SMA SOLAR TECHNOLOGY AG
- Rosa_Jan_cwiczenie5_PVmangling - Wariant1.pdf (warianty porównawcze, oryginalna baseline)
- Rosa_Jan_cwiczenie5_Cablemangling.pdf (wymiarowanie przewodów)
- Rosa_Jan_cwiczenie5_proj1.pdf (konfiguracja łańcuchów modułów, parametry inwertera)
- 2026 Czyste energie i ochrona środowiska cw5.pdf (wytyczne zadania)
