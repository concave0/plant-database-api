from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 


from routes import router


app = FastAPI() 
app.include_router(router)


def main(): 
  pass 



if __name__ == "__main__": 
  main() 

