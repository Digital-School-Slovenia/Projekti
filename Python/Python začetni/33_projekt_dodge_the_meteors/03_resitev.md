# Rešitev / učiteljske usmeritve – 33 – Projekt – Dodge the Meteors

## Kako vodiš to uro

- hitro do igralca, hitro do meteorjev, hitro do trka,
- točke in težavnost sta šele po delujočem jedru,
- seznam meteorjev naj učenci res razumejo.

## Minimalni referenčni okvir

```python
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 700)
meteors = []
```

## Učiteljski checkpointi

1. Ladja se premika.
2. Meteorji nastajajo in padajo.
3. Trk zaključi igro ali spremeni stanje.

## Python datoteke v tej mapi

- `06_uciteljska_resitev.py`
