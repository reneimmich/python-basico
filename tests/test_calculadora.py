import pytest
from calculadora import somar, subtrair, multiplicar, dividir


class TestSomar:
    def test_soma_positivos(self):
        assert somar(2, 3) == 5

    def test_soma_negativos(self):
        assert somar(-1, -4) == -5

    def test_soma_zero(self):
        assert somar(0, 7) == 7

    def test_soma_floats(self):
        assert somar(1.5, 2.5) == pytest.approx(4.0)


class TestSubtrair:
    def test_subtracao_basica(self):
        assert subtrair(10, 4) == 6

    def test_resultado_negativo(self):
        assert subtrair(3, 8) == -5

    def test_subtracao_zero(self):
        assert subtrair(5, 0) == 5


class TestMultiplicar:
    def test_multiplicacao_basica(self):
        assert multiplicar(3, 4) == 12

    def test_multiplicacao_por_zero(self):
        assert multiplicar(99, 0) == 0

    def test_multiplicacao_negativos(self):
        assert multiplicar(-2, 3) == -6

    def test_dois_negativos(self):
        assert multiplicar(-2, -5) == 10


class TestDividir:
    def test_divisao_basica(self):
        assert dividir(10, 2) == 5.0

    def test_divisao_por_zero(self):
        resultado = dividir(10, 0)
        assert resultado == "Erro: divisao por zero!"

    def test_divisao_resulta_float(self):
        assert dividir(7, 2) == pytest.approx(3.5)

    def test_divisao_negativos(self):
        assert dividir(-8, 2) == -4.0
