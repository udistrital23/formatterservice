# language: es
Característica: Validación de bases y dígitos

  Regla: La base debe estar entre 2 y 10
  Regla: Un número solo puede contener dígitos menores que su base

  Escenario: Base válida
    Dado que la base es 8
    Entonces la base es aceptada

  Escenario: Base inválida
    Dado que la base es 1
    Entonces la base es rechazada

  Escenario: Número válido para la base
    Dado que el número "1207" tiene base 8
    Entonces el número es aceptado

  Escenario: Número inválido para la base
    Dado que el número "1982" tiene base 8
    Entonces el número es rechazado