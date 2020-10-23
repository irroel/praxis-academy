import psycopg2

def get_connection():
    # connect to the PostgreSQL server
    conn = psycopg2.connect(
        user = 'postgres',
        password = 'passwd',
        host = '127.0.0.1',
        port = '5432',
        database = 'db_praxs')
    
    return conn

def close_connection(conn):
    if conn:
        conn.close()
        print("Postgres connection is closed !!!")

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands_table3 = (
         """ CREATE TABLE TABLE3 (
            SALUTATION_ID INT NOT NULL PRIMARY KEY,
            SALUTATION VARCHAR(4)
            )
        """)
    commands_table1 = (
        """ CREATE TABLE TABLE1 (
            MEMBERSHIP_ID SERIAL PRIMARY KEY,
            FULL_NAME VARCHAR(12) NOT NULL,
            PHYSICAL_ADDRESS TEXT NOT NULL,
            SALUTATION_ID VARCHAR(4) NOT NULL,
            CONSTRAINT fk_table2
                FOREIGN KEY(SALUTATION_ID)
                REFERENCES TABLE3(SALUTATION_ID)
            )        
        """)
    commands_table2 = (
        """ CREATE TABLE TABLE2 (
            MEMBERSHIP_ID INT NOT NULL,
            MOVIES_RENTED VARCHAR(25) NOT NULL,
            CONSTRAINT fk_table1
                FOREIGN KEY(MEMBERSHIP_ID)
                REFERENCES TABLE1(MEMBERSHIP_ID)                        
            )
        """)
    conn = get_connection()
    try:
        cursor = conn.cursor()
        # drop table if exist
        cursor.execute("DROP TABLE IF EXISTS TABLE1")
        cursor.execute("DROP TABLE IF EXISTS TABLE2")
        cursor.execute("DROP TABLE IF EXISTS TABLE3")
        # create table
        cursor.execute(commands_table3)
        cursor.execute(commands_table1)
        cursor.execute(commands_table2)
        print('Create tables successfully ............')
        # commit the changes
        conn.commit()
        # close communication with the PostgreSQL database server
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        close_connection(conn)

def insert_data(data1, data2, data3):
    conn = get_connection()
    query_table1 = """INSERT INTO TABLE1 (MEMBERSHIP_ID, FULL_NAME, PHYSICAL_ADDRESS, SALUTATION_ID) VALUES (%s, %s, %s, %s)"""
    query_table2 = """INSERT INTO TABLE2 (MEMBERSHIP_ID, MOVIES_RENTED) VALUES (%s,%s)"""
    query_table3 = """INSERT INTO TABLE3 (SALUTATION_ID, SALUTATION) VALUES (%s, %s)"""

    cursor = conn.cursor()
    cursor.executemany(query_table3, data3)
    cursor.executemany(query_table1, data1)
    cursor.executemany(query_table2, data3)

    conn.commit()
    cursor.close()    

if __name__ == '__main__':
    get_connection()
    create_tables()
    insert_data(
        [
            (1, "Janet Jones", "First Street Plot No 4", 2),
            (2, "Robert Phil", "3rd Street 34", 1),
            (3,"Robert Phil", "5th Avenue", 1)
        ],
        [
            (1, 'Pirates of the carribean'),
            (1, 'Class of the titans'),
            (2, 'Forgetting sarah marshal'),
            (2, "Daddy's little girls"),
            (3, 'Clash of the titans'),
        ],
        [
            (1, 'Mr.'),
            (2, 'Ms.'),
            (3, 'Mrs.'),
            (4, 'Dr')
        ]
    )