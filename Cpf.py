from validate_docbr import CPF


class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!!")

    def __str__(self):
        return self.cpf_formatado()

    def cpf_e_valido(self, cpf):

        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
            # importei o pacote na internet
            # para validar o CPF para não passar
        else:
            return False

    def cpf_formatado(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

        # Código na mão, mas vou por o pacte da mássacara do cpf


"""
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_treis = self.cpf[6:9]
        fatia_quarto = self.cpf[9:]

        return "{}.{}.{}-{}".format(
            fatia_um, fatia_dois, fatia_treis, fatia_quarto
        )
"""
