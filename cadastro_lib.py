
def Nome_validacao(nome, sobrenome):
    # true - sem erro
    # false - com erro
    error = True
    error_type = ""
    if nome == "" or sobrenome == "":
        error_type = 'nome e sobrenome obrigatórios.'
        error = False
    if not nome.isalpha():
        error_type = 'Não é permitido o uso de números no nome de cadastro.'
        error = False
    if not sobrenome.isalpha():
        error_type = 'Não é permitido o uso de números no nome de cadastro.'

    return error, error_type

def Cpf_validacao(cpf):
    # true - sem erro
    # false - com erro
    error = True
    error_type = ""
    if cpf == "":
        error_type = 'CPF obrigratório.'
        error = False
    if cpf.isnumeric and len(cpf) != 11:
        error_type = 'O CPF deve possuir estritamente 11 números.'
        error = False
    
    return error, error_type

def Email_validacao(email):
    # true - sem erro
    # false - com erro
    error = True
    error_type = ""
    if email == "":
        error_type = 'Email obirgatório.'
        error = False
    x = email.find("@")
    if email.count("@") > 1:
        error_type = 'Mais de um "@" encontrado em "email".'
        error = False
    if x == -1:
        error_type = 'É preciso inserir o caractere "@" para separar o subdomínio do comínio.'
        error = False
    elif x == 0:
        error_type += 'É preciso ter um subdomínio antes de "@".'
        error = False
    elif x == len(email)-1:
        error_type += 'É preciso ter um domínio depois de "@".'
        error = False

    return error, error_type

def Telefone_validacao(ddd, telefone):
    # true - sem erro
    # false - com erro
    error = True
    error_type = ""
    if ddd == "" or telefone == "":
        error_type = "ddd e telefone obrigatórios."
        error = False
    if len(ddd) != 2 or not ddd.isnumeric():
        error_type = 'ddd inválido.'
        error = False
    elif not telefone.isnumeric():
        error_type += 'O telefone deve conter apenas números.'
        error = False

    return error, error_type

def File_out_create(file_name):
    with open(file_name, "r"):
        pass

def File_out(file_name, nome, sobrenome, cpf, email, ddd, telefone):
    with open(file_name, "a") as file:
        file.write(nome + ";" + sobrenome + ";" + cpf + ";" + email + ";" + ddd + ";" + telefone + "\n")

if __name__ == '__main__':
    # File_out_create("arquivo")
    File_out("arquivo.csv", "leko", "tth", "999", "leko@tth", "61", "99999999")
