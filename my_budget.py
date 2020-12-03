import datetime
from os import path

def details():
    salary = input('Please enter your monthly salary (in rands): R  ')
    payday = input('What day of the month do you get your salary: ')
    budget = input('what is your spending budget for this month (in rands): R ')
    savings = input('how much are you saving from your salary this month (in rands): R ')

    with open('money.txt','w') as my_data:
        
        my_data.write(salary)
        my_data.write('\n')
        my_data.write(payday)
        my_data.write('\n')
        my_data.write(budget)
        my_data.write('\n')
        my_data.write(savings)
    print('Details entered!!')
   

def fetch_details():
    my_labels = ['salary','payday','budget','savings']
    my_vals = []
    with open('money.txt','r') as my_data:
        my_money = my_data.readlines()
        for i in my_money:
            my_vals.append(int(i))
        # print(my_vals)
        my_info = dict(zip(my_labels,my_vals))
        return my_info



# savings = 0

x = datetime.datetime.now()
day_ = int(x.strftime("%d"))

my_information = fetch_details()
for k,v in my_information.items():
    if k == 'payday':
        payday = v

days_left_to_payday = payday - day_


if days_left_to_payday <= 4 and days_left_to_payday > 0:
    a = input('would you like to add your monthly budget and savings today? (y/n) ')
    if a.lower() == 'y':
        fetch_details()
    else:
        print('okay, let me know when you want to')
    print('I hope you are sticking to the budget this month')




