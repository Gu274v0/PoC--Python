from fastapi import FastAPI
from src.router import api_router

title = "Python - PoC"
app = FastAPI(title=title)
app.include_router(api_router)


@app.get("/", name="Home", description="Home Page")
def home():
    return {
        "title": 'Welcome to ' + title,
        "routes": [{"path": route.path, "name": route.name, "description": route.description if hasattr(route, 'description') else "Withou descriptioon", "type": None}
                   for route in app.routes]
    }
