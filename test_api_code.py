import unittest
import json
from api_code import app, grids

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_create_grid(self):
        """
        Test case for creating a grid via the API.

        Sends a POST request to create a grid with specified size and values.
        Asserts that the response status code is 200, and checks if the grid ID exists in the `grids` dictionary.
        """
        data = {
            "size": 3,
            "values": "4,2,3,2,2,1,3,2,1"
        }
        response = self.app.post('/sun-spot-analyser-api/grid',
                                 data=json.dumps(data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertTrue('id' in response_data)
        grid_id = response_data['id']
        self.assertTrue(grid_id in grids)

    def test_get_scores(self):
        """
        Test case for retrieving the scores of a grid via the API.

        Sends a GET request to retrieve the scores of a grid with a specified ID.
        Asserts that the response status code is 200, and checks if the 'scores' key exists in the response data.
        """
        grid_id = 1  # Assuming there is at least one grid in the `grids` dictionary
        response = self.app.get(f'/sun-spot-analyser-api/scores?id={grid_id}')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertTrue('scores' in response_data)

    def test_get_scores_with_invalid_id(self):
        """
        Test case for retrieving the scores of a grid with an invalid ID via the API.

        Sends a GET request to retrieve the scores of a grid with an invalid ID.
        Asserts that the response status code is 404, and checks if the response data is "Grid not found".
        """
        grid_id = 9999  # Assuming this grid ID does not exist
        response = self.app.get(f'/sun-spot-analyser-api/scores?id={grid_id}')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_data(as_text=True), "Grid not found")

if __name__ == '__main__':
    unittest.main()
