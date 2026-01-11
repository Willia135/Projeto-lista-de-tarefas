#Cria uma lista vazia
tarefas = []

def salvar_tarefas():
        with open("tarefas.txt", "w", encoding="utf-8") as arquivo:#w modo write (escrita), sobrescreve o arquivo
            for tarefa in tarefas:
                arquivo.write(tarefa + "\n")#arquivo.write escreve uma linha por tarefa

try:#tratam erros caso o arquivo ainda nao exista
    with open("tarefas.txt", "r") as arquivo:#with open abre o arquivo no modo leitura
        for linha in arquivo:
            tarefas.append(linha.strip())#strip remove espacoes e quebras de linha
        print(f"{len(tarefas)} tarefas carregadas do arquivo.")
except FileNotFoundError:#tratam erros caso o arquivo ainda nao exista
    print("Nenhum arquivo encontrado. Comecando do zero. ")

print("Estudar Python")
print("Fazer exercicios")
print("Descanso")
print("Voltar a estudar")
print("Realizar mais exercicios")
print("Fazer exercicios")

print("Minhas tarefas")
for tarefa in tarefas: #percorre a lista
    print("-", tarefa)

while True:#Cria um loop infinito (o programa só para quando o usuario escolhe "Sair")
    print("\n--- GERENCIADOR DE TAREFAS ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefa")
    print("3.Remover tarefa")
    print("4. Sair")
    
    opcao_str = input("Escolha uma opcao (1-4):")#input le a escolha do usuario
    if not opcao_str.isdigit():
        print("Digite apenas números (1-4).")
        continue
    opcao = int(opcao_str)

    match opcao:
        case 1: #Controla oque o programa faz com base na escolha
            tarefa = input("Digite a nova tarefa: ")
            tarefas.append(tarefa)
            print(f"Tarefa '{tarefa}' adicionado com sucesso!")

        case 2: #Controla oque o programa faz com base na escolha
            print("\nSuas tarefas:")
            if not tarefas:#Controla oque o programa faz com base na escolha
                print("Nenhuma tarefa foi adicionada.")
            else: #Controla oque o programa faz com base na escolha
                for i, tarefa in enumerate(tarefas, start=1):#enumerate() mostra o numero e o nome da tarefa ao mesmo tempo
                    print(f"{i}. {tarefa}")

        case 3:#Controla oque o programa faz com base na escolha
            print("\nRemover tarefa:")
            for i, tarefa in enumerate(tarefas, start=1):#enumerate() mostra o numero e o nome da tarefa ao mesmo tempo
                print(f"{i}. {tarefa}")
                num = int(input("Digite o numero da tarefa que deseja remover: ")) - 1
            if 0 <= num < len(tarefas):#Controla oque o programa faz com base na escolha
                removida = tarefas.pop(num)
                salvar_tarefas()
                print(f"Tarefa '{removida}'removida com sucesso")#enumerate() mostra o numero e o nome da tarefa ao mesmo tempo
            else:#Controla oque o programa faz com base na escolha
                print("Número inválido.")

        case 4:
            print("Saindo...")
            break#Encerra o loop
            
        case _:#Controla oque o programa faz com base na escolha
            print("Opcao inválida.")

