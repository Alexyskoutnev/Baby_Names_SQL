# Baby_Names_SQL
Utilizes SQL Server and Python to analyze a baby names data set.

============================= Initialization (Step 1) ==================================
1. The data set is a text file (names.txt), have the file in the working dictionary.
2. Python code was tested in MySQL, therefore you must have a working MySQL server to connect to.
3. Inputted all the server login infomation and run the Baby_Names_SQL.py file.
4. SQL_Connection.py is used to test if your computer can connect to the MySQL server (Also was the first build of the program).
5. import mysql.connector and os onto your Python external packages.
6. Baby_Names_SQL.py will give you a list of options on what you want to do with the data set.

============================= Program Initialization (Step 2) ===================================
1. Allows you to enter the data (names.txt) in the MySQL database (do this first before you run anything!).
2. Allows you start working with the data and you would need to enter the database name and its password on the MYSQL server.

============================= Data Analysis (Step 3) ===================================
-- Once pressing 2 on the previous step, there should be connection between your computer and the MySQL server. --
1. - Finds a specific name in the database and its highest ranking popularity in a decade since 1900.
2.- Finds a specific name in the database and its corresponding popularity each decade since 1900.
3. - Finds a specific decade in the database and its corresponding name rankings from least to greatest.
4. - Finds a specific name that only appears once in a single decade since the 1900s.
5. - Finds names that are increasing in popularity every decade since the 1900s.
6. - Finds names that are decreasing in popularity every decade since the 1900s.
7. - Exits the program.



