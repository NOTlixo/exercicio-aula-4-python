#vetor: uma estrutura dimensional, que comporta conteudo de mesmo tipo.

#append: adiciona um novo item ao fim do vetor
    #EX: lista.append('abacaxi')

#del: deleta conteudo de uma posição
   #EX: del lista[2]l

#remove: apaga um item baseado no conteudo
    #EX: lista.remove('cebola')

#pop:remove item indexada
    #EX: aux = lista.pop(3)
listalunos = int(input("quantos alunos vc quer ver a media?:"))
contador = 1

while contador <= listalunos:

        nome = str(input(f"digite o nome do seu aluno {contador}:"))
        n1 = float(input(f"digite a primeira nota de {nome}:"))
        n2 = float(input(f"digite a segunda nota {nome}:"))
        media = (n1 + n2)/2
        v1 = [nome, n1, n2]
        v2 = [nome, media]
        contador += 1
        print("--------+--------")
        print(v1)
        print(v2)
        print("--------+--------")




