# ud_loganalysis
python code for udacity nanodegree project-3 Term 1  
# Log Analysis project
This Source code is part of Udacity nanodegree term 1 project that i have done,
its main function is to fetch a postgress database to answer three questions,
these quesions are:

 1- **What are the most popular three articles of all time?**
 2- **Who are the most popular article authors of all time?**
 3- **On which days did more than 1% of requests lead to errors?** 

The Database named as newsdata.sql consists of 3 tables:
* authors table: table includes information about the authors of articles.
* articles table:  table includes the articles themselves.
* log table: table includes one entry for each time a user has accessed the site.

## Requirements
To use this reporting tool you should have psycopg2 already installed, you could
use the below command to install it:
```
pip install psycopg2
```
also you should have a database called (news) that stores the required tables
you couold get a copy of these tables by using the newsdata.sql file shipped with
this tool, use the below command to populate the news database.

```
$ psql -d news -f newsdata.sql
```

## Installation

clone the github repository and use python to run the code
```
 $ git clone https://github.com/ibrasec/ud_loganalysis
 $ cd ud_loganalysis
 $ python ud_loganalysis.py
```

## File hierarchy

If you clone or download this repository you should have the below files:

 1- **ud_loganalysis.py**: Access the postgress database and fetches the tables to
get the answer of the 3 questions

 2- **newsdata.sql**: Stores the database tables.
 
 3- **SampleOutput.txt**: a copy of what the program prints out.

 4- **README.md**


## Usage

cd to the code directory and then execute the python code:

```
$ python ud_loganalysis.py
```


## License

ud_loganalysis is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

ud_loganalysis  is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ud_loganalysis.  If not, see <http://www.gnu.org/licenses/>.


## Thanks to

Udacity, Udacity instructor ( Karl Krueger ) and the mentor ( Amr Mohamed ) for
helping me understanding the concept and find my way to complete this project.


