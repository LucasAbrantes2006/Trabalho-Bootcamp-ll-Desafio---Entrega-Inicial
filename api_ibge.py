import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


IBGE_MUNICIPIOS_URL = (
    "https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"
)


class IBGEApiError(Exception):
    """Erro ao consultar ou interpretar a API publica do IBGE."""


def buscar_municipios_por_uf(uf, opener=urlopen, timeout=10):
    uf_normalizada = str(uf).strip().upper()
    if len(uf_normalizada) != 2 or not uf_normalizada.isalpha():
        raise ValueError("Informe uma UF valida com 2 letras. Exemplo: SP")

    url = IBGE_MUNICIPIOS_URL.format(uf=uf_normalizada)

    try:
        with opener(url, timeout=timeout) as resposta:
            payload = resposta.read().decode("utf-8")
    except HTTPError as erro:
        raise IBGEApiError(f"API do IBGE retornou status {erro.code}.") from erro
    except URLError as erro:
        raise IBGEApiError("Nao foi possivel conectar a API do IBGE.") from erro

    try:
        dados = json.loads(payload)
    except json.JSONDecodeError as erro:
        raise IBGEApiError("Resposta invalida recebida da API do IBGE.") from erro

    if not isinstance(dados, list):
        raise IBGEApiError("Formato inesperado na resposta da API do IBGE.")

    municipios = []
    for item in dados:
        nome = item.get("nome") if isinstance(item, dict) else None
        if nome:
            municipios.append(nome)

    if not municipios:
        raise IBGEApiError("Nenhum municipio encontrado para a UF informada.")

    return municipios
