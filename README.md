# 💸 Simulador de Investimentos

Este projeto simula investimentos em ações ou criptomoedas usando **dados reais** do mercado com a biblioteca `yfinance`.  
O usuário insere o ativo, a data de compra, quantidade e valor pago, e o programa calcula automaticamente o lucro ou prejuízo atual com base nos preços mais recentes.

---

## 🧠 Como funciona

Você insere:

- Código do ativo (ex: `PETR4.SA` ou `BTC-USD`)
- Quantidade adquirida
- Preço pago por unidade
- Data da compra

E o programa retorna:

- Valor atual do ativo
- Valor atual do investimento
- Lucro ou prejuízo simulado

---

## ✅ Requisitos

- Python 3.7 ou superior
- Bibliotecas: `pandas` e `yfinance`

### 💡 Instale as dependências com:

```bash
pip install yfinance
pip install pandas
