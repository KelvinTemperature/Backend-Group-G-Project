#!/usr/bin/python3

import sqlite3


def insert_student_details(student_id, first_name, last_name, phone, email):
    try:
        sqliteConnection = sqlite3.connect('backend_student_info.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_with_param = """insert into student_information
                                    (student_id,first_name,last_name,
                                    phone,email)values(?,?,?,?,?);"""

        data_tuple = (student_id, first_name, last_name, phone, email)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Student details inserted successfully into\
                student_information table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert student details into\
                student_information table", error)

    finally:
        if (sqliteConnection):
            sqliteConnection.close()
        print("The SQLite connection is closed")
