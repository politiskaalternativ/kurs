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
