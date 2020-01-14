#Author : Alexy Skoutnev
#Connection to Baby_Names SQL Server and inserts values from names.txt
#Date : 1/12/2020

import mysql.connector
import os

def Sql_Baby_Names_Insertion(list, passwords, database_name):
    cnx = mysql.connector.connect(user='root', password= passwords, host='127.0.0.1', database= database_name)
    mycursor = cnx.cursor()
    for x in list:
       sql = "Insert Into babynames (First_Name, Year_1900, Year_1910, Year_1920, Year_1930, Year_1940, Year_1950, Year_1960, Year_1970, Year_1980, Year_1990, Year_2000) Values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
       val = tuple(x)
       mycursor.execute(sql, val)
       cnx.commit()
    cnx.close()

def main():
    database_name = input("Enter the Database you want to enter: ")
    password = input("Enter the database password: ")
    try:
        cnx = mysql.connector.connect(user='root', password= password, host='127.0.0.1', database = database_name) #SQL Connection
        mycursor = cnx.cursor()
        list = []
        This_Folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(This_Folder, 'names.txt')
        file = open(my_file, "r")
        for line in file:
            list.append(line.strip().split())
        try:
            Sql_Baby_Names_Insertion(list, password, database_name)
        except:
            print("You have already inserted similar values")
            cnx.close()
    except:
        exit()
main()