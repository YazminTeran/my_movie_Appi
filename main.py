from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app. title= "Mi aplicacion con fastApi"
app.version= "0.0.1"

movies_list = [
    {
        "id": 1,
        "title": "Palpito",
        "overview":"serie de trafico de organos",
        "year": 2023,
        "rating": 10.0
    
    },
     {
        "id": 2,
        "title": "manifiesto",
        "overview":"serie de vuelo perdido  cinco años",
        "year": 2023,
        "rating": 10.0
    
    } ,

    {    "id": 3,
        "title": "brigerton",
        "overview":"serie ",
        "year": 2024,
        "rating": 10.0
    
    },

    {    "id": 4,
        "title": "el pajaro loco",
        "overview":"el pajaro loco se va a acampar",
        "year": 2024,
        "rating": 10.0
    
    },

    {    "id": 5,
        "title": "sing 1",
        "overview":"concurso musical",
        "year": 2016,
        "rating": 10.0
    
    },

    {    "id": 6,
        "title": "sing 2",
        "overview":"ven y canta de nuevo",
        "year": 2021,
        "rating": 10.0
    
    },
   
    {    "id": 7,
        "title": "chicas pesadas",
        "overview":"comeia fresca y deivertida",
        "year": 2004,
        "rating": 10.0
    
    },
    {    "id": 8,
        "title": "kung fu panda",
        "overview":"el guerrero draon",
        "year": 2023,
        "rating": 10.0
    
    },
    {    "id": 9,
        "title": "la era de hielo 3",
        "overview":"Nace morita",
        "year": 2009,
        "rating": 10.0
    
    },
    {    "id": 10,
        "title": "la era de hielo",
        "overview":"Choquee de mundos",
        "year": 2016,
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
