import re

from rest_framework import serializers


def cpf_format(cpf):
    cpf_masked_format = "[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}"
    cpf_unmasked_format = "[0-9]{11}"

    if re.findall(cpf_masked_format, cpf) or re.findall(
            cpf_unmasked_format, cpf):
        return unmask_cpf(cpf)
    else:
        raise serializers.ValidationError({
            "cpf": "Formato do CPF inválido"
        })


def cpf_number(cpf):
    cpf_format(cpf)

    cpf_all_equal = len(unmask_cpf(cpf)) * cpf[0]
    if unmask_cpf(cpf) == cpf_all_equal:
        raise serializers.ValidationError({
            "cpf": "Número do CPF inválido"
        })

    unmasked_cpf = unmask_cpf(cpf)
    new_cpf = unmasked_cpf[0:9]
    while len(new_cpf) < 11:
        if len(new_cpf) == 9:
            countdown = 10
        else:
            countdown = 11

        multiplied_cpf = 0
        for i in range(0, countdown - 1):
            multiplied_cpf += int(new_cpf[i]) * (countdown - i)

        if multiplied_cpf % 11 < 2:
            digit = 0
        else:
            digit = 11 - (multiplied_cpf % 11)

        new_cpf += str(digit)

    if new_cpf != unmasked_cpf:
        raise serializers.ValidationError({
            "cpf": "Número do CPF inválido"
        })

    return unmask_cpf(cpf)


def unmask_cpf(cpf):
    return re.sub(r'\W', '', cpf)
