# Blatt 4

## Ziel
Das Ziel von Blatt 4 ist die folgeden Fragen zu beantworten.

1. Wie definiere ich eine Funktion?
1. Was ist der Aufruf einer Funktion?
1. Was sind die Parameter einer Funktion?
1. Was ist der Rueckgabewert einer Funktion?

## Aufgabe 2.1 - Funktionen selbst definieren

Lege eine neue Python-Datei `function.py` an.
Oeffne die Datei und tippe das folgende Programm ab.
Speichere die Datei und fuehre das Programm aus.

```python
def add_stars(str):
  print("input is: " + str)
  return "* " + str + " *"

s = add_stars('lala')

print(s)
```

### 2.1.a
Fuehre das Program auf der Konsole aus mit: `python function.py`. Erklaere.

### 2.1.b

Wir aendern das Programm leicht ab. Sage *vorher* was passieren wird.

```python
def add_stars(str):
  print("input is: " + str)
  return "* " + str + " *"

s = add_stars('lala')
s = add_stars('lala')

print(s)
```

### 2.1.c

Wir aendern das Programm leicht ab. Sage *vorher* was passieren wird.

```python
def add_stars(str):
  print("input is: " + str)
  return "* " + str + " *"

s = add_stars('lala')
s = add_stars('s)

print(s)
```

### 2.1.d

Wir aendern das Programm leicht ab. Sage *vorher* was passieren wird.

```python
def add_stars(str):
  print("input is: " + str)
  return "* " + str + " *"

s = add_stars(add_stars('lala'))

print(s)
```

### 2.1.e

```python
def add_stars(str):
  print("input is: " + str)
  return "* " + str + " *"

s = add_stars(add_stars('lala'))

print(s)
```

## 2.2 Extra parameter

Wir benutzen die Funktion `add_stars()` in einer neuen Funktion
`add_many_stars`.

```python
def add_stars(str):
  print("input is: " + str)
  return "* " + str + " *"

def add_many_stars(n, str):
  print("input is: " + str)

  s = str
  for i in range(n):
    s = add_stars(s)

  return s

s = add_many_stars("oh yeah")

print(s)
```

## 2.2.a
Fuehre das neue Programm aus und erklaere.

## 2.2.b
Benutze `add_many_stars()` um in den Minecraft Chat eine Nachricht mit vielen Sternen zu schreiben.


## 2.3

```python
def range_for(centre, size):
  return range(centre - size, centre + size + 1)
        
def area(x, y, z, size, block_type):
  blocks = []
  for i in range_for(x, size):
    for j in range_for(z, size):
      blocks.append([i, y, j, block_type])

  return blocks

def pyramid(x, y, z, hight, block_type):
  blocks = []
  for h in range(y, y + hight):
    blocks = blocks + area(y, h, z, size, block_type)

print(area(10, 0, 100, 3, 42))
```

## 2.3.a

Benutze die Funktion, um eine Pyramiden zu bauen.
