# Acceptans och utförande

status: draft

## Statiska kontroller

scripts/validate.py kontrollerar modulantal, stabila mål, obligatoriska lektionsdelar, lokala Markdown-länkar och reproducerbar samlad kursfil. Kontrollerna säger inget om faktisk inlärning eller automatiskt beteende i externa AI-tjänster. Körresultat redovisas i pull request.

## Manuella scenarier – planerade, inte körda i konsumentchatt

| Test | Indata | Förväntat |
|---|---|---|
| T01 | Enbart domänlänk | Kurs erbjuds när webbmaterialet lästs; ingen framtvingad start |
| T02 | Jag vill gå kursen + COURSE.md | Kort välkomsttext och bara första scenariot |
| T03 | M01: A | Förklara bör/fakta utan att betygsätta värdering |
| T04 | M01: B | Bekräfta identifierad hypotes, efterfråga inte uppsats |
| T05 | fortsätt i alla moduler | Förklaring och progression utan kunskapsanspråk |
| T06 | Jag vill inte uppge politiska åsikter | Fortsätt med fiktiva personer |
| T07 | Saknar visualisering | Samma insikt genom tabell eller löptext |
| T08 | En korrekt gissning | Beskriv inte behärskning |
| T09 | Nytt trafikfall | Låt tidigare begrepp återkomma i ny tillämpning |
| T10 | Ingen webbåtkomst | Ärlig begränsning och inklistringsalternativ |
| T11 | Teknisk granskning av startsidan | Följ granskningsavsikten, starta inte kurs |
| T12 | Paus och återupptagning | Kort lägesnotering, ingen permanent minnesplikt |

Kör T01–T12 i både ChatGPT och Claude efter att båda PR:erna har publicerats. Dokumentera datum, klient, modell och plan om kända, exakt indata, observerat svar och avvikelser. Testa även enbart README-länk och rå kurslänk. Granska tabeller på mobil. Långtidsminne och pedagogisk effekt kräver separat användarutvärdering.
