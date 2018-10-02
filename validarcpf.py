# -*- coding: utf-8 -*-

def validar_cpf(cpf):

    # Verifica se CPF contém menos de 11 caracteres
    if len(cpf) < 11:
        return "Número informado possui menos de 11 caracteres"

    # Verifica se CPF contém mais de 11 caracteres
    if len(cpf) > 11:
        return "Número informado excede 11 caracteres"

    # Verifica se CPF contém apenas números
    if not cpf.isdigit():
        return "Digite apenas números!"

    if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
        return cpf in [s * 11 for s in [str(n) for n in range(10)]]

    calc = [i for i in range(1, 10)]
    d1 = (sum([int(a)*b for a,b in zip(cpf[:-2], calc)]) % 11) % 10
    d2 = (sum([int(a)*b for a,b in zip(reversed(cpf[:-2]), calc)]) % 11) % 10
    if (str(d1) == cpf[-2] and str(d2) == cpf[-1]) == True:
        return "O CPF informado é válido"
    else:
        return "O CPF informado é inválido"
        
# Para testar o código, digite
# print validar_cpf(número do cpf aqui)
