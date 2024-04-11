import criaremail
import entrartorneio
import resgatar

print(f"""
      
=================================================================
      
 ######          ###                     ######          ##   ##
  ##  ##          ##                      ##  ##         ### ###
  ##  ##  ####    ##  ##  ####   ######   ##  ##         #######
  #####  ##  ##   ## ##  ##  ##   ##  ##  #####  ######  #######
  ##     ##  ##   ####   ######   ##      ##             ## # ##
  ##     ##  ##   ## ##  ##       ##      ##             ##   ##
 ####     ####    ##  ##  #####  ####    ####            ##   ##
      
=================================================================
            
Oque voce deseja fazer:
      
[0] Inserir senha
[1] Criar e colocar emails no club
[2] Entrar no torneio (1)
[3] Entrar no torneio (2)
[4] Resgatar 15k*contas
[!] Sair
      
=================================================================
      """)

senha=(str(input("SENHA: ")))
escolha=str(input("ESCOLHA: "))
print("")

if escolha == "0":
      senha=str(input("SENHA: "))
      with open("credentials.txt", "a") as arquivo:
            arquivo.write(senha+"\n")

elif escolha=="1":
      criaremail.criar_o_email(int(input("QUANTOS EMAIS CRIAR: ")))

elif escolha == "2":
      entrartorneio.entra_na_torneira1(str(input("LINK TORNEIO: ")))

elif escolha == "3":
      entrartorneio.entra_na_torneira2(str(input("LINK TORNEIO: ")))

elif escolha =="4":
      print("EXECUTANDO RESGATAR_15")
      resgatar.resgatar15()

else:
      print("\033[31mENCERRADO\033[33m")

