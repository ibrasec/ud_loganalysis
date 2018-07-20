#!/usr/bin/env python2
#
# This program is used to access the news database which consists of 3 tables
# 1. logs    2. authors   3.articles
#
# please make sure to read the README file to add the essential views

import psycopg2
import sys


def try_connect(db='news'):
    """
    Try to connect to the passed database name,
    The returned value is a psycipg2.connect value
    if the database is unreacable or it is not created
    an Error message will be printed out and the program
    will exit.

    try_connect(news) -> psycopg2.extensions.connection
    """
    try:
        return psycopg2.connect("dbname="+db)
    except psycopg2.Error as e:
        print "Unable to connect to database", db
        sys.exit(1)


# Answering what are the most popular three articles of all time


def most_popular_three_articles(dbconnect):
    """
    Answers What are the most popular three articles of all time?
    Example:
     Princess Shellfish Marries Prince Handsome" -- 1201 views
     Baltimore Ravens Defeat Rhode Island Shoggoths" -- 915 views
     Political Scandal Ends In Political Scandal" -- 553 views
    """
    print("finding the most popular three articals of all time...")
    cur = dbconnect.cursor()
    cur.execute("""SELECT articles.title, AccessAllArticles.num
                FROM articles JOIN AccessAllArticles
                ON articles.slug = AccessAllArticles.subtitle
                ORDER BY num DESC LIMIT 3""")
    response = cur.fetchall()
    for article, views in response:
        print("{} __ {} views".format(article, views))

# Answering who are the most popular article authors of all time


def most_popular_authors(dbconnect):
    """
    Answers Who are the most popular article authors of all time?

    Example:
     Ursula La Multa -- 2304 views
     Rudolf von Treppenwitz -- 1985 views
     Markoff Chaney -- 1723 views
     Anonymous Contributor -- 1023 views
    """
    print("finding the most popular article authors of all time...")
    cur = dbconnect.cursor()
    cur.execute("""SELECT name,AuthorsViewSummary.sum
                 FROM authors JOIN AuthorsViewSummary
                 ON authors.id = AuthorsViewSummary.author
                 ORDER BY sum DESC;""")
    response = cur.fetchall()
    for author, views in response:
        print("{} __ {} views".format(author.ljust(22), views))

# Answering on which days did more than 1% of requests lead to errors


def days_above_apercent_error(dbconnect):
    """
    Answers On which days did more than 1% of requests lead to errors?

    Example:
    July 29, 2016 -- 2.5% errors
    """
    print("finding On which days more than 1% of requests lead to errors...")
    cur = dbconnect.cursor()
    cur.execute("""SELECT date,jumla
                FROM (SELECT NotFoundStatusHistory.date,
                round(
                (NotFoundStatusHistory.sum_nf*100.0)/AllstatusHistory.sum_all,2
                ) AS jumla FROM NotFoundStatusHistory JOIN AllstatusHistory
                ON NotFoundStatusHistory.date = AllstatusHistory.date
                ORDER BY jumla desc) AS final
                WHERE jumla > 1.00;""")
    response = cur.fetchall()
    for date, percentage in response:
        print("{} __ {}% errors".format(date, percentage))


if __name__ == '__main__':
    con = try_connect('news')
    most_popular_three_articles(con)
    print("")
    most_popular_authors(con)
    print("")
    days_above_apercent_error(con)
    con.close()
