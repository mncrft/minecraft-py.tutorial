def add_stars(str):
  return "* " + str + " *"

def add_many_stars(str, n):
  print("input is: " + str)

  s = str
  for i in range(n):
    s = add_stars(s)

  return s

message = add_many_stars("oh yeah", 10)

print(message)
