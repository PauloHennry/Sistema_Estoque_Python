
def interface():
    print("============================\n")
    print("      Interface Users       \n")
    print("     Sistema de Estoque      \n")

    print("         1 -  Adm           ")
    print("        2 - Tecnico         ")
    print("        3 - Usuario         ")
    print("   4- Escolher outra Opção  ")
    print("           0 - Sair         ")

    print("============================\n")

def login_Cadastro(Option,user,chave):
    
    while True:

        Option = int(input("Ja é usuario de nosso sistema S(1)/n(0)?"))

        #ENtrada como usuario
        if(Option == 1):
            
            login = input("Login: ")
            senha = input("Senha: ")
            print("Entrando....")
            break

        elif(Option == 2):
            #Cadastro de Usuario
            print("Cadastrar usuario:")
            user = input("Digite um login: ")
            chave = input("Digite uma senha: ")

            print("Cadastro feito com sucesso...")
            break
        else:
            print("Opções invalidas..")

def Entrada_Users(Op):
    while True:

        Op = int(input("Como deseja entrar no sistema ?"))

        if(Op == 1):
            print("Voce esta entrando como administrador...\n")
            break
        elif(Op == 2):
            print("Voce esta entrando como Tecnico.....\n")
            break
        elif(Op == 3):
            print("Voce esta entrando como usuario...\n")
            break
        elif(Op == 4):
            print("Escolha novamente uma entrada ?...\n")
        elif(Op == 0):
            print("Programa encerrado!!")
            break
        else:
            print("Sistema indiponivel..")

def Opção_entrada_adm(OptAdm):

    while True:
    
        OptAdm = int(input("O que deseja realizar ?"))

        if(OptAdm == 1):
            print("1 - Adicionar itens \n")
            break
        elif(OptAdm == 2):
            print("2 - Remover itens\n")
            break
        elif(OptAdm == 3):
            print("Visualizar itens\n")
            break
        elif(OptAdm == 0):
            print("Saindo do programa...\n")
        elif(OptAdm != 1 or OptAdm !=2 or OptAdm != 3):
            print("Nenhuma das ecolhas foi selecionada, escolha uma !!!")
            break
        else:
            print("Sistema indiponivel..")

def tela_adm():
    print("    Sistema Adiministrador ")
    print("=============================")
    print("    1 - Adicionar Item       ")
    print("     2 - Remover Item        ")
    print("    3 - visualizar estoque   ")
    print("         0 - Sair            ")
    print("=============================")

def Opção_adicionando_itens(item,qtd,escolha):
    
    while True:

        item = input("Nome do Item:  ?")
        qtd = int(input("Quantas unidades?"))
        print("----------------------------------")
        print("Item adicionado: ",item)
        print("Total de unidades: ",qtd ,"unidades")
        print(".....")
        print("Item adicionado com sucesso..")

        escolha =int(input("Deseja realizar mais algum item s(1)/n(0): \n"))

        if(escolha == 1):
            print("Adicionar item:")
            break
        elif(escolha == 0):
            print("Programa encerrado !!")
            break





        
    
        
