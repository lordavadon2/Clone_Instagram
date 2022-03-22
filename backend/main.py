import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.app import routers


app = FastAPI(title='Clone_Instagram',
              version='0.0.1',
              docs_url='/private_docs',
              redoc_url=None)

app.include_router(routers.api_router)

app.mount('/images', StaticFiles(directory='images'), name='images')

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
