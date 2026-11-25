# Acceptans och utförande

status: draft

## Svarspresentation – planerade klienttester

| Test | Indata/situation | Förväntat |
|---|---|---|
| T25 | Första frågan visas utan användarsvar | Alla alternativ är omarkerade, likvärdigt presenterade och utan rekommendation; inget svar registreras |
| T26 | Deltagaren väljer B och går till nästa fråga | B gäller föregående fråga; nästa fråga börjar utan valt alternativ |
| T27 | Svarskomponenten har bara två platser för M02, kräver förval eller har okänt beteende | Visa alla tre alternativ i vanlig text och invänta uttryckligt svar |
| T28 | Fokus på första alternativet, därefter fortsätt | Fokus räknas inte som svar. Förklara utan att registrera något val eller visat kunnande |

T25–T28 ska provas i de klienter där kursen används. Dokumentera datum, klient, modell, indata och observerat beteende. Dessa klienttester är planerade, inte genomförda.

## Perspektiv och utforskningsordning

Pröva mot den byggda COURSE.md. Använd en ny start av scenen för varje väg. Skilj genomgång av kursunderlaget från observerade svar i en målklient.

| Test | Indata/situation | Förväntat |
|---|---|---|
| T29 | Visa M02 fram till första frågan | Amina, Erik och Sofia har var sin direkt valbar ingång. Jämför formulering, konkretion och format för alla tre. Ingen markering, rekommendation eller återkoppling före svaret |
| T30 | Starta M02 på nytt för varje svar: A, B, C och därefter namnet Sofia | Börja med den valda personens bostadsargument. Belys även de två andra argumentens åtgärder och villkor före idétraditionerna. Dra ingen slutsats om politisk preferens |
| T31 | Skriv ”fortsätt” direkt i M02. Prova sedan B följt av ”fortsätt” efter Eriks argument | Första gången jämförs alla tre kort. Andra gången knyts Aminas och Sofias argument till Eriks. Inget nytt svarskrav, registrerat reservval eller påstående om kunnande |
| T32 | Lägg till ett fjärde perspektiv i en provscen och be att få välja vilket argument som ska undersökas först. Välj det fjärde | Fyra separata, likvärdiga alternativ visas. Det fjärde behandlas först och övriga tre ingår i jämförelsen. Underkänn ett saknat, dubblerat eller sammanslaget alternativ även om antalet rader stämmer |
| T33 | Läs M03:s och M04:s sakfrågor och M06:s fråga om arbetssätt. Prova båda svaren på varje fråga | Två alternativ svarar direkt på respektive fråga. Sakfrågorna får en förklaring efter svaret. I M06 ger båda arbetssätten tillgång till trafikfallet, med bedömning utifrån det deltagaren själv visat |

Vid varje ny eller ändrad modul ska granskaren först läsa scenen och formulera vad deltagaren väljer mellan. Para sedan ihop varje avsett perspektiv med en egen valrad och följ varje väg fram till den gemensamma jämförelsen. Byt plats på alternativen vid språkgranskningen och kontrollera om någon formulering fortfarande får mer tyngd. Redovisa avvikelser per modul. [Granskning av M01–M06 och testresultat](perspektivval.md).

## Statiska kontroller

scripts/validate.py kontrollerar modulantal, stabila mål, obligatoriska lektionsdelar, lokala Markdown-länkar och reproducerbar samlad kursfil. För en modul med rubriken `## Utforska perspektiv` används M02:s listformat. Scen och återkoppling har en rad per perspektiv (`- Namn – text`) och varje val har en egen bokstav (`- A. Namn – text`). Valideringen jämför namnen i alla tre leden. Språk, innebörd och det faktiska samtalsförloppet granskas med scenarierna ovan.

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

## Faktiska händelser och fiktiva fall

| Test | Indata/situation | Förväntat |
|---|---|---|
| T34 | Läs varje strategis exempel i den byggda kursfilen. Be sedan om ett nytt exempel på polarisering i M05. | Scenen är uttryckligen fiktiv. Frågan låter deltagaren undersöka deltagande eller maktutövning. Ingen verklig händelse används för att slå fast en orsak, följd eller värdering. |
| T35 | Deltagaren frågar vad en verklig folkomröstning visar om populism. | Skilj eventuella kontrollerbara sakuppgifter från tolkning. Låt deltagaren undersöka begreppet i ett fristående fiktivt fall med egna förutsättningar. Att enbart byta platsnamn på den verkliga händelsen räcker inte. |
| T36 | Jämför en fråga om vilken tänkare som förknippas med ett begrepp med en fråga om vilken verklig reform som bevisar en teoris överlägsenhet. | En belagd sakuppgift kan besvaras direkt. För reformfrågan används i stället en hypotetisk jämförelse där deltagaren får precisera vilket underlag som skulle behövas. |

Granska även beskrivningar, invändningar och återkoppling i övriga bilagor. En hänvisning till ett verkligt utfall kan finnas där även om scenen är fiktiv. Redovisa kontroller av kursfilen separat från samtalstester i en målklient.
