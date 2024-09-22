from fastapi import FastAPI , Body
from fastapi.responses import HTMLResponse
from movis_list import movies_list

app = FastAPI()
app. title= "Mi aplicacion con fastApi"
app.version= "0.0.1"



@app.get('/',tags=["Home"])
def messaje ():
    return HTMLResponse ('<h1>Hello word</h1>')

@app.get('/movies',tags=["Movies"])
def get_movies():
    return movies_list

@app.get('/movies/{id}' , tags=["Movies"])
def get_movies(id:int):
    for item in movies_list:
        if item['id']== id:
            return item 
    return[]

@app.get('/movies/' , tags=["Movies"])
def get_movies_by_category(category:str,year:int):
    movies_list_found=[]
    for item in movies_list:
        if item["year"]==year:
            movies_list_found.append(item)
    return movies_list_found

@app.post('/movies/' , tags=["Movies"])
def create_ovie(id: int= Body(), title: str = Body(), overview: str=Body(),yeard:int= Body(), rating:float=Body(),category:str=Body()):
  
    movies_list.append({
        "id": id,
        "title":title,
        "overview": overview,
        "yeard":yeard,
        "rating":rating,
        "category":category})
    return movies_list