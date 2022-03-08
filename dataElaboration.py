from flask import request
from datetime import date
import csv
expenses = []
transactions = []
lista = []


def openData():
    with open('expensesData.csv') as data_file:
        data = csv.reader(data_file)
        for row in data:
            expenses.append(row)
    expenses.pop(0)


def retrieveData():
    with open('expensesData.csv', 'a', newline='') as data_file:
        txt_writer = csv.writer(data_file)
        if request.method == 'POST':
            today = date.today()
            transactions.append(date.isoformat(today))
            transactions.append(request.form.get('category'))
            transactions.append(request.form.get('cost'))
            txt_writer.writerow(transactions)
            transactions.clear()
            expenses.clear()
            openData()


def costGrocery():
    grocery = 0
    for value in expenses:
        if value[1] == 'grocery':
            grocery += int(value[2])
    return(grocery)


def costEntertainment():
    entertainment = 0
    for value in expenses:
        if value[1] == 'entertainment':
            entertainment += int(value[2])
    lista.append(entertainment)
    return(entertainment)


def costShopping():
    shopping = 0
    for value in expenses:
        if value[1] == 'shopping':
            shopping += int(value[2])
    return(shopping)


def costHealth():
    health = 0
    for value in expenses:
        if value[1] == 'health':
            health += int(value[2])
    return(health)


def costTransport():
    transport = 0
    for value in expenses:
        if value[1] == 'transport':
            transport += int(value[2])
    return(transport)


def costHome():
    home = 0
    for value in expenses:
        if value[1] == 'home':
            home += int(value[2])
    return(home)


def spent():
    money = costHome() + costEntertainment() + costGrocery() + \
        costHealth() + costShopping() + costTransport()
    return(money)
