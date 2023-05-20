# Sun Spot Analyser API

The Sun Spot Analyser API is a Flask-based web application that allows users to create grids and retrieve scores for those grids. The API provides endpoints for creating a grid and getting the scores of a grid.

## Setup Instructions

To set up the Sun Spot Analyser API, follow the steps below:

1. Install Docker:
   - Ensure you have Docker installed on your system. You can download it from the official Docker website: https://www.docker.com/get-started

2. Clone or download the code:
   - Clone the code from the repository using Git, or download the ZIP file and extract it to your desired location.

3. Build the Docker image:
   - Open a command prompt or terminal.
   - Navigate to the directory where the API code is located.
   - Run the following command to build the Docker image:
     ```
     docker build -t sun-spot-analyser-api .
     ```

4. Run the Docker container:
   - Run the following command to start the Docker container:
     ```
     docker run -p 5000:5000 sun-spot-analyser-api
     ```

5. The API should now be running on `http://localhost:5000`.

## Usage

The Sun Spot Analyser API provides the following endpoints:

### Create a Grid

- Endpoint: `/sun-spot-analyser-api/grid`
- Method: POST
- Request Body: JSON payload with the following structure:
  ```
  {
    "size": <int>,
    "values": "<comma-separated values>"
  }
  ```
  - `size`: The size of the grid.
  - `values`: A comma-separated string of integers representing the grid values.

- Response: JSON response containing the ID of the created grid.

### Retrieve Scores

- Endpoint: `/sun-spot-analyser-api/scores`
- Method: GET
- Query Parameter: `id` (the ID of the grid to retrieve scores for)
- Response: JSON response containing the scores of the grid.

## Client Code

The `client_code.py` file provided in this repository demonstrates how to interact with the Sun Spot Analyser API. It sends a POST request to create a grid and a GET request to retrieve the scores of the created grid.

To use the client code:

1. Ensure that the API is running.
2. Open a command prompt or terminal.
3. Navigate to the directory where the `client_code.py` file is located.
4. Run the following command to execute the code:
   ```
   python client_code.py
   ```

The output in the console will display the response from the API.

## Test Cases

The `test_api.py` file provided in this repository contains unit tests for the Sun Spot Analyser API. It uses the `unittest` library to define and run the test cases.

To run the test cases:

1. Ensure that the API is running.
2. Open a command prompt or terminal.
3. Navigate to the directory where the `test_api.py` file is located.
4
