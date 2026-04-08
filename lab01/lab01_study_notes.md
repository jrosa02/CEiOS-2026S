# Laboratorium ćw. 1: Czyste Energie i Ochrona Środowiska - Notatki Studyjne

## Cel Ćwiczenia

Zrozumienie technicznych, ekonomicznych i ekologicznych aspektów różnych nośników energii w kontekście typowego gospodarstwa domowego, ze szczególnym naciskiem na **energię elektryczną** (w przeciwieństwie do Lab 2, które skupiało się na energii cieplnej).

---

## Metodologia

- **Samodzielne badania** — przede wszystkim przez wyszukiwanie informacji w Internecie
- **Weryfikacja źródeł** — każde znalezione dane należy zweryfikować w co najmniej 2 różnych źródłach
- **Cytowanie** — wszystkie źródła muszą być wymienione w sprawozdaniu
- **Internetowe kalkulatory i dane statystyczne** — GUS, Eurostat, TGE, portale producenckie

---

## Kluczowe Koncepcje do Opanowania

### 1. Jednostki Energii i Ich Konwersje

**Podstawowe jednostki**:
- **GJ** (gigajul) = 10⁹ J
- **MJ** (megajul) = 10⁶ J
- **kWh** (kilowatogodzina) — często używana dla energii elektrycznej
- **MWh** (megawatogodzina) — dla większych ilości

**Konwersje (dwukierunkowo)**:
- Zrozumieć relacje: GJ ↔ MJ ↔ kWh ↔ MWh
- Najważniejsza konwersja dla energii elektrycznej: 1 kWh = 3,6 MJ

**Znaczenie**: Pozwala porównywać różne nośniki energii na wspólnej podstawie

### 2. Ceny Energii na Towarowej Giełdzie Energii (TGE)

**Źródło danych**: www.tge.pl — portal publiczny

**Co analizować**:
- **Raporty miesięczne i roczne** — dostępne dla publiczzności
- **Średnie ceny miesięczne** — trend przez ostatnie 5+ lat
- **Ceny godzinowe** — zmienność w ciągu doby

**Dwa okresy do porównania**:

1. **Przed 2019** (przed masowym rozwojem fotowoltaiki w Polsce)
   - Ceny godzinowe w pełnym cyklu dobowym
   - Rozkład popytu przez dobę

2. **Ostatnie 2 lata** (z masową fotowoltaiką)
   - Godziny nocne — brak produkcji słonecznej, wyższe ceny
   - Okres zimowy — mniejsza produkcja FV, inne wzorce cenowe
   - Widoczny wpływ OZE na rynek

**Obserwacje kluczowe**: Fotowoltaika zmienia rozkład cen w ciągu dnia

### 3. Analiza Taryf Energii Elektrycznej — Tauron S.A.

**Cel**: Znaleźć najtańszą taryfę dla konkretnego profilu zużycia

**Taryfy do porównania**:
- **G11** — taryfa jednosschodkowa (jedna cena przez całą dobę)
- **G12** — taryfa dwusschodkowa (Peak i Off-Peak — dzień/noc)
- **G12w** — taryfa weekendowa (specjalne traktowanie weekendów i dni wolnych)
- **G13** — taryfa trójsschodkowa (Peak, Standard, Off-Peak — 3 różne ceny)

**Komponenty kosztów do uwzględnienia**:
- **Opłata za zakup energii** — cena za kWh (różna w zależności od strefy czasowej)
- **Opłata za dystrybucję** — opłata za przesył (różna w zależności od strefy czasowej)
- **Opłaty stałe** (składniki bazowe) — muszą być rozpisane
- **VAT 23%** — doliczyć na końcu

**Forma wyniku**: Tabela zawierająca:
- Jednostkowe ceny zakupu (netto) w każdej strefie czasowej
- Jednostkowe ceny dystrybucji (netto) w każdej strefie czasowej
- Ilość energii pobranej w każdej strefie czasowej (dla całego roku)
- Opłaty stałe (z rozbiciem na podstawowe składniki)
- Finalne koszty (netto i brutto z VAT)

