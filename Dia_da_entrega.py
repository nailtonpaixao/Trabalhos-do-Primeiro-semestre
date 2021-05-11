diasDaSemana = [
    'domingo', 'segunda', 'terca',
    'quarta', 'quinta', 'sexta', 'sabado'
]

diasParaNumero = {
    'domingo': 0,
    'segunda': 1,
    'terca': 2,
    'quarta': 3,
    'quinta': 4,
    'sexta': 5,
    'sabado': 6
}


def pegarProximoDia(numeroDia, diasParaEntrega):
    index = (numeroDia + diasParaEntrega) % 7
    return diasDaSemana[index]


def diaEntrega(diaDeCompra, diasParaEntrega):
    if diasParaEntrega == 0:
        return "chega hoje!"

    return "sera entregue " + pegarProximoDia(
        diasParaNumero[diaDeCompra],
        diasParaEntrega
    )


diaDeCompra = str(input())
diasParaEntrega = int(input())
