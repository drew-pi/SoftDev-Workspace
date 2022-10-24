If the named file does not exist, a new database file with the given name will be created automatically.

If no database file is specified on the command-line, a temporary database is created and automatically deleted when the "sqlite3" program exits. 


## Simple but useful commands:

#### ```create table TABLENAME(VARONE_NAME OPT_TYPE, VARTWO_NAME OPT_TYPE, ...);```

 - This is how you would make a table with two columns
 - column data types are optional will work with or without the same


#### ```insert into TABLENAME values(VAL1,VAL2,...);```

- Inserts values into the table TABLENAME

#### ```select HEADER from TABLENAME where HEADER1 = DEFINEDVALUE;```

 - for example in a table called ```table1``` that looked like this:
    | name | id |
    |------|----|
    |Andrew| 9000|
 - When you call ```select name from table1 where id = 9000;```, it will return Andrew

#### ```select HEADER from TABLENAME;```
 
 - it will return all of the non null values in the table under the defined header


#### ```.mode column```

 - will make return statements more informative because will have their headers on top with rows below

#### ```.tables```

 - prints out all of the tables you have saved





