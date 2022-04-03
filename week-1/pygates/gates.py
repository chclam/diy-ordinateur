def nand(a, b):
  return not (a and b)

def not_(a):
  return nand(a, a)

def and_(a, b):
  return nand(nand(a, b), nand(a, b))

def or_(a, b):
  return nand(nand(a, a), nand(b, b))

def xor(a, b):
  return and_(or_(a, b), nand(a, b))

def mux(a, b, sel):
  return or_(and_(not_(sel), a), and_(sel, b))

def dmux(a, sel):
  return and_(not_(sel), a), and_(sel, a)

def not16(a):
  assert(len(a) == 16)
  return [not_(a[i]) for i in range(len(a))]

def and16(a, b):
  assert(len(a) == 16 and len(b) == 16)
  return [and_(a[i], b[i]) for i in range(len(a))]

def or16(a, b):
  assert(len(a) == 16 and len(b) == 16)
  return [or_(a[i], b[i]) for i in range(len(a))]

def mux16(a, b, sel):
  assert(len(a) == 16 and len(b) == 16)
  return [mux(a[i], b[i], sel) for i in range(len(a))]

def or8way(a):
  assert(len(a) == 8)
  ret = 0
  for i in range(len(a)):
    ret = or_(ret, a[i])
  return ret

def and8way(a):
  assert(len(a) == 8)
  ret = 1
  for i in range(len(a)):
    ret = and_(ret, a[i])
  return ret
  
def half_adder(a, b):
  carry = and_(a, b)
  sum_ = xor(a, b)
  return carry, sum_

def full_adder(a, b, c):
  carry = or_(and_(c, or_(a, b)), and_(and_(a, b), not_(c)))
  sum_ = or_(and_(xor(a, b), not_(c)), and_(c, not_(xor(a, b))))
  return carry, sum_

