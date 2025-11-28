from app.validator import validar_base, validar_numero, convert_to_base_10, convert_base


def test_base_valida():
    assert validar_base(8) is True


def test_base_fuera_de_rango():
    assert validar_base(1) is False
    assert validar_base(11) is False


def test_numero_valido_para_base():
    assert validar_numero("1207", 8) is True


def test_numero_invalido_para_base():
    assert validar_numero("1982", 8) is False


def test_convert_to_base_10_octal():
    """Convierte 1207 en base 8 a base 10."""
    resultado = convert_to_base_10("1207", 8)
    assert resultado == 647  # 1*8^3 + 2*8^2 + 0*8^1 + 7*8^0 = 512 + 128 + 0 + 7 = 647


def test_convert_to_base_10_binary():
    """Convierte 1010 en base 2 a base 10."""
    resultado = convert_to_base_10("1010", 2)
    assert resultado == 10  # 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0 = 8 + 0 + 2 + 0 = 10


def test_convert_to_base_10_decimal():
    """Convierte 123 en base 10 a base 10 (debe retornar lo mismo)."""
    resultado = convert_to_base_10("123", 10)
    assert resultado == 123


def test_convert_base_octal_to_binary():
    """Convierte 1207 en base 8 a base 2."""
    # 1207 base 8 = 647 base 10 = 1010000111 base 2
    resultado = convert_base("1207", 8, 2)
    assert resultado == "1010000111"


def test_convert_base_binary_to_decimal():
    """Convierte 1010 en base 2 a base 10."""
    resultado = convert_base("1010", 2, 10)
    assert resultado == "10"


def test_convert_base_decimal_to_octal():
    """Convierte 647 en base 10 a base 8."""
    resultado = convert_base("647", 10, 8)
    assert resultado == "1207"


def test_convert_base_decimal_to_binary():
    """Convierte 42 en base 10 a base 2."""
    resultado = convert_base("42", 10, 2)
    assert resultado == "101010"


def test_convert_base_same_base():
    """Convierte un número de base 10 a base 10 (debe ser igual)."""
    resultado = convert_base("123", 10, 10)
    assert resultado == "123"


def test_convert_base_zero():
    """Convierte 0 desde base 2 a base 10."""
    resultado = convert_base("0", 2, 10)
    assert resultado == "0"


def test_convert_base_invalid_base_origen():
    """Prueba que lanza error si base_origen es inválida."""
    try:
        convert_base("101", 11, 10)
        assert False, "Debería haber lanzado ValueError"
    except ValueError as e:
        assert "Base origen inválida" in str(e)


def test_convert_base_invalid_base_destino():
    """Prueba que lanza error si base_destino es inválida."""
    try:
        convert_base("101", 2, 1)
        assert False, "Debería haber lanzado ValueError"
    except ValueError as e:
        assert "Base destino inválida" in str(e)


def test_convert_base_invalid_number():
    """Prueba que lanza error si el número es inválido para la base."""
    try:
        convert_base("1982", 8, 10)
        assert False, "Debería haber lanzado ValueError"
    except ValueError as e:
        assert "Número inválido" in str(e)
