# udacity Log Analysis project
This Source code is part of Udacity nanodegree term 1 project that i have done,
its main function is to fetch a postgresSQL database to answer three questions,
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

## PostgreSQL views
The python code depends on 5 postgreSQL views, these views has to be added to
the (news) database before running the program

please follow these steps:

``` 
$ psql news

CREATE VIEW AccessAllArticles AS
SELECT substring(path,10) AS subtitle,
count(*) AS num
FROM log WHERE path <> '/'
GROUP BY path ORDER BY num DESC;

CREATE VIEW AccessRegisteredArticles AS
SELECT articles.title, AccessAllArticles.num
FROM articles JOIN AccessAllArticles ON articles.slug = AccessAllArticles.subtitle
ORDER BY num DESC;

CREATE VIEW AuthorsViewSummary AS
SELECT author, sum(num)
FROM (select articles.author , AccessRegisteredArticles.num
FROM AccessRegisteredArticles JOIN articles ON articles.title=AccessRegisteredArticles.title) AS FOO
GROUP BY author ORDER BY sum DESC;

CREATE VIEW NotFoundStatusHistory AS
SELECT to_char(time,'YYYY-MM-DD') AS date,count(*) AS sum_nf
FROM log WHERE status = '404 NOT FOUND'
GROUP BY date ORDER BY date;

CREATE VIEW AllstatusHistory AS
SELECT to_char(time,'YYYY-MM-DD') AS date,count(*) AS sum_all
FROM log GROUP BY date ORDER BY date;
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

 1- **ud_loganalysis.py**: Access the postgreSQL database and fetches the tables to
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


