# Base Converter Service

Servicio web para convertir números entre diferentes bases numéricas (2-10).

## Requisitos

- Python 3.8+
- pip

## Instalación

1. Clonar o descargar el proyecto
2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecutar el servicio

```bash
python -m uvicorn app.main:app --reload --port 8001
```

El servicio estará disponible en: `http://localhost:8001`

Documentación interactiva (Swagger): `http://localhost:8001/docs`

## Endpoints de la API

### 1. Root - Información del servicio
**GET** `/`

Retorna información básica del servicio.

**Respuesta:**
```json
{
  "service": "base-converter",
  "port": 8001
}
```

---

### 2. Validar - Validar base y número
**POST** `/validate`

Valida que una base sea válida (entre 2 y 10) y opcionalmente valida que un número sea válido para esa base.

**Body (JSON):**
```json
{
  "base": 8,
  "numero": "1207"
}
```

**Parámetros:**
- `base` (int, requerido): Base numérica a validar (2-10)
- `numero` (str, opcional): Número a validar en la base especificada

**Respuestas:**

Validación exitosa de base:
```json
{
  "status": "Base aceptada"
}
```

Validación exitosa de número en base:
```json
{
  "status": "Número aceptado"
}
```

Error - Base inválida:
```json
{
  "detail": "Base inválida"
}
```

Error - Número inválido para la base:
```json
{
  "detail": "Número inválido para la base"
}
```

---

### 3. Converter - Convertir entre bases
**POST** `/converter`

Convierte un número desde una base a otra base (2-10).

**Body (JSON):**
```json
{
  "numero": "1207",
  "base_origen": 8,
  "base_destino": 2
}
```

**Parámetros:**
- `numero` (str, requerido): Cadena de dígitos en la base_origen
- `base_origen` (int, requerido): Base del número de entrada (2-10)
- `base_destino` (int, requerido): Base a la cual convertir (2-10)

**Respuesta exitosa:**
```json
{
  "numero": "1010000111",
  "base_destino": 2
}
```

**Errores:**
```json
{
  "detail": "Base origen inválida"
}
```
```json
{
  "detail": "Base destino inválida"
}
```
```json
{
  "detail": "Número inválido para la base origen"
}
```

---

## Ejemplos en Postman

### Ejemplo 1: Validar base
1. Crear nueva request **POST**
2. URL: `http://localhost:8001/validate`
3. Body (JSON):
```json
{
  "base": 8
}
```
4. Click en **Send**

### Ejemplo 2: Validar número en base octal
1. Crear nueva request **POST**
2. URL: `http://localhost:8001/validate`
3. Body (JSON):
```json
{
  "base": 8,
  "numero": "1207"
}
```
4. Click en **Send**

### Ejemplo 3: Convertir octal a binario
1. Crear nueva request **POST**
2. URL: `http://localhost:8001/converter`
3. Body (JSON):
```json
{
  "numero": "1207",
  "base_origen": 8,
  "base_destino": 2
}
```
4. Click en **Send**
5. Resultado esperado: `1010000111` en base 2

### Ejemplo 4: Convertir binario a decimal
1. Crear nueva request **POST**
2. URL: `http://localhost:8001/converter`
3. Body (JSON):
```json
{
  "numero": "1010",
  "base_origen": 2,
  "base_destino": 10
}
```
4. Click en **Send**
5. Resultado esperado: `10` en base 10

### Ejemplo 5: Convertir decimal a octal
1. Crear nueva request **POST**
2. URL: `http://localhost:8001/converter`
3. Body (JSON):
```json
{
  "numero": "647",
  "base_origen": 10,
  "base_destino": 8
}
```
4. Click en **Send**
5. Resultado esperado: `1207` en base 8

### Ejemplo 6: Convertir decimal a binario
1. Crear nueva request **POST**
2. URL: `http://localhost:8001/converter`
3. Body (JSON):
```json
{
  "numero": "42",
  "base_origen": 10,
  "base_destino": 2
}
```
4. Click en **Send**
5. Resultado esperado: `101010` en base 2

---

## Pruebas automatizadas

### Ejecutar tests
```bash
pytest tests/test_validator.py -v
```

### Coverage
```bash
pytest tests/test_validator.py --cov=app --cov-report=html
```

---

## Estructura del proyecto

```
.
├── app/
│   ├── __init__.py
│   ├── main.py          # Endpoints de la API
│   └── validator.py     # Funciones de validación y conversión
├── features/
│   ├── environment.py
│   ├── validacion.feature
│   └── steps/
│       └── steps.py     # Tests BDD con Behave
├── tests/
│   ├── __init__.py
│   └── test_validator.py # Tests unitarios con pytest
├── Dockerfile
├── Makefile
├── requirements.txt
└── README.md
```

---

## Docker

### Construir imagen
```bash
docker build -t formatter-service:latest .
```

### Ejecutar contenedor
```bash
docker run -p 8001:8001 formatter-service:latest
```

---

## Notas

- Las bases válidas están en el rango 2 a 10 (inclusive)
- Los dígitos válidos para cada base van de 0 a (base-1)
- El servicio usa conversión a través de base 10 como intermedio
