import re
import actions

intent_dict = {
        r"^(Quero|Preciso|Estou|Onde encontro|procuro)\s+[a-zA-Z\s]+\s(.+)$":actions.control
        }


def solicite(valor):
    if valor == "sair":
        return False
    for key, function in intent_dict.items():
        pattern = re.compile(key)
        point = pattern.findall(valor)
        
        # match = re.match(pattern, valor)
        # print(match)
        if point:
            print("Encontrei uma intenção! Computando...")
            function((point[0][1]).lower())
    return True      
    


def main():
    sair = True
    print("Chat inicializado, para sair basta escrever sair e dar enter")
    while sair:
        sair = solicite(input("Solicite algo ?"))
    print("Programa encerrado com sucesso!")


if __name__ == "__main__":
    main()





