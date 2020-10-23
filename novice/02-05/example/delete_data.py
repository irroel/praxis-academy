import psycopg2

def delete_data(bookid):
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

        print("Book table before deleting")
        sql_select = """SELECT * FROM book WHERE id = %s"""
        cursor.execute(sql_select, (bookid, ))
        book_record = cursor.fetchone()
        print(book_record)

        # delete the data form table book
        sql_delete = "DELETE FROM book WHERE id = {}".format(bookid)
        cursor.execute(sql_delete)
        connection.commit()
        count = cursor.rowcount
        print(count, "Successfully deleted!", count, ' rows.')

        print("Book table after deleting data")
        sql_select = """SELECT * FROM book WHERE id = %s"""

        # execute the above SQL string
        cursor.execute(sql_select, (bookid,))
        book_record = cursor.fetchone()
        print(book_record)    

    except (Exception, psycopg2.Error) as error:
        print("Error in Deleting the data: ", error)
        connection = None

    # Close the connection to the PostgreSQL database
    finally:
        if (connection)!= None:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")

if __name__ == "__main__":
    bookid = 1
    # call psycopg2 function to execute SQL
    delete_data(bookid)