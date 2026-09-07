# Przegląd konkurencji i rynku — SeniorAI

**Data sporządzenia:** 07.09.2026
**Metodologia:** Research webowy (WebSearch/WebFetch), priorytet dla źródeł oficjalnych (strony producentów, learn.microsoft.com, support.microsoft.com, raporty urzędowe: FTC, FBI/IC3, Eurostat, GUS, US Census, Pew Research). Każda informacja opatrzona źródłem (organizacja + data + URL). Tam, gdzie danych nie udało się zweryfikować w źródle pierwotnym, jest to wprost oznaczone jako **„nie zweryfikowano"**. Ceny i funkcje zmieniają się często — traktować jako stan na dzień researchu, nie jako gwarancję aktualności.

---

## Streszczenie wykonawcze

1. **Nikt na rynku nie łączy wszystkich elementów wizji SeniorAI w jednym produkcie.** Nie znaleziono rozwiązania, które jednocześnie oferuje: żywą nakładkę cross-aplikacyjną (nie tylko w jednej stronie/apce), AI rozumiejące dowolny ekran, aktywne blokowanie ryzykownych kroków w czasie rzeczywistym, asystenta głosowego, lupę i opcjonalne częściowe przejęcie kontroli — na zwykłym Windows, bez zakupu dedykowanego sprzętu i bez subskrypcji AI stron trzecich. To realna, ale wąska luka.
2. **Microsoft buduje dokładnie w tym kierunku i ma przewagę dystrybucyjną nie do podrobienia.** Copilot Vision, Click to Do, Windows Recall i eksperymentalne Copilot Actions/Agent Workspace pokazują jasny kierunek „agentic OS" ogłoszony na Ignite (Microsoft, listopad 2025). To największe ryzyko strategiczne dla SeniorAI — nie tylko konkurent, ale platforma, na której SeniorAI musi działać.
3. **Kategoria „AI computer use" rozwija się w tempie, które trudno przecenić.** Wynik Claude na benchmarku OSWorld wzrósł z ~15% (październik 2024) do ponad 80% (połowa 2026) w niecałe dwa lata (Anthropic, 2024–2026). To sugeruje, że fundament technologiczny („AI, które rozumie i obsługuje dowolny ekran") lepiej kupić/wynająć jako API od dużego laba niż budować od zera.
4. **Dedykowane komputery/tablety dla seniorów istnieją od 15–20 lat i mają ograniczoną skalę.** Eldy — lider kategorii non-profit — ma ok. 400 000 użytkowników od 2006 r. (Eldy, brak daty rocznej na stronie). To niewiele wobec ~56 mln samych Amerykanów 65+ korzystających z internetu (Pew Research, 2025). Dowód trudnego go-to-market, nie braku potrzeby.
5. **Zdalny dostęp (TeamViewer, AnyDesk, Quick Assist, RustDesk) to jednocześnie najpopularniejsze narzędzie pomocy i narzędzie nr 1 w oszustwach na seniorach.** Osoby 60+ odpowiadały w 2024 r. za 58% strat finansowych ze scamów typu „tech support/call center" mimo że stanowiły 40% ofiar (FBI IC3, 2024, za pośrednictwem AARP). To jednocześnie najmocniejszy argument produktowy SeniorAI („bezpieczniejsza alternatywa") i największe ryzyko wizerunkowe (funkcja co-pilot/przejęcie kontroli wygląda z zewnątrz identycznie jak schemat oszustwa).
6. **Digital Adoption Platforms (WalkMe, Whatfix) rozwiązały technicznie UX „podświetl i pokaż" — ale tylko w obrębie jednej, ręcznie zinstrumentowanej aplikacji webowej, za enterprise'owe pieniądze** (mediana 43–79 tys. USD/rok, wdrożenia do 800 tys. USD/rok — Vendr/Userpilot, 2025–2026). Nikt nie zrobił tego cross-aplikacyjnie na poziomie systemu operacyjnego dla konsumenta.
7. **Narzędzia anty-scam szybko dodają AI i poszerzają zasięg.** Malwarebytes Scam Guard wystartował na mobile w czerwcu 2025, a już w lutym 2026 trafił na desktop Windows/Mac (Malwarebytes, 2025–2026). Okno czasowe na zbudowanie przewagi w kategorii „AI wykrywa oszustwo na żywo" szybko się zamyka.
8. **Wbudowane funkcje dostępności Windows są darmowe i stale ulepszane, ale każda robi jedną rzecz osobno.** Magnifier powiększa, Narrator czyta, Voice Access steruje głosem, Copilot Vision odpowiada na pytania o ekran (wymaga subskrypcji Microsoft 365) — żadna nie prowadzi seniora krok po kroku przez konkretne zadanie w dowolnej aplikacji ani nie ocenia ryzyka kroku.
9. **Rynek demograficzny jest bezsprzecznie duży i rośnie**: 21,6% ludności UE ma 65+ lat (Eurostat, dane na 01.01.2024), w Polsce to 7,7 mln osób / 20,6% populacji (GUS, 2025), w USA 61,2 mln / 18% (US Census Bureau, czerwiec 2025). 90% Amerykanów 65+ korzysta z internetu (Pew Research, 2025) — ale monetyzacja pozostaje niepewna: większość udanych graczy w kategorii senior-tech to darmowe non-profity (Eldy, Cyber-Seniors) albo sprzedawcy jednorazowego sprzętu (Telikin, GrandPad), nie subskrypcje software'u.
10. **Największym ryzykiem SeniorAI nie jest brak popytu, lecz wiarygodność.** W kategorii zbudowanej wokół „ochrony bliskiej osoby przed oszustwem", jeden głośny błąd — fałszywy alarm blokujący legalną czynność albo przepuszczenie prawdziwego ataku — może być nieodwracalny wizerunkowo, zwłaszcza że funkcja „przejęcia kontroli" architektonicznie przypomina mechanizm, przed którym produkt ma chronić.

---

## Tabela porównawcza

