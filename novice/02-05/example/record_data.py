# import the python driver for postgresql
from re import error
import psycopg2
from psycopg2 import connect

# create a connection credentials to the Postgresql database
try:
    connection = psycopg2.connect(
        user = 'postgres',
        password = 'passwd',
        host = 'localhost',
        port = '5432',
        database = 'db_praxs'
    )

    cursor = connection.cursor()

    # get the column name of a table inside the database and put some values
    sql_query = """ INSERT INTO book (id, author, isbn, title, date_published)
                    VALUES (%s,%s, %s, %s, %s) """
    value = (
        1, # record ID
        'Layla Nowitzki',
        '789-1-46-268414-1',
        'How to become a professional programmer',
        'January 25 2011'
    )

    # execute the above SQL String
    cursor.execute(sql_query, value)

    # commit transaction and prints the result succesfully
    connection.commit()

    count = cursor.rowcount
    print('Succesfully inserted', count, 'records.')

except (Exception, psycopg2.Error) as error:
    print('Error connecting to PostgreSQL Database', error)
    connection = None

finally:
    # close the connection to the PostgreSQL Database
    if connection != None:
        cursor.close()
        connection.close()
        print('The PostgreSQL connection is now closed')