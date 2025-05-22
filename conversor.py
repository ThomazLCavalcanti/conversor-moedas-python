import requests

def obter_cotacao(moeda_origem, moeda_destino):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        par = f"{moeda_origem}{moeda_destino}"
        return float(dados[par]["bid"])
    except (requests.exceptions.RequestException, KeyError, ValueError) as e:
        print(f"Erro ao obter cotação: {e}")
        return None

def converter_moeda():
    print("=== Conversor de Moedas ===")
    moeda_origem = input("Digite a moeda de origem (ex: USD): ").upper()
    moeda_destino = input("Digite a moeda de destino (ex: BRL): ").upper()
    try:
        valor = float(input(f"Digite o valor em {moeda_origem}: "))
    except ValueError:
        print("Valor inválido.")
        return

    cotacao = obter_cotacao(moeda_origem, moeda_destino)
    if cotacao:
        valor_convertido = valor * cotacao
        print(f"\n{valor:.2f} {moeda_origem} = {valor_convertido:.2f} {moeda_destino}\n")

if __name__ == "__main__":
    converter_moeda()
