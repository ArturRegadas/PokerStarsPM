import entrartorneio
import resgatar


print(f"""\033[m
      
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
      
[1] Cadastrar email
[2] Entrar no torneio 
[3] Resgatar 15k*contas
[!] Sair
      
=================================================================
      """)

escolha=str(input("ESCOLHA: "))
print("")


if escolha=="1":
      while True:
            oemail=str(input("[!sair]email: "))
            if oemail == "!":
                  break
            else:
                  with open("logins.txt", "w") as arquivo:
                        arquivo.write(oemail+"\n")

elif escolha == "2":

      entrartorneio.entra_na_torneira1(str(input("LINK TORNEIO: ")))

elif escolha =="3":

      print("EXECUTANDO RESGATAR_15")
      resgatar.resgatar15()

else:
      print("\033[31mENCERRADO\033[m")

print("")
nadadasdada=input("FINALIZAR: ")

