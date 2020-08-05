import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()
    c.execute("select a.city, a.population, b.region from population a join regions b on a.city=b.city")
    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1], r[2])