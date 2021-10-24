from Funçoes import interface
from Funçoes import Entrada_Users
from Funçoes import tela_adm
from Funçoes import Opção_entrada_adm
from Funçoes import Opção_adicionando_itens
from Funçoes import login_Cadastro

#Interface Do Programa
interface()

#Estrutura de decisão de como o usuario vai entrar no sistema
Entrada_Users('Op')

#ADM cadastrado ou Ja logado no sistema
login_Cadastro('Option','user','chave')

#Entrando como ADM
tela_adm()

#Opção_Adm
Opção_entrada_adm('OptAdm')

#Op_Adicionando_itens
Opção_adicionando_itens('qtd','escolha','item')

  

  
    