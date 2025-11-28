from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.validator import validar_base, validar_numero, convert_base, convert_to_base_10


class ConverterRequest(BaseModel):
    base: int
    numero: Optional[str] = None
    base_origen: Optional[int] = None
    base_destino: Optional[int] = None


app = FastAPI(title="Base Converter Service")


@app.get("/")
async def root():
    return {"service": "base-converter", "port": 8001}


@app.post("/validate")
async def validate(req: ConverterRequest):
    # Validar base (siempre requerido)
    if not validar_base(req.base):
        raise HTTPException(status_code=400, detail="Base inválida")
    
    # Si solo hay validación de base (sin número)
    if req.numero is None:
        return {"status": "Base aceptada"}
    
    # Validar número según la base
    if not validar_numero(req.numero, req.base):
        raise HTTPException(status_code=400, detail="Número inválido para la base")
    
    return {"status": "Número aceptado"}


class ConvertRequest(BaseModel):
    numero: str
    base_origen: int
    base_destino: int


@app.post("/converter")
async def converter(req: ConvertRequest):
    """Convierte un número desde una base a otra base (2-10).

    Args:
        numero: Cadena de dígitos en la base_origen
        base_origen: Base del número de entrada
        base_destino: Base a la cual convertir

    Returns:
        JSON con "numero" (valor en base_destino) y "base_destino"
    """
    try:
        resultado = convert_base(req.numero, req.base_origen, req.base_destino)
        return {"numero": resultado, "base_destino": req.base_destino}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

