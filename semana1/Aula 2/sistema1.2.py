#!/usr/bin/python

usuarios = []

while True:
    print " \
           1 - Cadastrar Usuario\n \
           2 - Acessar Sistema\n \
           3 - Sair\n"

    opcao = input("Digite a numero da opcao desejada: ")

    if opcao == 1:
        usuario = {"login":"","senha":""}
        usuario["login"] = raw_input("Digite o login do usuario: ")
        usuario["senha"] = raw_input("Digite a senha do usuario: ")
        usuarios.append(usuario)

    elif opcao == 2:
        print "-= Sistema de Autenticacao =-"
        login = raw_input("Digite o login do usuario: ")
        senha = raw_input("Digite a senha do usuario: ")

        for u in (usuarios):
            if u["login"] == login and u["senha"] == senha:
                print "Usuario Autenticado com Sucesso"
                break
            else:
                print "Senha incorreta"
                break
        else:
            print "Usuario nao cadastrado"

    if opcao == 3:
        break
