import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()
    c.execute("""create table regions (city text, region text)""")

    cities = [
        ('New York City', 'Northeast'),
        ('San Francisco', 'West'),
        ('Chicago', 'Midwest'),
        ('Houston', 'South'),
        ('Phoenix', 'West'),
        ('Boston', 'Northeast'),
        ('Los Angeles', 'West'),
        ('Houston', 'South'),
        ('Philadelphia', 'Northeast'),
        ('San Antonio', 'South'),
        ('San Diego', 'West'),
        ('Dallas', 'South'),
        ('San Jose', 'West'),
        ('Jacksonville', 'South'),
        ('Indianapolis', 'Midwest'),
        ('Austin', 'South'),
        ('Detroit', 'Midwest')
    ]

    c.executemany("insert into regions values (?,?)", cities)
    c.execute("select * from regions")
    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1])