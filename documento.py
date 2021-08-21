# criamos um arquivo para cria uma class com a junação do
# CNPJ e CPF com isso realizamos o metodo factory nessa doc
from validate_docbr import CNPJ, CPF


class Documento:
    @staticmethod
    def criar_novo(documento):
        doc_str = str(documento)
        if len(doc_str) == 11:
            return DocCpf(doc_str)
        if len(doc_str) == 14:
            return DocCnpj(doc_str)
        else:
            raise ValueError("Documento incorreto!")


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!!")

    def __str__(self):
        return self.cpf_formatado()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)
        # importei o pacote na internet
        # para validar o CPF para não passar

    def cpf_formatado(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ Inválido!!")

    def __str__(self):
        return self.cnpj_formatado()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)
        # importei o pacote na internet
        # para validar o cnpj para não passar

    def cnpj_formatado(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
