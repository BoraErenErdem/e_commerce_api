

from fastapi import FastAPI
from settings import engine
import models
from routers import category,auth
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    # API ile konuşacak app'lerin domain bilgileri buraya yazılacak
    # bizde domain name local host karşıladığı için ecommerce_client gost bilgisini ekledik
    'http://127.0.0.1:8000/'
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tüm domainlere izin verir, belirli domainler için ["https://example.com"]
    allow_credentials=True,
    allow_methods=["*"],  # Tüm HTTP metodlarına izin verir
    allow_headers=["*"],  # Tüm başlıklara izin verir
)


models.Base.metadata.create_all(bind=engine)

app.include_router(category.router)
app.include_router(auth.router)