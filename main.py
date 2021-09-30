'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  '''
  Returneaza true daca n este prim si false daca nu este prim.
  :param n: n, ok, i
  :return: true sau false
  '''
  if n < 2:
    return False
  else:
    ok=True
    for i in range (2,n//2+1):
      if n%i == 0:
        ok=False
    if ok:
      return True
    else:
      return False
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  y=1
  x=len(lst)
  for i in range(x):
    y=lst[i]*y
  return y


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  r=x%y
  while r>0 :
    x=y
    y=r
    r=x%y
  return y




'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  while x!=y :
    if x>y :
      x=x-y
    else :
      y=y-x
  return x



def main():
  n = int(input("Dati numarul:"))
  print(is_prime(n))
  lst = [2, 5, 8, 2, 3, 9]
  print(get_product(lst))
  x=int(input("Dati primul numar:"))
  y=int(input("Dati al doilea numar:"))
  print(get_cmmdc_v1(x,y))
  print(get_cmmdc_v2(x,y))

if __name__ == '__main__':
  main()