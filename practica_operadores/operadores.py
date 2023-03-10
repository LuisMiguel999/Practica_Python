123 + 222
#345
1.5 * 4
#6.0
2 ** 100
#1267650600228229401496703205376
len(893)
#TypeError: object of type 'int' has no len()
len("893")
#3
len([2, 3, 4, 5])
#4
len(str(2 ** 1000000))
#ValueError: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
import math
#
Math.pi
#NameError: name 'Math' is not defined
math.sqrt(85)
#9.219544457292887
import random
#
random.random()
#0.7169103735766297
random.choice([1, 2, 3, 4])
#2
st = 'Spam'
#
len(st)
#4
st[0]
#'S'
st[-1]
#'m'
st[1:3]
#'pa'
st[1:]
#'pam'
st[:]
#'Spam'
st + "Hola"
#'SpamHola'
st * 5
#NameError: name 'st' is not defined
st[0] = 'z'
#TypeError: 'str' object does not support item assignment
# inmutabilidad los strings no cambian de valor como las # listas
st = 'z' + st[1:]
#
print(st)
#zpam
