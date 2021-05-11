def calcularValorTotal(valorUnitario, quantidade):
    return valorUnitario * quantidade


def calcularValorComDesconto(valorTotal, valorUnitario, quantidade):
    descontoPorUnidade = (quantidade * 0.01) * valorTotal
    descontoFixo = valorTotal * 0.1

    return valorTotal - descontoPorUnidade - descontoFixo


valorUnitario = float(input())
quantidade = int(input())

valorTotal = calcularValorTotal(valorUnitario, quantidade)
valorComDesconto = calcularValorComDesconto(
    valorTotal,
    valorUnitario,
    quantidade
)
print(f"{valorTotal:.2f}")
print(f"{valorComDesconto:.2f}")
