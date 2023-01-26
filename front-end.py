import db
import os, time

menu = """
Novo Registro       [1]
Alterar Registro    [2]
Excluir Registro    [3]
Verificar           [4]\n\n
"""

while True:
    print(menu)
    
    resposta = input("Selecione opção : ")

    if resposta.isnumeric():

        resposta = int(resposta)
        
        if resposta in [1 , 2, 3 , 4]:

            # executar programa
            if resposta == 1:

                nome = input("Qual o nome do usuario : ")
                senha = input("Digite uma senha : ")

                db.novousuario(nome,senha)
                os.system("cls")
                
                resultado = db.get_ususarios()

                print(resultado)

                break

        else:

            print( "Opção nao existe!" )

            time.sleep(10)
            os.system("cls")
            
            continue

    os.system("cls")

##teste*