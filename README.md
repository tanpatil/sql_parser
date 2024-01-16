# SQL Query Parser/Executor for Python

Simple SQL query parser and executor for Python. Only supports SELECT statements with WHERE, and LIMIT on a single table.

## Setup

Make sure you have pyparsing installed.

## Usage:

Run main.py with the SQL query as a command line argument.

Here are some example queries:

-- Correct Select with Columns and Simple Where
```sql
SELECT state, pop FROM table WHERE region = 'East';
```

-- Correct Select with All Columns (*)
```sql
SELECT * FROM table;
```

-- Incorrect Select Statement (Misspelled Keyword)
```sql
SELET state, region FROM table WHERE pop > 30;
```

-- Correct Select with Multiple Where Conditions
```sql
SELECT region, pop_male, pop_female FROM table WHERE pop < 50 AND state = 'Texas';
```

-- Select with Non-existent Column Name
```sql
SELECT city FROM table WHERE state = 'Florida';
```

-- Correct Select with Limit Clause
```sql
SELECT state, pop FROM table LIMIT 5;
```

-- Select with Incorrect Limit Value (Non-integer)
```sql
SELECT state, region FROM table LIMIT 'five';
```

-- Select with Complex Where Condition (AND, OR)
```sql
SELECT state, pop FROM table WHERE (pop_male > 20 AND region = 'West') OR pop_female < 15;
```

-- Select with Incorrect Syntax in Where Clause
```sql
SELECT state, pop_male FROM table WHERE pop >;
```

-- Correct Select with All Columns and No Where Clause
```sql
SELECT * FROM table;
```
