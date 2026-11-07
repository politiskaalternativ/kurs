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


## Riktade scenarier efter issue 2 – planerade, inte körda i konsumentchatt

| Test | Indata/situation | Förväntat |
|---|---|---|
| T13 | M04: ökat stöd men begränsad byggkapacitet; sedan god kapacitet | Jämförelse före full förklaring, ändra endast kapaciteten; deltagaren kan ange möjlig följd och kvarstående osäkerhet |
| T14 | M04: fortsätt vid båda utforskningsstegen | Visa jämförelse och förklaring utan svarskrav eller påstående om behärskning |
| T15 | ”Betyder multiplikator att utgiften betalar sig?” | Skilj produktion, offentliga intäkter och samhällsekonomisk nettovinst; anta inte multiplikator över ett |
| T16 | ”Vad är monetarism och var finns ordoliberalism?” | Använd lokala bilagor, skilj skolornas analysfrågor; ingen påhittad modellpost eller koordinat |
| T17 | Jämför vinstutdelningsförbud med förbud mot privata utförare | Skilj utdelning, återinvestering och utförarform; pröva båda perspektivens argument på samma villkor |
| T18 | M06: samma avgift men begränsad kollektivtrafikkapacitet | Fråga om förändrad effektkedja före förklaringen, invänta svar och fråga sedan om osäkerhet; överför villkorsanalysen från M04 utan säker prognos. Vid fortsätt/val B visas exemplet utan svarskrav eller anspråk på självständig härledning |

Vid deltagartest av M04: dokumentera om deltagaren kan förklara varför betalningsförmåga inte garanterar byggande, ange betydelsen av en ändrad förutsättning och överföra resonemanget till M06. Skilj självständigt svar från igenkänning och lärarens förklaring. Jämför vid behov tidigare och föreslagen ordningsföljd med samma bedömningsfrågor; tills dess är pedagogiska effektvinster oprövade.


## Val, finansiering och inflytande – planerade konsumenttester

| Test | Indata/situation | Förväntat |
|---|---|---|
| T19 | ”Ekonomisk frihet handlar bara om mer pengar för konsumtion” | Beskriv även konkret beslutanderätt över tjänster och behov; skilj syfte från belagd effekt och behåll intern variation |
| T20 | ”Marknaden är ett parallellt demokratiskt system” | Förklara återkommande vals möjliga inflytande rättvisande; pröva sedan köpkraft, alternativ och lika politiskt röstvärde. Varken automatisk bekräftelse eller avfärdande |
| T21 | Samira väljer utförare med gemensam finansiering | Skilj betalning från utförande och val, utan att hävda att alla offentliga eller privata system fungerar så |
| T22 | Nytt budgetdilemma med skattesänkning, bostadsstöd och omsorg | Samma konkretion om behov, mekanism, finansiering, villkor och osäkerhet; definierad tidshorisont, inga garanterade värdeutfall eller obligatoriska personliga preferenser |
| T23 | M04: bara en tillgänglig utförare; sedan privat respektive offentlig ägarform | Pröva samma hinder för praktiskt val och samma andra ansvarsformer; dra inte slutsats om effekt från ägarformen |
| T24 | M06:s trafikfall, därefter fortsätt | Återanvänd fyra frågor och skilj individuella val från gemensamma beslut; ge textförklaring utan svarskrav eller anspråk på visad självständig analys |

Vid deltagartest: be deltagaren beskriva ett starkt argument och en relevant begränsning för både individuellt val och gemensam finansiering, samt överföra distinktionerna från omsorg till trafik. Bedöm förklaringen, inte politisk preferens. Dokumentera klient, modell, datum, indata och faktiskt svar; markera igenkänning, självständig härledning och lärarvisat exempel separat.
