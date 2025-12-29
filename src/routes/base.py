from fastapi import FastAPI, APIRouter, Depends
import os
from helpers.config import getsettings , Settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@base_router.get("/")
async def welcome(app_settings : Settings = Depends(getsettings)):
    app_name = app_settings.APP_NAME 
    app_version = app_settings.APP_VERSION

    return {
        "message": "Welcome to " + app_name ,
        "version": app_version
        }
