# Python Básico — Scripts e Testes Automatizados

Scripts Python com cobertura de testes via **pytest** — do básico ao QA aplicado.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-50%20testes-green?style=flat-square&logo=pytest&logoColor=white)
![Status](https://img.shields.io/badge/testes-passando-brightgreen?style=flat-square)

---

## Projetos

| Script | Descrição | Testes |
|--------|-----------|--------|
| `calculadora.py` | Operações matemáticas básicas | `tests/test_calculadora.py` |
| `conversor_temperatura.py` | Conversão entre Celsius, Fahrenheit e Kelvin | `tests/test_conversor_temperatura.py` |
| `verificador_senha.py` | Verifica força e gera senhas seguras | `tests/test_verificador_senha.py` |
| `jogo_adivinhacao.py` | Jogo de adivinhação com tentativas limitadas | — |
| `lista_tarefas.py` | Gerenciador de tarefas em memória | — |

---

## Como executar

```bash
# Clonar o repositório
git clone https://github.com/reneimmich/python-basico.git
cd python-basico

# Instalar dependências
pip install -r requirements.txt

# Rodar um script
python calculadora.py

# Rodar os testes
pytest

# Rodar testes com detalhes
pytest -v

# Rodar testes com cobertura
pytest --cov=. --cov-report=term-missing
```

---

## Estrutura de Testes (QA)

```
tests/
├── conftest.py                    # Configuração global do pytest
├── test_calculadora.py            # 15 testes — operações e casos de borda
├── test_conversor_temperatura.py  # 16 testes — conversões e erros esperados
└── test_verificador_senha.py      # 19 testes — força, geração e parametrize
```

**Técnicas aplicadas:**
- Classes de teste organizadas por módulo (`TestSomar`, `TestDividir`, etc.)
- `pytest.approx` para comparação de floats com precisão
- `pytest.raises` para validar exceções esperadas
- `@pytest.mark.parametrize` para testes com múltiplos cenários
- Casos de borda: zero, negativos, valores inválidos

---

## Tecnologias

- Python 3.x
- pytest / pytest-cov

---

## Autor

**Renê Immich** — [LinkedIn](https://linkedin.com/in/reneimmich) | [GitHub](https://github.com/reneimmich)
