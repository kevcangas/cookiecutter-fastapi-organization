#Schemas


#Services
from api.services import get
from api.services import post
from api.services import put
from api.services import delete


#FastAPI
from fastapi import APIRouter
from fastapi import Path, Body


api = APIRouter()
ver = '/v1'