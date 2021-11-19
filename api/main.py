# External packages
from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


# Internal packages
from earthquake import insert_earthquake, get_earthquakes, get_earthquakes_count, \
    get_earthquakes_aggregation

# Constants
DB_NAME = 'dsaster'

# Initialize
app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://0.0.0.0:3000",
    "localhost:3000",
    "0.0.0.0:3000",
    "http://localhost:8002",
    "http://0.0.0.0:8002",
    "localhost:8002",
    "0.0.0.0:8002"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return JSONResponse(status_code=HTTPStatus.OK, content={"Hello": "World"})

@app.get("/db/earthquakes/find")
def earthquakes(limit: int=25, min_magnitude: float=None, max_magnitude: float=None, tsunami:bool=None):
    try:
        items = get_earthquakes(DB_NAME, limit, min_magnitude, max_magnitude, bool(tsunami))
        return JSONResponse(status_code=HTTPStatus.OK, content=items)

    except Exception as e:
        content = {"status": "Failure", "exception": str(e)}
        return JSONResponse(status_code=HTTPStatus.CONFLICT, content=content)

@app.post("/db/insert")
def insert_element(earthquake: dict):
    try:
        # Insert element to database
        insert_earthquake(DB_NAME, earthquake)
        return JSONResponse(status_code=HTTPStatus.CREATED, content={"status": "Success", 'element': earthquake})

    except Exception as e:
        content = {"status": "Failure", "exception": str(e), 'element': earthquake}
        return JSONResponse(status_code=HTTPStatus.CONFLICT, content=content)

@app.get("/db/earthquakes/count")
def eartquakes_count(min_magnitude: float=None):
    try:
        # Insert element to database
        count = get_earthquakes_count(DB_NAME, min_magnitude)
        return JSONResponse(status_code=HTTPStatus.OK, content={"status": "Success", 'count': count})

    except Exception as e:
        content = {"status": "Failure", "exception": str(e)}
        return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, content=content)

@app.get("/db/earthquakes/aggregation")
def eartquakes_aggregation(type_agg: str):
    try:
        # Insert element to database
        aggreg = get_earthquakes_aggregation(DB_NAME, type_agg)
        return JSONResponse(status_code=HTTPStatus.OK, content={"status": "Success", 'value': aggreg})

    except Exception as e:
        content = {"status": "Failure", "exception": str(e)}
        return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, content=content)

