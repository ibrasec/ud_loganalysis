#!/usr/bin/env python2
#
# This program is used to access the news database which consists of 3 tables
# 1. logs    2. authors   3.articles
#
# The program will answer the below questions
# 1. What are the most popular three articles of all time?
# Example:
#    "Princess Shellfish Marries Prince Handsome" -- 1201 views
#    "Baltimore Ravens Defeat Rhode Island Shoggoths" -- 915 views
#    "Political Scandal Ends In Political Scandal" -- 553 views
#
# 2. Who are the most popular article authors of all time?
# Example:
#    Ursula La Multa -- 2304 views
#    Rudolf von Treppenwitz -- 1985 views
#    Markoff Chaney -- 1723 views
#    Anonymous Contributor -- 1023 views
#
# 3. On which days did more than 1% of requests lead to errors?
# Example:
#    July 29, 2016 -- 2.5% errors

import psycopg2

# view_1,view_2 and view_3 are used to help us finding the second answer
view_1 = """
        CREATE VIEW view_1 AS
        SELECT substring(path,10) AS subtitle,
        count(*) AS num
        FROM log WHERE path <> '/'
        GROUP BY path ORDER BY num DESC LIMIT 8;
        """

view_2 = """
        CREATE VIEW view_2 AS
        SELECT articles.title, view_1.num
        FROM articles JOIN view_1 ON articles.slug = view_1.subtitle
        ORDER BY num DESC;
        """

view_3 = """
        CREATE VIEW view_3 AS
        SELECT author, sum(num)
        FROM (select articles.author , view_2.num
        FROM view_2 JOIN articles ON articles.title=view_2.title) AS FOO
        GROUP BY author ORDER BY sum desc;
        """

# view_4 and view_5 are used to help us finding the last answer
view_4 = """
        CREATE VIEW view_4 AS
        SELECT to_char(time,'YYYY-MM-DD') AS date,count(*) AS sum_nf
        FROM log WHERE status = '404 NOT FOUND'
        GROUP BY date ORDER BY date;
        """

view_5 = """
        CREATE VIEW view_5 AS
        SELECT to_char(time,'YYYY-MM-DD') AS date,count(*) AS sum_all
        FROM log GROUP BY date ORDER BY date;
        """


# Answering what are the most popular three articles of all time


def most_popular_three_articles():
    print("finding the most popular three articals of all time...")
    con = psycopg2.connect("dbname = news")
    cur = con.cursor()
    try:
        cur.execute(view_1)
    except Exception as e:
        pass
    cur.execute("""SELECT articles.title, view_1.num
             FROM articles JOIN view_1 ON articles.slug = view_1.subtitle
             ORDER BY num DESC LIMIT 3""")
    response = cur.fetchall()
    con.close()
    for i, j in response:
        print("{} __ {} views".format(i, j))

# Answering who are the most popular article authors of all time


def most_popular_authors():
    print("finding the most popular article authors of all time...")
    con = psycopg2.connect("dbname = news")
    cur = con.cursor()
    try:
        cur.execute(view_1)
        cur.execute(view_2)
        cur.execute(view_3)
    except Exception as e:
        pass
    cur.execute("""SELECT name,view_3.sum
                 FROM authors JOIN view_3 ON authors.id = view_3.author
                 ORDER BY sum DESC;""")
    response = cur.fetchall()
    con.close()
    for i, j in response:
        print("{} __ {} views".format(i.ljust(22), j))

# Answering on which days did more than 1% of requests lead to errors


def days_above_apercent_error():
    print("finding On which days more than 1% of requests lead to errors...")
    con = psycopg2.connect("dbname = news")
    cur = con.cursor()
    try:
        cur.execute(view_4)
        cur.execute(view_5)
    except Exception as e:
        pass
    cur.execute("""SELECT date,jumla
                FROM (SELECT view_4.date,
                round( (view_4.sum_nf*100.0) / view_5.sum_all, 2) AS jumla
                FROM view_4 join view_5 on view_4.date = view_5.date
                ORDER BY jumla desc) AS final
                WHERE jumla > 1.00;""")
    response = cur.fetchall()
    con.close()
    for i, j in response:
        print("{} __ {}% errors".format(i, j))


if __name__ == '__main__':
    most_popular_three_articles()
    print("")
    most_popular_authors()
    print("")
    days_above_apercent_error()
