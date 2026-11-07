# Val, välfärd och inflytande – utvecklingsgranskning

Datum: 2026-11-07. Status: draft. Metod: Discovery Learning 0.2.0.
Basrevision: 443c0915a5922044e45f82efcfc88a2784302950.

## Syfte och avgränsning

Gör marknadsvalets tänkta inflytande över konkreta livsbehov begripligt utan att likställa köp med lika politisk rösträtt. Ge kollektiv finansierings motiv om tillgång och delade kostnader samma konkretion. Skilj fyra frågor: finansiering, utförande, beslutanderätt och riskdelning. Ingen finansieringsmodell tillskrivs alla liberaler, och inget alternativ garanterar kvalitet eller jämlik tillgång. Frivilliga föreningar, försäkring och gemensam finansiering ryms i jämförelsen.

Utgångsdilemmat med 100 miljoner återfinns inte i basrevisionen. Ändringen ersätter därför ingen sådan originalövning, utan ger AI-läraren begreppsstöd och regler för framtida dilemman. Inga budgetbelopp, prognoser eller verkliga svenska rättsliga befogenheter införs. Befintliga L01–L06 och de sex modulerna behålls.

## Progression och återkomst

| Modul | Funktion | Tecken på förståelse |
|---|---|---|
| M01 | Gemensamma behov kan mötas med olika medel | Skiljer mål från effektpåstående |
| M02 | Samiras omsorg: vem betalar och vem väljer? | Skiljer offentligt finansierat val från egen betalning |
| M03 | Samma kartplacering kan rymma olika upplägg | Härleder inte finansieringsform från ett utförarval |
| M04 | Fyra frågor och en ändrad förutsättning | Prövar betydelsen av antal tillgängliga utförare, oavsett ägarform |
| M05 | Marknadsval, politisk rösträtt och ansvarsutkrävande | Kan förklara både liknelsens idé och skillnaden i röstvärde/köpkraft |
| M06 | Ny tillämpning i trafikfallet | Skiljer finansiering, utförare och resenärens val utan att kräva samma lösning som för omsorg |

Tabellerna visar begrepp och hypotetiska modeller, inte effektstorlekar. Varje tabell har textalternativ. Undervisningen hålls i korta steg med en fråga i taget, förklaring efter svar/fortsätt och inga krav på personlig politisk preferens. Eget exempel är inte belägg för deltagarens självständiga kunnande.

## Källkontroll och evidensgränser

Kontrollerat 2026-11-07:

- Milton Friedman, *The Role of Government in Education*, originalargument återgivet av EdChoice: https://www.edchoice.org/about/legacy/articles/the-role-of-government-in-education/ . Finansiering och drift hålls uttryckligen isär och ett offentligt finansierat föräldravalsförslag beskrivs. Används för att kontrollera att ett marknadsliberalt argument kan förena gemensam finansiering med individuellt val, inte för att belägga att samma modell fungerar i omsorg. EdChoice är en förespråkande organisation och texten ett normativt originalargument, inte en neutral effektutvärdering.
- OECD, Blöchliger (2018), *Market mechanisms in public service provision*, publikationssidans abstract: https://www.oecd.org/en/publications/market-mechanisms-in-public-service-provision_4c56c441-en.html . Skiljer brukarval, konkurrens, avgifter och finansieringsinstrument och redovisar möjliga målkonflikter om effektivitet, jämlikhet och ansvar. Inga effektstorlekar eller resultat för Samiras modell hämtas härifrån. Hela rapporten har inte granskats.
- FN/OHCHR, ICCPR artikel 25: https://2covenants.ohchr.org/About-ICCPR.html . Artikeltext återgiven i sökresultat anger allmän och lika rösträtt. Direktöppning av OHCHR:s ordinarie konventionssida gav 403. Underlaget avser principen om politiskt röstvärde, inte uttömmande definition av demokrati eller dagens svenska valregler.

Liknelsen om marknaden som parallellt demokratiskt system behandlas som en argumentationsmodell som kursen undersöker. Ingen konsensus om uttrycket påstås. Påståenden om att enskilda val kan påverka utförare är villkorade mekanismer, inte uppmätta utfall. Rätt att köpa, råd att köpa och försäkringens täckning hålls isär; inga juridiska rättigheter fastslås.

## Neutralitetskontroll

Både offentliga och privata upplägg prövas för information, tillgängliga alternativ, brukarinflytande och ansvar. Individens val motiveras med konkreta behov och självbestämmande; gemensam finansiering med tillgång och riskdelning. Beskriv först avsedd nytta, därefter villkor och begränsningar för båda. Det innebär ingen lika evidensstyrka eller krav att deltagaren värderar dem lika.

ideologies.js och problems.json är kursanpassade även i denna ändring. Äldre generaliseringar utanför de berörda avsnitten är inte fullständigt omgranskade; inget innehåll får status verified. Kursens komplettering ingår i COURSE.md och har inget externt läsberoende.

## Teststatus

Utfört i lokal Linuxmiljö 2026-11-07:

- Byggning och scripts/validate.py med -X warn_default_encoding -W error::EncodingWarning: godkända. Sex moduler, mål, lokala länkar, fem bilagor och reproducerbar COURSE.md kontrollerade.
- Syntaxkontroll med Node av den ändrade ideologies.js och JSON-avkodning av problems.json: godkända.
- git diff --check: godkänd.
- Manuell granskning av ändrade moduler, begreppsstöd, perspektivbeskrivningar och bedömning: gemensamma behov och både individens och kollektivets mekanismer framgår; inga effektstorlekar eller ideologiska facit införs. Före/efter-ordningen och fortsätt-vägen är beskrivna, inte provkörda i konsumentchatt.

 T19–T24 är planerade konsument- och deltagartester, inte utförda. Inga påståenden om bättre läranderesultat, mobilrendering eller faktisk undervisning i nya ChatGPT-/Claude-chattar görs.
