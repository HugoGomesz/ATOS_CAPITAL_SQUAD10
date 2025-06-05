from sqlalchemy.orm import Session
from src.models import NumeroEmpresa
import httpx
from datetime import datetime

backend_url = "http://host.docker.internal:8000"



def get_empresa_name(db: Session, numero: str) -> str | None:
    empresa = db.query(NumeroEmpresa).filter(NumeroEmpresa.numero == numero).first()
    return empresa.empresa if empresa else None


def register_empresa(db: Session, numero: str, empresa_nome: str) -> bool:
    existing = db.query(NumeroEmpresa).filter(NumeroEmpresa.numero == numero).first()
    
    if existing:
        existing.empresa = empresa_nome
    else:
        nova_empresa = NumeroEmpresa(numero=numero, empresa=empresa_nome)
        db.add(nova_empresa)
    
    db.commit()
    return True


def get_data_atual():
    hoje = datetime.today()
    return hoje.year, hoje.month, hoje.day



#  BACKEND 
def canRegisterEmpresa(empresa: str) -> bool:
    #TODO NO BACKEND :P
    return True


async def vendas_dia_anterior(filial: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{backend_url}/vendas-dia-anterior?filial=FILIAL_MANAUS")
        return response.json().get("total_vendas")


async def acumulado_mes(filial: str | None = None):
    ano, mes, _ = get_data_atual()
    params = {"ano": ano, "mes": mes}
    if filial:
        params["filial"] = filial

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{backend_url}/acumulado-mes", params=params)
        return response.json().get("acumulado")


async def filial_top_vendas(ano: int | None = None, mes: int | None = None, dia: int | None = None):
    if ano is None or mes is None:
        ano, mes, dia_atual = get_data_atual()
        dia = dia or dia_atual

    params = {"ano": ano, "mes": mes}
    if dia is not None:
        params["dia"] = 31

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{backend_url}/filial-mais-vendeu", params=params)
        a = response.json()
        return f"{a.get('filial')} com: {a.get('valor_total')} reais"



async def previsao_por_filial(filial: str | None = None):
    ano, mes, _ = get_data_atual()
    params = {"ano": ano, "mes": mes}
    if filial:
        params["filial"] = filial

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{backend_url}/previsao-por-filial", params=params)
        return response.json().get("vlVenda")