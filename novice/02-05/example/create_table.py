# Import the Python driver for PostgreSQL
import psycopg2

# Import the SQL library from the adapter
from psycopg2 import sql, extensions

# Connect to PostgreSQL
connection = psycopg2.connect(
    user = "postgres",
    password = "passwd",
    host = "localhost",
    port = "5432",
    database = "db_praxs"
)

autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT

connection.set_isolation_level(autocommit)

# Instantiate a cursor object from the connection
cursor = connection.cursor()

table_name = "book"

# Concatenate SQL string
create_table = "CREATE TABLE {} (id INTEGER PRIMARY KEY, author VARCHAR(128), "
create_table += "isbn VARCHAR(128), title VARCHAR(128), date_published DATE);"

# use the sql module instead to avoid SQL injection attacks
cursor.execute(sql.SQL(
    create_table
).format(sql.Identifier( table_name )))
