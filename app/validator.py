from typing import Tuple


def validar_base(base: int) -> bool:
    """La base debe estar entre 2 y 10 (inclusive)."""
    return 2 <= base <= 10


def validar_numero(numero: str, base: int) -> bool:
    """Valida que `numero` sólo contenga dígitos y que cada dígito sea < base.

    También valida que la base sea válida.
    """
    if not validar_base(base):
        return False
    if not numero.isdigit():
        return False
    return all(int(d) < base for d in numero)


def convert_to_base_10(numero: str, base: int) -> int:
    """Convierte un número desde la base dada a base 10.

    Args:
        numero: Cadena de dígitos en la base especificada
        base: Base del número (entre 2 y 10)

    Returns:
        El número en base 10 como entero

    Raises:
        ValueError si la base no es válida o el número contiene dígitos inválidos
    """
    if not validar_base(base):
        raise ValueError("Base inválida")
    if not validar_numero(numero, base):
        raise ValueError("Número inválido para la base")

    value = 0
    for d in numero:
        value = value * base + int(d)
    return value


def convert_base(numero: str, base_origen: int, base_destino: int) -> str:
    """Convierte `numero` (string) desde `base_origen` a `base_destino`.

    Args:
        numero: Cadena de dígitos en la base_origen
        base_origen: Base del número de entrada (entre 2 y 10)
        base_destino: Base del número de salida (entre 2 y 10)

    Returns:
        El número convertido en la base_destino como string

    Raises:
        ValueError si alguna base no es válida o el número contiene dígitos inválidos
    """
    if not validar_base(base_origen):
        raise ValueError("Base origen inválida")
    if not validar_base(base_destino):
        raise ValueError("Base destino inválida")
    if not validar_numero(numero, base_origen):
        raise ValueError("Número inválido para la base origen")

    # Convertir a base 10 (como intermedio)
    value = 0
    for d in numero:
        value = value * base_origen + int(d)

    # Convertir de base 10 a base_destino
    if value == 0:
        return "0"
    digits = []
    while value > 0:
        digits.append(str(value % base_destino))
        value //= base_destino
    return "".join(reversed(digits))
