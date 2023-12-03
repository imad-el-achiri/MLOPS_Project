from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from typing import Annotated
import os, requests, json
dir_path = os.path.dirname(os.path.realpath(__file__))
app = FastAPI()
app.mount("/static", StaticFiles(directory=f"{dir_path}/static"), name="static")
templates = Jinja2Templates(directory=f"{dir_path}/templates")
#For local use: 
FASTAPI_URL = "http://localhost:80"
#For use with Docker, we use container name instead of localhost :
#FASTAPI_URL = "http://movie_app:80"
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
 return templates.TemplateResponse("index.html", {"request": request, "prediction_text": ""})


@app.post('/predict', response_class=HTMLResponse)
async def predict(request: Request, review: Annotated[str, Form()]):
    pred = requests.post(f"{FASTAPI_URL}/make_predictions", json={"input": review})
    pred = pred.json()["prediction"].strip('\"')
    return templates.TemplateResponse("index.html", {"request": request, "prediction_text": f"prediction value : {pred}"})


if __name__ == "__main__":
 uvicorn.run("movie_app_html:app", host="0.0.0.0", port=8080, reload=True)