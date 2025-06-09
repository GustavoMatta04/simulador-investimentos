import yfinance as yf
import pandas as pd
from datetime import datetime

def obter_dados(ticker, data_compra):
    dados = yf.download(ticker, start=data_compra)
    if dados.empty:
        print(f"[!] Não foi possível obter dados para {ticker}.")
        return None
    return dados

def simular_investimento(ticker, quantidade, preco_compra, data_compra):
    dados = obter_dados(ticker, data_compra)
    if dados is None:
        return

    preco_atual = dados['Close'][-1]
    investimento_inicial = quantidade * preco_compra
    valor_atual = quantidade * preco_atual
    lucro_prejuizo = valor_atual - investimento_inicial

    print(f"\n=== Simulação para {ticker} ===")
    print(f"Data da compra: {data_compra}")
    print(f"Preço de compra: R$ {preco_compra:.2f}")
    print(f"Preço atual:    R$ {preco_atual:.2f}")
    print(f"Quantidade:     {quantidade}")
    print(f"Valor investido: R$ {investimento_inicial:.2f}")
    print(f"Valor atual:     R$ {valor_atual:.2f}")
    print(f"Lucro/Prejuízo:  R$ {lucro_prejuizo:.2f}\n")

def main():
    print("=== Simulador de Investimentos ===")
    while True:
        ticker = input("Digite o código do ativo (ex: PETR4.SA, BTC-USD): ").strip().upper()
        quantidade = float(input("Quantidade adquirida: "))
        preco_compra = float(input("Preço de compra por unidade: R$ "))
        data_compra = input("Data da compra (YYYY-MM-DD): ")

        try:
            datetime.strptime(data_compra, "%Y-%m-%d")
        except ValueError:
            print("Data inválida. Use o formato YYYY-MM-DD.")
            continue

        simular_investimento(ticker, quantidade, preco_compra, data_compra)

        continuar = input("Deseja simular outro ativo? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando simulação.")
            break

if __name__ == "__main__":
    main()
