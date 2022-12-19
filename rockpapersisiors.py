import random
def main():
    print(check_who_wins())


def check_who_wins():
    print('choose, rock paper or sisors: ')
    x = input('rock paper sisors shot ')
    x.strip()
    comp_choise = random_rps()
    while True:
        try:
            x == 'sisors' or x == 'rock' or x == 'paper'
            if x == 'sisors' and comp_choise == 'rock':
                return 'the computer chose rock the computer wins'
            elif x == 'sisors' and comp_choise == 'paper':
                return 'the computer chose paper you win'
            elif x == 'rock' and comp_choise == 'paper':
                return 'the computer chose paper the computer wins'
            elif x == 'rock' and comp_choise == 'sisors':
                return 'the computer chose sisors you win'
            elif x == 'paper' and comp_choise == 'sisors':
                return 'the computer chose sisors the computer wins'
            elif x == 'paper' and comp_choise == 'rock':
                return 'the computer chose rock you win'
            else:
                return "the comuter chose the same ,it's a tie"
        except ValueError:
            print('please chose; rock paper or sisors:')
            
       


def random_rps():
    options = ['rock','paper','sisors']
    random.shuffle(options)
    return(options[0])
   

main()
