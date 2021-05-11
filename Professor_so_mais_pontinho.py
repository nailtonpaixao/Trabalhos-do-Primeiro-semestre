def calcularMedia(trabalho, prova):
    return (trabalho + prova) / 2

def pegarSituacao(trabalho, prova, estaComProvaSub=False):
    notaTotal = calcularMedia(trabalho, prova)

    if notaTotal < 6 and not estaComProvaSub:
        return pegarSituacao(trabalho, 10, True)
    elif notaTotal < 6:
        return "reprovado"
    elif estaComProvaSub:
        return "talvez com a sub"
    else:
        return "aprovado"


pontosTrabalho = float(input())
pontosProva = float(input())

print(pegarSituacao(pontosTrabalho, pontosProva))
