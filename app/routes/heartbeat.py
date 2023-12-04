# prediction API endpoint
from fastapi import APIRouter, Response
import json
import logging

router = APIRouter()


@router.post("/heartbeat", methods = ['GET'])
def heartbeat():
    message = json.dumps({'Status': 'heartbeat'})
    return Response(message, status = 200, mimetype = 'applicaion/json')
