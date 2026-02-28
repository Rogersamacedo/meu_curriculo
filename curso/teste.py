# print("Hello World!")


# print("=======================================")
# def soma(a, b):
#     return a + b
# print("Resultado da soma:", soma(2, 3))
# #soma(10,4)
# print("=======================================")
# def multiplicacao(a, b):
#     return a * b
# print("Resultado da multiplicação:", multiplicacao(4, 5))    


#laços de repetição for, while e do while
print("========================================")
for i in range(5):
    print("Iteração:", i)

print("========================================")

turma_aula = ["Alice", "Bob", "Charlie", "Diana"]
for aluno in turma_aula:
    print("Aluno:", aluno)

print("=================liberar_acesso=======================")

def liberar_acesso(idade):
    if idade >= 18:      # 4 espaços de recuo
        return "Acesso liberado"
    else:                # 4 espaços de recuo
        return "Acesso negado"

# Fora da função, você pede o input e chama a função
idade = int(input("Digite sua idade: "))
print(liberar_acesso(idade))

print("========================================")



#print(liberar_acesso(idade))
    
# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Acesso liberado")  # Não esqueça dos 4 espaços aqui!
# else:
#     print("Acesso negado")
