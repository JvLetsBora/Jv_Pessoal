#route_homepage.py

from fastapi import APIRouter
from fastapi import APIRouter
from supabase import create_client, Client
from fastapi import  File, UploadFile
from pydantic import BaseModel
import shutil
from datetime import datetime


class Image(BaseModel):
    name: str
    url: str

url = "https://xmeanomwqyzpxrhmybkn.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhtZWFub213cXl6cHhyaG15YmtuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4Njg0NDYwMywiZXhwIjoyMDAyNDIwNjAzfQ.2C0LDwgWOKpH4wN6rWlLe3hJHdeGI_rCCPMa99pWpOI"
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
    #wb ->
    with open(f"static/{file_name}", "wb") as w:
        shutil.copyfileobj(file.file, w)
        with open(f"static/{file_name}", "+rb") as r:
            # Convert ROS Image message to OpenCV image
            
            # Display image
            
            my_string = r.read()
            supabase.storage.from_(bucket_name).upload(f"{file_name}", my_string)

    image_url = f"{url}/storage/v1/object/public/imagens/{file_name}"
    image = Image(name=file.filename, url=image_url)

    return image

