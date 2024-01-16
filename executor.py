import operator
import math

def evaluate_condition(condition, record):
    if len(condition) == 1:
        return evaluate_condition(condition[0], record)
    elif len(condition) == 3:
        left, op, right = condition

        # Handling nested conditions in left and right
        if isinstance(left, list):
            left_value = evaluate_condition(left, record)
        else:
            left = left.strip("'") if isinstance(left, str) and left[0] == left[-1] == "'" else left
            left_value = record[left] if left in record else left

        if isinstance(right, list):
            right_value = evaluate_condition(right, record)
        else:
            right = right.strip("'") if isinstance(right, str) and right[0] == right[-1] == "'" else right
            right_value = record[right] if right in record else right

        # Map of operators to their corresponding functions
        operators_map = {
            "=": operator.eq,
            "!=": operator.ne,
            "<>": operator.ne,
            "<": operator.lt,
            ">": operator.gt,
            "<=": operator.le,
            ">=": operator.ge,
            "AND": operator.and_,
            "and": operator.and_,
            "OR": operator.or_,
            "or": operator.or_
        }

        return operators_map[op](left_value, right_value)

    return False

# Executor function
def execute_query(parsed_query, json_data):
    if parsed_query.get('tables')[0] != 'TABLE':
        print("Table name is not 'TABLE'")
        return

    selected_columns = parsed_query.get('columns', [['*']])[0]
    for col in selected_columns:
        if col == '*':
            continue
        elif col not in json_data[0]:
            print(f"Column '{col}' does not exist in the table")
            return

    where_clause = parsed_query.get('where', '').as_list()
    where_clause = None if where_clause == [''] else where_clause
    select_all = '*' in selected_columns
    filtered_records = []

    for record in json_data:
        if where_clause and not evaluate_condition(where_clause[0][1], record):
            continue

        selected_record = record if select_all else {col: record[col] for col in selected_columns if col in record}
        filtered_records.append(selected_record)

    if 'limit' in parsed_query:
        limit = parsed_query.get('limit')[0][1]
        return filtered_records[:limit]
    
    return filtered_records