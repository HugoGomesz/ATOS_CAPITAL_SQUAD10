from fastapi import FastAPI, HTTPException, Depends, Header
from src.db import engine, Base
from src.controller import router 
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

API_KEYS = {"atoscapitais"}

async def verify_api_key(api_key: Optional[str] = Header(None)):
    if api_key not in API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

app.include_router(
    router,
    prefix="/api",
    dependencies=[Depends(verify_api_key)]  
)

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)