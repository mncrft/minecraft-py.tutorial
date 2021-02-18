# Blatt 3 - Schleife in Schleife

## Ziel
Das Ziel von Blatt 3 ist die folgeden Fragen zu beantworten.

1. Wofuer ist eine geschachtelte Schleife gut? (Beispiel)
1. Wie schreibe ich eine geschachtelte Schleife? (Beispiel)

## Wiederholung
1. Wie fuehre ich ein Python-Programm aus?
1. Was ist eine Schleife?

## Aufgabe 3.1 - Funktionen selbst definieren

Lege eine neue Python-Datei `loop2.py` an.
Oeffne die Datei und tippe das folgende Programm ab.
Speichere die Datei. 

```python
snacks = ['fritten', 'snickers', 'mc flurry']
names = ['enderman', 'frau ruebenach']

for n in names:
  for s in snacks:
    print(n, "isst gerne", s)
```

### 3.1.a
Fuehre das Programm auf der Konsole aus mit `python loop2.py`.
Was siehst Du? Erklaere jede Zeile des Programms.
Wie oft wird print aufgerufen?

### 3.1.b
Aendere das Programm mit anderen `foods` und `names`.

### 3.1.c
Jetzt teste das folgende Programm.

```python
for x in range(4):
  for y in range(4):
    print(x, y)
```

Wie oft wird `print()` aufgerufen?

## Aufgabe 3.2 - Doppelschelfeife auf dem Server (*schwierig*)

Benutze eine doppelte Schleife.

### 3.2.a
Schreibe ein Programm, das eine Flaeche aus Bloecken in Minecraft baut.

### 3.2.b
Schreibe ein Programm, das einen Wuerfel aus Bloecken in Minecraft baut.

### 3.3
Fuehre aus und erklaere.

```py
import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *

colors = [14, 1, 4, 5, 3, 11, 10]

mc = minecraft.Minecraft.create()
height = 60

mc.setBlocks(-64,0,0,64,height + len(colors),0,0)
for x in range(0, 128):
	for colourindex in range(0, len(colors)):
		y = sin((x / 128.0) * pi) * height + colourindex
		mc.setBlock(x - 64, y, 0, block.WOOL.id, colors[len(colors) - 1 - colourindex])
```
