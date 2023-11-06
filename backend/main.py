from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from requests import get

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi', redoc_url=None, title='This Person Does Not Exist', description='Unofficial RESTful API for the [ThisPersonDoesNotExist]( ThisPersonDoesNotExist ) website. [ThisPersonDoesNotExist]( ThisPersonDoesNotExist ) is a website that uses artificial intelligence (AI) to generate realistic human faces that do not actually exist.', version='0.0.1')

#endpoint for health check
@app.get('/api/health', tags=['HealthChecks'])
def health():
    #returns a JSON response with a status of "OK"
    return {'status': 'OK'}

#endpoint for fetching and streaming an image of a person that doesn't exist; from ThisPersonDoesNotExist API
@app.get('/api/person', tags=['Person'])
def image():
    #URL of the image to fetch
    image_url = 'https://thispersondoesnotexist.com'
    #fetch the image content from the URL
    response = get(image_url, stream=True)
    #return the image as a streaming response
    return StreamingResponse(response.iter_content(chunk_size=1024), media_type='image/jpeg')
