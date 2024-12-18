# Product Recommendation API

## Endpoints

### 1. Get All Products
- **URL**: `/api/products/`
- **Method**: GET
- **Response**:
    ```json
    [
        {
            "id":1,
            "name":"Laptop:,
            "description":"A high-performance laptop",
            "price":1000.00,
            "category":"Electronics"
        }
    ]

### 2. Log User Interaction
- **URL**-`/api/interactions/`
- **Method**: POST
- **Request**:
    ```json
    [
        {
            "user": 1,
            "product": 1,
            "action": "view"
        }
    ]
- **Response**:
    ```json
    [
        {
            "id": 1,
            "user": 1,
            "product": 1,
            "action": "view",
            "timestamp": "2024-12-15T00:00:00.000Z"
        }
    ]

### 3. Get Recommendations
- **URL**: `/api/recommendations/`
- **Method**: GET
- **Response**:
    ```json
    [
        {
            "id": 2,
            "name": "Tablet",
            "description": "A lightweight tablet",
            "price": 300.00,
            "category": "Electronics"
        }
    ]
