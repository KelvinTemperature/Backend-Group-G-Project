#!/usr/bin/python3

import sqlite3


def create_table():
    try:
        sqliteConnection = sqlite3.connect('backend_student_info.db')
        sqlite_create_table_query = '''CREATE TABLE `student_information` (
                        `student_id` INTEGER PRIMARY KEY NOT NULL,
                        `first_name` varchar ( 128 ) NOT NULL,
                        `last_name` varchar ( 128 ) NOT NULL,
                        `phone` int ( 10 ) NOT NULL,
                        `email` varchar ( 255 ) NOT NULL);'''

        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("Table created")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating table", error)

    finally:
        if (sqliteConnection):
            sqliteConnection.close()
        print("sqlite connection is closed")
