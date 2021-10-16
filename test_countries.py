import prueba


def test_countries():

    # Arrange
    valor_esperado = True

    # Act
    valor_retornado = prueba.countries()

    # Assert
    assert valor_esperado == valor_retornado
