# 💱 Conversor de Moedas com API Externa

Este projeto é um conversor de moedas que utiliza uma API externa para obter taxas de câmbio em tempo real.

## Funcionalidades

- Converte valores entre diferentes moedas (ex: USD, EUR, BRL, etc.)
- Utiliza a API gratuita da [ExchangeRate.host](https://exchangerate.host)
- Mostra o valor convertido diretamente no terminal

## Exemplo de Uso

```
Digite a moeda de origem (ex: USD): USD
Digite a moeda de destino (ex: BRL): BRL
Digite o valor: 10
💱 10.0 USD equivalem a 51.23 BRL
```

## Requisitos

- Python 3.8+
- Conexão com a internet

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/ThomazLCavalcanti/conversor-moedas.git
   cd conversor-moedas
   ```

2. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução

```bash
python conversor.py
```

## Licença

Este projeto está licenciado sob a Licença MIT.

---
📌 Projeto criado por Thomaz
