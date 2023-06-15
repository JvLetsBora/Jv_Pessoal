#route_homepage.py

from fastapi import APIRouter
from fastapi import APIRouter
from supabase import create_client, Client
from fastapi import  File, UploadFile
from pydantic import BaseModel
import shutil
import os
from datetime import datetime

class Image(BaseModel):
    name: str
    url: str

url = "https://xwotfvgmtbaarrqamwcn.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh3b3RmdmdtdGJhYXJycWFtd2NuIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODU3MzAwNDEsImV4cCI6MjAwMTMwNjA0MX0.JS4W8RMdj_jRCpByhyFj8tA80TrW1Ti_n1vslJnDc1A"
image_router = APIRouter(prefix="/images")
bucket_name = "imagens"


supabase: Client = create_client(supabase_url=url,
                                 supabase_key=key)


@image_router.get("/tt") #remove this, It is no longer needed.
def hello_api():
    return {"msg":"Hello API"}




@image_router.get("/get_all")
async def get_all_list():
    
    response = supabase.storage.from_(bucket_name).list("imagens")
    return {"Falhou":response}


@image_router.get("/get/{file}")
async def get_all(file):
    address = supabase.storage.from_(bucket_name).get_public_url(f"{file}")
    return {"URL":address}


    
@image_router.post("/add_a")
async def upload_image(file: UploadFile = File(...)):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"{timestamp}_{file.filename}"
    with open(f"static/{file_name}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        supabase.storage.from_(bucket_name).upload(f"{file_name}", file)

    image_url = f"{url}/{file_name}"
    image = Image(name=file.filename, url=image_url)

    return image