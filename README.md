# bookrestfulAPI
A simple flask restful API that saves information about books control. 
Note: Only works on Linux

## Installation 

Clone this repository 

	$ git clone https://github.com/kanguarrovi/bookrestfulAPI.git

Create a virtualenv (on Debian based Linux)

    $ cd bookrestfulAPI
	$ python3 -m venv booksAPI
	$ source booksAPI/bin/activate

Upgrade pip if it is needed 

	$ pip install --upgrade pip

Install requirements 

	$ pip install -r requirements.txt

Start Database
Install sqlite3 if it is needed.

    $cd bookrestfulAPI
    $sqlite3 books.db < books.sql

## Run in development

	$ cd bookrestfulAPI
	$ source booksAPI/bin/activate
    $ python booksapi.py

Go to the browser at 127.0.0.1:5000 and begin to use it.

