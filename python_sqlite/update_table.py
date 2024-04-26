#!/usr/bin/python3

import sqlite3


def update_student_phone(student_id, phone):
    try:
        sqliteConnection = sqlite3.connect('backend_student_info.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update student_information set
                            phone = ? where student_id = ?"""
        data = (phone, student_id)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Student details Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update student details", error)

    finally:
        if (sqliteConnection):
            sqliteConnection.close()
        print("The sqlite connection is closed")


def update_student_email(student_id, email):
    try:
        sqliteConnection = sqlite3.connect('backend_student_info.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update student_information set
                            email = ? where student_id = ?"""
        data = (email, student_id)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Student details Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update student details", error)

    finally:
        if (sqliteConnection):
            sqliteConnection.close()
        print("The sqlite connection is closed")
