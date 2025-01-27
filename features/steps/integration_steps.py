import json
from behave import given, when, then
from src_py.data_processor import process_data
from src_py.database import insert_data, query_table
from src_py.api_client import get_api_data

import os

print("Current working directory:", os.getcwd())

import os
import json

@given('I have the input file "{file_path}"')
def step_load_input_file(context, file_path):
    # Resolve file path relative to this script
    abs_path = os.path.join(os.path.dirname(__file__), '..', file_path)
    abs_path = os.path.abspath(abs_path)

    print(f"Loading input file {file_path} from {abs_path}")
    with open(abs_path, 'r') as f:
        context.input_data = json.load(f)

@when('I process the data using the "process_data" function')
def stepcprocess_data(context):
    context.processed_data = process_data(context.input_data)

@then('the output should match "{expected_file_path}"')
def step_validate_output(context, expected_file_path):
    abs_path = os.path.join(os.path.dirname(__file__), '..', expected_file_path)
    abs_path = os.path.abspath(abs_path)
    with open(abs_path, 'r') as f:
        expected_output = json.load(f)
    assert context.processed_data == expected_output, "Processed data does not match the expected output."

@when('I insert the data into the "{table_name}" table')
def step_insert_data(context, table_name):
    context.inserted_records = insert_data(context.processed_data, table_name)

@then('the database should contain the inserted records')
def step_validate_db_records(context):
    db_records = query_table("users")
    assert len(db_records) == len(context.inserted_records), "Inserted records do not match database records."


from unittest.mock import patch

@when('I make a GET request to "{endpoint}"')
def step_fetch_api_data(context, endpoint):
    with patch('src.api_client.get_api_data') as mock_get_api_data:
        mock_get_api_data.return_value = [{"id": 1}, {"id": 2}, {"id": 3}]
        context.api_response = mock_get_api_data(endpoint)

@then('the response should contain at least {min_items:d} items')
def step_validate_api_response(context, min_items):
    assert len(context.api_response) >= min_items, "API response contains fewer items than expected."
