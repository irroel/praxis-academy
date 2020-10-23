import psycopg2

def update_table(bookid, title):
    # create a connection credentials to the Postgresql database
    try:
        connection = psycopg2.connect(
            user = 'postgres',
            password = 'passwd',
            host = 'localhost',
            port = '5432',
            database = 'db_praxs'
        )
        # Create a connection instance for the PostgreSQL and fetch data from the table
        cursor = connection.cursor()

        print("Book table before updating")
        sql_select = """SELECT * FROM book WHERE id = %s"""
        cursor.execute(sql_select, (bookid, ))
        book_record = cursor.fetchone()
        print(book_record)

        # update the row from book
        sql_update = """UPDATE book SET title = %s WHERE id = %s"""
        cursor.execute(sql_update, (title, bookid))
        connection.commit()
        count = cursor.rowcount
        print(count, "Successfully Updated!")

        print("Book table after updating")
        sql_select = """SELECT * FROM book WHERE id = %s"""

        # execute the above SQL string
        cursor.execute(sql_select, (bookid,))
        book_record = cursor.fetchone()
        print(book_record)    

    except (Exception, psycopg2.Error) as error:
        print("Error sin updating the data: ", error)
        connection = None

    # Close the connection to the PostgreSQL database
    finally:
        if (connection)!= None:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")

if __name__ == "__main__":
    _id = 1
    title = 'Tutorials in FrontEnd Developers'

    # call psycopg2 function to execute SQL
    update_table(1, 'How to become professional programmer')