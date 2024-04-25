#!/usr/bin/python3
import sqlite3


def delete_student_details(student_id):
    try:
        sqliteConnection = sqlite3.connect('backend_student_info.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_delete_query = """DELETE from student_information where student_id = ?"""
        cursor.execute(sql_delete_query, (student_id, ))
        sqliteConnection.commit()
        print("Student details deleted successfully")
        cursor.close()
    
    except sqlite3.Error as error:
        print("Failed to delete student details from table", error)
    
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
        print("sqlite connection is closed")
