print('Desafio 26')
nome = str(input('Digite uma frase: ')).strip().lower()
print(f'Existe {nome.count("a")} Letras a nesse nome\n'
      f'A primeira Letra a aparece na posição {nome.find("a")+1}\n'
      f'E a ultima letra a aparece na posição {nome.rfind("a")+1}\n')

