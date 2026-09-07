# SeniorAI — nakładka asystująca na Windows dla osób starszych

Koncepcja produktu w wersji 0.1: makieta, prezentacja i cztery dossier badawcze.
**Przed pierwszą linijką kodu produkcyjnego.**

## Deliverables

| Co | Gdzie |
|---|---|
| Interaktywna makieta (5 scenariuszy) | [`mockup/index.html`](mockup/index.html) · <https://claude.ai/code/artifact/ec06b0b9-057f-4911-ad23-8a4e60f1766b> |
| Prezentacja (32 slajdy) | [`deck/index.html`](deck/index.html) · <https://claude.ai/code/artifact/619b289c-f15c-43b2-a3e2-5f79d1dfea11> |
| Research | [`research/`](research/) — 4 dokumenty, ok. 37 tys. słów |

Prezentacja: `←`/`→` nawigacja, `O` siatka slajdów, `F` pełny ekran, `Ctrl+P` eksport do PDF.

## Produkt w jednym akapicie

Nakładka rysowana na istniejącym pulpicie Windows. Przyciemnia ekran poza jednym elementem,
obrysowuje go i mówi, co zrobić — ale **klika użytkownik**. Pięć poziomów asysty (0 — cisza,
4 — wykonanie zadania z widocznym kursorem i dziennikiem kroków) plus **Tarcza**: zawsze włączona
warstwa przerywająca oszustwa, jedyny element, który uruchamia się bez pytania.

## Dossier badawcze

| Plik | Zakres |
|---|---|
| [`research/01-competitive-landscape.md`](research/01-competitive-landscape.md) | 34 rozwiązania w 7 kategoriach, tabela porównawcza, krytyczna analiza luki rynkowej |
| [`research/02-gerontech-hci-evidence.md`](research/02-gerontech-hci-evidence.md) | Dowody HCI/gerontechnologii, 20 par „badanie → decyzja projektowa", 59 pozycji bibliografii |
| [`research/03-technical-feasibility.md`](research/03-technical-feasibility.md) | API Windows, benchmarki agentów, twarde ograniczenia, architektura, koszt API |
| [`research/04-market-and-need.md`](research/04-market-and-need.md) | Dane GUS / FBI IC3 / CERT Polska / Pew, 20 liczb na slajdy, krytyka danych |

## Sześć ustaleń, które ukształtowały projekt

1. **Nikt nie łączy tych funkcji w jednym produkcie na zwykłym Windowsie** — ale Microsoft buduje
   w tym kierunku i ma przewagę dystrybucyjną nie do podrobienia.
2. **Pełna autonomia AI na pulpicie nie działa.** Na WindowsAgentArena — benchmarku samego Microsoftu —
   najlepszy agent osiąga 19,5% wobec 74,5% u człowieka. Potwierdzenie każdego kroku to sufit techniczny,
   nie tylko decyzja o bezpieczeństwie.
3. **Okno UAC jest nieprzekraczalne.** Windows rysuje je na chronionym pulpicie; żaden podpis ani
   uprawnienie tego nie zmienia. „Kliknij Tak za seniora" wypada z zakresu produktu.
4. **Zdalny dostęp to główny wektor oszustw** — 1,04 mld USD strat Amerykanów 60+ w kategorii
   „wsparcie techniczne" (2025). Funkcja przejęcia kontroli architektonicznie przypomina atak,
   przed którym ma chronić. To jednocześnie największa szansa i największe ryzyko produktu.
5. **Wyręczanie może odbierać korzyść, którą obiecujemy.** Metaanaliza obejmująca 411 430 osób wiąże
   *aktywne* korzystanie z technologii z niższym ryzykiem pogorszenia funkcji poznawczych. Dlatego
   sukcesem jest spadający, nie rosnący poziom asysty.
6. **Model biznesowy jest nieudowodniony.** Przez dwie dekady żadna samodzielna subskrypcja
   oprogramowania dla seniorów nie osiągnęła skali. Rekomendowany wedge: partner, dla którego
   straty z oszustw są pozycją w rachunku wyników.

## Zasady metodologiczne

- Każda liczba w prezentacji ma źródło w pasku `ŹRÓDŁA` na slajdzie.
- Dane oznaczone w researchu jako „nie zweryfikowano" nie trafiły na slajdy.
- Dwie liczby krążące w automatycznych streszczeniach zostały odrzucone jako błędne
  (235 tys. phishingu w Polsce → faktycznie 40 120 wg CERT Polska; „średnia strata 83 tys. USD" →
  wewnętrznie sprzeczna, zastąpiona zweryfikowaną wartością 38,5 tys. USD z raportu IC3 2025).
- Sekcje „Krytyka danych" i „Twarde ograniczenia" w dossier wskazują, czego **nie** wolno cytować.

## Budowanie

```bash
python3 mockup/build.py   # src/index.html + zrzut pulpitu → mockup/index.html
python3 deck/build.py     # src/shell.html + src/slides.html + assets/*.jpg → deck/index.html
```

Oba skrypty wstawiają obrazy jako data URI, więc publikowane pliki są samowystarczalne.
Makieta rysuje nakładkę na `Windows_11_Desktop_bee0wa.webp` — prawdziwym zrzucie pulpitu Windows 11.
Zrzuty w `deck/assets/` pochodzą z makiety: po jej zmianie trzeba je odtworzyć i przebudować prezentację.

## System wizualny nakładki

| Rola | Kolor | Tekst na nim |
|---|---|---|
| Twoja kolej — podświetlenie, główne działanie | pomarańczowy `#FF6A1F` | czarny (7,2:1) |
| Teraz działa asystent | czarny `#0B0B0C` | pomarańczowy |
| Stop, zagrożenie | czerwony `#B3261E` | biały |
| Bezpiecznie, zrobione | zielony `#0B6B3A` | biały |

**Niebieskiego nie używamy w ogóle** — z trzech niezależnych powodów: żółknąca soczewka pochłania fale
krótkie, więc niebieski jest najgorszym kolorem sygnałowym dla tej grupy wiekowej; niebieski należy do
Windowsa, a oszust potrafi podrobić niebieskie okno systemu; i wreszcie pomarańcz maksymalnie odcina się
od niebieskiej tapety oraz akcentów systemu. Krój pisma nakładki to Atkinson Hyperlegible (Braille
Institute), a każde zdanie w interfejsie jest krótkie, w stronie czynnej i bez słownictwa branżowego.

## Zastrzeżenie

Symulowany pulpit Windows, treści wiadomości i postać „Haliny" są fikcyjne, stworzone na potrzeby
prezentacji. Nie są zrzutem z działającego produktu ani komunikatem Microsoftu. Analiza prawna
(RODO, akt o sztucznej inteligencji) jest wstępna i nie stanowi opinii prawnej.
