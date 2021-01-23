# Blatt 1

## Ziel

Das Ziel von Blatt 1 ist die folgeden Fragen zu beantwroten.

1. Wie redent man ueber Python mit dem Minecraft-Server?
1. Wie laesst man ein Python-Programm laufen (was ist ein Programm)?
1. Wie ruft man eine Funtion auf? (Was sind Funktionen, Parameter, Rueckgabewerte - Beispiele dafuer)?
1. Was sind Variablen (Zuweisung von Werten - Beispiele)?

## Setup

Das setup ist [hier](https://github.com/mncrft/homecraft.doc) beschrieben.

## Aufgabe 1.1

Schau Dir das folgenden Hello-World-Programm an.

```python
# Hello world

import sys
sys.path.append('/Users/jsaito/projects/minecraft/py')

from mcpi.minecraft import Minecraft

mc = Minecraft.create(address='192.168.178.45', port=4711)

mc.postToChat("Hallo World")
```

### Task 1.1 - Interactive Python-Console

#### 1.1.a - Python-Console oeffnen
Rufe auf der shell auf: `idle`. (*`idle3`*)

#### 1.1.b - Mit dem Server reden
Tippe jede Zeile in `idle` ein.
Beschreib was passiert.

#### 1.1.c - Chat
Aendere die Chat-Nachricht.

### Task 1.2 - Variablen, Functionsaufrufe und print

Probiere jetzt die folgenden Befehle aus und beschreibe was passiert.

#### 1.2.a Functionsaufruf, Variable

```python
r = mc.player.getRotation()
mc.postToChat(r)
```

#### 1.2.b Variablen benutzen

```python
mc.postToChat(r + 90)
```

#### 1.2.c Print

```python
print(r)
print(r + 90)
```

#### 1.2.d Functionsaufruf

```python
mc.player.setRotation(r+180)
```

#### 1.2.d Koordinaten

```python
x, y, z = mc.player.getPos()
print(x, y, z)
```


#### 1.2.f Koordinaten II

```python
mc.player.setPos(x, y+3, z)
```

Kannst du den Player 10 Blocks tief droppen?

#### 1.2.g Blocks

```python
mc.setBlock(x, y, z + 1, 10)
mc.setBlock(x, y, z + 1, 20)
mc.setBlock(x, y, z + 1, 20)

mc.setBlocks(x+1, y+2, z+1, x+10, y+10, z+1, 7)
```

Jetzt spiel mit den Werten rum.


### 1.3 Play time

## Naechstes mal

Die `idle` Console gibt manchmal Fehler und stuertzt dann ab.
Naechsets mal fuehren wir ein Programm ohne idle aus und schauen uns an, wie man mehr Blocks hintereinander setzt.