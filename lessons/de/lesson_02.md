# Blatt 2

## Ziel
Das Ziel von Blatt 2 ist die folgeden Fragen zu beantworten.

1. Wie lege ich eine Python-Programmdatei an?
1. Wie fuehre ich ein Python-Programm aus?
1. Wofuer ist eine for-Schleife gut? (Beispiel)

## Wiederholung
1. Was ist eine *Fuktion*?
1. Was ist ein *Parameter* einer *Funktion*?
1. Was sind *Strings*?


## Aufgabe 2.1 - Python ohne idle

Oeffne eine neue Datei `aufgabe2.py` mit dem Text editor
und tippe das folgende Beispielprogramm ab.

```python
# Hello world

print("hello world")
```

### 2.1.a
Fuehre das Program auf der Konsole aus mit: `python hello.py`.

### 2.1.b
Was ist anders als mit `idle`?

### 2.1.c
Veraendere das Programm und gib einen anderen Text aus.

### 2.1.c
Kopiere das hello-world-Programm aus Blatt 1 in eine Datei `hallo_server.py` und fuehre es aus.
Der Text soll auf im Minecraft Chat erscheinen.


## Aufgabe 2.2 - Schleife mit for

Lege eine Datei 'loop1.py` mit folgendem Inhalt an.

```python
list = ["Hugo", "Filpper", "Gaston"]
print(list)
```

Und fuehre aus.

### 2.1.b
Jetzt aendere das Programm wie folgt und fuehre aus.

```python
list = ["Hugo", "Filpper", "Gaston"]
for name in list:
  print(name)
```

Erklaere was du siehst.

### 2.2.b

Jetzt aendere die Liste und fuehre aus.

```python
list = range(10)
print(list)

for i in list:
  print(i)
```


## Aufgabe 2.3 - Schleife mit Minecraft

Lege eine neue Datei `loop2.py` mit folgendem Inhalt an.

```python
from mcpi.minecraft import Minecraft

mc = Minecraft.create(address='192.168.178.45', port=4711)

list = ["Hugo", "Filpper", "Gaston"]

for name in list
  mc.postToChat(name)
```

### Aufgabe 2.3.a
Aendere die Parameter fuer `postToChat` in der liste `list`.


### Aufgabe 2.3.b (*schwierig*)
Aendere das Programm, damit es einen 10 Bloecke hohen Turm in der Naehe von `mc.player` baut.
Benutze dazu Teile aus [Aufgabe 1.2.g](./lesson_01.md#12g-blocks).


## Next

Verschachtelte Schleifen.
