import openpyxl
from os import path
import datetime
from my_budget import fetch_details

#load existing workbook or create new workbook if it does not exist
def load_my_workbook(w_path):
    if path.exists(w_path):
        return openpyxl.load_workbook(w_path)
    return openpyxl.Workbook()


my_path = 'expenses.xlsx'
wb = load_my_workbook(my_path)
sheet = wb['Detailed_Expenses'] 

#enter new data into sheet
def enter_expense(sheet):
    d = datetime.datetime.now()
    my_date = d.strftime("%d/%m/%Y %H:%M")

    expense_desc = input('what did you spend the money on: ')

    amount = float(input('how much total did you spend in rands: R'))

    sheet.append((my_date,expense_desc,amount))

    wb.save(my_path)

    return sheet

#fetch data from money.txt through my_budget.py
my_information = fetch_details()
for k,v in my_information.items():
    if k == 'budget':
        my_exp_budget = v

#fetch data from expenses.xlsx and add the toatal expenses
my_total = 0
my_amount = sheet['c']
for i in my_amount[1:]:
    v = i.value
    my_total += v

#inform user of the current state of budget
def budget_left(total,budget):
    return f'You have a budget of R{float(budget)}, the total amount spent is R{float(my_total)}. You only have R{float(budget - my_total)} left for spending this month'


print(budget_left(my_total,my_exp_budget))

