import numpy as np
import sqlite3
import pandas as pd

con = sqlite3.connect("project1.db")
cursor =con.cursor()


def total_expense():
      cursor.execute("SELECT SUM(amount) FROM expenses")
      data = cursor.fetchall()
      print(data)

def add_expense(date, time, category, amount, payment_method):
    cursor.execute("INSERT INTO expenses(date,time,category,amount,payment_method) VALUES (?,?,?,?,?)",(date,time,category,amount,payment_method))
    con.commit()
    print("Entered value has been updated !")

def total_expense_on(date):
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE date = ?", (date,))
    data = cursor.fetchall()
    print(data)
def category_expense(category):
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE category = ?", (category,))
    data = cursor.fetchall()
    print(data)
def payment_method_expense(payment_method):
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE payment_method = ?", (payment_method,))
    data = cursor.fetchall()
    print(data)
def get_expenses():
    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()
    print(data)

while True:
  try:
    choice = int(input("""
    Enter 1 to add an expense,
    2 to view all expenses,
    3 to view total expenses on a particular date,
    4 to view total expenses on a particular category,
    5 to view total expense,
    6 to view total expenses on a particular payment method: """))


    if choice == 1:
        date = input("Enter date(YYYY-MM-DD): ").lower().strip()
        time = input("Enter time(HH:MM): ").lower().strip()
        category = input("Enter category: ").capitalize().strip()
        amount = float(input("Enter amount: "))
        payment_method = input("Enter payment method: ").capitalize().strip()
        add_expense(date, time, category, amount, payment_method)

    if choice == 2:
        get_expenses()

    if choice == 3:
        date = input("Enter date(YYYY-MM-DD): ")
        total_expense_on(date)

    if choice == 4:
        category = input("Enter category: ").capitalize().strip()
        category_expense(category)

    if choice == 5:
        total_expense()


    if choice == 6:
        payment_method = input("Enter payment method: ").capitalize().strip()
        payment_method_expense(payment_method)

    Ask_user_to_continue = input("Do you want to continue?(yes/no)")

    if Ask_user_to_continue == "no":
          print("Thank you for using the application")
          break
  except:
       print("Please enter a valid input")