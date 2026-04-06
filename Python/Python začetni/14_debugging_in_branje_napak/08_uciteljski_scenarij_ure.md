# Učiteljski scenarij ure – 14 – Debugging in branje napak

## Pred uro

- Odpri `02_ucni_list.md`, `03_resitev.md` in ta scenarij.
- Pripravi tudi ``06_pokvarjeni_programi.py``.
- Pripravi tudi ``07_popravljene_resitve.py``.
- Vnaprej določi minimum, ki mora do konca ure delovati.
- Pripravi en zelo kratek primer ali demonstracijo.

## Potek ure

### 0–10 min: začetek

Učitelj:
- zelo kratko poveš cilj ure,
- pokažeš mikro-primer ali mini demonstracijo,
- učencem daš prvo najmanjšo nalogo, da takoj začnejo tipkati.

Učenci:
- Popravi program z manjkajočim dvopičjem pri `if`.
- Popravi program z napačno zamaknjenim blokom.

### 10–25 min: ogrevanje

Učitelj:
- hodiš med njimi,
- popravljaš samo prve blokade,
- ne rešuješ cele naloge namesto njih,
- iščeš ponavljajoče se napake in jih razrešiš na hitro za celo skupino.

Učenci:
- Popravi program, ki sešteva niz in število brez pretvorbe.

### 25–55 min: glavni del

Učenci:
- Popravi `NameError`, kjer je ime spremenljivke napačno.
- Popravi `IndexError`, kjer program bere element izven seznama.
- Popravi `while` zanko, ki se nikoli ne ustavi.
- Pri vsakem primeru zapiši, kaj je bilo narobe.

### 55–75 min: razširitev

Učenci:
- dokončajo jedro,
- počistijo napake,
- uredijo izpis, logiko ali strukturo,
- pokažejo vsaj dve delujoči stvari.

Opomba:
- Za hitrejše: Primerjaj `SyntaxError` in `TypeError`.
- Za hitrejše: Namerno pokvari delujoč program in ga nato popravi.
- Za hitrejše: Dodaj `print()` preverjanje v program, ki vrača čuden rezultat.
- Izziv: Pripravi 3 pokvarjene programe za sošolca.
- Izziv: Naredi mini checklisto za debugging.

### 75–95 min: skupni pregled

### 95–110 min: zaključevanje

Opomba:
- delujoče jedro: Popravi program z manjkajočim dvopičjem pri `if`.
- vsaj še ena pravilno rešena naloga iz glavnega bloka
- učenec zna pokazati, kaj je popravil ali dodal

### 110–120 min: zaključek

## Tipične napake

- skočijo popravljat brez branja napake
- ignorirajo številko vrstice
- na slepo spreminjajo več stvari hkrati

## Ko se kdo zatakne

- pravilo: preberi vrsto napake, vrstico, šele nato popravljaj
- naj popravljajo eno stvar naenkrat
- uporabi `print()` debugging pred večjimi spremembami

## Vprašanja za učitelja

- Kaj je najmanjša stvar, ki mora že delovati? (Popravi program z manjkajočim dvopičjem pri `if`.)
- Kateri del glavnega bloka trenutno gradiš? (Popravi `NameError`, kjer je ime spremenljivke napačno.)
- Kaj si nazadnje spremenil, preden je program prenehal delovati?
- Ali znaš pokazati en primer vhoda in pričakovanega izhoda?

## Kdaj ustaviš učenca

- odpre bonus, preden ima delujoče jedro,
- 10 minut ponavlja isti napačen poskus brez testiranja,
- piše preveč kode naenkrat brez vmesnega zagona,
- sam ne zna povedati, kaj naj bi trenutni del kode sploh naredil.

## Kdaj ga pustiš delati

- napreduje v malih korakih,
- pogosto zažene program,
- zna povedati, kaj testira,
- si sam beleži ali razlaga, kaj trenutno ne dela.

## Opomba

Pokaži en korak. Potem naj učenci delajo. Pomagaj z majhnimi posegi, ne z dolgim govorom.
