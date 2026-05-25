import pytest
from conversor_temperatura import (
    celsius_para_fahrenheit,
    celsius_para_kelvin,
    fahrenheit_para_celsius,
    fahrenheit_para_kelvin,
    kelvin_para_celsius,
    kelvin_para_fahrenheit,
)


class TestCelsiusParaFahrenheit:
    def test_ponto_congelamento(self):
        assert celsius_para_fahrenheit(0) == pytest.approx(32.0)

    def test_ponto_ebulicao(self):
        assert celsius_para_fahrenheit(100) == pytest.approx(212.0)

    def test_temperatura_negativa(self):
        assert celsius_para_fahrenheit(-40) == pytest.approx(-40.0)

    def test_temperatura_corporal(self):
        assert celsius_para_fahrenheit(37) == pytest.approx(98.6)


class TestCelsiusParaKelvin:
    def test_zero_absoluto(self):
        assert celsius_para_kelvin(-273.15) == pytest.approx(0.0)

    def test_ponto_congelamento(self):
        assert celsius_para_kelvin(0) == pytest.approx(273.15)

    def test_ponto_ebulicao(self):
        assert celsius_para_kelvin(100) == pytest.approx(373.15)


class TestFahrenheitParaCelsius:
    def test_ponto_congelamento(self):
        assert fahrenheit_para_celsius(32) == pytest.approx(0.0)

    def test_ponto_ebulicao(self):
        assert fahrenheit_para_celsius(212) == pytest.approx(100.0)

    def test_temperatura_negativa(self):
        assert fahrenheit_para_celsius(-40) == pytest.approx(-40.0)


class TestKelvinParaCelsius:
    def test_zero_absoluto(self):
        assert kelvin_para_celsius(0) == pytest.approx(-273.15)

    def test_ponto_congelamento(self):
        assert kelvin_para_celsius(273.15) == pytest.approx(0.0)

    def test_kelvin_negativo_levanta_erro(self):
        with pytest.raises(ValueError, match="Kelvin nao pode ser negativo"):
            kelvin_para_celsius(-1)


class TestFahrenheitParaKelvin:
    def test_ponto_congelamento(self):
        assert fahrenheit_para_kelvin(32) == pytest.approx(273.15)

    def test_ponto_ebulicao(self):
        assert fahrenheit_para_kelvin(212) == pytest.approx(373.15)


class TestKelvinParaFahrenheit:
    def test_ponto_congelamento(self):
        assert kelvin_para_fahrenheit(273.15) == pytest.approx(32.0)

    def test_ponto_ebulicao(self):
        assert kelvin_para_fahrenheit(373.15) == pytest.approx(212.0)
