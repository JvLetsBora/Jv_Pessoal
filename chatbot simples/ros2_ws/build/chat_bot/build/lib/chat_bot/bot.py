import re
from chat_bot.actions import go_to, control

intent_dict = {
        r"\b^([Qq]uero|[Pp]reciso|[Ee]stou|[Oo]nde encontro|[Pp]rocuro)\s+[a-zA-Z\s]+\s(.+)$":control,
        r"\b[Vv][áa](?:\spara)?\s?[oa]?\s(.+)":go_to,
        r"\b[Mm]e\sleve até\s?[oa]?\s(.+)":go_to
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
            if function is go_to:
                function((point[0]).lower())
                break

            else:
                function((point[0][1]).lower())
                break
        else:
            if r"\b[Mm]e\sleve até\s?[oa]?\s(.+)" == key:
                print("Comando não reconhecido")

    return True      
    


def main():
    sair = True
    print("Chat inicializado, para sair basta escrever sair e dar enter")
    while sair:
        sair = solicite(input("Solicite algo ?"))
    print("Programa encerrado com sucesso!")


if __name__ == "__main__":
    main()





