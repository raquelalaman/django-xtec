from django.http import HttpResponse
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/index")
def hello():
    return {"message": "Hola FastAPI"}

def index(request):
    return HttpResponse("Vista de clients")

