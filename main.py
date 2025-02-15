from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="/opt")  # Make sure this is the correct directory path

@app.get("/")  # Corrected the decorator
def form_port(request: Request):
    return templates.TemplateResponse("form.html", context={"request": request})  # Corrected the context