**Dyskusja wyników**: Porównanie taryf i wskazanie, która jest najtańsza

---

## Dane Referencyjne do Zadania 3

### Parametry Gospodarstwa Domowego

| Parametr | Wartość |
|----------|---------|
| **Lokalizacja** | Kraków |
| **Rok rozpatrzenia** | 2026 (365 dni) |
| **Licznik** | Trójfazowy |
| **Cykl rozliczeniowy** | 2 miesiące |
| **Struktura rodziny** | 4 osoby: 2 pracujące, 2 dzieci |

### Dni Wolne w 2026

- **Weekendy** = wszystkie soboty i niedziele
- **Święta/dni ustawowe** = dodatkowo 13 dni wolnych z mocy ustawy
- **Razem dni wolnych** = weekendy + 13 dni
- **Dni robocze** = 365 − (dni wolne)

**Wskazówka**: Oblicz dokładnie, ponieważ wpływa na straty w taryfach G12w i G13

### Profil Godzinowy Zużycia Energii

Dane zawarte w instrukcji ćwiczenia (tablica godzinowa):
- Zużycie **zmienia się w ciągu doby** — niższe w nocy, wyższe wieczorem
- Przyjąć, że **każdy dzień roku ma identyczne zużycie godzinowe**
- Najmniejsze zużycie: ~02:00–04:00 (0,15–0,17 kWh)
- Największe zużycie: ~19:00–20:00 (0,40–0,43 kWh)

**Obliczenie rocznego zużycia**: Sumuj zużycie godzinowe × 365 dni

### Strefy Czasowe Taryf

**G11**: Jedna cena przez całą dobę

**G12** (dzień/noc):
- Peak (godziny 7–21) — wyższa cena
- Off-Peak (godziny 22–6) — niższa cena

**G12w** (z weekendami):
- Dni robocze: Peak i Off-Peak (jak G12)
- Dni wolne: Cała doba Off-Peak (najniższa cena)

**G13** (trójsschodkowa):
- Peak (godziny 8–10, 17–21) — najwyższa cena
- Standard (godziny 11–16, 22–7) — średnia cena
- Off-Peak (godziny 1–7) — najniższa cena
- **Uproszczenie**: Przez cały rok stosuj strefy czasowe **jak dla lata** (nie zmieniaj w zimie)

---

## Zagadnienia Szczegółowe do Każdego Zadania

### Zadanie 1: Konwersje Jednostek

**Co robić**:
- Zbudować tabelę konwersji między: GJ, MJ, kWh, MWh
- Pokazać relacje w obu kierunkach (A→B i B→A)

**Wzory pomocne**:
- 1 kWh = 3,6 MJ (kluczowa konwersja!)
- 1 GJ = 1000 MJ
- 1 MWh = 3600 MJ

### Zadanie 2: Analiza Cen na TGE

**Struktura analizy**:
1. **Dane historyczne** — średnie ceny miesięczne z 5+ lat (trend długoterminowy)
2. **Okres przed-FV (przed 2019)** — ceny godzinowe w ciągu doby (normalny rozkład)
3. **Okres post-FV (ostatnie 2 lata)** — porównanie nocy vs dnia, zima vs lato

**Obserwacje do zrobienia**:
- Jak wzrosły ceny w ostatnich latach?
- Jak fotowoltaika zmienia cenę w godzinach szczytowych produkcji (południe)?
- Jaka jest różnica między nocą a dniem w ostatnich latach?
- Jaka była ta różnica przed 2019?

### Zadanie 3: Wybór Najlepszej Taryfy — Metodologia

**Kroki do wykonania**:

