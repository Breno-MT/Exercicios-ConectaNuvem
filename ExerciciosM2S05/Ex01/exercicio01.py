class Endereco:

    def __init__(self, logradouro, numero, complemento, bairro, cidade, uf):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
    
    def cadastrar_endereco(self):
        pass

    def exibir_endereco(self):
        pass

    def salvar_endereco(self):
        pass



class Pessoa:

    def __init__(self, nome, celular, email):
        self.nome = nome 
        self.celular = celular
        self.email = email
    
    def cadastrar_pessoa(self):
        pass

    def exibir_pessoa(self):
        pass

    def salvar_pessoa(self):
        pass


class Paciente(Pessoa):

    def __init__(self, nome, celular, email, rg, cpf, telefone, convenio, data_de_nascimento):
        super().__init__(nome, celular, email)
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone
        self.convenio = convenio
        self.data_de_nascimento = data_de_nascimento

    def cadastrar_paciente(self):
        pass

    def exibir_paciente(self):
        pass

    def salvar_paciente(self):
        pass


class Medico(Pessoa):

    def __init__(self, nome, celular, email, crm, telefone_secundario):
        super().__init__(nome, celular, email)

        self.crm = crm
        self.telefone_secundario = telefone_secundario
    
    def cadastrar_medico(self):
        pass

    def exibir_medico(self):
        pass

    def salvar_medico(self):
        pass


class Agenda(Medico, Paciente):

    def __init__(self, cpf_paciente, crm_medico, dia, mes, ano, hora, observacao):
        self.crm_medico = crm_medico
        self.cpf_paciente = cpf_paciente
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.hora = hora
        self.observacao = observacao

    def cadastrar_agenda(self):
        pass

    def exibir_agenda(self):
        pass

    def salvar_agenda(self):
        pass



    