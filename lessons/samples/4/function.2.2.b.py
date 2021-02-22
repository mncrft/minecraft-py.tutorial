from mcpi.minecraft import Minecraft
mc = Minecraft.create(address='erebor.saito.berlin', port=4711)

def add_stars(str):
  return "* " + str + " *"

def add_many_stars(str, n):
  s = str
  for i in range(n):
    s = add_stars(s)

  return s

message = add_many_stars("oh yeah", 10)
mc.postToChat(message)
