#!/usr/bin/python

usuarios = []
senhas = []

while True:
    print " \
           1 - Cadastrar Usuario\n \
           2 - Acessar Sistema\n \
           3 - Sair\n"

    opcao = input("Digite a numero da opcao desejada: ")

    if opcao == 1:
        login = raw_input("Digite o login do usuario: ")
        senha = raw_input("Digite a senha do usuario: ")
        usuarios.append(login)
        senhas.append(senha)

    elif opcao == 2:
        print "-= Sistema de Autenticacao =-"
        login = raw_input("Digite o login do usuario: ")
        senha = raw_input("Digite a senha do usuario: ")

        for i,u in enumerate(usuarios):
            if u == login:
                if senha == senhas[i]:
                    print "Usuario Autenticado com Sucesso"
                    break
                else:
                    print "Senha incorreta"
                    break
            else:
                print "Usuario nao cadastrado"

    if opcao == 3:
        break
