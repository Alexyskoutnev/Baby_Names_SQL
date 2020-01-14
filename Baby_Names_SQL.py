#  File: Baby_Names_SQL.py
#  Description:  Utilizes SQL Server to analyze baby names data set
#  Author:  Alexy Skoutnev

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
    while (True):
        result = eval(input("1: Input file into SQl Server (names.txt)  \n2: Run Program \n3: Exit "))
        if (result == 1):
            print("Database Input, type exit to quit")
            database_name = input("Enter the Database you want to enter: ")
            if (database_name == "exit"):
                continue
            password = input("Enter the database password: ")
            try:
                cnx = mysql.connector.connect(user='root', password=password, host='127.0.0.1', database=database_name)  # SQL Connection
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
                print("Not Valid")
                pass
        elif (result == 2):
            print("Please connect to the SQL Server")
            database_name = input("Enter the database you want to enter: ")
            pass_word = input("Enter the password to that database: ")
            cnx = mysql.connector.connect(user='root', password= pass_word, host='127.0.0.1', database= database_name) #database connection
            print("Options: \n Enter 1 to search for names. \n Enter 2 to display data for one name. \n Enter 3 to display all names that appear in only one decade. \n Enter 4 to display all names that appear in all decades. \n Enter 5 to display all names that are more popular in every decade. \n Enter 6 to display all names that are less popular in every decade. \n Enter 7 to quit.")
            print()
            choice = eval(input("Enter choice "))
            decadedlist = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000]
            while (True):   #this is the while loop that the menu cycles through
                try:
                    if (choice == 1):   #finds a name
                        arrayname = []
                        name = str(input("Please input name "))
                        index = 0
                        mycursor = cnx.cursor()
                        try:
                            mycursor.execute("select * from baby_names.babynames First_name where First_name = \"" + name + "\"")
                            myresult = mycursor.fetchone()
                            for x in myresult:
                                arrayname.append(x)
                            number_list = arrayname[1:]
                            number_list = [int(i) for i in number_list]
                            index = number_list.index(min(number_list))
                            print("The matches with their highest ranking decade are: ")
                            print(str(arrayname[0]) + " " + str(decadedlist[index]) + "\n")
                            cnx.close()
                        except:
                            print("Error in finding the name ")
                    elif (choice == 2):
                        arrayname = []
                        name = str(input("Please input name: "))
                        mycursor = cnx.cursor()
                        try:
                            mycursor.execute("select * from baby_names.babynames First_name where First_name = \"" + name + "\"")
                            myresult = mycursor.fetchone()
                            for x in myresult:
                                arrayname.append(str(x))
                            number_list = arrayname[1:]
                            number_list = [int(i) for i in number_list]
                            print(str(name) + ": " + str(" ".join(arrayname[1:])))
                            for i in range(len(number_list)):  # displays the decade and name
                                print(str(decadedlist[i]) + ": " + str(number_list[i]))
                            cnx.close()
                        except:
                            print("Error in finding the name ")
                    elif (choice == 3):
                        try:
                            mycursor = cnx.cursor()
                            decade = input("Enter Decade: ")
                            index = decadedlist.index(int(decade))
                            list_of_columns = ["Year_1900", "Year_1910", "Year_1920", "Year_1930", "Year_1940", "Year_1950", "Year_1960", "Year_1970", "Year_1980", "Year_1990", "Year_2000"]
                            Year = list_of_columns[index]
                            print("The names are in order of rank:")
                            sql = "select First_name, "+ Year  +" from baby_names.babynames where " + Year + " != 0 order by " + Year
                            mycursor.execute(sql)
                            sql_result = mycursor.fetchall()
                            for name in sql_result:
                                print(str(name[0]) + ": " + str(name[1]))
                            print()
                            cnx.close()
                        except:
                            print("Error in finding names in Decade")
                    elif (choice == 4):
                        try:
                            mycursor = cnx.cursor()
                            list_of_columns = ["Year_1900", "Year_1910", "Year_1920", "Year_1930", "Year_1940", "Year_1950", "Year_1960", "Year_1970", "Year_1980", "Year_1990", "Year_2000"]
                            sql = "select First_name from baby_names.babynames where (Year_1900 != 0 and Year_1910 != 0 and Year_1920 != 0 and Year_1930 != 0 and Year_1940 != 0 and Year_1950 != 0 and Year_1960 != 0 and Year_1970 != 0 and Year_1980 != 0 and Year_1990 != 0 and Year_2000 != 0) order by First_name"
                            mycursor.execute(sql)
                            sql_result = mycursor.fetchall()
                            print(sql_result)
                            for name in sql_result:
                                print(name[0])
                            cnx.close()
                        except:
                            print("Error in finding names in Decade")
                    elif (choice == 5):
                        try:
                            mycursor = cnx.cursor()
                            sql = "select First_name from baby_names.babynames where Year_1900 > Year_1910 and Year_1910 > Year_1920 and Year_1920 > Year_1930 and Year_1930 > Year_1940 and Year_1940 > Year_1950 and Year_1950 > Year_1960 and Year_1960 > Year_1970 and Year_1970 > Year_1980 and Year_1980 > Year_1990 and Year_1990 > Year_2000 order by First_name"
                            mycursor.execute(sql)
                            sql_result = mycursor.fetchall()
                            print(str(len(sql_result)) + " names are more popular in every decade.")
                            for name in sql_result:
                                print(name[0])
                            cnx.close()
                        except:
                            print("Error in finding most popular increasing name")
                    elif (choice == 6):
                        try:
                            mycursor = cnx.cursor()
                            sql = "select First_name from baby_names.babynames where Year_1900 < Year_1910 and Year_1910 < Year_1920  and Year_1920 < Year_1930 and Year_1930 < Year_1940 and Year_1940 < Year_1950 and Year_1950 < Year_1960 and Year_1960 < Year_1970 and Year_1970 < Year_1980 and Year_1980 < Year_1990 and (Year_1990 < Year_2000 or Year_2000 = 0) order by First_name"
                            mycursor.execute(sql)
                            sql_result = mycursor.fetchall()
                            print(str(len(sql_result)) + " names are less popular in every decade.")
                            for name in sql_result:
                                print(name[0])
                            cnx.close()
                        except:
                            print("Error in finding most popular decreasing name")
                    elif (choice == 7):
                        print()
                        print("Goodbye.")
                        exit()
                    print("Options: \n Enter 1 to search for names. \n Enter 2 to display data for one name. \n Enter 3 to display all names that appear in only one decade. \n Enter 4 to display all names that appear in all decades. \n Enter 5 to display all names that are more popular in every decade. \n Enter 6 to display all names that are less popular in every decade. \n Enter 7 to quit.")
                    print()
                    choice = eval(input("Enter choice "))
                except (RuntimeError, TypeError, NameError):
                    print("Redo your input")
            cnx.close()
        elif (result != 2 or result != 3):
            exit()
main()