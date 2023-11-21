#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:43:01 2023

@author: brena
"""
import bcrypt
import getpass

class ControleUsuario:
    def __init__(self):
        self.usuarios = {}

    def valida_senha(self, senha_digitada, hash_senha):
        return bcrypt.checkpw(senha_digitada, hash_senha)

    def insere_usuario(self, usuario, senha, tipo):
        if tipo not in (0, 1, 2):
            print("Tipo de usuário inválido. Use 0 para Funcionário, 1 para Administrador, ou 2 para Fornecedor.")
            return
        hash_senha = bcrypt.hashpw(senha, bcrypt.gensalt())
        self.usuarios[usuario] = {
            "senha": hash_senha,
            "tipo": tipo
        }

    def fazer_login(self, usuario, senha, tipo):
        if usuario in self.usuarios:
            info_usuario = self.usuarios[usuario]
            if self.valida_senha(senha, info_usuario["senha"]):
                if int(info_usuario["tipo"]) == tipo:
                    tipo_usuario = ""
                    if tipo == 0:
                        tipo_usuario = "Funcionário"
                    elif tipo == 1:
                        tipo_usuario = "Administrador"
                    elif tipo == 2:
                        tipo_usuario = "Fornecedor"
                    print("Usuário autenticado com sucesso. Tipo de usuário: {}".format(tipo_usuario))
                    
                else:
                    print("Tipo de usuário incorreto.")
            else:
                print("Senha incorreta.")
        else:
            print("Usuário não encontrado.")

if __name__ == '__main__':
    controle_usuario = ControleUsuario()
    
    while True:
        print("Escolha uma opção:")
        print("1. Fazer Login")
        print("2. Cadastrar Novo Usuário")
        print("3. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            name_login = input('Digite o Nome do Usuário para fazer login: ')
            senha_login = getpass.getpass('Digite a Senha do Usuário para fazer login: ')
            tipo_login = int(input('Digite o Tipo do Usuário (0 para Funcionário, 1 para Administrador, 2 para Fornecedor): '))
            controle_usuario.fazer_login(name_login, senha_login.encode(), tipo_login)
        elif opcao == '2':
            name = input('Digite o Nome do Novo Usuário: ')
            senha = getpass.getpass('Digite a Senha do Novo Usuário: ')
            tipo = int(input('Digite o Tipo do Novo Usuário (0 para Funcionário, 1 para Administrador, 2 para Fornecedor): '))
            controle_usuario.insere_usuario(name, senha.encode(), tipo)
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")




 
    

