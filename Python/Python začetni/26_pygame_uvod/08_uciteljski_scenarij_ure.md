# Učiteljski scenarij ure – 26 – Pygame – uvod, okno, risanje in premikanje

## Pred uro

- Odpri `02_ucni_list.md`, `03_resitev.md` in ta scenarij.
- Pripravi tudi ``06_osnovna_struktura.py``.
- Pripravi tudi ``07_premik_kvadrata.py``.
- Vnaprej določi minimum, ki mora do konca ure delovati.
- Pripravi en zelo kratek primer ali demonstracijo.

## Potek ure

### 0–10 min: začetek

Učitelj:
- zelo kratko poveš cilj ure,
- pokažeš mikro-primer ali mini demonstracijo,
- učencem daš prvo najmanjšo nalogo, da takoj začnejo tipkati.

Učenci:
- Ustvari okno 600 × 400 ali 800 × 500.
- Omogoči zapiranje okna z gumbom X.

### 10–25 min: ogrevanje

Učitelj:
- hodiš med njimi,
- popravljaš samo prve blokade,
- ne rešuješ cele naloge namesto njih,
- iščeš ponavljajoče se napake in jih razrešiš na hitro za celo skupino.

Učenci:
- Dodaj `screen.fill()` in preizkusi več barv.

### 25–55 min: glavni del

Učenci:
- Nariši pravokotnik ali krog.
- Dodaj igralca kot `pygame.Rect`.
- Premikaj igralca s puščicami.
- Omeji igralca na zaslon.

### 55–75 min: razširitev

Učenci:
- dokončajo jedro,
- počistijo napake,
- uredijo izpis, logiko ali strukturo,
- pokažejo vsaj dve delujoči stvari.

Opomba:
- Za hitrejše: Nariši hišo, sonce in tla.
- Za hitrejše: Dodaj še drugi objekt.
- Za hitrejše: Dodaj hitrost v ločeni spremenljivki.
- Izziv: Naredi mini igro lovljenja.
- Izziv: Dodaj restart ali reset.

### 75–95 min: skupni pregled

### 95–110 min: zaključevanje

Opomba:
- delujoče jedro: Ustvari okno 600 × 400 ali 800 × 500.
- vsaj še ena pravilno rešena naloga iz glavnega bloka
- učenec zna pokazati, kaj je popravil ali dodal

### 110–120 min: zaključek

## Tipične napake

- pozabijo glavno zanko
- zaslon se ne osveži
- premik se dogaja brez omejitve ali brez event handlinga

## Ko se kdo zatakne

- naj najprej zaženejo najosnovnejše okno
- dodajaj le en nov element naenkrat
- če se vse podre, vrni program na zadnjo delujočo verzijo

## Vprašanja za učitelja

- Kaj je najmanjša stvar, ki mora že delovati? (Ustvari okno 600 × 400 ali 800 × 500.)
- Kateri del glavnega bloka trenutno gradiš? (Nariši pravokotnik ali krog.)
- Kaj si nazadnje spremenil, preden je program prenehal delovati?
- Ali že imaš delujoče jedro, preden odpiraš bonuse?

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
