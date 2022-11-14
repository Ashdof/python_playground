#### Portfolio Project 1

# **My ProNetwork Application**
This is a simple commandline based application for storing the name, profession, email and phone numbers of people in my professional network. The purpose of this project is to practice what I learned after studying basics in Python. This programme is hosted on [GitHub](https://github.com/Ashdof/My_ProNetwork_App).

## Programme Structure
There are six files in the application's folder: mypronetwork.py file, pronetwork.py file, userdirect.py file, the database file, procons.db and the application's manual, manpro.

- #### mypronetwork.py file
This is the main class of the application, the entry point for the application to start. This class enables the user to input a command to execute; be it adding a new record, displaying list of records, updating a record, deleting a record from the database or display the manual of the application.

- #### pronetwork.py file
This file acts as the glue between the User direct class and the database files. It accepts instructions from the userdirect file, queries the database and returns the response back to the userdirect file.

- #### userdirect.py file
This class handles the logic for user interaction. It ensures the correct commands and data are provided by the user. It also enables the user to execute a particular action repeatedly until it is terminated by an appropriate command.

- #### procons.db file
A simple sqlite3 database file for storing records.

## Reference Resources

[Think Python by Allen B. Downey](https://greenteapress.com/wp/think-python/)

[SQLite and Python - Tutorials Point](https://www.tutorialspoint.com/sqlite/sqlite_python.htm/)

[SQLite3 and Python - Pynative Python Programming](https://pynative.com/python-sqlite/)

# Final Note
This application is not extensively developed. It is still a work in progress and it's aimed at showcasing my programming skills. The basic concepts highlighted in this programme are:

- Lists
- While loops
- For loops
- Nested loops 
- Switch case 
- Function definition and calling
- Class definition, initialisation and importing
- Method definition 
- File I/O
- Database CRUD 