from parser import simpleSQLParser
from executor import execute_query
import pandas as pd
import sys
import json

json_data_test = json.load(open('test_data.json'))

# Function to convert all keys in json data to uppercase
def load_json_data(json_data):
    temp = []
    for row in json_data:
        temp_row = {}
        for key in row:
            temp_row[key.upper()] = row[key]
        temp.append(temp_row)
    return temp

json_data_test = load_json_data(json_data_test)

# Function to flatten nested lists
def flatten(l):
    flattened = []
    for i in l:
        if isinstance(i, list):
            flattened.extend(flatten(i))
        else:
            flattened.append(i)
    return flattened

# Function to run tests
def run_tests(query, json_data):
    # Catch and display any parsing errors
    try:
        parsed_query = simpleSQLParser.parseString(query)
        if ('limit' in query.lower() and 'limit' not in parsed_query) or ('where' in query.lower() and parsed_query.get('where').as_list() == ['']):
            raise ValueError("Invalid query")
    except Exception as e:
        print(f"Failed to parse query: {query}\nError: {e}\n")
        return

    # Catch and display any execution errors
    try:
        result = execute_query(parsed_query, json_data)
    except Exception as e:
        print(f"Failed to execute query: {query}\nError: {e}\n")
        return

    return result

# Main function
if __name__ == '__main__':
    while True:
        inp_query = ""
        print("Enter query (end with ';'):", end=" ")
        while True:
            line = input()
            inp_query += line
            if ';' in line:
                inp_query = inp_query[:inp_query.index(';')]
                break
        print()
        result = run_tests(inp_query, json_data_test)
        if result:
            df = pd.DataFrame(result)
            df.to_csv(sys.stdout, index=False)
            print()