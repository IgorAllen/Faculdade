#Criar um programa de login: Implemente um programa simples de login onde o usuário deve inserir um nome de usuário e uma senha. Use estruturas condicionais (if, elif, else) para verificar se as credenciais estão corretas.

'''

nome = input("Usuario:")
senha = input("Digite a senha:")


nomeusuario = input("Nome de usuario:")
senhausuario = input("Digite a senha de usuario:")

if senhausuario == senha and nomeusuario == nome:
    print("Bem-vindo ", nome)
elif senhausuario != senha and nomeusuario == nome:
    print("Usuario não identificado")
elif senhausuario == senha and nomeusuario != nome:
    print("Usuario não identificado")
else:
    print("Tente novamente")
    
'''

