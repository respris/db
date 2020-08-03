import csv

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    employees = csv.reader(open("employees.csv", newline=''))

    c.execute("create table employees (firstname text, lastname text)")

    c.executemany("insert into employees (firstname, lastname) values (?,?)", employees)