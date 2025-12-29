from fastapi import FastAPI, APIRouter, Depends , UploadFile , status
import os
from helpers.config import getsettings , Settings
from controllers import DataController , ProjectController
from models import ResponseSignal
from fastapi.responses import JSONResponse
import aiofiles 
import logging

logger = logging.getLogger('unvicorn.error')

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1" , "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id : str , file : UploadFile , app_settings : Settings = Depends(getsettings)):
    data_controller = DataController()
    is_valid , signal = data_controller.validate_uploaded_file(file)

    if not is_valid:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {
                "signal" : signal
                }
        )

    project_controller_path = ProjectController().get_project_path(project_id = project_id)

    file_path, file_id = data_controller.generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )

    try:
        async with aiofiles.open(file_path , "wb") as f:
            while True:
                chunk = await file.read(app_settings.FILE_CHUNK_SIZE)
                if not chunk:
                    break
                await f.write(chunk)
    except Exception as e:
        logging.error(f"Failed to upload file: {e}")    
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )   
    
    
    return JSONResponse(
        content = {
            "signal" : ResponseSignal.FILE_UPLOAD_SUCCESS.value,
            "file_id" : file_id 
        }
    )


    
    
    


