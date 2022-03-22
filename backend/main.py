import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from src.app import routers
from src.settings.config import ALLOWED_HOSTS

app = FastAPI(title='Clone_Instagram',
              version='0.0.1',
              docs_url='/private_docs',
              redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(routers.api_router)

app.mount('/images', StaticFiles(directory='images'), name='images')

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
