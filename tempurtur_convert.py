#converts c to f
print('what would you like to convert c to f, or f to c? ')
while True:
    try:
        x = int(input('write 1 for option 1, and 2 for option 2: '))
        if x == 1:
            while True:
                try:
                    c = float(input('what c would you like to convert: '))
                    f = c * (9/5) + 32
                    print(round(f,2))
                    
                except ValueError:
                    print('please write a number for c')
            
        elif x == 2:
            while True:
                try:
                    f = float(input('what f would you like to convert: '))
                    c = 5/9 * (f-32)
                    print(round(c,2))
                    
                except ValueError:
                    print('please write a number for f')
            
    except ValueError:
        print('plese select 1 or 2')


#def main():
   


    def calculation(x):
        while True:
            try:
                if x == 1:
                    while True:
                        try:
                            c = float(input('what c would you like to convert: '))
                            f = c * (9/5) + 32
                            return round(f,2)
                        except ValueError:
                            print('please write a number for c')
                elif x == 2:
                    while True:
                        try:
                            f = float(input('what f would you like to convert: '))
                            c = 5/9 * (f-32)
                            return round(c,2)
                        except ValueError:
                            print('please write a number for f')
                            
            except ValueError:
                print('plese select 1 or 2')


    def conversion_type():
        print('what would you like to convert c to f, or f to c? ')
        x = int(input('write 1 for option 1, and 2 for option 2: '))
    
 

 