1. **Pobierz dane taryfowe** z Tauron S.A. dla Krakowa (2026)
2. **Oblicz zużycie w każdej strefie czasowej**:
   - Dla każdej godziny doby: zużycie × liczba dni w tej strefie × cena
   - Sumuj dla całego roku
3. **Dla G12w i G13**: Najpierw oblicz, ile dni wolnych w 2026
   - Dni wolne: wszystkie godziny → Off-Peak (najniższa cena)
   - Dni robocze: strefy czasowe jak zwykle
4. **Dodaj opłaty stałe** (rozbite na komponenty)
5. **Pomnóż przez VAT 23%** (obliczenia można robić netto, VAT na koniec)
6. **Stwórz tabelę** pokazującą koszty w każdej taryfie
7. **Napisz dyskusję**: Która taryfa jest najtańsza i dlaczego?

**Wniosek**: Najprostsza taryfa (G11) nie zawsze jest najdroższa, jeśli profil zużycia jest odpowiedni

### Zadanie 4: Zapotrzebowanie na Energię Elektryczną

**Cel**: Oszacować roczne zużycie prądu dla rodziny 4-osobowej

**Źródła danych**:
- Kalkulatory internetowe (portale energetyczne)
- GUS (dane statystyczne Polsce)
- Eurostat (dane europejskie)

**Założenia**:
- Brak grzania elektrycznego domu (energia grzewcza pochodzi z innego źródła)
- Typowe urządzenia: oświetlenie, AGD, sprzęty elektroniczne, ciepła woda (elektryczna?)

**Wynik**: Roczne kWh dla porównania z Zadaniem 3

### Zadanie 5: Analiza Własnego Domu

**Struktura odpowiedzi**:

a. **Charakterystyka domu**:
   - Typ budynku (dom, mieszkanie)
   - Powierzchnia
   - Liczba osób
   - System ogrzewania (gaz, węgiel, pompa ciepła, itp.)
   - Duże odbiorniki (piece, klimatyzacja, itp.)
   - Źródła odnawialne (panele słoneczne, FV, itp.)

b. **Zużycie energii elektrycznej**:
   - Przeanalizuj faktury za elektryę (rzeczywiste dane)
   - Roczne zużycie [kWh]
   - Roczne koszty [PLN]
   - Trendy (sezonowość?)

c. **Zużycie na ogrzewanie**:
   - Przeanalizuj faktury za gaz, węgiel, drewno, itp.
   - Roczne zużycie (w naturalne jednostki)
   - Roczne koszty [PLN]
   - Rozdzielić CO (ogrzewanie domu) i CWU (ciepła woda) jeśli możliwe

d. **Emisja CO₂**:
   - Użyć współczynników KOBIZE
   - Całkowita emisja roczna z całego domu

### Zadanie 6: Elektromobilność

**Cel**: Zrozumieć energetyczną i ekonomiczną stronę pojazdów elektrycznych

**Struktura**:

a. **Wybór aut** — po jednym z każdej kategorii:
   - Małe auto miejskie (np. Tesla Model 3 Lite, Nissan Leaf)
   - Duże auto miejskie (np. Tesla Model S)
   - SUV (np. Tesla Model Y, Audi e-tron)

b. **Parametry każdego auta** (w tabeli):

   1. **Pojemność akumulatora** [kWh]
   
   2. **Czas ładowania** (przy różnych ładowarkach):
      - Szybka ładowarka DC (stacja)
      - Ładowarka AC (domowa, 3-fazowa 11 kW)
      - **Najtańsza ładowarka domowa** — jednofazowe gniazdko (2,3 kW)
   
   3. **Zużycie energii** [kWh/100 km]:
      - W ruchu miejskim
      - W trasie (szosie)
      - W ruchu mieszanym
   
   4. **Zasięg** [km]:
      - W ruchu miejskim
      - W trasie
      - W ruchu mieszanym

c. **Scenariusz codziennego użytku**:
   - 30 km dziennie, ruch miejski
   - Ile % energii z akumulatora? (30 km / zasięg miejski)
   - Czas ponownego ładowania do pełna (najtańszą ładowarką domową)
   - Obliczenia dla każdego z 3 aut

