import sqlite3

database_file = "static/web-site.db"

def create_db():
    # All your initialization code
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # Create and populate your database tables. Here's an example to get you started.
    cursor.execute("drop table if exists table1")
    cursor.execute("create table if not exists table1("+
                   "column1 text primary key not null" +
                   ", column2 text not null" +
                   ", column3 int not null default 0)")
    cursor.execute("insert or ignore into table1 values ('value1', 'value2', 123)")

    cursor.execute("drop table if exists events")
    cursor.execute("create table if not exists events("+
                   "description text primary key not null" +
                   ", date text not null" +
                   ", credits int not null default 0)")
    cursor.execute("insert or ignore into events values ('Give presentation to the rest of the club on a CS topic', '11/2/2017', 2)")

    cursor.execute("insert or ignore into events values ('Give presentation to the rest of the Club on a CS topic', '11/9/2017', 3)")

    # Save (commit) the changes
    connection.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    connection.close()


def read_table1(column1_value):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # Retrieve a record from table1 whose column1 value matches the value passed to this function
    cursor.execute("select * from table where column='%s'" % (column1_value))
    row = cursor.fetchone()

    connection.close()

    return row[0]


def update_table1(column1_value, column2_new_value):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # Update the column2 value in table1 whose column1 value matches the value passed to this function
    cursor.execute("UPDATE table1 SET colum2='%s' WHERE column1='%s'" % (column2_new_value, column1_value))

    connection.close()

def list_events():
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # Retrieve all the events
    cursor.execute("SELECT * FROM events")
    rows = cursor.fetchall()

    print (rows)

    connection.close()

    return rows
