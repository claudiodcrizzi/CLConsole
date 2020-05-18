import os

def pathVariables():
    global command

def header():
    print("------------------ CLConsole ------------------")
    print(" Copyright© 2020 Claudio Donizeti Colsera Rizzi")
    print("----------------------------------------------------")

def cls():
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
    finishCommand()

def echo():
    ptr = input("Mensagem> ")
    print(ptr)
    finishCommand()

def create():
    create = input("Criar> ")
    if(create == "variavel"):
        vlVar = input("Criar> Variável> (_1)> Valor> ")
        _1 = vlVar
        print("A Variável foi definida, se você usar essa função novamente, ela será sobrescrevida.")
        finishCommand()
    elif(create == "pasta"):
        nf = input("Criar> pasta> Desktop> Nome> ")
        print("C:\%userprofile%\desktop\ (" + nf + ")")
        finishCommand()
    elif(create == "arquivo"):
        na = input("Criar> Arquivo> Desktop> Nome> ")
        print("C:\%userprofile%\desktop\ (" + na + ")")
        finishCommand()
        

    else:
        ntDefinedCommand()
    

def ntDefinedCommand():
    commandInterpreter()

def finishCommand():
    commandInterpreter()

def quitfn():
    exit()

def commandInterpreter():
    command = input("Terminal> ")
    if(command == "-Null-" or command == "" or command == " " or command == "/n"):
        ntDefinedCommand()
        
    elif(command == "limpar"):
        cls()

    elif(command == "mensagem"):
        echo()

    elif(command == "criar"):
        create()
    elif(command == "sair"):
        quitfn()
    else:
         ntDefinedCommand()

pathVariables()

header()

commandInterpreter()

