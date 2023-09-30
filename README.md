# Django Auction API

This is a Django-based REST API for managing user accounts and auctions.

## Features

### Accounts

- Admin with full access to user data.
- Admin authentication using a static API secret.
- Basic CRUD operations on users.
- Token-based user authentication for secure login and bidding.

### Auctions

- CRUD operations on auctions.
- Auctions have start time, end time, start price, and item name.
- Users can view ongoing auctions.
- Admin can view the status of all auctions at any time.
- Auctions are won by the user with the highest bid after the end time.

## Installation

1. Clone the repository:
git clone https://github.com/shrey1010/auction_project.git
```python
cd django-auction-api
```

2. Install dependencies:
```python
pip install -r requirements.txt
```
3. Apply database migrations:
```python
python manage.py migrate
```
4. Create a superuser for admin access:
```python
python manage.py createsuperuser
```
5. Run the development server:
```python
python manage.py runserver
```
The API will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

### Accounts

- **List/Create Users**: `GET /api/users/`, `POST /api/users/`
- **Get/Update/Delete User**: `GET /api/users/<user_id>/`, `PUT /api/users/<user_id>/`, `DELETE /api/users/<user_id>/`

### Auctions

- **List/Create Auctions**: `GET /api/auctions/`, `POST /api/auctions/`
- **Get/Update/Delete Auction**: `GET /api/auctions/<auction_id>/`, `PUT /api/auctions/<auction_id>/`, `DELETE /api/auctions/<auction_id>/`

### Authentication

- **Token-based Authentication**: `POST /api/token/`

To authenticate as an admin, include the static API secret in the `Authorization` header.

## Usage

1. **Admin Access**: Visit `http://127.0.0.1:8000/admin/` to log in as an admin with the superuser credentials.

2. **API Usage**:

    - Use tools like Postman or cURL to interact with the API.
    - Obtain an access token by sending a POST request to `/api/token/` with valid user credentials.
    - Include the token in the `Authorization` header for authenticated user access.

## Testing

To run the test suite:
python manage.py test


## Docker Support

This project is Dockerized for easy deployment. Follow the provided Docker instructions to build and run the Docker image.

### Build the Docker image

Open a terminal and navigate to the directory where your Dockerfile is located. Then run:
```python
docker build -t django-auction-api .
```
Start the Docker container

If you're using Docker Compose, run:
```pytho
docker-compose up
```
If you're not using Docker Compose, run:
```python
docker run -p 8000:8000 django-auction-api
```
Your Django API should now be running inside a Docker container.

## Contributing

If you'd like to contribute, please fork the repository and create a new pull request. Thank you for your contributions!

