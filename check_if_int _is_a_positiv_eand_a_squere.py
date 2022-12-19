import math

def check_if_power_of_2():
    print('check if the number is a positive number by the power of 2')
    while True:
        try:
            x = float(input('plese write your number '))
            if x == 0:
                print('please write a positive number')
            else:
                y = math.sqrt(x)
                z = round(y)
                if (y%z == 0):
                    print(str(x) + 'is a positive integer is a power of two')
                    break
                else:
                    print(f'{x} is not a positive integer is a power of two')
                    break
        except ValueError:
            print('please write a positive number')

check_if_power_of_2()
#checks if number is 2 by the power of somthing
def is_perfect_square(n):
    x = n // 2
    y = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y: return False
        y.add(x)
    return True
n = int(input('number'))
print(is_perfect_square(n))
def check_if_squere(n):
    while n > 0:
       x = (math.sqrt(n))
       if n == x * x:
          return n == x*x
       return n == x*x
n = float(input('number: '))
print(check_if_squere((n)))

        