d. **Roczne zużycie energii**:
   - Rocznie 12 000 km
   - 70% w ruchu miejskim, 30% w trasie
   - Roczne kWh dla każdego auta

e. **Pokrycie fotowoltaiką**:
   - Ile kWp paneli słonecznych potrzeba, by całoroczne zużycie auta pokryć?
   - Założenie: 1 kWp produkuje ~1100 kWh/rok (warunki Polsce)
   - Wzór: kWp = (roczne kWh z pkt d) / 1100

**Obserwacje**: 
- Różne auta mają drastycznie różne zużycie energii
- Mała ładowarka domowa może być wystarczająca dla codziennych potrzeb
- Mała instalacja FV może zrównoważyć całość zużycia

---

## Kluczowe Dane Numeryczne do Pamiętania

| Wielkość | Wartość |
|----------|---------|
| 1 kWh | 3,6 MJ |
| 1 MWh | 3600 MJ |
| 1 kWp FV (Polska) | ~1100 kWh/rok |
| Taryfa G11 | Jedna cena przez dobę |
| Taryfa G12 | Peak 7–21, Off-Peak 22–6 |
| Taryfa G13 | Peak 8–10, 17–21; Standard 11–16, 22–7; Off-Peak 1–7 |

---

## Źródła Danych — Gdzie Szukać

**Ceny energii**:
- www.tge.pl — Towarowa Giełda Energii (raporty miesięczne/roczne)
- Strona Tauron S.A. — taryfy G11, G12, G12w, G13

**Dane statystyczne**:
- GUS (Główny Urząd Statystyczny) — polskie dane zużycia
- Eurostat — europejskie dane porównawcze

**Emisje CO₂**:
- KOBIZE (Krajowy Ośrodek Bilansowania i Zarządzania Emisjami)

**Pojazdy elektryczne**:
- Strony producentów (Tesla, Nissan, Audi, itp.)
- Portale oceny samochodów (np. ADAC, Which?)

**Panele słoneczne**:
- Dane producenckie, roczna produkcja energii

---

## Wskazówki do Sprawozdania

✓ **Format**: PDF, plik: `Nazwisko_Imię_sprawozdanie_cw1.pdf`

✓ **Zawartość**: Wszystkie 6 zadań z wynikami

✓ **Formy prezentacji**:
- Zadanie 1: Tabela konwersji
- Zadanie 2: Wykresy/tabele z analizą cen
- Zadanie 3: Duża tabela kosztów + dyskusja
- Zadania 4–5: Tekst + tabele ze zdnymi rzeczywistymi
- Zadanie 6: Tabela z parametrami aut + obliczenia

✓ **Komentarze**: Każdy wynik powinien być interpretowany

✓ **Źródła**: Wymienić co najmniej 2 źródła dla każdego typu danych

✓ **Dokładność**: Szczególnie w Zadaniu 3 — liczby muszą się zgadzać

✓ **Terminowość**: Umieścić w katalogu na UPeL przed kolejnymi zajęciami

---

## Kluczowe Wnioski do Zrozumienia

1. **Ceny energii są zmienne** — zarówno w ciągu doby, jak i sezonie
2. **Prawidłowy wybór taryfy oszczędza tysiące złotych rocznie** — nie zawsze najprosta taryfa (G11) jest najdroższa
3. **Fotowoltaika drastycznie zmienia rynek energii** — spłaszcza ceny w ciągu dnia
4. **Pojazdy elektryczne są energooszczędne** — znacznie mniej zużywają niż spalinowe
5. **Małe instalacje FV mogą pokryć całość zużycia auta** — jeśli auto jezdzi lokalnie
6. **Analiza rzeczywistych danych domu pokazuje rzeczywiste możliwości oszczędności** — każdy dom jest inny
