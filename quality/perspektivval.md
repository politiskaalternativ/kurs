# Granskning av kursens svarsalternativ

Granskad 2026-11-25 med `05607b3` på main som utgångspunkt. På den revisionen gick projektets validering igenom trots att M02 saknade ett eget val för varje person.

| Modul och mål | Vad deltagaren väljer mellan | Iakttagelse och ändring |
|---|---|---|
| M01 · L01 | Aminas och Eriks påståenden | Båda gick att välja. Varje påstående har nu en egen valrad. Sakförklaringen följer efter svaret. |
| M02 · L02 | Tre personers argument om bostadsprogrammet | Två breda teman ersatte de tre personernas argument i frågan. Nu har Amina, Erik och Sofia var sin ingång med en möjlig åtgärd och en fråga om dess villkor. Alla tre ingår i jämförelsen före idétraditionerna. |
| M03 · L03 | Ja eller nej till en slutsats om den ekonomiska axeln | De två svaren täcker frågan. Personerna utgör underlag för att pröva slutsatsen. Båda svaren visas på egna rader. |
| M04 · L04 | Ja eller nej till om ökad efterfrågan säkert leder till fler bostäder | Uppmaningen att ange vad som saknades antydde svaret. Deltagaren kan nu motivera vilket svar som helst före återkopplingen. |
| M05 · L05 | Två grunder för att bedöma demokratisk risk | Frågan gäller analysgrunden. Alternativen har fått parallella formuleringar på egna rader. |
| M06 · L06 | Egen analys eller arbetat exempel | En bedömningskommentar stod direkt intill det arbetade exemplet. Båda arbetssätten presenteras nu kortfattat. Bedömningsanvisningen finns i lärarstödet. |

Ramverket anger hur perspektiven får egna ingångar även i nya scenarier. Kursstarten och textreserven tar hänsyn till hela frågans alternativ vid begränsat utrymme eller förval i klienten.

## Utförda kontroller

**Pedagogisk genomgång av COURSE.md.** Varje väg i M02 följdes från utforskningsfrågan till den gemensamma jämförelsen. Tabellen visar vad som finns i kursunderlaget. Språket granskades även med valen i omvänd ordning. Alla tre ställer samma slags öppna fråga och återkopplingen ger varje person en tänkbar åtgärd och ett villkor att undersöka.

| Indata vid genomgången | Första innehåll | Innehåll som därefter knyts till jämförelsen |
|---|---|---|
| A | Amina om hushållens ekonomi och bostadsstödets villkor | Eriks etableringsfråga och Sofias fråga om lokala gemenskaper |
| B | Erik om marktilldelning och hinder för att bygga | Aminas fråga om betalningsförmåga och Sofias fråga om lokala gemenskaper |
| C eller Sofia | Sofia om ombyggnad i etapper och följder för bostadssökande | Aminas fråga om betalningsförmåga och Eriks etableringsfråga |
| fortsätt direkt | Kort jämförelse av samtliga tre argument | Idétraditionerna, utan registrerat val |
| B, sedan fortsätt | Erik utforskas först | Aminas och Sofias argument knyts till jämförelsen utan nytt svarskrav |

**Bygge och presentation.** `python3 scripts/build.py` regenererade COURSE.md. `python3 scripts/validate.py` godkände moduler, mål, valrader, återkoppling, länkar, fem ämnesbilagor och reproducerbar kursfil. Även körningen med `-X warn_default_encoding -W error::EncodingWarning` och `git diff --check` gick igenom. Lärandemålens tabell och de sex modulernas mål-ID jämfördes med main och var ordagrant lika. De sex utforskningsfrågorna i COURSE.md renderades lokalt med Pandoc 3.1.11.1 från GitHub-flavored Markdown till HTML. Varje val blev ett oformaterat listelement på samma nivå. ”Fortsätt” låg utanför listan i samtliga moduler.

**Regressionstest.** Varje provvariant byggdes om i en tillfällig kopia innan projektets validering kördes. Alla tolv utfall stämde med förväntan.

| Provvariant | Observerat resultat |
|---|---|
| M02 från main med de två tematiska valen | Avvisad av perspektivkontrollen |
| Utan C, med dubblerad Erik, med sammanslagen Amina/Erik respektive med dubblerad bokstav B | Alla fyra avvisade |
| Utan Sofias återkoppling respektive med förkryssat C | Båda avvisade |
| Fyra perspektiv i M02, först utan och sedan med det fjärde valet | Första avvisad, andra godkänd |
| Samma fyrperspektivscen som provmodul på annan plats | Godkänd med fyra val, avvisad med tre |
| Korrigerad M02 | Godkänd |

## Planerade klient- och deltagartester

T25–T33 återstår i nya ChatGPT- och Claude-konversationer. Där behöver man observera vilket perspektiv läraren faktiskt börjar med, hur återstående perspektiv behandlas och hur alternativen visas på mobil och vid tangentbordsfokus. Lärande över tid kräver deltagaruppföljning. Projektet följer dessa frågor i [issue 6](https://github.com/politiskaalternativ/kurs/issues/6).
