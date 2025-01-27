Feature: Data processing and integration testing

  Scenario: Process JSON data and validate the output
    Given I have the input file "test_data/sample_input.json"
    When I process the data using the "process_data" function
    Then the output should match "test_data/expected_output.json"

  Scenario: Insert processed data into the database
    Given I have the processed data
    When I insert the data into the "users" table
    Then the database should contain the inserted records

  Scenario: Fetch data from the API
    When I make a GET request to "/api/data"
    Then the response should contain at least 10 items
