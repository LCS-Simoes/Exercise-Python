def cadastrar_usuario():
    nome = input("Informe o nome do usuário: ")
    idade = int(input("Informe a idade do usuário: "))
    saldo = float(input("Informe o saldo inicial: "))
    nasc = input("Informe a data de nascimento no formato DD/MM/AAAA: ")
    while True:
        senha = input("Digite sua senha: ")
        if senha.islower():
            print("A senha deve ter pelo menos um caractere MAIÚSCULO.")
        elif len(senha) < 8:
            print("A senha deve ter pelo menos 8 caracteres.")
        elif senha.isalpha():
            print("Necessita de um número.")
        elif senha.isalnum():
            print("Necessita de um caractere especial.")
        else:
            break
    print("Senha criada com sucesso.")
    while True:
        cpf = input("Informe seu CPF (somente números): ")
        if valida_cpf(cpf):
            break
        print("CPF inválido. Tente novamente.")
    # Armazenando os dados do usuário em um dicionário (provisório até um banco de dados)
    usuario = {"nome": nome, "idade": idade, "saldo": saldo, "transacoes": [], "saques": [], "senha": senha, "cpf": cpf, "nasc": nasc}
    return usuario

def valida_cpf(cpf):
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    # Verifica se há caracteres não numéricos no CPF
    if not cpf.isdigit():
        return False
    # Verifica se o CPF é composto por todos os mesmos dígitos
    if len(set(cpf)) == 1:
        return False
    # Verificação dos dígitos verificadores
    calc1 = 0
    calc2 = 0
    for i in range(9):
        calc1 += int(cpf[i]) * (10 - i)
        calc2 += int(cpf[i]) * (11 - i)
    calc1 %= 11
    calc1 = 11 - calc1 if calc1 > 1 else 0
    calc2 += calc1 * 2
    calc2 %= 11
    return cpf[-2:] == f"{calc1}{calc2}"

def calcular_saques(usuario):
    nome = usuario["nome"]
    saldo = usuario["saldo"]
    print(f"O saldo de {nome} é R${saldo:.2f}.")
    sacar = float(input("Digite o valor que deseja sacar: "))
    if saldo < sacar:
        print("Não é possível sacar o valor desejado.")
        return
    saldo -= sacar
    saque = {"sacar": sacar}
    usuario["saldo"] = saldo
    usuario["saques"].append(saque)
    print(f"Foi sacado de sua conta bancária o valor de R${sacar:.2f}.")
    print(f"O saldo de {nome} agora é de R${saldo:.2f}.")

def calcular_deposito(usuario):
    nome = usuario["nome"]
    saldo = usuario["saldo"]
    print(f"O saldo de {nome} é de R${saldo:.2f}.")
    depositar = float(input("Informe o valor que deseja depositar: "))
    saldo += depositar
    transacao = {"depositar": depositar}
    usuario["saldo"] = saldo
    usuario["transacoes"].append(transacao)
# Função para exibir o saldo de um usuário
def exibir_saldo(usuario):
    nome = usuario["nome"]
    saldo = usuario["saldo"]
    print(f"O saldo de {nome} é de R${saldo:.2f}")

# Função principal
def main():
    usuarios = []
    opcao = 0
    while opcao != 3:
        print("1 - Cadastrar usuário")
        print("2 - Faça Login")
        #print("3 - Depositar")
        #print("4 - Sacar")
        print("3 - Sair")
        opcao = int(input("Informe a opção desejada: "))

        if opcao == 1:
            usuario = cadastrar_usuario()
            usuarios.append(usuario)
        elif opcao == 2:
            print("Bem vindo ao banco Not Life")
            nome = input("Informe o nome do usuário: ")
            
            for u in usuarios:
                if u["nome"] == nome:
                    cpf = input("Informe o CPF do usuário: ")
                else:
                    print("Usuário não encontrado.")
                    if u["cpf"] == cpf:
                        senha = input("Informe a SENHA do usuário")
                        if u["senha"] == senha:
                            print(f"Seja bem vindo a sua conta {nome}")
                            opcao = 0
                            while opcao != 3:
                                print("1 - Depositar em sua conta")
                                print("2 - Sacar em sua conta")
                                print("3 - Saldo Bancário")
                                opcao = int(input("Informe a opção desejada: "))
                                if opcao == 1:
                                    nome = int(input("Informe seu nome"))
                                    nasc = int(input("Informe sua data de nascimento"))
                                    for u in usuarios:
                                        if u["nome"] == nome and u["nasc"] == nasc:
                                            calcular_deposito(u)
                                        else: 
                                            print("Usuário não encontrado ou data incorreta")
                                elif opcao == 2:
                                    nome = int(input("Informe seu nome"))
                                    nasc = int(input("Informe sua data de nascimento"))
                                    for u in usuarios:
                                        if u["nome"] == nome and u["nasc"] == nasc:
                                            calcular_saques(u)
                                        else:
                                            print("Usuário não encontrado ou senha incorreta")
                                elif opcao == 3:
                                    nome = int(input("Informe seu nome"))
                                    nasc = int(input("Informe sua data de nascimento"))
                                    for u in usuarios:
                                        if u["nome"] == nome and u["nasc"] == nasc:
                                            exibir_saldo(u)
                                        else: 
                                            print("Usuário não encontrado ou senha incorreta")
# Chamando a função principal
if __name__ == "__main__":
    main()
