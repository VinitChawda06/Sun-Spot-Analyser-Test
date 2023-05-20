# API Documentation

## Create Grid [POST /sun-spot-analyser-api/grid]

Creates a grid and calculates scores for each cell.

### Request

- Method: POST
- Endpoint: /sun-spot-analyser-api/grid
- Content-Type: application/json

Request Body:
{
  "size": <int>,
  "values": "<comma-separated values>"
}

### Response

- Status Code: 200 OK
- Content-Type: application/json

Response Body:
{
  "id": <int>
}

---

## Get Scores [GET /sun-spot-analyser-api/scores]

Retrieves the scores of a specific grid.

### Request

- Method: GET
- Endpoint: /sun-spot-analyser-api/scores?id=<grid_id>

### Response

- Status Code: 200 OK
- Content-Type: application/json

Response Body:
{
  "scores": [
    {
      "score": <int>,
      "x": <int>,
      "y": <int>
    },
    ...
  ]
}

---

## Example Usage

### Create a Grid

Request:
POST /sun-spot-analyser-api/grid

Request Body:
{
  "size": 3,
  "values": "4,2,3,2,2,1,3,2,1"
}

Response:
{
  "id": 1
}

### Get Scores for a Grid

Request:
GET /sun-spot-analyser-api/scores?id=1

Response:
{
  "scores": [
    {
      "score": 10,
      "x": 1,
      "y": 1
    },
    {
      "score": 14,
      "x": 1,
      "y": 2
    },
    {
      "score": 8,
      "x": 1,
      "y": 3
    },
    ...
  ]
}
