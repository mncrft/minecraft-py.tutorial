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
  for i in range(hight):
    blocks = blocks + area(x, y+i, z, hight - i - 1, block_type)

  return blocks

print(len(pyramid(10, 0, 100, 3, 0)))
# pyramid(10, 0, 100, 3, 0)
