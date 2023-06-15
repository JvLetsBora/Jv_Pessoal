#main.py 

from fastapi import FastAPI
from core.config import settings
from apis.general_pages.route_homepage import general_pages_router
from apis.route_image import image_router
from fastapi.staticfiles import StaticFiles


def include_router(app):
	app.include_router(general_pages_router)
	app.include_router(image_router)


def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	app.mount("/static", StaticFiles(directory="static"), name="static")
	include_router(app)
	return app 


app = start_application()


@app.get("/") #remove this, It is no longer needed.
def hello_api():
    return {"msg":"Hello API"}



