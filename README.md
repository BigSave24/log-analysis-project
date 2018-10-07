# Log Analysis Project



## Objective
-------------
The log analysis reporting tool is a simple application that is used to answer the following questions:

	1) What are the most popular three articles of all time? 

	2) Who are the most popular article authors of all time? 

	3) On which days did more than 1% of requests lead to errors? 
	
These questions are answered using SQL queries ran against a PostgresSQL database populated with custom records.  


## Requirements
----------------
The following software is needed to run this project:

- [Python 3](https://www.python.org/download/releases/3.0/)
    - [pyscopg2](http://initd.org/psycopg/)
- [PostgreSQL](https://www.postgresql.org/)
- [Vagrant Tool](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)


## Using The Log Analysis Tool
------------------------------
### Project Files 
   - `log-analysis-reporting-tool.py` Python program file 
   - `Vagrant` Configuration file
   - `newsdata.zip` PostgresSQL database files 
   - `README.md` README documentation
   
### Open a terminal window
Linux\Mac - Use the default terminal application. 

Windows - You can use a terminal application such as 
[Git Bash](https://gitforwindows.org/) or [Ubuntu](https://www.howtogeek.com/265900/everything-you-can-do-with-windows-10s-new-bash-shell/).  

### Start the VM using Vagrant
Use Vagrant to startup the virtual machine. 

##### COMMAND: `vagrant up` 

**_\*NOTE\*_** The initial start up may take longer than normal due to the Vagrant managed virtual machine setup process. 

### Access the VM using ssh via Vagrant 
Log into the virtual machine using ssh. 

##### COMMAND: `vagrant ssh`

### Navigate to the *log analysis* directory 
After accessing the virtual machine, navigate to the */vagrant/log analysis/* directory. 

##### COMMAND: `cd /vagrant`

### Extract the database files
Extract the database files from the *newsdata* zip file.

##### COMMAND: `unzip newsdata.zip`

### Load the files into the database
Import the database files into the database, named *'news'*.

##### COMMAND: `psql -d news -f newsdata.sql`

### Run the Log Analysis Reporting Tool
Run the log analysis reporting tool using Python 3.

##### COMMAND: `python3 log-analysis-reporting-tool.py`

### Shut down and exit the VM
Once completed, you can exit the virtual machine.

##### COMMAND: `exit`

Shut down the virtual machine after logging out.

##### COMMAND: `vagrant halt`


