import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import _clibash
import locaf as af
import starlette
from starlette.responses import Response

app = FastAPI()
app.mount('/app', StaticFiles(directory = af.path('dist/spa')), name = 'static')

app.add_middleware(
  CORSMiddleware,
  allow_origins = [
    'http://localhost:5145',
    'http://127.0.0.1:5145'
  ],
  allow_credentials = True,
  allow_methods = ['*'],
  allow_headers = ['*']
)

@app.get('/{path:path}')
async def mainpath(path: str, response: Response):
  return starlette.responses.RedirectResponse(url='/app/index.html')

if __name__ == '__main__':
  uvicorn.run(app, host='127.0.0.1', port=5145)
