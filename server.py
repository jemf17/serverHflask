from fastapi import FastAPI
from routes import Capitulo, Comentario, Obra, Page, Tag
from fastapi.middleware.gzip import GZipMiddleware
import uvicorn

app = FastAPI()

# FastAPI middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)

#routes
app.include_router(Capitulo.mainCapi)
app.include_router(Comentario.mainComent)
app.include_router(Obra.mainObra)
app.include_router(Page.mainPage)
app.include_router(Tag.mainTag)

if __name__ == "__main__":
    # Configurar host y puerto
    uvicorn.run(app, host="0.0.0.0", port=5000)