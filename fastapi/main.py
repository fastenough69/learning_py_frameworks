from fastapi import FastAPI, Response, Query, Path, status
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/users")
def get_info(name: str=Query(default="undef", min_length=3), age: int = 0):
    data: dict = {"user_name": name, "user_age": age}
    json_data = jsonable_encoder(data)
    return json_data

@app.get("/")
def get_main():
    return FileResponse("pages/index.html")

@app.get("/peoples")
def get_info_persons(people: list = Query()):
    return JSONResponse(content={"peoples": people})

@app.get("/new/{name}")
def new_heandler(name: str = Path(min_length=3), age: int = Query(default=0, lt=110)):
    data: dict = {"name": name, "age": age}
    return JSONResponse(content=data)

@app.get("/old")
def redir_old_page():
    return RedirectResponse("/notfound")

@app.get("/notfound", status_code=404)
def error_heandler():
    return PlainTextResponse(content="page not found")