from random import randint
def get_numbers_ticket(min_num:int,  max_num: int, quantity: int):
    if min_num >=1 and max_num<=1000 and min_num<max_num and 0<quantity<=(max_num-min_num):
        win_numbers = set()
        while len(win_numbers)< quantity:
            number = randint(min_num, max_num)
            win_numbers.add(number)
        return list(win_numbers)
    else:
        print ("Некорректний формат введення")
        return []
                
min_value=1
max_value=1000
quantity_win_numbers=10

result=get_numbers_ticket(min_value, max_value, quantity_win_numbers)
print (result)