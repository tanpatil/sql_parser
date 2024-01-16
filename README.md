# SQL Query Parser/Executor for Python

Simple SQL query parser and executor for Python. Only supports SELECT statements with WHERE, and LIMIT on a single table.

## Setup

Make sure you have pyparsing installed.

## Usage:

Run main.py with the SQL query as a command line argument.

Here are some example queries:

#### Correct Select with Columns and Simple Where

- `SELECT state, pop FROM table WHERE region = 'East';`

#### Correct Select with All Columns (\*)

- `SELECT * FROM table;`

#### Incorrect Select Statement (Misspelled Keyword)

- `SELET state, region FROM table WHERE pop > 30;`

#### Correct Select with Multiple Where Conditions

- `SELECT region, pop_male, pop_female FROM table WHERE pop < 50 AND state = 'Texas';`

#### Select with Non-existent Column Name

- `SELECT city FROM table WHERE state = 'Florida';`

#### Correct Select with Limit Clause

- `SELECT state, pop FROM table LIMIT 5;`

#### Select with Incorrect Limit Value (Non-integer)

- `SELECT state, region FROM table LIMIT 'five';`

#### Select with Complex Where Condition (AND, OR)

- `SELECT state, pop FROM table WHERE (pop_male > 20 AND region = 'West') OR pop_female < 15;`

#### Select with Incorrect Syntax in Where Clause

- `SELECT state, pop_male FROM table WHERE pop >;`

#### Correct Select with All Columns and No Where Clause

- `SELECT * FROM table;`

#### Faulty Spelling of SELECT

- `SELEC state FROM table;`

#### Incorrect/Missing Column Names

- `SELECT non_existent_column FROM table;`
- `SELECT state, FROM table;`

#### Multiple Columns

- `SELECT state, region, pop FROM table;`

#### Missing FROM Clause

- `SELECT state WHERE pop > 20;`

#### Incorrect Table Name

- `SELECT state FROM non_existent_table;`

#### Missing WHERE Clause

- `SELECT state, pop;`

#### Incorrect WHERE Clause

- `SELECT state FROM table WHERE non_existent_column > 20;`

#### Nested WHERE Clause

- `SELECT state FROM table WHERE region = 'South' AND (pop > 20 OR pop_male > 10);`

#### Missing LIMIT Clause

- `SELECT state FROM table;`

#### Incorrect LIMIT Clause

- `SELECT state FROM table LIMIT twenty;`

#### Large LIMIT Clause

- `SELECT state FROM table LIMIT 1000000;`

#### With and Without Parentheses

- `SELECT state FROM table WHERE (region = 'South');`
- `SELECT state FROM table WHERE region = 'South';`

#### Fail Silently

- `SELECT state FROM table WHERE;`
