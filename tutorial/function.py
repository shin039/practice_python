# coding:UTF-8

def hello(name):
  try:
    print("hello " + name)
  except:
    print("err")


hello("a")

def calc_add(a, b):
  return  a + b

print(calc_add(1, 2))

print(None == hello("b"))
  
