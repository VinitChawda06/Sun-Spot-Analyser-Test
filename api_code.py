# Import the necessary libraries
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)
grids = {}  # Store grids in memory for this example

# Define the Grid class
class Grid:
    def __init__(self, size, values):
        """
        Initializes a Grid object.

        Args:
            size (int): The size of the grid.
            values (list): A list of integers representing the grid values.
        """
        self.size = size
        self.values = [values[i*size:(i+1)*size] for i in range(size)]
        self.scores = self.calculate_scores()

    def calculate_scores(self):
        """
        Calculates the scores for each cell in the grid.

        Returns:
            list: A list of dictionaries containing the scores for each cell.
        """
        scores = []
        for i in range(self.size):
            for j in range(self.size):
                score = self.values[i][j]
                for x in [i-1, i, i+1]:
                    for y in [j-1, j, j+1]:
                        if 0 <= x < self.size and 0 <= y < self.size and (x, y) != (i, j):
                            score += self.values[x][y]
                scores.append({'x': i+1, 'y': j+1, 'score': score})
        return scores

# Define the endpoint for creating a grid
@app.route('/sun-spot-analyser-api/grid', methods=['POST'])
def create_grid():
    """
    Endpoint for creating a grid.

    Expects a JSON payload with the following structure:
    {
        "size": <int>,
        "values": "<comma-separated values>"
    }

    Returns:
        JSON: A JSON response containing the ID of the created grid.
    """
    size = request.json['size']
    values = list(map(int, request.json['values'].split(',')))
    grid = Grid(size, values)
    id = len(grids) + 1
    grids[id] = grid
    return jsonify({'id': id}), 200

# Define the endpoint for retrieving scores
@app.route('/sun-spot-analyser-api/scores', methods=['GET'])
def get_scores():
    """
    Endpoint for retrieving the scores of a grid.

    Expects the 'id' parameter in the query string.

    Returns:
        JSON: A JSON response containing the scores of the grid.
    """
    id = int(request.args.get('id'))
    grid = grids.get(id)
    if grid is not None:
        return jsonify({'scores': grid.scores}), 200
    else:
        return "Grid not found", 404

# Define the main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
