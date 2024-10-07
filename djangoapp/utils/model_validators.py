''' Este módulo contém funções para validar campos de modelos. '''


def validar_nif(nif):
    # Remover espaços em branco e outros caracteres não numéricos
    nif = ''.join(filter(str.isdigit, nif))

    # Verificar se o NIF tem 9 dígitos após remover caracteres não numéricos
    if len(nif) != 9:
        return False

    # Converter o NIF para uma lista de inteiros
    nif_digitos = [int(digito) for digito in nif]

    # Verificar o dígito de controlo
    total = 0
    for i in range(8):
        total += nif_digitos[i] * (9 - i)

    resto = total % 11
    digito_controlo_calculado = 11 - resto if resto != 0 and resto != 1 else 0

    return digito_controlo_calculado == nif_digitos[8]
