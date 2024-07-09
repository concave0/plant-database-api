from fastapi import APIRouter , Depends , HTTPException , status , Query , Body , Path , UploadFile , File , Form , Request , Response , Security , BackgroundTasks
from pydantic.types import Json
from pydantic_core.core_schema import JsonSchema
from starlette.responses import JSONResponse, RedirectResponse 
from token.token_generate import TokenGenerate


router = APIRouter() 

""" HEALTH CHECK ROUTES """
@router.get("/") 
def root(request:Request) -> JSONResponse: 
  return JSONResponse(content={"message":"I am up and running"})

@router.get("/health_check")
def health_check(request:Request) -> JSONResponse: 
  return JSONResponse(content={"message":"I am heathly"})


""" PROTECTED ROUTES """

@router.put("/update_databae/{id}/{plant_detailed_data}")
def update_database(request:Request,id:int,plant_detailed_data) -> JSONResponse:
  # TOOD add functionality for updating the database
  return JSONResponse(content={"message":"Done updateing database"})
  
@router.post("/create_new_data/{plants_data}")
def create_new_data(request:Request,plants_data) -> JSONResponse: 
  # TODO add functionality for creating new data in the database 
  return JSONResponse(content={"message":"Done creating new data"}) 

@router.patch("/delete_data/{id}") 
def delete_data(request:Request,id:int) -> JSONResponse: 
  # TODO add functionality for deleting data from the database 
  return JSONResponse(content={"message":"Done deleting data"}) 

@router.get("/get_data/{id}")
def get_data(request:Request, id: int) -> JSONResponse:
  # TODO add functionality for getting data from the database
  data = None # replace with actual data fetching logic
  return JSONResponse(content={"message": f"{data}"})


""" UNPROTECTED ROUTES """

@router.get("/get_api_key")
def get_api_key(request:Request) -> Response:
  # TODO add functionality for getting api key from database
  api_key = None # replace with actual api_key fetching logic
  return JSONResponse(content={"message": f"{api_key}"})
  
@router.post("/create_token_api_token/{user_id}/{secret}") 
def create_token_api_token(request:Request, user_id:int, secret:str):
  token =  TokenGenerate()
  token_api_key = token.generate_jwt_token(payload={"{user_id}": user_id}, secret=secret)
  # To
  return JSONResponse(content={"message": f"Your api key is {token_api_key} do not share with anyone."}) 









  
  
  



