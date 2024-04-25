#!/usr/bin/python3

import sqlite3


def read_table():
    try:
        sqliteConnection = sqlite3.connect('backend_student_info.db')
        cursor = sqliteConnection.cursor()
        print("----------------------------------------------")
        print("| Connected to backend_student_info database |")
        print("----------------------------------------------")
        
        sqlite_select_query = """SELECT * from student_information"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("      {} Total Rows: Printing Each Row".format(len(records)))
        print("----------------------------------------------")

        for row in records:
            print("student_id: ", row[0])
            print("first_name: ", row[1])
            print("last_name: ", row[2])
            print("phone: ", row[3])
            print("email: ", row[4])
            print("----------------------------------------------")
        
        cursor.close()
    
    except sqlite3.Error as error:
        print("Failed to read data from backend_student_info database", error)
    
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
        print("|     The database connection is closed      |")
        print("----------------------------------------------")
