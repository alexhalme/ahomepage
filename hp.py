import json
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import _clibash
import locaf as f
import starlette
from starlette.responses import Response, RedirectResponse, JSONResponse
import re
from locaf import Eni as En
import csv
from datetime import datetime as DT
import requests
import sys
import httpx

app = FastAPI()
app.mount('/app', StaticFiles(directory = f.path('dist/spa')), name = 'static')

DEV_SERVER = True

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

def getSku(something):
  return str(re.sub(r'[^0-9A-Za-z]', r'', something).__hash__())[0:8]

def getFeesCSV():
  retval = []
  with open('fees.csv', newline='', encoding='utf-8') as F:
    retval = [x for x in csv.reader(F)]

  if True if not retval else not retval[0]:
    return retval

  retval[0][0] = retval[0][0][1:]
  return retval

FEES_CSV = getFeesCSV()
Inflater = f.Inflation()

@app.get('/fees')
def getFees():

  return JSONResponse([{
    'cost': float(f"{Inflater.get(DT(2022, 1, 1, 0, 0, 0)) * float(x[0]):.2f}"),
    **{k: v for k, v in zip(['label', 'form', 'pages', 'starpages', 'icon'], x[1:])}
  } for x in FEES_CSV])



@app.get('/redirect/{category}/{what}')
async def redirect(category, what):
  try:
    redirects = json.loads(f.iob('redirects.json'))
  except:
    redirects = {}

  return RedirectResponse(redirects.get(f'{category}/{what}', 'https://alexhal.me/'))

@app.get('/{path:path}')
async def mainpath(path: str, response: Response):
  #return starlette.responses.RedirectResponse(url='/app/index.html')
  if not DEV_SERVER or sys.platform == 'linux':
    return starlette.responses.RedirectResponse(url='/app/index.html')

  if DEV_SERVER:
    async with httpx.AsyncClient() as client:
      proxy = await client.get(f'http://127.0.0.1:8080/{path}')
    response.body = proxy.content
    response.status_code = proxy.status_code
    return response
  else:
    try:
      async with httpx.AsyncClient() as client:
        proxy = await client.get(f'http://127.0.0.1:8080/{path}')
      response.body = proxy.content
      response.status_code = proxy.status_code
      return response
    except:
      return starlette.responses.RedirectResponse(url='/app/index.html')

if __name__ == '__main__':
  if sys.platform == 'linux':
    DEV_SERVER = False
  else:
    DEV_SERVER = True
    try:
      requests.get('http://localhost:8080', timeout=0.01)
    except: # requests.exceptions.ConnectTimeout as reqError:
      DEV_SERVER = False
  print(f"DEV_SERVER: {DEV_SERVER}")

  uvicorn.run(app, host='127.0.0.1', port=5145)