| Rozwiązanie | Kategoria | Platforma | Overlay na żywo? | AI ekranu? | Głos? | Lupa? | Blokada ryzyka? | Przejęcie kontroli? | Cena | Źródło |
|---|---|---|---|---|---|---|---|---|---|---|
| **Eldy** | Nakładka dla seniorów | Windows/Linux/Mac/Android/TV | Nie | Nie | Nie zweryfikowano | Nie | Nie | Nie | Darmowe | [eldy.eu](http://www.eldy.eu/en/about-us/) |
| **Telikin (Elite/Freedom)** | Dedykowany komputer AiO | Własny system (zamknięty) | Nie | Nie | Text-to-speech (czyta e-maile) | Nie zweryfikowano | Nie | Tak — płatny „VIP Support"/Tech Buddy (człowiek) | ok. 699–1299 USD + support (dokładna cena support nie zweryfikowana) | [telikin.com](https://www.telikin.com/telikin_elite_2.php) |
| **WOW! Computer** | Dedykowany komputer AiO | Własny Linux (zamknięty) | Nie | Nie | Nie zweryfikowano | Tak (zoom do 200% jednym przyciskiem) | Nie | Nie zweryfikowano | 1299 USD (cena katalogowa) | [mywowcomputer.com](https://www.mywowcomputer.com/) |
| **GrandPad** | Dedykowany tablet | Android (zamknięty launcher) | Nie | Nie zweryfikowano | Wideorozmowy (nie sterowanie głosem) | Nie zweryfikowano | Nie (zamknięta lista kontaktów ogranicza, ale nie aktywnie blokuje) | Nie | Tablet 200–400 USD (rozbieżne dane wg sprzedawcy) + subskrypcja 25–65 USD/mies. | [grandpad.net](https://www.grandpad.net/); [Consumer Cellular](https://www.consumercellular.com/blog/meet-grandpad-unique-solution-family-connections/) |
| **Claris Companion** | Dedykowany tablet/aplikacja | Android (zamknięty) | Nie | Nie zweryfikowano | Nie zweryfikowano | Nie zweryfikowano | Tak (zamknięte środowisko bez ryzyka pobrań/spamu — wg producenta) | Nie | Nie zweryfikowano (model B2B/wycena indywidualna) | [clarishealthcare.com](https://clarishealthcare.com/claris-companion/) |
| **SeeYouLink** | Nakładka dla seniorów | Windows | Nie | Nie | Nie zweryfikowano | Nie zweryfikowano | Nie | Tak (funkcja zdalnego dostępu dla rodziny) | 4,95 USD/mies. po 3-mies. trialu | [seeyoulink.com](https://www.seeyoulink.com/download) |
| **Inteset Secure Lockdown** | Blokada/kiosk Windows | Windows | Nie | Nie | Nie | Nie | Częściowo (statyczna konfiguracja — blokuje dostęp do niechcianych aplikacji/stron) | Nie (integruje się z TeamViewer) | Licencja jednorazowa (dokładna cena nie zweryfikowana) | [inteset.com](https://www.inteset.com/secure-computers-for-senior-citizens) |
| **Candoo Tech** | Usługa wsparcia ludzkiego | Dowolna (zdalna pomoc/wideo) | Nie | Nie | Nie | Nie | Nie | Tak (człowiek, nie AI) | Członkostwo 228–240 USD/rok, sesja 75–80 USD | [candootech.com](https://www.candootech.com/service-offerings) |
| **Uniper Care** | Platforma zaangażowania społecznego | TV/PC/tablet/smartfon | Nie | Nie | Nie | Nie | Nie | Nie | Nie zweryfikowano (model B2B: plany zdrowotne, placówki) | [unipercare.com](https://www.unipercare.com/blog/uniper-launches-cross-platform-telehealth-and-social-engagement-service-for-older-adult) |
| **Cyber-Seniors** | Program szkoleniowy (non-profit) | Dowolna | Nie (to ludzie-wolontariusze) | Nie | Nie | Nie | Nie | Nie | Darmowe | [cyberseniors.org](https://cyberseniors.org/) |
| **Windows Magnifier** | Wbudowana dostępność | Windows | Nie | Nie | Nie | **Tak** | Nie | Nie | Darmowe | [support.microsoft.com](https://support.microsoft.com/en-us/windows/use-magnifier-to-make-things-on-the-screen-easier-to-see-414948ba-8b1c-d3bd-8615-0e5e32204198) |
| **Windows Narrator** | Wbudowana dostępność | Windows | Nie | Częściowo (AI opisuje obrazy od 2025) | Tak (czyta ekran) | Nie | Nie | Nie | Darmowe | [support.microsoft.com](https://support.microsoft.com/en-us/accessibility/windows/narrator/complete-guide-to-narrator); [blogs.windows.com](https://blogs.windows.com/windowsexperience/2025/12/03/2025-a-year-in-recap-windows-accessibility/) |
| **Windows Voice Access** | Wbudowana dostępność | Windows 11 (22H2+) | Nie (wykonuje komendy, nie prowadzi przez zadanie) | Nie | **Tak** (pełne sterowanie, offline) | Nie | Nie | Nie | Darmowe | [support.microsoft.com](https://support.microsoft.com/en-us/accessibility/windows/voice-access/get-started-with-voice-access) |
| **Windows Copilot Vision** | AI asystent ekranowy | Windows/Edge/mobile | Częściowo (odpowiada o ekranie na żywo, nie klika za użytkownika) | **Tak** | **Tak** (tylko przez rozmowę głosową) | Nie | Nie | Nie | Wymaga subskrypcji Microsoft 365 (Personal/Family/Premium) | [support.microsoft.com](https://support.microsoft.com/en-us/microsoft-copilot/using-copilot-vision-with-microsoft-copilot) |
| **Windows Recall** | AI pamięci ekranu (Copilot+ PC) | Windows (tylko sprzęt z NPU) | Nie (retrospektywne, nie „na żywo") | **Tak** | Nie | Nie | Nie | Nie | Darmowe, wymaga sprzętu Copilot+ PC | [learn.microsoft.com](https://learn.microsoft.com/en-us/windows/apps/develop/windows-integration/recall/) |
| **Windows Click to Do** | AI ekranowe (Copilot+ PC) | Windows (tylko Copilot+ PC) | Nie (reaktywne, jednorazowe) | **Tak** | Nie | Nie | Nie | Nie | Darmowe, wymaga sprzętu Copilot+ | [learn.microsoft.com](https://learn.microsoft.com/en-us/windows/client-management/manage-click-to-do) |
| **Windows Quick Assist** | Zdalna pomoc | Windows | Nie | Nie | Nie | Nie | Nie | **Tak** (pełne przejęcie przez inną osobę) | Darmowe | [support.microsoft.com](https://support.microsoft.com/en-us/windows/apps/solve-pc-problems-remotely-using-quick-assist) — **masowo nadużywane w oszustwach, patrz sekcja 4** |
| **Copilot Actions / Windows Agent Workspace** | Agent AI (eksperymentalne) | Windows 11 Insider Preview | Częściowo (wieloetapowe zadania) | **Tak** | Nie zweryfikowano | Nie | Częściowo (zgody per-folder, log audytowy, „least privilege") | Tak (w odizolowanym koncie agenta) | Darmowe, domyślnie **wyłączone**, tylko Insider Preview | [support.microsoft.com](https://support.microsoft.com/en-us/windows/ai/ai-features/experimental-agentic-features) |
| **Anthropic Computer Use (API)** | Agent AI „computer use" | Sandbox/VM (nie żywy desktop użytkownika) | **Tak** (w izolowanym środowisku) | **Tak** | Nie | Nie | Częściowo (zalecany, nie wymuszony human-in-the-loop) | Tak — ale w sandboxie, nie na realnym pulpicie | Cena API (za token), produkt deweloperski | [anthropic.com](https://www.anthropic.com/news/3-5-models-and-computer-use); [platform.claude.com](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) |
| **OpenAI ChatGPT Agent** (następca Operatora) | Agent AI przeglądarkowy | Chmura (przeglądarka w chmurze) | Tak | Tak | Nie zweryfikowano | Nie | Nie zweryfikowano | Tak (w izolowanej przeglądarce chmurowej) | W ramach planu ChatGPT (Plus/Pro) | [openai.com](https://openai.com/index/introducing-chatgpt-agent/) |
| **Google Gemini Computer Use (model)** | Model/API agenta | Chmura/API | Tak | Tak | Nie zweryfikowano | Nie | Nie zweryfikowano | Tak (dla deweloperów) | API (opłata za token) | [blog.google](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/) |
| **Rabbit R1 (DLAM)** | Dedykowane urządzenie z LAM | Własny sprzęt (Rabbit OS) | Częściowo | Tak | **Tak** (mikrofon jako główny input) | Nie | Nie zweryfikowano | Tak („plug-and-play" kontroler wg producenta) | Urządzenie 199 USD | [rabbit.tech](https://www.rabbit.tech/blog/first-major-update-of-2026-dlam-openclaw-and-a-surprise) |
| **Simular Agent S2** | Otwarty framework agenta | Windows/lokalnie lub chmura | Tak | Tak | Nie | Nie | Nie zweryfikowano | Tak | Open source (koszt = wybrany model LLM) | [simular.ai](https://www.simular.ai/articles/agent-s2); [GitHub](https://github.com/simular-ai/Agent-S) |
| **Open Interpreter** | Otwarty agent lokalny | Lokalnie, dowolny system | Tak | Tak (zależnie od modelu) | Tak (moduł „01") | Nie | Częściowo (prosi o zgodę przed uruchomieniem kodu; **brak sandboxa domyślnie** wg własnej dokumentacji) | Tak | Open source, darmowy (koszt = model LLM) | [GitHub](https://github.com/openinterpreter/openinterpreter) |
| **TeamViewer** | Zdalny dostęp (komercyjny) | Windows/Mac/mobile | Nie | Nie | Nie | Nie | Nie | **Tak** | Płatny (biznes), darmowy do użytku niekomercyjnego | [teamviewer.com](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/security/teamviewer-and-scamming/) |
| **Chrome Remote Desktop** | Zdalny dostęp (Google) | Dowolna (przez przeglądarkę) | Nie | Nie | Nie | Nie | Nie | **Tak** | Darmowe | [support.google.com](https://support.google.com/chrome/answer/1649523) |
| **RustDesk** | Zdalny dostęp open source | Windows/Mac/Linux/mobile/web | Nie | Nie | Nie | Nie | Częściowo (własne komunikaty anty-scam wbudowane w produkt) | **Tak** | Darmowe (self-hosted), funkcje enterprise płatne | [rustdesk.com](https://rustdesk.com/blog/rustdesk-and-remote-access-scams/) |
| **WalkMe** | Digital Adoption Platform | Web (+ Workstation jako hub) | Tak — ale tylko w obrębie zinstrumentowanej aplikacji webowej | Częściowo (DeepUI rozpoznaje elementy UI) | Nie | Nie | Nie | Nie | Enterprise, custom: mediana 43–79 tys. USD/rok | [userpilot.com](https://userpilot.com/blog/walkme-pricing/); [vendr.com](https://www.vendr.com/marketplace/walkme) |
| **Whatfix** | Digital Adoption Platform | Web/desktop/mobile/Citrix VDI | Tak — w obrębie zinstrumentowanej aplikacji | Częściowo | Nie | Nie | Nie | Nie | Enterprise, custom (brak cennika publicznego) | [whatfix.com](https://whatfix.com/blog/desktop-and-vdi-app-adoption/) |
| **Intro.js / Shepherd.js** | Biblioteka open source | Tylko przeglądarka (własna strona) | Tak — w obrębie własnej strony | Nie | Nie | Nie | Nie | Nie | Darmowe / licencja komercyjna od 9,99 USD (Intro.js) | [introjs.com](https://introjs.com/); [GitHub Shepherd](https://github.com/shipshapecode/shepherd) |
| **Aura** | Ochrona przed oszustwami/tożsamością | Windows/Mac/mobile | Nie | Nie | Nie | Nie | Częściowo (blokowanie połączeń/spamu, monitoring) | Nie | od 12 USD/mies. (single); 30 USD/mies. rodzina do 5 os. | [aura.com](https://www.aura.com/identity-theft-protection) |
| **EverSafe** | Monitoring finansowy | Web/e-mail | Nie | Częściowo (silnik AI „CATCH" wykrywa anomalie transakcji) | Nie | Nie | Tak (alerty do rodziny/opiekunów) | Nie | 7,49–24,99 USD/mies. (3 plany) | [eversafe.com](https://www.eversafe.com/) |
| **Trend Micro Check (ID Protection)** | Rozszerzenie anty-scam | Chrome i in. przeglądarki | Nie | Częściowo (ocena linków) | Nie | Nie | Tak (blokuje niebezpieczne strony) | Nie | Darmowe | [trendmicro.com](https://www.trendmicro.com/en_us/forHome/products/trend-micro-scam-check.html) |
| **Malwarebytes Scam Guard** | AI anty-scam | iOS/Android (2025), Windows/Mac (2026) | Częściowo (czat AI na żądanie) | **Tak** | Nie zweryfikowano | Nie | Częściowo (ostrzega, nie blokuje aktywnie akcji systemowej) | Nie | Darmowe + warianty płatne | [malwarebytes.com](https://www.malwarebytes.com/press/2025/06/03/malwarebytes-launches-scam-guard-an-ai-powered-mobile-first-digital-safety-companion-to-combat-todays-most-pernicious-threats) |
| **Microsoft Defender SmartScreen** | Wbudowana ochrona | Windows/Edge | Nie | Nie | Nie | Nie | **Tak** (blokuje znane złośliwe strony/pliki/hasła wielokrotnego użytku) | Nie | Darmowe (wbudowane) | [learn.microsoft.com](https://learn.microsoft.com/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/) |

*Uwaga: „SimplicITy" (UK, ok. 2009, Valerie Singleton/Wessex Computers) uznano za projekt historyczny bez potwierdzonej aktywności — pominięto w tabeli, opisano w sekcji 1. „K-Ploud" oraz konkretny produkt „PC-Ware Senior PC" nie zostały odnalezione w żadnym zweryfikowanym źródle — patrz zastrzeżenie w sekcji 1.*

---

## 1. Dedykowane nakładki / uproszczone interfejsy dla seniorów

**Ogólny wniosek:** kategoria istnieje od dwóch dekad, jest rozdrobniona, w większości non-profit lub bardzo mała skala, i w zdecydowanej większości opiera się na **zamkniętej, statycznej powłoce** (ograniczony zestaw dużych przycisków) — a nie na **AI, które rozumie kontekst i prowadzi przez zadanie**. To ważne: żaden z tych graczy nie robi tego, co ma robić SeniorAI (żywe prowadzenie krok po kroku + rozumienie dowolnego ekranu).

- **Eldy** ([eldy.eu](http://www.eldy.eu/en/)) — darmowe oprogramowanie non-profit (włoskie stowarzyszenie Eldy), zamienia dowolny PC w uproszczony interfejs 6-przyciskowy (e-mail, internet, czat, wideorozmowy, dokumenty, zdjęcia, Skype). Działa na Windows, Linux, Mac, tabletach i TV. Ponad 400 000 użytkowników od 2006 r., bez reklam. Brak funkcji AI, brak żywego prowadzenia przez zadania — to statyczny, uproszczony launcher, nie asystent. *Źródło: [Eldy — What is Eldy](http://www.eldy.eu/en/about-us/); wersja 2.3 nadal dostępna do pobrania (stan researchu 09.2026).* Uwaga: istnieje osobny, niepowiązany produkt **ELDYcare** (Estonia, 2025) — oprogramowanie do zarządzania opieką w domach seniora dla personelu, a nie nakładka dla użytkownika końcowego — nie mylić z Eldy. *Źródło: [estoniadigital.wordpress.com, wrzesień 2025](https://estoniadigital.wordpress.com/2025/09/28/healthtech-startup-eldycare-introduces-software-to-harmonise-care-for-the-elderly/).*

- **Telikin** ([telikin.com](https://www.telikin.com/telikin_elite_2.php)) — dedykowany komputer all-in-one z ekranem dotykowym (18,6"–22"), zamknięty system. Wbudowane: e-mail, wideorozmowy (Skype), przeglądarka, edytor tekstu, arkusz kalkulacyjny, czytnik DVD/CD, funkcja text-to-speech czytająca e-maile na głos, płatny „Tech Buddy"/„VIP Support" (pomoc zdalna człowieka). Cena historyczna 699–1299 USD w zależności od modelu; aktualny cennik niepodany publicznie na stronie (trzeba dzwonić). Brak AI rozumiejącego ekran. *Źródło: [Telikin Elite II](https://www.telikin.com/telikin_elite_2.php); [Wikipedia — Telikin](https://en.wikipedia.org/wiki/Telikin).*

- **WOW! Computer** ([mywowcomputer.com](https://www.mywowcomputer.com/)) — komputer all-in-one 22" na bazie Linuksa, firma działająca od 2007 r. (Ocala, Floryda). Duże kwadratowe ikony, jednoprzyciskowy zoom do 200%, wbudowany antywirus, automatyczne aktualizacje. Cena katalogowa 1299 USD (częste promocje -200 USD). Brak potwierdzonych funkcji AI. *Relacja korporacyjna z Telikin pojawiła się w jednym z wtórnych źródeł, ale nie została potwierdzona w źródle pierwotnym — traktować jako nie zweryfikowane.* *Źródło: [mywowcomputer.com](https://www.mywowcomputer.com/computer-for-seniors/); [elderguru.com](https://www.elderguru.com/wow-computer-for-seniors/).*

- **GrandPad** ([grandpad.net](https://www.grandpad.net/)) — tablet Android z zamkniętym launcherem, zablokowany pod konkretnego operatora, wymaga planu/subskrypcji. Ceny sprzętu i abonamentu **istotnie się różnią między źródłami**: sprzęt od ok. 200 USD (z EasyPay) do 399,99 USD (Amazon); subskrypcja od 25 USD/mies. (rocznie 275 USD) do 65 USD/mies., zależnie od sprzedawcy (bezpośrednio GrandPad vs. Consumer Cellular vs. Amazon). Zawiera nielimitowane 4G LTE, wideorozmowy, wsparcie 24/7. Obecność na CES 2025 z zapowiedzią zastąpienia telefonu/komputera. Brak potwierdzonych funkcji AI ekranowego. *Źródło: [Consumer Cellular blog](https://www.consumercellular.com/blog/meet-grandpad-unique-solution-family-connections/); [Reviewed.com](https://www.reviewed.com/accessibility/content/grandpad-review-price-tablet-for-seniors-accessible); [Podfeet — CES 2025](https://www.podfeet.com/blog/2025/04/ces-2025-grandpad/).*

- **Claris Companion** ([clarishealthcare.com](https://clarishealthcare.com/claris-companion/)) — tablet (Samsung Galaxy, Wi-Fi lub komórkowy) lub wersja software-only DIY na własny tablet Android, sprzedawany głównie do agencji opieki (B2B). Zamknięte środowisko bez możliwości pobierania aplikacji/spamu wg producenta. Funkcje: przypomnienia o lekach, programy wellness, monitoring zdalny przez opiekunów. Cena nie zweryfikowana (model wyceny indywidualnej dla instytucji). *Źródło: [clarishealthcare.com/claris-for-family](https://clarishealthcare.com/claris-companion/claris-for-family/).*

- **SeeYouLink** ([seeyoulink.com](https://www.seeyoulink.com/download)) — dodatkowe znalezisko spoza listy z briefu, ale bezpośrednio konkurencyjne: oprogramowanie webowe zmieniające dowolny Windows PC w uproszczony interfejs 6-przyciskowy, z funkcją zdalnego dostępu dla rodziny. Model: 3 miesiące za darmo, potem 4,95 USD/mies. Firma z Las Vegas, założona 2011. *Źródło: [Modern Health Talk](https://mhealthtalk.com/helping-seniors-master-computers/).*

- **Inteset Secure Lockdown** ([inteset.com](https://www.inteset.com/secure-computers-for-senior-citizens)) — nie jest produktem „dla seniorów" sensu stricto, lecz narzędziem blokady/kiosku dla Windows, jawnie promowanym też pod tym kątem: blokuje pulpit i ogranicza dostęp do wybranych aplikacji, integruje się z TeamViewer do zdalnej pomocy IT/rodziny. To ilustruje istniejące, tanie rozwiązanie „ograniczonego dostępu", ale statyczne — nie ocenia ryzyka na bieżąco. *Źródło: [inteset.com](https://www.inteset.com/secure-computers-for-senior-citizens).*

- **Simplicity Computers** (UK, [simplicitycomputers.co.uk](https://www.simplicitycomputers.co.uk/)) — aktywna obecnie brytyjska Community Interest Company (non-profit) sprzedająca uproszczone komputery/laptopy. Odrębna od historycznego projektu **SimplicITy** (ok. 2009, Valerie Singleton + Wessex Computers, system z 6 głównymi przyciskami) — ten drugi wygląda na projekt zakończony/martwy (brak śladów aktywności po ok. 2010–2011 w dostępnych źródłach); status **nie zweryfikowano definitywnie**, ale prawdopodobnie nieaktywny. *Źródło: [IT Pro](https://www.itpro.com/617494/older-people-get-their-own-simple-computer); [Crunchbase](https://www.crunchbase.com/organization/simplicity-computers).*

- **Candoo Tech** ([candootech.com](https://www.candootech.com/)) — nie jest software'em, lecz **usługą wsparcia ludzkiego** (NYC, USA): abonament 228–240 USD/rok (lub ok. 19–28 USD/mies.) obejmujący sesję startową do 90 min + nielimitowany „Quick Support" (30 min), dodatkowe sesje 75–80 USD/h. Ważny model biznesowy do rozważenia jako substytut/komplement dla SeniorAI — konsjerż-człowiek na żywo, a nie AI. *Źródło: [candootech.com/service-offerings](https://www.candootech.com/service-offerings).*

- **Uniper Care** ([unipercare.com](https://www.unipercare.com/)) — platforma telezdrowia i zaangażowania społecznego (nie accessibility-overlay) na TV/PC/tablet/smartfon, walcząca z samotnością seniorów. Finansowanie: 4 mln USD (2020) + kolejne 14,5 mln USD (łącznie 21 mln USD), model B2B (plany zdrowotne, placówki opieki, VA). Współpraca z amerykańskim Department of Veterans Affairs. Nie konkuruje bezpośrednio z SeniorAI funkcjonalnie, ale konkuruje o budżet/uwagę rodzin. *Źródło: [PR Newswire, 2020](https://www.prnewswire.com/news-releases/uniper-launches-cross-platform-telehealth-and-social-engagement-service-for-older-adult-population-in-response-to-covid-19-outbreak-to-address-isolation-hardships-301029485.html); [PRWeb — finansowanie](https://www.prweb.com/releases/uniper-care-secures-4-million-in-funding-to-combat-loneliness-and-isolation-among-older-adults-874568053.html).*

- **Cyber-Seniors** ([cyberseniors.org](https://cyberseniors.org/)) — non-profit (od 2015, powstały z filmu dokumentalnego), model wolontariacki: młodzież szkoli seniorów (internet, telezdrowie, portale świadczeń). Ponad 3000 wolontariuszy, 16 000+ godzin. To program edukacyjny, nie produkt technologiczny — ale pokazuje, że „nauczenie" bywa preferowanym rozwiązaniem problemu zamiast „zastąpienia/uproszczenia" interfejsu. *Źródło: [cyberseniors.org](https://cyberseniors.org/).*

- **Silver Surfers** — to nie jeden produkt, lecz **generyczna nazwa** używana przez wiele niezależnych brytyjskich organizacji charytatywnych/lokalnych (Age UK, Silver City Surfers Aberdeen, Silver Surfers Training Worcestershire i inne) prowadzących darmowe/płatne kursy komputerowe dla seniorów. Brak jednego scentralizowanego produktu do porównania. *Źródło: [Age UK Waltham Forest](https://www.ageuk.org.uk/walthamforest/activities-and-events/silver-surfers-computer-classes/); [Silver City Surfers](https://silvercitysurfers.co.uk/).*

- **Zastrzeżenie — pozycje nie zweryfikowane:** **„K-Ploud"** — mimo wielokrotnych prób (różne warianty pisowni) nie odnaleziono żadnego produktu/firmy o tej nazwie związanej z technologią dla seniorów. **„PC-Ware" / „Senior PC"** (wskazane w briefie jako potencjalny polski produkt) — nie odnaleziono konkretnego, nazwanego tak produktu; polskie wyniki wyszukiwania zwracają wyłącznie generyczne poradniki „jaki komputer dla seniora kupić" (Morele.net, Xlap24, Altreo), a nie dedykowany produkt/nakładkę o tej nazwie. **Obie pozycje traktować jako nie zweryfikowane — możliwe, że nie istnieją jako samodzielne produkty, są bardzo niszowe/regionalne, lub funkcjonują pod inną nazwą.**

---

## 2. Wbudowane funkcje dostępności Windows (baseline konkurencyjny)

To jest **prawdziwy, bezpłatny punkt odniesienia**, z którym SeniorAI konkuruje na starcie — każdy Windows PC już to ma.

- **Magnifier (Lupa)** — darmowe, wbudowane. Skróty Win+`+`/Win+Esc, tryby pełnoekranowy/soczewka/zadokowany. **Czego NIE robi:** nie rozumie co powiększa, nie podąża inteligentnie za kontekstem zadania, nie integruje się z prowadzeniem krok po kroku. *Źródło: [support.microsoft.com](https://support.microsoft.com/en-us/windows/use-magnifier-to-make-things-on-the-screen-easier-to-see-414948ba-8b1c-d3bd-8615-0e5e32204198).*

- **Narrator** — czytnik ekranu. W 2025 r. dodano opisy obrazów generowane przez AI, tryb skanowania, „Screen Curtain" (wygaszanie ekranu przy zachowaniu odczytu głosowego). **Czego NIE robi:** zaprojektowany dla użytkowników niewidomych/słabowidzących — wymaga nauczenia się sporego słownika komend/nawigacji, co dla przeciętnego, niewprawnego seniora bywa barierą samą w sobie, a nie rozwiązaniem. *Źródło: [support.microsoft.com — Complete guide to Narrator](https://support.microsoft.com/en-us/accessibility/windows/narrator/complete-guide-to-narrator); [blogs.windows.com, grudzień 2025](https://blogs.windows.com/windowsexperience/2025/12/03/2025-a-year-in-recap-windows-accessibility/).*

- **Voice Access** — pełne sterowanie PC głosem bez internetu, dostępne od Windows 11 22H2. Otwieranie/przełączanie aplikacji, dyktowanie tekstu, komendy korekcyjne, interaktywny przewodnik nauki komend. **Czego NIE robi:** nie prowadzi proaktywnie przez zadanie („teraz powiedz X, żeby zrobić Y") — użytkownik musi znać komendę, nie odwrotnie; to narzędzie sterowania, nie asystent. *Źródło: [support.microsoft.com](https://support.microsoft.com/en-us/accessibility/windows/voice-access/get-started-with-voice-access).*

- **Live Captions** — napisy na żywo z dowolnego audio, przetwarzanie w 100% lokalne (on-device), tłumaczenie w czasie rzeczywistym na Copilot+ PC. **Czego NIE robi:** wyłącznie napisy — nie ma żadnego elementu sterowania pulpitem ani wskazywania gdzie kliknąć. *Źródło: [support.microsoft.com](https://support.microsoft.com/en-us/accessibility/windows/use-live-captions-to-better-understand-audio).*

- **Ease of Access / Ustawienia dostępności** — centralny hub (Win+U) grupujący Magnifier, Narrator, kontrast, klawiaturę itd. **Czego NIE robi:** to katalog ustawień, nie proaktywny asystent — użytkownik musi już wiedzieć, że problem istnieje i gdzie szukać rozwiązania. *Źródło: [support.microsoft.com](https://support.microsoft.com/en-ph/help/17180/windows-10-make-your-pc-easier-to-use).*

- **Windows Copilot / Copilot Vision** — AI „widzi" pulpit/aplikacje/przeglądarkę podczas rozmowy głosowej i odpowiada na pytania lub podpowiada kroki. **Kluczowe ograniczenia:** (1) wymaga subskrypcji **Microsoft 365 Personal/Family/Premium** — to nie jest darmowa funkcja Windows; (2) działa wyłącznie w ramach rozmowy głosowej zainicjowanej przez użytkownika, nie jest „zawsze włączonym" stróżem; (3) **doradza, ale nie wykonuje akcji** — nie kliknie, nie wypełni formularza za użytkownika (to zadanie osobnej, dużo wcześniejszej fazy funkcji „Copilot Actions"). *Źródło: [support.microsoft.com](https://support.microsoft.com/en-us/microsoft-copilot/using-copilot-vision-with-microsoft-copilot).*

- **Windows Recall** — lokalne, szyfrowane (TPM) zrzuty ekranu przeszukiwalne językiem naturalnym, z filtrowaniem danych wrażliwych i wymogiem Windows Hello przy każdym uruchomieniu/zmianie ustawień. **Kluczowe ograniczenia:** (1) wymaga sprzętu **Copilot+ PC** (dedykowany NPU) — nie działa na starszych/tańszych komputerach, które realnie mają seniorzy; (2) domyślnie **wyłączone** (opt-in); (3) to pamięć **retrospektywna** („co robiłem wcześniej"), nie żywe prowadzenie/ostrzeganie w danej chwili. *Źródło: [learn.microsoft.com](https://learn.microsoft.com/en-us/windows/apps/develop/windows-integration/recall/); [blogs.windows.com, wrzesień 2024](https://blogs.windows.com/windowsexperience/2024/09/27/update-on-recall-security-and-privacy-architecture/).*

- **Windows Click to Do** — na Copilot+ PC: zrzut ekranu na żądanie + AI rozpoznaje tekst/obrazy i proponuje akcje (kopiuj, podsumuj, szukaj w sieci, zapytaj Copilota). Przetwarzanie lokalne (on-device). **Kluczowe ograniczenia:** (1) tylko sprzęt Copilot+ PC; (2) reaktywne i jednorazowe — użytkownik musi aktywnie wywołać funkcję, nie ma trybu „obserwuj i ostrzegaj na bieżąco"; (3) rozpoznaje tekst/obrazy, ale nie „rozumie" zadania w toku. *Źródło: [learn.microsoft.com](https://learn.microsoft.com/en-us/windows/client-management/manage-click-to-do); [Windows Central](https://www.windowscentral.com/software-apps/windows-11/what-is-click-to-do-and-how-do-you-get-started-ai-actions-for-windows-11-explained).*

- **Quick Assist** — darmowe, wbudowane narzędzie zdalnej pomocy (kod 6-cyfrowy, laser wskaźnika, adnotacje, czat, opcja pełnego przejęcia kontroli). **Krytyczny problem:** to narzędzie jest **masowo nadużywane w atakach ransomware/oszustwach** (patrz sekcja 4) — Microsoft sam rekomenduje rozważenie blokowania/odinstalowania tego narzędzia w środowiskach, gdzie nie jest używane. *Źródło: [support.microsoft.com](https://support.microsoft.com/en-us/windows/apps/solve-pc-problems-remotely-using-quick-assist); [Microsoft Security Blog, 15.05.2024](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/).*

- **Steps Recorder (Problem Steps Recorder)** — **wycofywane**: zapowiedź deprecjacji w listopadzie 2023, baner ostrzegawczy od aktualizacji z lutego 2024, planowane usunięcie (data nieznana). Microsoft rekomenduje zamienniki: Snipping Tool, Xbox Game Bar, Clipchamp — **żaden z nich nie nagrywa automatycznie opisanych kroków (zrzut + adnotacja tekstowa każdej akcji)** tak jak PSR. To realna luka, którą Microsoft świadomie zamyka zamiast rozwijać — dokładnie w momencie, gdy technologia „pokaż mi krok po kroku co zrobiłeś" mogłaby być bazą pod AI-asystenta. *Źródło: [support.microsoft.com/steps-recorder-deprecation](https://support.microsoft.com/en-us/windows/apps/steps-recorder-deprecation).*

- **Focus Assist** — wyciszanie powiadomień (tryby: wyłączony/tylko priorytetowe/tylko alarmy), automatyczne reguły czasowe. To zarządzanie rozpraszaczami, niezwiązane z prowadzeniem przez zadania. *Źródło: [support.microsoft.com](https://support.microsoft.com/en-us/windows/make-it-easier-to-focus-on-tasks-0d259fd9-e9d0-702c-c027-007f0e78eaf2).*

- **Copilot Actions / Windows Agent Workspace** — zapowiedziane na Ignite (listopad 2025), agent AI wykonujący wieloetapowe zadania („wyciągnij tabele z PDF-ów, podsumuj, wyślij e-mail") w odizolowanym koncie/przestrzeni roboczej. Zabezpieczenia opisane oficjalnie: zasada „non-repudiation" (każda akcja agenta jest odróżnialna od akcji użytkownika), logi audytowe odporne na manipulację, zasada najmniejszych uprawnień, zgody per-folder („zawsze pozwól"/„pytaj za każdym razem"/„nigdy"), **domyślnie wyłączone**, tylko w Windows Insider Preview (build 26100.7344+), wymaga włączenia przez administratora. **To pokazuje kierunek, w którym zmierza Microsoft — praktycznie opis funkcji bardzo zbliżonej do rdzenia SeniorAI, ale na wczesnym, eksperymentalnym etapie i bez profilu „senior/dostępność".** *Źródło: [support.microsoft.com/experimental-agentic-features](https://support.microsoft.com/en-us/windows/ai/ai-features/experimental-agentic-features).*

**Wniosek dla sekcji 2:** baseline Windows jest mocny i **darmowy**, ale rozdrobniony na osobne narzędzia, z kluczowymi funkcjami AI zamkniętymi za (a) płatną subskrypcją M365 (Copilot Vision) lub (b) drogim sprzętem Copilot+ PC z NPU (Recall, Click to Do) — obie bariery, które SeniorAI może ominąć, jeśli zbuduje własne, tańsze/dostępniejsze rozwiązanie AI działające na zwykłym sprzęcie. Jednocześnie eksperymentalne Copilot Actions pokazują, że Microsoft **już projektuje** dokładnie klasę zabezpieczeń (audyt, zgody, izolacja), którą SeniorAI musi zbudować samodzielnie — i ma do tego uprzywilejowany dostęp na poziomie systemu operacyjnego.

---

## 3. AI „computer use" / agenci sterujący pulpitem

**Kluczowe pytanie dla SeniorAI: czy budować własny model rozumienia ekranu, czy oprzeć się na API dużego laba?** Dane poniżej sugerują to drugie — tempo postępu jest zbyt szybkie, by konkurować od podstaw.

### Benchmarki — twarde liczby ze źródeł

| Model/Agent | Benchmark | Wynik | Data | Źródło |
|---|---|---|---|---|
| Claude 3.5 Sonnet (computer use, pierwsza wersja) | OSWorld (tylko zrzuty ekranu) | 14,9% (najbliższy konkurent: 7,8%) | 22.10.2024 | [Anthropic](https://www.anthropic.com/news/3-5-models-and-computer-use) |
| Claude 3.5 Sonnet (computer use, z dodatkowymi krokami) | OSWorld | 22,0% | 22.10.2024 | [Anthropic](https://www.anthropic.com/news/3-5-models-and-computer-use) |
| Claude Opus 4.6 | OSWorld | 72,7% (≈ ludzki baseline 72,36%) | 05.02.2026 | Anthropic (za pośrednictwem agregatora [benchlm.ai](https://benchlm.ai/benchmarks/osworld)) |
| Claude Sonnet 4.6 | OSWorld-Verified | 72,5% | 02.2026 | Anthropic (jw.) |
| Claude Opus 4.7 | OSWorld-Verified | 78,0% (vs. GPT-5.4: 75,0%) | 04.2026 | Anthropic (jw.) |
| Claude Opus 4.8 | OSWorld-Verified | 82,3% | 2026 | Anthropic (jw.) |
| OpenAI Operator | OSWorld | 38,1% | 01.02.2025 (start) | [Wikipedia — OpenAI Operator](https://en.wikipedia.org/wiki/OpenAI_Operator) |
| OpenAI Operator | WebArena | 58,1% | 2025 | jw. |
| OpenAI CUA (model bazowy dla Operatora) | WebVoyager | 87% | 2025 | jw. |
| ChatGPT agent (następca Operatora) | BrowseComp | 68,9% (o 17,4 pp. wyżej niż „deep research") | 07.2025 | [OpenAI — Introducing ChatGPT agent](https://openai.com/index/introducing-chatgpt-agent/) |
| Google Project Mariner | WebVoyager | 83,5% (SOTA w momencie premiery) | 12.2024 | [MediaPost](https://www.mediapost.com/publications/article/401869/google-tests-project-mariner-an-ai-agent-that-can.html) |
| Simular Agent S2 | 50-step evaluation | 34,5% (vs. ówczesny SOTA — Operator/CUA: 32,6%) | 2025 | [simular.ai](https://www.simular.ai/articles/agent-s2) |
| Simular Agent S2 | WindowsAgentArena | +52,8% względem poprzedniego najlepszego wyniku | 2025 | jw. |

**Uwaga metodologiczna:** liczby dla najnowszych modeli Claude (Opus 4.6–4.8, Opus 5) pochodzą z komunikatów Anthropic cytowanych przez agregator branżowy (benchlm.ai), nie z bezpośredniego odczytu każdego release notu — kierunek trendu (gwałtowny wzrost wyników OSWorld z ~15% do >80% w niespełna 2 lata) jest wiarygodny, ale pojedyncze wartości procentowe warto zweryfikować bezpośrednio na anthropic.com/news przed użyciem w materiałach zewnętrznych. Wynik Opus 5 na „OSWorld 2.0" (lipiec 2026) — Anthropic deklaruje przewagę nad konkurencją „przy dowolnym budżecie kosztowym", ale **dokładna wartość procentowa nie została odnaleziona w dostępnym źródle — nie zweryfikowano**.

**Co mierzą te benchmarki, a czego nie mierzą (ważne dla SeniorAI):** OSWorld (369 zadań), WebArena (812 zadań) i WebVoyager oceniają **skuteczność ukończenia dobrze zdefiniowanego zadania** w kontrolowanym środowisku VM. **Żaden z tych benchmarków nie mierzy**: rozpoznawania scamu/fałszywego okna w czasie rzeczywistym, bezpiecznego zachowania przy niejednoznacznej/ryzykownej instrukcji, ani wydajności w kontakcie z niepewnym, wahającym się użytkownikiem-seniorem. Wysoki wynik na OSWorld **nie jest dowodem, że dany agent jest bezpieczny dla babci** — optymalizuje pod autonomię i skuteczność, nie pod czytelność, odwracalność i odmowę działania w sytuacji ryzyka.

### Poszczególni gracze

- **Anthropic Computer Use** (narzędzie API, nie produkt konsumencki) — Claude otrzymuje zrzuty ekranu i wykonuje ruchy myszy/klawiatury. **Zabezpieczenia opisane oficjalnie:** automatyczne klasyfikatory wykrywające prompt injection (mogą wymusić potwierdzenie użytkownika), rekomendacja uruchamiania w dedykowanej maszynie wirtualnej/kontenerze z minimalnymi uprawnieniami, rekomendacja ograniczenia dostępu do internetu do allowlisty domen, oraz **zalecenie** (nie wymuszenie na poziomie platformy) pytania człowieka o potwierdzenie przy „konsekwentnych" akcjach (transakcje finansowe, akceptacja regulaminów, dane logowania). Referencyjna implementacja działa w kontenerze Docker z wirtualnym wyświetlaczem (Xvfb) — **to NIE jest mechanizm działający bezpośrednio na żywym pulpicie użytkownika**, tylko na izolowanym środowisku, które deweloper musi sam zbudować. *Źródło: [anthropic.com, 22.10.2024](https://www.anthropic.com/news/3-5-models-and-computer-use); [platform.claude.com](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool).*

- **OpenAI Operator → ChatGPT agent** — Operator (dostępny od 01.02.2025 dla ChatGPT Pro w USA) wykonywał zadania przeglądarkowe (formularze, zamówienia, rezerwacje) w izolowanej przeglądarce chmurowej. **Wycofany 31.08.2025**, w pełni zintegrowany z ChatGPT jako „agent mode" (od lipca 2025). *Źródło: [Wikipedia — OpenAI Operator](https://en.wikipedia.org/wiki/OpenAI_Operator); [OpenAI — Introducing Operator](https://openai.com/index/introducing-operator/).*

- **Google Project Mariner → Gemini 2.5 Computer Use model** — prototyp na bazie Gemini 2.0, rozszerzenie Chrome. **Wygaszony w 2026 r.**, funkcje przeniesione do Gemini API/Vertex AI jako model „Gemini 2.5 Computer Use", z deklarowaną (przez Google) przewagą nad konkurencją na benchmarkach web/mobile przy niższym opóźnieniu — **konkretna wartość procentowa nie została odnaleziona, nie zweryfikowano**. *Źródło: [blog.google](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/); [ai2.work](https://ai2.work/blog/google-kills-project-mariner-as-the-industry-pivots-to-api-first-agents).*

- **Rabbit R1 / DLAM** — dedykowane urządzenie (199 USD), pierwotnie z „Large Action Model" (LAM), które nie spełniło obietnic premiery. W 2026 r. nowy agent „DLAM" opisywany przez producenta jako „pierwszy plug-and-play kontroler komputera dla użytkowników na każdym poziomie technicznym" — **retorycznie bardzo blisko wizji SeniorAI**, choć zrealizowany jako osobne urządzenie sprzętowe, nie nakładka na Windows. Integracja z „OpenClaw" (2026). Status: „żywy, ale wciąż niszowy, wciąż nie dowożący pełnej wizji LAM z premiery" wg niezależnych recenzji. *Źródło: [rabbit.tech/blog](https://www.rabbit.tech/blog/first-major-update-of-2026-dlam-openclaw-and-a-surprise); [layer3labs.io](https://www.layer3labs.io/gear/reviews/rabbit-r1).*

- **Adept ACT-1** — pierwszy głośny publiczny demo LLM sterującego przeglądarką. Firma Adept została w czerwcu 2024 r. „acqui-hired" przez Amazon (CEO David Luan + zespół badawczy dołączyli do Amazon + licencja technologii); Amazon rozwinął to jako „Nova Act" (marzec 2025). Oryginalny Adept nie zamknął się formalnie — kontynuował pod nowym CEO (Zach Brock) w węższym zakresie. Efektywnie: **status jako niezależny produkt konsumencki — zakończony/wchłonięty**. *Źródło: [GeekWire](https://www.geekwire.com/2026/head-of-amazons-agi-lab-is-leaving-in-latest-exit-from-high-profile-adept-deal/); [eesel.ai](https://www.eesel.ai/blog/adept-ai).*

- **Simular (Agent S2)** — otwarty, akademicko zorientowany framework, instalacja lokalna w ~5 minut lub w chmurze. Innowacje: „Proactive Hierarchical Planning" i „Mixture-of-Grounding". Kod open source. *Źródło: [simular.ai](https://www.simular.ai/articles/agent-s2); [GitHub](https://github.com/simular-ai/Agent-S).*

- **Highlight AI** — desktopowy asystent (Mac/Windows) „widzący" bieżący ekran na żądanie, transkrybujący audio rozmów, integrujący się z GitHub/Notion/Slack/Google Calendar. **To nie jest agent wykonujący akcje za użytkownika** — bliżej Copilot Vision (kontekst + odpowiedzi) niż „computer use". Obecnie darmowy, spin-off z Medal, 10 mln USD finansowania (2024). *Źródło: [TechCrunch, 11.07.2024](https://techcrunch.com/2024/07/11/medal-raises-13m-as-it-builds-out-a-new-ai-platform-for-desktop).*

- **Open Interpreter** — open source, lokalne wykonywanie kodu (Python/JS/Shell) generowanego przez LLM, z promptem o zgodę przed uruchomieniem. **Istotna różnica względem zalecanej przez Anthropic praktyki:** projekt sam opisuje się jako działający lokalnie „bez ograniczeń sandboxa" — czyli dokładne przeciwieństwo rekomendowanego przez Anthropic modelu izolacji. To pokazuje realne ryzyko bezpieczeństwa w kategorii „lokalny agent AI o pełnym dostępie do systemu", którego SeniorAI musi unikać. *Źródło: [GitHub — Open Interpreter](https://github.com/openinterpreter/openinterpreter); [openinterpreter.com](https://www.openinterpreter.com/).*

---

## 4. Zdalna pomoc / przejęcie kontroli — i problem nadużyć w oszustwach na seniorach

**To najważniejsza sekcja pod kątem uzasadnienia produktowego SeniorAI.** Dokumentacja poniżej pokazuje, że narzędzia zdalnego dostępu są jednocześnie standardem branżowym pomocy i głównym wektorem ataku na seniorów.

### Narzędzia

- **TeamViewer** — oficjalne stanowisko firmy: „TeamViewer nie świadczy usług wsparcia zdalnego. Jeśli ktoś zadzwonił lub wyskoczyło okienko każące zadzwonić pod numer i zainstalować TeamViewer — to niemal na pewno oszustwo." *Źródło: [teamviewer.com — TeamViewer and scamming](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/security/teamviewer-and-scamming/).*
- **AnyDesk** — regularnie wykorzystywany do podszywania się pod wsparcie techniczne dużych marek (Amazon, Apple, Microsoft, PayPal, Geek Squad i inne). *Źródło: [Guard.io](https://guard.io/blog/anydesk-scams-the-good-the-bad-and-the-risky); [Moonlock](https://moonlock.com/anydesk-scams).*
- **Windows Quick Assist** — od kwietnia 2024 r. aktywnie nadużywany przez grupę Storm-1811 (ransomware Black Basta) w atakach vishingowych: atakujący podszywa się pod dział IT, przekonuje ofiarę do udzielenia dostępu, następnie żąda pełnej kontroli i wdraża złośliwe oprogramowanie. Microsoft zgłasza blokowanie **tysięcy podejrzanych połączeń dziennie** i rekomenduje rozważenie odinstalowania narzędzia w organizacjach, które go nie potrzebują. *Źródło: [Microsoft Security Blog, 15.05.2024](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/).*
- **Chrome Remote Desktop** — identyczny wzorzec ryzyka: darmowy, generuje jednorazowy kod dostępu w przepływie „Uzyskaj wsparcie" — mechanika nieodróżnialna od tej wykorzystywanej w oszustwach. *Źródło: [support.google.com](https://support.google.com/chrome/answer/1649523).*
- **RustDesk** — otwarcie i wprost przyznaje się do problemu na własnym blogu: „RustDesk to legalne oprogramowanie open source, ale legalne oprogramowanie da się nadużyć — szyfrowanie nie naprawia zgody uzyskanej podstępem." Firma wprowadziła ostrzeżenia w wielu punktach (strona, flow Android, kanały dystrybucji), a **Google usunęło aplikację ze sklepu Play** z powodu nadużyć; logowanie do publicznego serwera wymaga teraz uwierzytelnienia (Google/GitHub) z powodu skali oszustw i botnetów. Firma antywirusowa Dr.Web raportuje, że RustDesk jest **najpopularniejszym narzędziem wśród oszustów** podszywających się pod wsparcie bankowe. *Źródło: [rustdesk.com/blog — RustDesk and Remote Access Scams](https://rustdesk.com/blog/rustdesk-and-remote-access-scams/); [Dr.Web News](https://news.drweb.com/show/?i=14755).*

### Dane o skali problemu (oszustwa na seniorach)

- **FTC** (raport do Kongresu USA, grudzień 2025): starsi Amerykanie zgłosili **159 mln USD strat** w oszustwach typu „tech support" w 2024 r. Ogólne straty finansowe osób 60+ ze wszystkich typów oszustw wzrosły **czterokrotnie od 2020 r.** — z ok. 600 mln USD do **2,4 mld USD w 2024 r.** FTC szacuje, że rzeczywiste (niezgłoszone) straty mogą sięgać nawet **82 mld USD rocznie**. *Źródło: [FTC — Protecting Older Consumers 2024–2025](https://www.ftc.gov/news-events/news/press-releases/2025/12/ftc-issues-annual-report-congress-agencys-actions-protect-older-adults), 12.2025.*
- **FBI / IC3** (za 2024 r.): łączne straty osób 60+ ze zgłoszonych oszustw internetowych wyniosły **4,885 mld USD** (147 127 zgłoszeń — wzrost zgłoszeń o 46% i strat o 43% rok do roku); **7500 poszkodowanych 60+ straciło ponad 100 000 USD każdy** (średnia strata 83 000 USD). Oszustwa typu „tech support"/„call center": łączne straty we wszystkich grupach wiekowych — **1,46 mld USD**; osoby 60+ stanowiły **40% ofiar, ale aż 58% strat finansowych** w tej kategorii (ok. 770 mln USD). *Źródło: [FBI IC3 Annual Report 2024](https://www.ic3.gov/AnnualReport/Reports/2024_IC3Report.pdf); podsumowanie via [AARP, 2025](https://www.aarp.org/money/scams-fraud/fbi-report-fraud-2024/).*

**Wniosek:** to najsilniejszy, w pełni udokumentowany argument produktowy SeniorAI — **ale jednocześnie największe ryzyko wizerunkowe.** Funkcja „częściowe przejęcie kontroli / co-pilot" w SeniorAI musi być zaprojektowana tak, by była **nieodróżnialna dla nikogo z zewnątrz** od legalnego mechanizmu (np. silna autoryzacja wyłącznie ze strony zaufanego, wcześniej zweryfikowanego kontaktu rodzinnego, jasne, spójne UI niemożliwe do podrobienia w fałszywym okienku, brak możliwości inicjacji przez nieznaną, przychodzącą stronę) — inaczej produkt sam odtwarza wzorzec ataku, przed którym ma chronić.

---

## 5. Onboarding / walkthrough overlay — Digital Adoption Platforms

**Wniosek ogólny:** technologia „podświetl element i pokaż krok po kroku" jest **dojrzałym, dobrze sfinansowanym rozwiązaniem UX** — ale wyłącznie w obrębie **jednej, ręcznie zinstrumentowanej aplikacji webowej**, sprzedawanym firmom (B2B enterprise), nie konsumentom.

- **WalkMe** ([walkme.com](https://www.walkme.com/)) — lider kategorii. Technologia „DeepUI" (opatentowana) rozpoznaje elementy interfejsu aplikacji webowej i „kotwiczy" do nich wskazówki/automatyzacje w czasie działania. Komponent **Workstation** to scentralizowany hub łączący powiadomienia i wskazówki z wielu narzędzi — **ale to głównie agregator/launcher, nie natywna nakładka na dowolną aplikację Win32.** Cennik: enterprise, custom, mediana **43 000–79 000 USD/rok**, realny zakres 9000–150 000+ USD/rok w zależności od skali; wdrożenia dla 500–1500 użytkowników sięgają 400 000 USD, duże wdrożenia enterprise przekraczają 800 000 USD; koszty wdrożenia dodatkowo 10 000–100 000+ USD. **Zerowa obecność w segmencie konsumenckim/senior.** *Źródło: [userpilot.com/blog/walkme-pricing](https://userpilot.com/blog/walkme-pricing/); [vendr.com](https://www.vendr.com/marketplace/walkme); [WalkMe — How it works](https://www.walkme.com/technology/).*

- **Whatfix** ([whatfix.com](https://whatfix.com/)) — **jedyny z tej grupy z jawnie potwierdzoną obsługą poza przeglądarką**: „Whatfix for Desktop" wspiera aplikacje desktopowe i środowiska Citrix VDI, obok web i mobile. „Whatfix Mirror" tworzy interaktywne repliki aplikacji do treningu bez dostępu do produkcji. Nadal jednak wymaga ręcznego zbudowania „Flows" (przepływów) per aplikacja/zadanie przez zespół wdrożeniowy klienta biznesowego — **nie ma ogólnej AI rozumiejącej dowolny, nieznany wcześniej ekran.** Cennik enterprise, niepubliczny. *Źródło: [whatfix.com/blog/desktop-and-vdi-app-adoption](https://whatfix.com/blog/desktop-and-vdi-app-adoption/).*

- **Pendo, Userpilot, Appcues, Chameleon, Userlane** — wszystkie działają **wyłącznie w przeglądarce** (skrypt JS osadzony w konkretnej aplikacji webowej klienta), model cenowy oparty o liczbę aktywnych użytkowników miesięcznie (MAU): Userpilot od 299 USD/mies., Appcues od ok. 375 USD/mies. za 2000 MAU, Chameleon od 349 USD/mies. (Startup) do 899+ USD/mies. (Growth), Pendo ma darmowy tier + plany custom (ceny wzrosły 20–34% rok do roku wg jednego źródła), Userlane bez jawnego cennika. **Żadne z tych narzędzi nie działa poza jedną, zainstrumentowaną aplikacją webową** — nie mogłyby np. podświetlić przycisku w osobnej aplikacji bankowej na Windows ani w Ustawieniach systemu. *Źródło: [Pendo blog — top digital adoption platforms](https://www.pendo.io/pendo-blog/top-10-digital-adoption-platforms/); [userpilot.com/blog/pendo-competitors](https://userpilot.com/blog/pendo-competitors/); [userguiding.com — Chameleon pricing](https://userguiding.com/blog/what-is-chameleon-software).*

- **Intro.js / Shepherd.js** — darmowe/tanie biblioteki open source (JavaScript) do budowania przewodników **we własnej stronie internetowej**. Intro.js: AGPL v3 (licencja komercyjna od 9,99 USD/dewelopera), ~12,5 KB. Shepherd.js: licencja MIT, ponad 170 wydań, ostatnie w marcu 2026, wsparcie dla React/Vue/Angular/Ember. **Walidują dojrzałość wzorca UX „podświetl i wyjaśnij", ale wyłącznie w obrębie DOM przeglądarki — kompletnie nieprzydatne poza web.** *Źródło: [introjs.com](https://introjs.com/); [GitHub — Shepherd](https://github.com/shipshapecode/shepherd).*

**Wniosek dla sekcji 5:** technicznie dojrzały wzorzec „highlight and guide" jest **rozwiązanym problemem w obrębie jednej strony webowej** i **niedotkniętym problemem na poziomie systemu operacyjnego dla konsumentów**. SeniorAI musi rozwiązać dużo trudniejszy problem generycznego rozpoznawania UI w dowolnej aplikacji Windows (nie tylko w jednej, ręcznie zaanotowanej aplikacji webowej klienta korporacyjnego) — to jest realna bariera techniczna, nie tylko rynkowa.

---

## 6. Narzędzia anty-scam / ochrona seniorów

- **Aura** ([aura.com](https://www.aura.com/identity-theft-protection)) — ochrona tożsamości + antywirus + VPN + blokowanie połączeń spamowych/oszukańczych, ubezpieczenie do 1–5 mln USD. Ceny: od 12 USD/mies. (pojedynczy plan), plan rodzinny 30 USD/mies. lub 300 USD/rok (do 5 dorosłych). Firma oferuje rabaty dla seniorów/rodzin wojskowych (szczegóły rabatu nie zweryfikowane). Wsparcie 24/7 US-based. *Źródło: [aura.com](https://www.aura.com/identity-theft-protection); [security.org — Aura review](https://www.security.org/identity-theft/aura/review/).*
- **Carefull** — wspominany w branży jako narzędzie do monitoringu finansowego rodziców, jednak **nie odnaleziono dedykowanej strony/profilu firmy z konkretnym cennikiem w przeprowadzonym researchu** — wyniki wyszukiwania zwróciły głównie generyczne poradniki o monitorowaniu finansów seniorów, nie materiały źródłowe samej firmy Carefull. **Funkcje i cena: nie zweryfikowano w tym researchu** — wymaga dodatkowego sprawdzenia bezpośrednio na stronie producenta.
- **EverSafe** ([eversafe.com](https://www.eversafe.com/)) — monitoring kont bankowych/inwestycyjnych/kart kredytowych/dark web 24/7, silnik AI „CATCH" wykrywający anomalie w transakcjach i e-mailach, dostęp „tylko do odczytu" dla zaufanych doradców/rodziny. Trzy plany: Essentials 7,49 USD/mies., Plus 14,99 USD/mies., Gold 24,99 USD/mies. *Źródło: [eversafe.com](https://www.eversafe.com/); [Fidelity — EverSafe Fact Sheet, 2026](https://sponsor.fidelity.com/bin-public/06_PSW_Website/documents/EverSafe%20Fact%20Sheet.pdf).*
- **Trend Micro Check** (obecnie „Trend Micro ID Protection"/„ScamCheck") — darmowe rozszerzenie przeglądarki, ocena bezpieczeństwa linków/stron w czasie rzeczywistym, deklarowana skuteczność wykrywania phishingu **99%** (dana producenta), blokowanie reklam/trackerów. *Źródło: [trendmicro.com](https://www.trendmicro.com/en_us/forHome/products/trend-micro-scam-check.html).*
- **Malwarebytes Scam Guard** — AI-owy „towarzysz bezpieczeństwa cyfrowego": ocenia podejrzane SMS-y/DM-y/e-maile/obrazy/linki w interfejsie czatu (jak ChatGPT/Gemini). Uruchomiony **3 czerwca 2025** na mobile (iOS/Android, w Malwarebytes Mobile Security, darmowy i płatny tier), rozszerzony na **desktop (Windows/Mac) w lutym 2026** — czyli w niecały rok. Producent deklaruje (PR własny, nie zweryfikowany niezależnie): „zapobiegł oszustwom wysokiego ryzyka w 15% interakcji, chroniąc użytkowników przed stratami 1000+ USD". *Źródło: [malwarebytes.com — komunikat prasowy, 03.06.2025](https://www.malwarebytes.com/press/2025/06/03/malwarebytes-launches-scam-guard-an-ai-powered-mobile-first-digital-safety-companion-to-combat-todays-most-pernicious-threats); [PR Newswire — wyniki, 2026](https://www.prnewswire.com/news-releases/malwarebytes-scam-guard-prevented-high-risk-fraud-in-15-of-interactions-protecting-users-from-1000-in-losses-or-significant-personal-risk-302687983.html).*
- **Microsoft Defender SmartScreen** — wbudowane w Windows/Edge, ocena reputacyjna URL-i/plików/aplikacji/certyfikatów, „Enhanced Phishing Protection" ostrzegająca przy wpisaniu hasła firmowego/szkolnego na podejrzanej stronie lub zapisaniu go jawnym tekstem (Notatnik/Word). Darmowe, domyślnie aktywne w Edge. *Źródło: [learn.microsoft.com](https://learn.microsoft.com/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/).*

**Wniosek dla sekcji 6:** ta kategoria porusza się **szybko** w stronę AI (Malwarebytes: mobile→desktop w 8 miesięcy) i ma już zaufanie/budżet rodzin kupujących ochronę dla starszych krewnych. **Żadne z tych narzędzi nie interweniuje w momencie żywej sesji zdalnego dostępu** („ktoś właśnie przejął twoją myszkę i otwiera stronę banku — czy na pewno tego chciałeś?") — to konkretna, wciąż wolna nisza, ale okno czasowe kurczy się w miarę jak te firmy dodają kolejne funkcje AI.

---

## 7. Dane rynkowe i demografia

### Wielkość rynku (uwaga: **duży rozrzut szacunków między firmami badawczymi — metodologie i zakresy różnią się istotnie, brak jednej „autorytatywnej" liczby**)

**Assistive Technology Market (globalny):**
- 26,43 mld USD (2025) → 43,88 mld USD (2030), CAGR 10,7% — *[custommarketinsights.com / 360iresearch.com, 2025](https://www.360iresearch.com/library/intelligence/assistive-technology)*
- CAGR 4,5% (2025–2029) — *[Technavio, 2025](https://www.technavio.com/report/assistive-technology-market-report-analysis)*
- CAGR 4,8% — *[market.us, 2026](https://market.us/report/assistive-technology-market/)*
- CAGR 8,7% — *[Global Growth Insights](https://www.globalgrowthinsights.com/market-reports/assistive-technology-market-106065)*
- 32,25 mld USD do 2030, CAGR 5% (2023–2030) — *[Coherent Market Insights via BioSpace](https://www.biospace.com/press-releases/assistive-technology-market-size-to-worth-usd-32-25-billion-by-2030-coherent-market-insights)*

**Aging-in-Place / Gerontechnology / AgeTech:**
- Aging in Place Technology: 9,1 mld USD (2024) → 15,2 mld USD (2033), CAGR 15,10% — *[HTF Market Insights](https://www.htfmarketinsights.com/report/4395068-aging-in-place-technology-market)*
- Aging-in-Place and Home Accessibility Solutions: 26,87 mld USD (2025) → 44,58 mld USD (2032), CAGR 7,5% — *[Stratistics MRC](https://www.strategymrc.com/report/aging-in-place-and-home-accessibility-solutions-market)*
- Gerontechnology (szersza kategoria): 69,56 mld USD (2024) → 245,60 mld USD (2033), CAGR 13,0% — *[DataM Intelligence](https://www.datamintelligence.com/research-report/gerontechnology-market)*
- AgeTech & Smart Aging Solutions: 22,4 mld USD (2025) → 77,1 mld USD (2034), CAGR 14,3%; podkategoria AI/ML rośnie najszybciej: ok. 17,2% CAGR do 2034 — *[marketintelo.com](https://marketintelo.com/report/agetech-smart-aging-solutions-market)*

**AgeTech Collaborative (AARP):** blisko **700 firm członkowskich** na CES 2026; osoby 50+ w USA wydały **77 mld USD** na technologię w 2022 r., prognoza ok. **120 mld USD do 2030 r.**; posiadanie technologii smart home wśród seniorów wzrosło z 10% (2019) do 27% (2025), posiadanie urządzeń bezpieczeństwa domowego z 19% (2024) do 34% (2025). *Źródło: [press.aarp.org, 08.01.2025](https://press.aarp.org/2025-1-8-New-Report-Finds-Growing-Interest-Tech-Aging-Well-Home); [agetechcollaborative.org](https://agetechcollaborative.org/).*

### Demografia

**Unia Europejska (Eurostat):** na 1 stycznia 2024 r. populacja UE wynosiła 449,3 mln osób, z czego **21,6% miało 65 lat lub więcej** (14,6% miało 0–14 lat, 63,8% było w wieku produkcyjnym 15–64 lata). Współczynnik obciążenia demograficznego osobami starszymi wzrósł z 33,9% (2024) do 34,5% (2025). Rozpiętość między krajami: od 22,0% (Luksemburg) do 39,0% (Włochy). *Źródło: [Eurostat — Population structure and ageing](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Population_structure_and_ageing).*

**Polska (GUS):** w 2024 r. liczba osób w wieku 65+ wzrosła o 175 tys. do ponad **7,7 mln, czyli 20,6% ludności kraju**. Indeks starości: 141 (na 100 dzieci 0–14 lat przypada 141 osób 65+). Mediana wieku: ponad 43 lata (wzrost o 7 lat od 2000 r.). Populacja Polski na koniec 2024 r.: 37 489 tys. (spadek o >147 tys. rok do roku). Prognoza: populacja 60+ ma wzrosnąć do 11,9 mln, czyli niemal 40% ludności, do końca horyzontu prognozy. *Źródło: [stat.gov.pl — Sytuacja osób starszych w Polsce w 2024 r.](https://stat.gov.pl/obszary-tematyczne/osoby-starsze/osoby-starsze/sytuacja-osob-starszych-w-polsce-w-2024-r-,2,7.html); [PAP, 2025](https://www.pap.pl/aktualnosci/gus-ponad-jedna-czwarta-populacji-polski-seniorzy).*

**USA (US Census Bureau):** populacja 65+ wzrosła o 3,1% do **61,2 mln** w 2024 r. (dane opublikowane 26.06.2025, „Vintage 2024 Population Estimates"). Udział populacji 65+ wzrósł z 12,4% (2004) do **18,0% (2024)**. W latach 2020–2024 populacja 65+ urosła o 13,0% wobec zaledwie 1,4% wzrostu populacji w wieku produkcyjnym. Osoby starsze przewyższają liczebnie dzieci już w 11 stanach (wzrost z 3 stanów w 2020 r.) i w niemal połowie hrabstw USA. *Źródło: [census.gov — komunikat prasowy, 26.06.2025](https://www.census.gov/newsroom/press-releases/2025/older-adults-outnumber-children.html).*

### Penetracja technologii wśród seniorów (Pew Research Center, USA)

Dane z badania przeprowadzonego 05.02.–18.06.2025, opublikowane 08.01.2026 (fact sheet) oraz 08.01.2026 (short-read):
- **90% dorosłych 65+ korzysta z internetu** (fact sheet, dane 2025). *Źródło: [Pew Research — Internet/Broadband Fact Sheet](https://www.pewresearch.org/internet/fact-sheet/internet-broadband/).*
- Tylko **14%** osób 65+ korzysta z internetu „niemal cały czas" — najniższy odsetek spośród wszystkich grup wiekowych (dla porównania: 63% osób 18–29 lat). *Źródło: [Pew Research, 08.01.2026](https://www.pewresearch.org/short-reads/2026/01/08/internet-use-smartphone-ownership-digital-divides-in-u-s/).*
- **78%** osób 65+ posiada smartfon — najniższy odsetek spośród grup wiekowych (97% wśród osób <50 lat, 90% wśród 50–64 lat). *Źródło: jw.*
- **70%** osób 65+ ma dostęp do szerokopasmowego internetu w domu (poniżej średniej krajowej 78%). *Źródło: jw.*
- **Nie zweryfikowano** w tym researchu: dokładny odsetek posiadania komputera stacjonarnego/laptopa wśród 65+ (dostępne źródła Pew opisują internet/smartfon/szerokopasmowy dostęp, nie samo posiadanie komputera PC).

**Wniosek dla sekcji 7:** rynek jest jednoznacznie duży i strukturalnie rosnący w każdym z trzech badanych regionów, a penetracja internetu wśród seniorów jest już wysoka (90% w USA) — więc **problem nie jest brakiem obecności online**, lecz jakością i bezpieczeństwem tej obecności (niska intensywność korzystania — 14% „stale online" vs 63% u młodych — sugeruje niepewność/dyskomfort, nie brak dostępu). To wspiera hipotezę produktową SeniorAI, ale nie mówi nic o gotowości seniorów/rodzin do **płacenia za software** — dowody z sekcji 1 (Eldy, SimplicITy) sugerują, że to osobne, niepewne pytanie.

---

## Luka rynkowa — analiza krytyczna

### Gdzie luka jest realna

Żadne znalezione rozwiązanie nie łączy jednocześnie: **(1)** żywej nakładki działającej **cross-aplikacyjnie** (nie tylko w jednej stronie WWW jak WalkMe/Whatfix/Intro.js), **(2)** AI ogólnego przeznaczenia rozumiejącego **dowolny, wcześniej nieznany ekran** (a nie ręcznie zaanotowany przez zespół wdrożeniowy), **(3)** aktywnego, działającego w czasie rzeczywistym blokowania ryzykownych kroków (a nie tylko retrospektywnego monitoringu jak EverSafe czy statycznej blokady jak Inteset), **(4)** asystenta głosowego, **(5)** lupy, **(6)** opcjonalnego, bezpiecznego częściowego przejęcia kontroli — działającego na **zwykłym, już posiadanym komputerze z Windows**, bez wymogu zakupu nowego dedykowanego sprzętu (jak Telikin/GrandPad/WOW), bez wymogu drogiego sprzętu Copilot+ PC z NPU (jak Recall/Click to Do) i bez płatnej subskrypcji zewnętrznej platformy AI jako warunku wstępnego (jak Copilot Vision wymaga M365). To wąska, ale prawdziwa przestrzeń.

### Gdzie konkurencja jest silna i może nas „zmiażdżyć"

1. **Microsoft ma przewagę dystrybucyjną nie do podrobienia.** Copilot Vision, Click to Do, Recall i eksperymentalne Copilot Actions/Agent Workspace pokazują, że firma **już buduje** dokładnie te elementy, i to z dostępem do jądra systemu, podpisanych komponentów systemowych oraz domyślnej instalacji na każdym nowym Windows PC — czegoś, czego żaden zewnętrzny dostawca nie odtworzy. Zapowiedziany na Ignite (listopad 2025) kierunek „agentic OS" to realny, publicznie ogłoszony plan 1–3-letni. Jeśli Microsoft doda do tego profil „senior/dostępność" (co byłoby naturalnym rozszerzeniem istniejącego działu Windows Accessibility, bardzo aktywnego w 2025 r. wg własnego podsumowania rocznego), przewaga SeniorAI może zniknąć w ciągu jednej-dwóch aktualizacji Windows.
2. **Wyścig zbrojeń w „computer use AI" toczy się poza SeniorAI i w oszałamiającym tempie.** Wynik OSWorld dla modeli Anthropic wzrósł z ~15% do >80% w niecałe dwa lata (2024→2026); OpenAI i Google skasowały własne produkty konsumenckie (Operator, Project Mariner) w mniej niż 18 miesięcy od premiery, żeby przenieść możliwości do warstwy API/modelowej. To sugeruje, że rdzeń technologiczny SeniorAI **musi** być zbudowany na cudzym API (Anthropic/OpenAI/Google), z pełną zależnością od ich cennika, polityki bezpieczeństwa i tempa zmian — nie jest to fundament, który SeniorAI kontroluje.
3. **DAP-y (WalkMe, Whatfix) mają dekadę doświadczenia w technicznie trudnym problemie rozpoznawania elementów UI** (DeepUI) i pokazują, ile to realnie kosztuje wdrożyć poprawnie (dziesiątki–setki tysięcy USD rocznie, nawet dla jednej dobrze zdefiniowanej aplikacji firmowej). To sugeruje, że „ogólne, niezawodne podświetlanie dowolnego UI" jest dużo trudniejsze technicznie, niż mogłoby się wydawać z zewnątrz.
4. **Firmy anty-scam (Aura, EverSafe, Malwarebytes) mają już zaufanie i bazę klientów w dokładnie tej grupie docelowej** (dorosłe dzieci kupujące ochronę dla rodziców) i poruszają się szybko w stronę AI (Malwarebytes: mobile→desktop w 8 miesięcy). Okno na zbudowanie unikalnej przewagi w „wykrywaniu scamu przez AI" się kurczy.
5. **Model usługi ludzkiej (Candoo Tech i podobne) jest sprawdzonym substytutem** — realny, płacący klienci (228–240 USD/rok) wybierają „człowieka na żywo" zamiast oprogramowania. To wskazuje, że dla części rynku docelowego zaufanie do AI może być niższe niż zaufanie do drugiego człowieka, niezależnie od jakości technologii.
6. **Dwie dekady prób „uproszczonej powłoki" (Eldy, SimplicITy, SeeYouLink, Telikin, WOW! Computer) osiągnęły skromną skalę** — lider kategorii (Eldy) ma ok. 400 tys. użytkowników wobec dziesiątek milionów seniorów online tylko w samych USA. To dowód na trudny go-to-market/monetyzację w tej kategorii produktowej, niezależnie od jakości wykonania.

### Gdzie SeniorAI może polec

1. **Paradoks rdzenia produktu:** funkcja „co-pilot/częściowe przejęcie kontroli" jest **architektonicznie identyczna** z mechanizmem udokumentowanym w sekcji 4 jako główny wektor oszustw na seniorach (FTC: 159 mln USD strat w 2024 r. tylko z „tech support scams"; FBI IC3: seniorzy to 58% strat w tej kategorii). Jeśli SeniorAI kiedykolwiek wprowadzi funkcję zdalnej pomocy rodziny/wsparcia, musi rozwiązać problem UX/bezpieczeństwa/zaufania, z którym **cała branża (włącznie z Microsoftem i RustDesk) jawnie się zmaga i przegrywa** — a jeden incydent bezpieczeństwa lub nawet zwykłe pomylenie „prawdziwej pomocy SeniorAI" z oszustwem przez samego seniora może być katastrofalny wizerunkowo dla marki zbudowanej wokół obietnicy ochrony.
2. **Poprzeczka niezawodności dla „blokowania ryzykownych kroków" jest ekstremalnie wysoka.** Liderzy benchmarku OSWorld dopiero w 2026 r. przekroczyli ~80% skuteczności na 369 wyselekcjonowanych, dobrze zdefiniowanych zadaniach w kontrolowanym środowisku VM. Prawdziwy pulpit zdezorientowanego, wahającego się seniora jest dużo bardziej chaotyczny niż zadania OSWorld. Fałszywy negatyw (przepuszczenie realnego oszustwa) niszczy zaufanie natychmiast i nieodwracalnie; fałszywy pozytyw (zablokowanie legalnej czynności, np. logowania do banku) frustruje dokładnie tę grupę użytkowników, która najmniej toleruje „oprogramowanie, które przeszkadza".
3. **Ryzyko zależności sprzętowej/architektonicznej.** Najbardziej zaawansowane, prywatne (on-device) funkcje AI Microsoftu (Recall, Click to Do) są zamknięte za wymogiem drogiego sprzętu Copilot+ PC (NPU) — jeśli SeniorAI chce porównywalnej prywatności bez wysyłania ciągłego strumienia zrzutów ekranu (potencjalnie z danymi bankowymi/medycznymi) do zewnętrznego API w chmurze, napotka ten sam sufit sprzętowy na starszych, tańszych komputerach, które realnie mają seniorzy. Jeśli zamiast tego wybierze przetwarzanie w chmurze, dziedziczy koszt per-token przy ciągłym „patrzeniu" na ekran (potencjalnie drogie w skali), opóźnienie, oraz istotne ryzyko związane z prywatnością danych (stały strumień zrzutów ekranu banku/dokumentacji medycznej do API strony trzeciej to poważne zobowiązanie w zakresie ochrony danych — potencjalnie trudniejsze do uzasadnienia niż już kontrowersyjny, ale w pełni lokalny model Recall).
4. **Niepewny model biznesowy.** Każdy sąsiadujący konkurent z realną trakcją konsumencką jest albo (a) darmowy/wbudowany w system operacyjny i z każdą wersją Windows coraz lepszy (Magnifier, Narrator, Voice Access, SmartScreen), albo (b) sprzedawany jako jednorazowy zakup sprzętu + opcjonalna subskrypcja (Telikin, GrandPad, WOW — 200–1300 USD raz + ewentualnie miesięczna opłata), albo (c) doczepiony do istniejącego budżetu na ochronę tożsamości, który rodziny już akceptują (Aura, EverSafe — 7–30 USD/mies.). Samodzielna subskrypcja „zainstaluj oprogramowanie na już posiadanym Windows" skierowana do seniorów **nie została udowodniona w żadnej istotnej skali** w ciągu ostatnich ~20 lat prób (Eldy jest darmowy; SimplicITy zniknęło; SeeYouLink pozostaje niszowe przy 4,95 USD/mies.) — to nieprzetestowany, a nie zwalidowany segment monetyzacji.

---

## Bibliografia (pełna lista źródeł)

### Kategoria 1 — Dedykowane nakładki dla seniorów
- Eldy — About Us: http://www.eldy.eu/en/about-us/
- Eldy — strona główna: http://www.eldy.eu/en/
- ELDYcare (Estonia, 2025) — Estonia Digital, wrzesień 2025: https://estoniadigital.wordpress.com/2025/09/28/healthtech-startup-eldycare-introduces-software-to-harmonise-care-for-the-elderly/
- Telikin Elite II — telikin.com: https://www.telikin.com/telikin_elite_2.php
- Telikin — Wikipedia: https://en.wikipedia.org/wiki/Telikin
- WOW! Computer — mywowcomputer.com: https://www.mywowcomputer.com/
- WOW! Computer — Elder Guru review: https://www.elderguru.com/wow-computer-for-seniors/
- GrandPad — Consumer Cellular blog: https://www.consumercellular.com/blog/meet-grandpad-unique-solution-family-connections/
- GrandPad — Reviewed.com: https://www.reviewed.com/accessibility/content/grandpad-review-price-tablet-for-seniors-accessible
- GrandPad — CES 2025, Podfeet: https://www.podfeet.com/blog/2025/04/ces-2025-grandpad/
- Claris Companion — clarishealthcare.com: https://clarishealthcare.com/claris-companion/claris-for-family/
- SeeYouLink — download.seeyoulink.com: https://www.seeyoulink.com/download
- SeeYouLink — Modern Health Talk: https://mhealthtalk.com/helping-seniors-master-computers/
- Inteset Secure Lockdown: https://www.inteset.com/secure-computers-for-senior-citizens
- Simplicity Computers CIC (UK): https://www.simplicitycomputers.co.uk/
- SimplicITy (historyczny projekt UK) — IT Pro: https://www.itpro.com/617494/older-people-get-their-own-simple-computer
- Candoo Tech — service offerings: https://www.candootech.com/service-offerings
- Uniper Care — PR Newswire, 2020: https://www.prnewswire.com/news-releases/uniper-launches-cross-platform-telehealth-and-social-engagement-service-for-older-adult-population-in-response-to-covid-19-outbreak-to-address-isolation-hardships-301029485.html
- Uniper Care — finansowanie, PRWeb: https://www.prweb.com/releases/uniper-care-secures-4-million-in-funding-to-combat-loneliness-and-isolation-among-older-adults-874568053.html
- Cyber-Seniors: https://cyberseniors.org/
- Silver Surfers — Age UK Waltham Forest: https://www.ageuk.org.uk/walthamforest/activities-and-events/silver-surfers-computer-classes/
- Silver City Surfers: https://silvercitysurfers.co.uk/

### Kategoria 2 — Wbudowane funkcje dostępności Windows
- Magnifier — support.microsoft.com: https://support.microsoft.com/en-us/windows/use-magnifier-to-make-things-on-the-screen-easier-to-see-414948ba-8b1c-d3bd-8615-0e5e32204198
- Narrator — Complete guide: https://support.microsoft.com/en-us/accessibility/windows/narrator/complete-guide-to-narrator
- Narrator 2025 recap — Windows Experience Blog, 03.12.2025: https://blogs.windows.com/windowsexperience/2025/12/03/2025-a-year-in-recap-windows-accessibility/
- Voice Access — support.microsoft.com: https://support.microsoft.com/en-us/accessibility/windows/voice-access/get-started-with-voice-access
- Live Captions — support.microsoft.com: https://support.microsoft.com/en-us/accessibility/windows/use-live-captions-to-better-understand-audio
- Ease of Access — support.microsoft.com: https://support.microsoft.com/en-ph/help/17180/windows-10-make-your-pc-easier-to-use
- Copilot Vision — support.microsoft.com: https://support.microsoft.com/en-us/microsoft-copilot/using-copilot-vision-with-microsoft-copilot
- Windows Recall — learn.microsoft.com: https://learn.microsoft.com/en-us/windows/apps/develop/windows-integration/recall/
- Windows Recall — bezpieczeństwo, Windows Experience Blog, 27.09.2024: https://blogs.windows.com/windowsexperience/2024/09/27/update-on-recall-security-and-privacy-architecture/
- Click to Do — learn.microsoft.com: https://learn.microsoft.com/en-us/windows/client-management/manage-click-to-do
- Click to Do — Windows Central: https://www.windowscentral.com/software-apps/windows-11/what-is-click-to-do-and-how-do-you-get-started-ai-actions-for-windows-11-explained
- Quick Assist — support.microsoft.com: https://support.microsoft.com/en-us/windows/apps/solve-pc-problems-remotely-using-quick-assist
- Steps Recorder deprecation — support.microsoft.com: https://support.microsoft.com/en-us/windows/apps/steps-recorder-deprecation
- Focus Assist — support.microsoft.com: https://support.microsoft.com/en-us/windows/make-it-easier-to-focus-on-tasks-0d259fd9-e9d0-702c-c027-007f0e78eaf2
- Experimental agentic features / Copilot Actions / Agent Workspace — support.microsoft.com: https://support.microsoft.com/en-us/windows/ai/ai-features/experimental-agentic-features

### Kategoria 3 — AI „computer use" / agenci
- Anthropic — Introducing computer use, 22.10.2024: https://www.anthropic.com/news/3-5-models-and-computer-use
- Anthropic — Computer use tool docs: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool
- OSWorld benchmark — leaderboard/agregator: https://benchlm.ai/benchmarks/osworld
- OSWorld — oficjalna strona projektu: https://os-world.github.io/
- OSWorld — arXiv paper: https://arxiv.org/abs/2404.07972
- WebArena — oficjalna strona: https://webarena.dev/
- WebArena — arXiv paper: https://arxiv.org/abs/2307.13854
- OpenAI Operator — Wikipedia: https://en.wikipedia.org/wiki/OpenAI_Operator
- OpenAI — Introducing Operator: https://openai.com/index/introducing-operator/
- OpenAI — Introducing ChatGPT agent, 07.2025: https://openai.com/index/introducing-chatgpt-agent/
- Google Project Mariner — MediaPost, 12.2024: https://www.mediapost.com/publications/article/401869/google-tests-project-mariner-an-ai-agent-that-can.html
- Google — Gemini 2.5 Computer Use model: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/
- Project Mariner shutdown — ai2.work: https://ai2.work/blog/google-kills-project-mariner-as-the-industry-pivots-to-api-first-agents
- Rabbit R1 / DLAM — rabbit.tech blog: https://www.rabbit.tech/blog/first-major-update-of-2026-dlam-openclaw-and-a-surprise
- Rabbit R1 review 2026 — Layer3labs: https://www.layer3labs.io/gear/reviews/rabbit-r1
- Adept ACT-1 — GeekWire, 2026: https://www.geekwire.com/2026/head-of-amazons-agi-lab-is-leaving-in-latest-exit-from-high-profile-adept-deal/
- Adept AI — eesel.ai: https://www.eesel.ai/blog/adept-ai
- Simular Agent S2: https://www.simular.ai/articles/agent-s2
- Simular Agent S2 — GitHub: https://github.com/simular-ai/Agent-S
- Highlight AI — TechCrunch, 11.07.2024: https://techcrunch.com/2024/07/11/medal-raises-13m-as-it-builds-out-a-new-ai-platform-for-desktop
- Open Interpreter — GitHub: https://github.com/openinterpreter/openinterpreter

### Kategoria 4 — Zdalna pomoc / oszustwa
- TeamViewer and scamming: https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/security/teamviewer-and-scamming/
- AnyDesk scams — Guard.io: https://guard.io/blog/anydesk-scams-the-good-the-bad-and-the-risky
- AnyDesk scams — Moonlock: https://moonlock.com/anydesk-scams
- Chrome Remote Desktop — support.google.com: https://support.google.com/chrome/answer/1649523
- RustDesk and Remote Access Scams — rustdesk.com blog: https://rustdesk.com/blog/rustdesk-and-remote-access-scams/
- Dr.Web — nadużycia remote access: https://news.drweb.com/show/?i=14755
- Microsoft Security Blog — Quick Assist abuse, 15.05.2024: https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/
- FTC — Protecting Older Consumers 2024–2025 (raport do Kongresu), 12.2025: https://www.ftc.gov/news-events/news/press-releases/2025/12/ftc-issues-annual-report-congress-agencys-actions-protect-older-adults
- FBI IC3 Annual Report 2024: https://www.ic3.gov/AnnualReport/Reports/2024_IC3Report.pdf
- FBI report na temat oszustw na seniorach — AARP, 2025: https://www.aarp.org/money/scams-fraud/fbi-report-fraud-2024/

### Kategoria 5 — Digital Adoption Platforms
- WalkMe — How it works: https://www.walkme.com/technology/
- WalkMe pricing — Userpilot: https://userpilot.com/blog/walkme-pricing/
- WalkMe pricing — Vendr: https://www.vendr.com/marketplace/walkme
- Whatfix for Desktop/VDI: https://whatfix.com/blog/desktop-and-vdi-app-adoption/
- Pendo — top digital adoption platforms: https://www.pendo.io/pendo-blog/top-10-digital-adoption-platforms/
- Pendo competitors — Userpilot: https://userpilot.com/blog/pendo-competitors/
- Chameleon pricing/features — UserGuiding: https://userguiding.com/blog/what-is-chameleon-software
- Chameleon vs Userlane — Userpilot: https://userpilot.com/blog/chameleon-vs-userlane/
- Intro.js: https://introjs.com/
- Shepherd.js — GitHub: https://github.com/shipshapecode/shepherd

### Kategoria 6 — Anty-scam
- Aura — Identity Theft Protection: https://www.aura.com/identity-theft-protection
- Aura review — Security.org: https://www.security.org/identity-theft/aura/review/
- EverSafe: https://www.eversafe.com/
- EverSafe Fact Sheet — Fidelity, 2026: https://sponsor.fidelity.com/bin-public/06_PSW_Website/documents/EverSafe%20Fact%20Sheet.pdf
- Trend Micro ScamCheck: https://www.trendmicro.com/en_us/forHome/products/trend-micro-scam-check.html
- Malwarebytes Scam Guard — komunikat prasowy, 03.06.2025: https://www.malwarebytes.com/press/2025/06/03/malwarebytes-launches-scam-guard-an-ai-powered-mobile-first-digital-safety-companion-to-combat-todays-most-pernicious-threats
- Malwarebytes Scam Guard — wyniki, PR Newswire, 2026: https://www.prnewswire.com/news-releases/malwarebytes-scam-guard-prevented-high-risk-fraud-in-15-of-interactions-protecting-users-from-1000-in-losses-or-significant-personal-risk-302687983.html
- Microsoft Defender SmartScreen — learn.microsoft.com: https://learn.microsoft.com/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/

### Kategoria 7 — Dane rynkowe i demograficzne
- Assistive Technology Market — 360iResearch: https://www.360iresearch.com/library/intelligence/assistive-technology
- Assistive Technology Market — Technavio: https://www.technavio.com/report/assistive-technology-market-report-analysis
- Assistive Technology Market — market.us: https://market.us/report/assistive-technology-market/
- Assistive Technology Market — Global Growth Insights: https://www.globalgrowthinsights.com/market-reports/assistive-technology-market-106065
- Assistive Technology Market — Coherent Market Insights via BioSpace: https://www.biospace.com/press-releases/assistive-technology-market-size-to-worth-usd-32-25-billion-by-2030-coherent-market-insights
- Aging in Place Technology Market — HTF Market Insights: https://www.htfmarketinsights.com/report/4395068-aging-in-place-technology-market
- Aging-in-Place and Home Accessibility Solutions Market — Stratistics MRC: https://www.strategymrc.com/report/aging-in-place-and-home-accessibility-solutions-market
- Gerontechnology Market — DataM Intelligence: https://www.datamintelligence.com/research-report/gerontechnology-market
- AgeTech & Smart Aging Solutions Market — Marketintelo: https://marketintelo.com/report/agetech-smart-aging-solutions-market
- AgeTech Collaborative (AARP) — komunikat prasowy, 08.01.2025: https://press.aarp.org/2025-1-8-New-Report-Finds-Growing-Interest-Tech-Aging-Well-Home
- AgeTech Collaborative — strona: https://agetechcollaborative.org/
- Eurostat — Population structure and ageing: https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Population_structure_and_ageing
- GUS — Sytuacja osób starszych w Polsce w 2024 r.: https://stat.gov.pl/obszary-tematyczne/osoby-starsze/osoby-starsze/sytuacja-osob-starszych-w-polsce-w-2024-r-,2,7.html
- GUS via PAP, 2025: https://www.pap.pl/aktualnosci/gus-ponad-jedna-czwarta-populacji-polski-seniorzy
- US Census Bureau — komunikat prasowy, 26.06.2025: https://www.census.gov/newsroom/press-releases/2025/older-adults-outnumber-children.html
- Pew Research — Internet/Broadband Fact Sheet (2025): https://www.pewresearch.org/internet/fact-sheet/internet-broadband/
- Pew Research — Internet use, smartphone ownership, digital divides, 08.01.2026: https://www.pewresearch.org/short-reads/2026/01/08/internet-use-smartphone-ownership-digital-divides-in-u-s/

---

*Koniec dokumentu. Plik: `/home/user/senior-ai/research/01-competitive-landscape.md`*
