from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from src.db import get_db
from src.models import NumeroEmpresa
from pydantic import BaseModel, field_validator
from src.chatbot import genResponse
from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

class NumeroEmpresaDto(BaseModel):
    empresa: str
    numero: str

class MsgDto(BaseModel):
    message: str
    number: str
    
    @field_validator("message")
    def validate_message_length(cls, value):
        if len(value) > 500:
            raise ValueError("Message too long")
        return value
    
    
@router.post("/message/")
@limiter.limit("5/minute")
async def post_message(
    request: Request,
    payload: MsgDto
):
    try:
        answer = await genResponse(payload.message, payload.number)
        return {"detail": answer}  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
    
@router.post("/registrar-empresa/", status_code=status.HTTP_201_CREATED)
async def registrar_empresa(
    empresa_data: NumeroEmpresaDto,
    db: Session = Depends(get_db)
):
    
    try:
        empresa = db.query(NumeroEmpresa).filter(NumeroEmpresa.numero == empresa_data.numero).first()
        
        if empresa:
            empresa.empresa = empresa_data.empresa
            action = "atualizada"
        else:
            nova_empresa = NumeroEmpresa(numero=empresa_data.numero, empresa=empresa_data.empresa)
            db.add(nova_empresa)
            action = "registrada"
        
        db.commit()
        
        return {
            "status": "success",
            "message": f"Empresa {action} com sucesso",
            "data": {
                "numero": empresa_data.numero,
                "empresa": empresa_data.empresa
            }
        }
        
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erro ao registrar empresa: {str(e)}"
        )