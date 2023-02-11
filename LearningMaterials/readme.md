# TODO LIST
	## Install Python MySQL Connector
		### install by using pip command: 
			pip install mysql-connector
			pip install mysql-connector-python
	## Install MySQL
		### https://dev.mysql.com/downloads/windows/installer/8.0.html
		### use "Developer Default" setup type and finish installing
		### no need to set MySQL Router
	## Test MySQL
		### start MySQL Workbench
		### start a connection by using your username and passwd (do not use root connection)
		### run Query:
			create database helloworld;
			use helloworld;
			create table myHelloworldTable (UID int auto_increment,STRING varchar(40) not null,primary key(`UID`));
			insert into myHelloworldTable (STRING) values ("helloworld");
			select * from myHelloworldTable;
		### if you see a table shows a record UID=1, STRING="helloworld" then everything goes correct
	## Test Python MySQL Connector
		### run mysqlConnectorTest.py
		### if there's output like <mysql.connector.connection.MySQLConnection object at 0x0000010DD8F6BFD0> your connector is successfully implemented
	## Download&Install Git for windows
		### https://git-scm.com/download/win
		### during installation using all just default configurations
	## (Recommended&Optional) using VSCode to use git and code python and run terminal all in one place
		### https://visualstudio.microsoft.com
		### Download and install Visual Studio Code
		### Download Python Extension
		### you can use "source control" menu enabled if you have correctly installed git
		### enjoy