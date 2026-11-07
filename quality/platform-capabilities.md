# Plattformskontroll 2026-11-05

Mål: ChatGPT och Claude i vanlig webb-/mobilchatt. API, Claude Code och andra agentklienter ingår inte i leveranslöftet.

| Funktion | ChatGPT | Claude | Reserv |
|---|---|---|---|
| Hämta webbinnehåll | documented; beror på verktyg, plan och inställningar | documented; web fetch vid länk med webbtillgång | Klistra in COURSE.md |
| Starta från enbart domän | unknown, inte sluttestat | unknown, inte sluttestat | Kopierbar uttrycklig kursbegäran |
| A/B/fortsätt i vanlig text | utformat, inte sluttestat i ny chatt | utformat, inte sluttestat | Samma text |
| Tabeller | Markdown-underlag finns, renderingen inte plattformstestad | Markdown-underlag finns, renderingen inte plattformstestad | Läs raderna som text |
| Widgets/diagram | unknown och inte nödvändigt | unknown och inte nödvändigt | Text och jämförelser |

Officiella dokument lästa 2026-11-05:
- https://help.openai.com/en/articles/9260256-chatgpt-capabilities-overview — verktyg beror på abonnemang och inställningar; visade relativ uppdatering ”8 days ago”.
- https://support.claude.com/en/articles/10684626-enable-and-use-web-search — beskriver web search och direkt web fetch; visade ”Updated over a month ago”.

Aktuell utvecklingsmiljö: GitHub-läsning och lokal kloning tested. Officiella dokument kunde öppnas. Webbverktygets försök att öppna https://politiskaalternativ.se/ misslyckades i denna session: blocked för just det försöket; det bevisar inte att domänen är otillgänglig för alla klienter. Ingen ny konsumentchatt i ChatGPT eller Claude har testats. Dokumenterade funktioner är inte kursacceptanstester.

llms.txt är kompletterande upptäcktshjälp, ingen garanterad standard för automatisk kursstart. Synlig HTML och uttrycklig reservprompt är primära ingångar. Kontrollera plattformarna igen vid nästa större ändring eller vid misslyckad hämtning. Ingen automatisk bevakning är konfigurerad.


## Uppföljning 2026-11-07

Samma målklienter och textreserv behålls. Inga nya widgets eller andra verktyg krävs av ändringarna för issue 2.

Officiell dokumentation kontrollerad på nytt: OpenAI:s capabilities overview ovan (visade ”Updated: 10 days ago”) anger att verktyg beror på abonnemang och inställningar. Claudes web search-dokument ovan (daterat 2026-10-07) beskriver web fetch med länkar och villkor för att aktivera webbtillgång. Detta är fortsatt documented, inte tested för kursstart eller undervisning i nya konsumentchattar. Tabellernas textalternativ och inklistring av COURSE.md kvarstår. GitHub-läsning och kloning fungerar i utvecklingsmiljön; det säger inget om deltagarens klient.


## Val och inflytande – uppföljning 2026-11-07

OpenAI:s capabilities overview och Claudes web search-dokument ovan öppnades på nytt vid denna ändring; samma dokumenterade villkor och datum som uppföljningen ovan. Inga nya plattformsfunktioner används: jämförelserna är vanlig text/tabeller med löptext som reserv. Nya konsumentchattar och mobilrendering för T19–T24 är inte testade. Dokumentkontroll är inte ett acceptanstest.
