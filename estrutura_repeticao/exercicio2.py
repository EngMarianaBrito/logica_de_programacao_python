name = str (input("Informe seu usuário: "))
senha = str (input("Informe sua senha: "))

while name == senha:
	print("ERRO ! Informe novamente! ")
	name = str (input("Usuário: "))
	senha = str (input("Senha: "))
else:
	print("Parabens,cadastro realizado com sucesso!")
