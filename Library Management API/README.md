# Library Management API

A FastAPI-based REST API for managing a library system with book inventory and student borrowing functionality.

## Features

- **Book Management**: Add, update, delete, and view books
- **Student Management**: Manage student records and track borrowed books
- **Book Borrowing**: Students can borrow and return books
- **RESTful API**: Full REST API with proper HTTP methods
- **Interactive API Docs**: Automatic Swagger UI and ReDoc documentation

## Project Structure

```
.
├── main.py              # Application entry point
├── index.py             # API endpoints
├── models.py            # Database models
├── schemas.py           # Pydantic schemas for validation
├── database.py          # Database configuration
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── __pycache__/        # Python cache (ignored in git)
```

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. Clone the repository
```bash
git clone <repository-url>
cd "Book Management API"
```

2. Create a virtual environment
```bash
python -m venv venv
```

3. Activate the virtual environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## API Endpoints

### Librarian Endpoints

#### Books
- `POST /add` - Add a new book
- `GET /book_details` - Get all books
- `PUT /update/{id}` - Update a book
- `DELETE /delete/{id}` - Delete a book

#### Students
- `GET /student_details` - Get all students
- `GET /student_data/{id}` - Get student by ID

#### Greeting
- `GET /greet/{name}` - Welcome greeting

### Student Endpoints

#### Books
- `GET /available_books` - View available books

#### Borrowing
- `GET /students/{id}` - Get student details
- `POST /borrow_book/{id}` - Borrow a book
- `POST /deposit_book/{name}` - Return a borrowed book

## Database

The application uses SQLite by default. Database file: `sql_app.db`

### Models

- **BookTable**: Stores book information (id, title, author)
- **StudentTable**: Stores student information and borrowed books (id, name, title)

## Environment Variables

Create a `.env` file for sensitive configuration:

```
DATABASE_URL=sqlite:///./sql_app.db
```

## Development

### Adding New Endpoints

1. Create the database model in `models.py`
2. Create the Pydantic schema in `schemas.py`
3. Add the route in `index.py`
4. Test using the Swagger UI at `/docs`

### Running Tests

```bash
pytest
```

## Technologies Used

- **FastAPI** - Modern web framework
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server
- **SQLite** - Database

## License

This project is open source and available under the MIT License.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Author

Created as a library management system demonstration project.

## Support

For issues and questions, please open an issue on the repository.
