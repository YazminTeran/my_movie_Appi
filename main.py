from fastapi import FastAPI

app = FastAPI()
app. title= "Mi aplicacion con fastApi"
app.version= "0.0.1"

@app.get('/',tags=["Home"])
def read_root():
    return {"Hello": "World"}



#127.0.0.1:8000
