alugar=[]
def aluguel():
    placaedata=input('Digite a placa e a data(use um espaço depois da placa , coloque os numeros para dd/mm/aa):')
    alugar.append(placaedata)
    
def devolução():
    print(alugar)
    d=int(input('escolha a data(apenas os dias):'))
    de=int(input('Coloque a data de devolução(apenas os dias):'))
    dias= de-d
    custo= dias * 100
    print(custo)
  
while 0==0:
    a=int(input("""     1-Alugar carro:
     2-Devolver carro:
     3-Carros alugados:
     0-Sair:
     Selecione uma opção:"""))
    if a == 1:
        aluguel()
    if a == 2:
        devolução()
    if a == 3:
        print(alugar)
    if a == 0:
        print('finished program...')
        print('me da um 10')
        exit()