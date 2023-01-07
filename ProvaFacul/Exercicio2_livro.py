"""Faça um programa que exiba seu nome na tela!"""
from pyparsing import str_type


nome = str
ativo = True

while ativo:
    nome = str(input("Digite por favor seu nome: "))
    pergunta = str(input("Deseja escrever  outro nome? [S/N]: ")).upper()
    if pergunta == "S":
        print(nome)
        print("Muito prazer em conhecer!, Seja bem- vindo!")
    
    if pergunta == "N":
        ativo = False
        print("Que pena!, até a próxima.")

