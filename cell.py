inport random
def inpos(x):
  def pos():
    lis = ["x         ", " x        ", "  x       ", "   x      ", "     x    ", "     x    ", "      x   ", "       x  ", "        x ", "         x"]
    ranpos = random.choice(lis)
    print(ranpos)
  pos(x)
def cellmake(x, y, z, e, o):
  cell = x
  pos1 = y
  pos2 = z
  type = e
  name = o
  i = inpos(cell)
  print(i, name, type)
