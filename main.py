from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates=Jinja2Templates(directory="C:\Users\flore\Desktop\k8-demo")

@app.get("/")
def form_post(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request})
