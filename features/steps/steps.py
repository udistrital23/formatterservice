from behave import given, then
from fastapi.testclient import TestClient

# --- Steps para Escenarios de solo BASE ---

@given('que la base es {base:d}')
def step_set_base(context, base):
    # Guardamos los datos en el contexto para usarlos en el paso "Entonces"
    # No enviamos 'numero' para probar solo la validación de base logicamente
    context.payload = {"base": base}

@then('la base es aceptada')
def step_base_accepted(context):
    response = context.client.post("/validate", json=context.payload)
    assert response.status_code == 200, f"Esperaba 200, obtuve {response.status_code}: {response.text}"
    assert response.json()["status"] == "Base aceptada"

@then('la base es rechazada')
def step_base_rejected(context):
    response = context.client.post("/validate", json=context.payload)
    # Esperamos un error 400 (Bad Request)
    assert response.status_code == 400, f"Esperaba 400, obtuve {response.status_code}"

# --- Steps para Escenarios de NÚMERO y BASE ---

@given('que el número "{numero}" tiene base {base:d}')
def step_set_number_and_base(context, numero, base):
    context.payload = {"base": base, "numero": numero}

@then('el número es aceptado')
def step_number_accepted(context):
    response = context.client.post("/validate", json=context.payload)
    assert response.status_code == 200, f"Error: {response.text}"
    assert response.json()["status"] == "Número aceptado"

@then('el número es rechazado')
def step_number_rejected(context):
    response = context.client.post("/validate", json=context.payload)
    assert response.status_code == 400, "El número debió ser rechazado pero fue aceptado"