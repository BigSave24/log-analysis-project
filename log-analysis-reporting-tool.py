#!/usr/bin/env python3
#
#   Project: Logs Analysis - Udacity
#
#   Questions the reporting tool will answer:
#   1. What are the most popular three articles of all time?
#   2. Who are the most popular article authors of all time?
#   3. On which days did more than 1% of requests lead to errors?
#
#
import psycopg2


def db_connect():
    # Connect to the database
    dbname = "news"

    try:
        db = psycopg2.connect(database=dbname)
        c = db.cursor()
    except:
        print("Database connection failed!")
    else:
        return c


def get_qOne(db_cursor):
# Query the database for answers to question 1
# Print and present information as a sorted list with the
# most popular article at the top.

        query1 = """
            select articles.title, count(*) as num
            from log join articles on (substring(path, 10) = articles.slug)
            where status = '200 OK'
            group by articles.title
            order by num desc limit 3;
        """

        Q1 = db_cursor.execute(query1)
        results = db_cursor.fetchall()

        print ("What are the three most popular articles of all-time?")
        print('')

        for result in results:
            article = result[0]
            views = result[1]
            print(article + ' - ' + str(views) + ' views')

        print('')
        return


def get_qTwo(db_cursor):
# Query the database for answers to question 2
# Print and present information as a sorted list with the
# most popular author at the top.

        query2 = """
            select authors.name, count(articles.title)
            from articles join authors on articles.author = authors.id
                  join log on articles.slug = substring(log.path, 10)
            where log.status = '200 OK'
            group by authors.name
            order by count(substring(log.path, 10)) desc;
        """

        Q2 = db_cursor.execute(query2)
        results = db_cursor.fetchall()

        print ("Who are the most popular articles authors of all-time?")
        print('')

        for result in results:
            author = result[0]
            views = result[1]
            print(author + ' - ' + str(views) + ' views')

        print('')
        return

def get_qThree(db_cursor):
# Query the database for answers to question 3
# Print and present information with full date of error occurances
# greater than 1%.

        query3 = """
        with requests as (
            select cast(time as date) as cal, count(*)
            from log
            group by cast(time as date) order by cast(time as date)),
        errors as (
            select cast(time as date) as cal, count(*)
            from log where status != '200 OK'
            group by cast(time as date)
            order by cast(time as date)),
        rate as (
            select requests.cal,
            (cast(errors.count as float) / cast(requests.count as float) * 100) as err_rate
            from requests, errors
            where requests.cal = errors.cal)
            select * from rate where err_rate > 1;
        """

        Q3 = db_cursor.execute(query3)
        results = db_cursor.fetchall()

        print ("On which days did more than 1% of requests lead to errors?")
        print('')

        for result in results:
            date = result[0]
            error = result[1]
            print(date.strftime('%a, %B %d, %Y') + ' - ' +
                str(round(error,1)) + '% errors')

        print('')
        return


if __name__ == '__main__':
    cursor = db_connect()
    if cursor:
        get_qOne(cursor)
        get_qTwo(cursor)
        get_qThree(cursor)
        cursor.close()
