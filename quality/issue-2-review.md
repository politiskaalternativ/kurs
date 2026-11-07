# Ändringar och granskningsunderlag för issue 2

Datum: 2026-11-07. Status: draft. Metod: Discovery Learning 0.2.0.
Utgångsrevision: c4cb278e808458e7f3a6852c8a955fe87305d300.

## Avgränsning och beslut

De fyra konkreta fynden åtgärdas. Befintliga L01–L06 behålls. M04:s befintliga kontrastövning utvecklas och tidigareläggs; detta är ett pedagogiskt förslag, inte en påvisad förbättring av läranderesultat. Ingen ny poängsättning, politisk profilering eller obligatorisk fritext införs.

Kursen lär ut perspektiv genom analys av konkreta fall. M01:s värde/hypotes används i M02 och M04; M03 skiljer kartor från effektbelägg; M04:s villkorsjämförelse överförs till M06; M05:s granskning av makten återkommer i samma slutuppgift. Ordlista, lärarstöd, bedömning och onboarding följer samma begrepp och nivå av kunskapsanspråk. M01 lämnas oförändrad eftersom dess grunddistinktion redan fungerar som ingång.

## Saklig kontroll

- Utgiftsmultiplikator: IMF, Jahan, Mahmud och Papageorgiou, *What Is Keynesian Economics?*, september 2014: https://www.imf.org/external/pubs/ft/fandd/2014/09/basics.htm . Avsnittet om multiplikatoreffekt villkorar en effekt över ett. Ökad produktion ska inte beskrivas som en garanti för självfinansiering eller samhällsekonomisk nettovinst.
- Monetarism: IMF, Jahan och Papageorgiou, *What Is Monetarism?*, mars 2014: https://www.elibrary.imf.org/view/journals/022/0051/001/article-A012-en.xml . Underlaget beskriver penningmängdens roll, kort/lång sikt, regelstyrning samt problemet med varierande omloppshastighet. Den nya posten är en kort självständig sammanfattning utan historiska effektstorlekar eller påhittade axelkoordinater.
- Läskontroll 2026-11-07: IMF:s vanliga HTML- och PDF-adresser gav 403 vid direktöppning. Innehållet kunde granskas i söktjänstens fullständigare återgivningar av IMF:s original och eLibrary-version. Detta är dokumentkontroll, inte en oberoende empirisk effektstudie.
- Vinstuttag: kontroll av förslag, axelrubrik och motargument i problems.json. Ett förbud mot utdelning innebär inte i sig ett förbud mot icke-vinstdrivande utförare. Ny invändning gäller regelutformning och möjlig administration; ingen faktisk rättslig eller uppmätt effekt hävdas.
- Ordoliberalismens fördjupningshänvisning pekar nu till ideologies.js där innehållet finns. Monetarism ligger i economics.js.
- Lindvik och trafikfallet är hypotetiska. Tabellerna visar möjligheter och osäkerheter, inte observerade utfall eller kalibrerade modeller. Inga nya numeriska beräkningar eller prognoser införs.

## Neutralitet och återstående ämnesgranskning

Lärarstöd och moduler kräver samma frågor om mål, mekanism, intern spänning och starkaste rimliga invändning. Attribution verifierar inte ett empiriskt påstående. Skillnader i evidensstyrka får redovisas.

De två konkreta bilagefelen är rättade, men samtliga historiska generaliseringar och kulturklassificeringar har inte faktagranskats. Exempelvis kvarstår breda formuleringar i ekonomibilagans kritik av planekonomi och marxistisk ekonomi för separat ämnesgranskning. De får inte användas som självständigt verifierade sakförklaringar. Även övriga problemscenariers kategoriska orsaks- och effektpåståenden behöver granskas. Att instruktionsstödet förbättrats innebär inte att bilagorna är godkända eller neutrala i varje detalj. Ingen status ändras till verified.

## Verifiering

Utfört 2026-11-07 i lokal Linuxmiljö:

- python3 scripts/build.py och python3 scripts/validate.py: godkända; sex moduler, målkoder, undervisningsdelar, lokala länkar, fem bilagor och reproducerbar COURSE.md.
- Byggning och validering med -X warn_default_encoding -W error::EncodingWarning: godkända.
- Simulerad cp1252-standard för pathlib.Path.open: byggning och validering godkända, byteidentiskt UTF-8-resultat samt LF-radslut. Detta är en regression för kodningsfelet, inte en faktisk Windowskörning.
- node --input-type=module --check för economics.js och JSON-avkodning av båda JSON-bilagorna: godkända.
- git diff --check: godkänd.
- Manuell genomläsning av samtliga sex moduler, onboarding, ramverk, ordlista och bedömning: befintliga mål och grundscenario behålls, återkoppling går från M01 till M06 och obligatoriskt innehåll har textalternativ. Detta är innehållskontroll, inte observerad undervisning.

 Nya ChatGPT-/Claude-konsumentchattar, mobilrendering och deltagarutvärdering är planerade och inte utförda. T13–T18 i acceptance-tests.md prövar de ändrade momenten. Tidigarelagd utforskning ska utvärderas innan samma ändring sprids generellt.
