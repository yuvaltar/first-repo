from random import shuffle
def main():
    users_n = int(input('what is the missing n? (1-10) '))
    list_y = list_w_10_r_numbers()
    # print(list_y)
    missing_n = list_y.pop(9)
    # print(list_y)
    if list_y.count(users_n) == 1:
        print(f'missing n is: {missing_n} your guess is wrong')
    else:
        print(f'missing n is: {missing_n} your guess is right')


def list_w_10_r_numbers():
    list_y = [1,2,3,4,5,6,7,8,9,10]
    shuffle(list_y)
    return list_y
# print(list_w_10_r_numbers())
# print('helo')
main()






