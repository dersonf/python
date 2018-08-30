#!/usr/bin/python

''' Como fiz
user = raw_input("Digite o seu login de usuario: ")
senha = raw_input("Digite a sua senha: ")
if user == "arthur.dent" and senha == "mochileiro":
    print "Usuario autenticado com sucesso!"
else:
    print "Acesso da nega:0"'''

usuario = "arthur.dent"
password = "mochileiro"

login = raw_input("Digite o seu login de usuario: ")
senha = raw_input("Digite a sua senha: ")

if (login == usuario) and (senha == password):
    print "Usuario autenticado com sucesso!"
    print "Seja Bem Vindo %s" % usuario
else:
    print "Acesso da negado!"
