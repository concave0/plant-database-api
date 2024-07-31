# Plant Database API

This is a database API of plant genetic sequences and care instructions for plants. This API is premature and is in active development and Minimal Viable Product (MVP) is still being worked on.  

## Modules

### `database/token_database.py`

#### Classes

- **TokenDatabase(BaseModel)**: 
  - Manages database operations using SQLAlchemy.

#### Methods

- **__init__(self, database_url='sqlite:///token_database.db')**: 
  - Initializes the database connection.

- **create_table(self, table_class)**: 
  - Creates a database table for the specified SQLAlchemy table class.

- **delete_table(self, table_class)**: 
  - Drops the database table for the specified SQLAlchemy table class.

- **add_value(self, table_class, **kwargs)**: 
  - Adds a new record to the specified table with given kwargs.

- **update_value(self, table_class, filters, updates)**: 
  - Updates existing records in the specified table according to filters and updates (incomplete).

### `database/uuid.py`

#### Classes

- **Hashobject**: 
  - Placeholder class, the role is not clearly defined.

#### Functions

- **hash_obj(obj) -> int**: 
  - Generates a unique hash value for the given object.

### `app_routes/app_router.py`

#### Variables

- **router**: 
  - Instance of APIRouter to define routes for the FastAPI application.

#### Routes

- **GET /**:
  - **root(request: Request) -> JSONResponse**:
    - Health check route. Returns a message indicating the service is running.

- **GET /health_check**:
  - **health_check(request: Request) -> JSONResponse**:
    - Health check route. Returns a message indicating the service is healthy.

- **PUT /update_databae/{id}/{plant_detailed_data}**:
  - **update_database(request: Request, id: int, plant_detailed_data) -> JSONResponse**:
    - Placeholder route for updating the database.

- **POST /create_new_data/{plants_data}**:
  - **create_new_data(request: Request, plants_data) -> JSONResponse**:
    - Placeholder route for creating new data in the database.

- **PATCH /delete_data/{id}**:
  - **delete_data(request: Request, id: int) -> JSONResponse**:
    - Placeholder route for deleting data from the database.

- **GET /get_data/{id}**:
  - **get_data(request: Request, id: int) -> JSONResponse**:
    - Placeholder route for getting data from the database.

- **GET /get_api_key**:
  - **get_api_key(request: Request) -> Response**:
    - Placeholder route for retrieving an API key from the database.

- **POST /create_token_api_token/{user_id}/{secret}**:
  - **create_token_api_token(request: Request, user_id: int, secret: str) -> JSONResponse**:
    - Generates a JWT token for a specified user.

### `token_gen/token_generate.py`

#### Classes

- **TokenGenerate**: 
  - Provides functionality to generate JWT tokens.

#### Methods

- **generate_jwt_token(payload, secret, algorithm='HS256')**: 
  - Generates a JWT token using the given payload and secret with the specified algorithm.

### `database/database_planets.py`

#### Classes

- **PlantDatabase(BaseModel)**: 
  - Manages database operations for plant database using SQLAlchemy.

#### Methods

- **__init__(self, database_url='sqlite:///plant_database.db')**: 
  - Initializes the plant database connection.

- **create_table(self, table_class)**: 
  - Creates a table in the plant database for the specified SQLAlchemy table class.

- **delete_table(self, table_class)**: 
  - Drops a table in the plant database for the specified SQLAlchemy table class.

- **add_value(self, table_class, **kwargs)**: 
  - Adds a new record to the plant database with given kwargs.

- **update_value(self, table_class, filters, updates)**: 
  - Updates records in the plant database according to filters and updates.

- **delete_value(self, table_class, filters)**: 
  - Deletes records in the plant database according to filters.

### `gen_data_explorer/plant_gen.py`

#### Classes

- **PlantGen**: 
  - Placeholder class, the role is not clearly defined.

### `main.py`

#### Functions

- **main()**: 
  - Entry point of the FastAPI application. Initializes the application and includes the router.


