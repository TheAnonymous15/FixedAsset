from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "project_name": "Fixed Asset Management"})

@app.post("/submit/")
async def submit_form(request: Request, name: str = Form(...)):
    # Process form submission or other backend logic
    return templates.TemplateResponse("submit.html", {"request": request, "name": name})