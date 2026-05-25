import pytest
from verificador_senha import verificar_forca, gerar_senha


class TestVerificarForca:
    def test_senha_fraca_curta(self):
        nivel, pontos, dicas = verificar_forca("abc")
        assert nivel == "FRACA"
        assert "Use pelo menos 8 caracteres" in dicas

    def test_senha_media(self):
        nivel, pontos, dicas = verificar_forca("Senha123")
        assert nivel in ("MEDIA", "FORTE")

    def test_senha_forte(self):
        nivel, pontos, dicas = verificar_forca("Senha@1234")
        assert nivel in ("FORTE", "MUITO FORTE")

    def test_senha_muito_forte(self):
        nivel, pontos, dicas = verificar_forca("Tr@nsicao2026!!Tech")
        assert nivel == "MUITO FORTE"
        assert len(dicas) == 0

    def test_sem_maiusculas(self):
        _, _, dicas = verificar_forca("senha123!")
        assert "Adicione letras maiusculas" in dicas

    def test_sem_minusculas(self):
        _, _, dicas = verificar_forca("SENHA123!")
        assert "Adicione letras minusculas" in dicas

    def test_sem_numeros(self):
        _, _, dicas = verificar_forca("SenhaForte!")
        assert "Adicione numeros" in dicas

    def test_sem_especiais(self):
        _, _, dicas = verificar_forca("Senha1234")
        assert "Adicione caracteres especiais (!@#$...)" in dicas

    def test_retorna_tres_valores(self):
        resultado = verificar_forca("qualquerCoisa1!")
        assert len(resultado) == 3


class TestGerarSenha:
    def test_tamanho_padrao(self):
        senha = gerar_senha()
        assert len(senha) == 12

    def test_tamanho_customizado(self):
        senha = gerar_senha(tamanho=20)
        assert len(senha) == 20

    def test_senha_gerada_e_forte(self):
        senha = gerar_senha(tamanho=16, usar_especiais=True)
        nivel, _, _ = verificar_forca(senha)
        assert nivel in ("FORTE", "MUITO FORTE")

    def test_sem_especiais(self):
        senha = gerar_senha(tamanho=12, usar_especiais=False)
        especiais = set("!@#$%&*")
        assert not any(c in especiais for c in senha)

    def test_com_especiais(self):
        # Gerada com especiais deve conter ao menos um caracter especial
        resultados = [gerar_senha(tamanho=12, usar_especiais=True) for _ in range(20)]
        especiais = set("!@#$%&*")
        assert any(any(c in especiais for c in s) for s in resultados)

    @pytest.mark.parametrize("tamanho", [8, 12, 16, 24])
    def test_varios_tamanhos(self, tamanho):
        senha = gerar_senha(tamanho=tamanho)
        assert len(senha) == tamanho
