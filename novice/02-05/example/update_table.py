import psycopg2

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
    sql_query = "SELECT * FROM book"

    cursor.execute(sql_query)
    # Execute and print the output
    print("Selected rows from book table")
    book_records = cursor.fetchall()

    print("Records of books in the table")
    for row in book_records:
        print("\nid = ", row[0])
        print("author = ", row[1])
        print("isbn  = ", row[2])
        print("title = ", row[3])
        print("date_published = ", row[4], "\n")

except (Exception, psycopg2.Error) as error:
    print("Error selecting data from table book", error)

# Close the connection to the PostgreSQL database
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is now closed")