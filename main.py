# pip install pyodbc
import pyodbc

# in my case i need to connect in a SQL Server database
DB_CONNECTIONSTRING = "Driver={SQL Server Native Client 11.0}; Server=SERVER_ADDRESS; " \
                      "Database=DATABSE_NAME; " \
                      "uid=USERNAME;" \
                      "pwd=PASSWORD;"


# example of an insert, the values variable is a list. values = [[1,'test'],[2,'test two']]
def insert_row(values):
    print('Inserting in database')
    conn = pyodbc.connect(DB_CONNECTIONSTRING)
    cursor = conn.cursor()
    cursor.fast_executemany = True
    try:
        # query with parameters: "insert into SOME_TABLE (column1, column2), values (?, ?)", values
        cursor.executemany(r"insert into SOME_TABLE (column1, column2), values (?, ?)", values)
        conn.commit()
    except Exception as e:
        print('An error has occurred trying to insert lines: ', e)
        conn.rollback()
    print('Insert finish')
    conn.close()


# example of a select
def select_file(name):
    print('Select SOMETHING from database')
    conn = pyodbc.connect(DB_CONNECTIONSTRING)
    cursor = conn.cursor()
    try:
        cursor.execute("select * from SOME_TABLES where COLUMN = (?)", name)
        # can use FETCHONE() or FETCHALL()
        row = cursor.fetchone()
        print('Select finish')
        conn.close()
        if row is None:
            print('nothing is founded')
        print('Row: ' + row)
        return False
    except Exception as e:
        print('An error has occurred trying to select: ', e)
        conn.close()

