# prediction API endpoint
from fastapi import APIRouter, Response
import json
import logging

router = APIRouter()

@router.get("/heartbeat")
def heartbeat():
    message = json.dumps({'Status': 'heartbeat'})
    return Response(message, status = 200, media_type = 'application/json')
