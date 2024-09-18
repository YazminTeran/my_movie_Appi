from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app. title= "Mi aplicacion con fastApi"
app.version= "0.0.1"

movies_list = [
    {
        "id": 1,
        "title": "Palpito",
        "overview":"trafico de organos",
        "year": 2023,
        "rating": 10.0
    
    },
     {
        "id": 2,
        "title": "manifiesto",
        "overview":"vuelo perdido  cinco años",
        "year": 2023,
        "rating": 10.0
    
    }
]

@app.get('/',tags=["Home"])
def messaje ():
    return HTMLResponse ('<h1>Hello word</h1>')
@app.get('/movies',tags=["Movies"])
def get_movies():
    return movies_list

@app.get('/movies'/{id}'',tags=["Movies"])
def get_movies(id:int):
    for item in movies_list:
        if item['id']== id:
            return item 
    return[]






#127.0.0.1:8000
