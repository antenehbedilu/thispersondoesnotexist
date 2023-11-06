from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from requests import get

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi', redoc_url=None, title='This Person Does Not Exist', description='Unofficial RESTful API for the [ThisPersonDoesNotExist]( ThisPersonDoesNotExist ) website. [ThisPersonDoesNotExist]( ThisPersonDoesNotExist ) is a website that uses artificial intelligence (AI) to generate realistic human faces that do not actually exist.', version='0.0.1')

#endpoint for health check
@app.get('/api/health', tags=['HealthChecks'])
def health():
    #returns a JSON response with a status of "OK"
    return {'status': 'OK'}
