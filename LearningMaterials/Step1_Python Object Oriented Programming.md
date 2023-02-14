# TODO List
    ## Python Object Oriented Programming
        ### pre-tutorial preparation:
            #### review python class/object, Inheritance, Modules
                ##### you can use https://www.w3schools.com/python/
            #### read about the solution of the Tower of Hanoi(this is the topic of an in-tutorial self practice)

        ### in-tutorial self practice:
            #### 1,Tower of Hanoi:
                Write a py code to solve the Tower of Hanoi problem.
                The input will be the total number of the disks. And you should print the step-by-step solution by printing one status-discribing line for each step
                You should use Object Oriented design to solve the problem

                sample input:
                3
                sample output:
                [1 2 3 ][ ][ ]
                [2 3 ][ ][1 ] 
                [3 ][2 ][1 ]
                [3 ][1 2 ][ ]
                [ ][1 2 ][3 ]
                [1 ][2 ][3 ]
                [1 ][ ][2 3 ]
                [ ][ ][1 2 3 ]

            #### 2,Modular solution of the Tower of Hanoi:
                separate your solution into several modules(one class for each module)
                import those modules into a py codefile named main.py
                the number of lines in main.py should not exceed 10
                use command line arguments to run main.py in your cmd terminal like:
                    python3 main.py 3
    ## MySQL Programming
        ### pre-tutorial preparation:
            #### learn MySQL grammar
                ##### you can use https://www.w3schools.com/mysql/
                ##### at least know the usage of these query:
                    create&drop&use database
                    create&drop table
                    insert into
                    select
                    update
                    delete
                    where&like

    ## usage of DAO(Data Access Object) in python programming
        ### pre-tutorial preparation:
            #### learn how to use mysql connector to connect to a database and run query in a python app
                ##### you can use https://www.w3schools.com/python/python_mysql_getstarted.asp

        ### in-tutorial self practice:
            #### User Management System:
                Write a command line python app
                Display the manu with options to user, user can input the number of option then press enter to select different options
                Display 3 options in your main manu:

                    1, log in
                    2, register
                    3, quit

                    When user choose log in, you should instruct user to input username and password. If the user can be identified, you should print HELLO and quit the app, otherwise you should print LOGIN FAILED and return to main menu
                    When user choose register, you should instruct user to input username and password. If the username does not exist, you should finish the register and record username&password into your database then quit the app, otherwise you should print REGISTER FAILED and return to main menu
                    Quit the app when user choose quit

                one file for each class
                the number of lines in main.py should not exceed 10
                your data access functions should be put together into a py class named UserDAO