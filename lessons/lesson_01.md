# Lesson 1

## Goals

The goal of this lesson is to answer the following questions.

1. How to talk to the server through Python using `idle`?
1. How to run a python program (what is a program)?
1. How to call function (functions, parameters and return values by exmple)?
1. What are variables (assignment by example)?

## Prerequisites

The Minecraft server, client, python, and the RasperryJucie library must be setup as
described by https://github.com/mncrft/homecraft.doc and you need a text editor.

## Task 1

Look at the folowing hello-world program below.

```python
# Hello world

import sys
sys.path.append('/Users/jsaito/projects/minecraft/py')

from mcpi.minecraft import Minecraft

mc = Minecraft.create(address='192.168.178.45', port=4711)

mc.postToChat("Hallo World")
```

### Task 1.1 - Interactive Python console

#### 1.1.a - Open the python console
Open `idle`. (*`idle3`*)

#### 1.1.b - Talk to server
Type each line into `idle`. After each line describe what it might mean and what you observe in your Minecraft client.

#### 1.1.c - Chat
Change the message in the chat.

### Task 1.2 - Variables, method calls and print

With `idle` still open, now try a few things: copy the following code line by line and explain.

#### 1.2.a Method call, variable

```python
r = mc.player.getRotation()
mc.postToChat(r)
```

*Answer.* `r` is a variables, stores players rotation in degrees.

#### 1.2.b Use variables

```python
mc.postToChat(r + 90)
```

#### 1.2.c Use variables

```python
print(r)
print(r + 90)
```

#### 1.2.d Use variables

```python
mc.player.getRotation(r+180)
```

#### 1.2.d Coordinates

```python
x, y, z = mc.player.getPos()
print(x, y, z)
```

*Answer* `x`, `y` and `z` are variables, print shows their content, they represent the player's position.


#### 1.2.f Play with coordiantes

```python
mc.player.setPos(x, y+3, z)
```

How can you drop the player from 10 blocks higher?

#### 1.2.g Blocks

```python
mc.setBlock(x, y, z + 1, 10)
mc.setBlock(x, y, z + 1, 20)
```

Now playaround with difft other values for the last parameter.


### 1.3 Play time

Now play around.

## Next time

Some times you saw errors and you had to restat `idle`. Next time let's write and call programs without idle.
