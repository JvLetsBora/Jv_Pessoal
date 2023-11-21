import re



# testeA = [
#      "Como posso atualizar meu cartão de crédito?", "Preciso mudar a forma de pagamento, o que fazer?", "Quero atualizar minhas informações de pagamento", "Método de pagamento desatualizado, como proceder para atualizar?"
# ]



# input_text = ""




# # $(como)|$(Como) & (atualizar) & (crédito) 
# # (forma) (pagamento) *(Preciso)
# # (pagamento) (atualizar)
# # $(Método) (pagamento) ^(atualizar)
# # (mudar) (forma de pagamento) 

# def solicite(a):
#     intencoes = {
#         r'/^(Como)/':"como",
#         r"\b[Vv][áa](?:\spara)?\s?[oa]?\s(.+)":"mudar",
#         r'/(d08980)/':"metodo",

#     }
#     acoes = {
#         'como':"Vá para aba meus cartões e entre em meu cartão de crédito",
#         'mudar':"Vá para aba meus pagamentos",
#         'metodo de pagamento':"Vá para aba mudar forma de pagamento",
#     }
#     input_text = a
#     if input_text == "sair":
#         return False
#    # print()

#     #if acoes[(intencoes[input_text]).lower()]:
#         print(acoes[intencoes[input_text]])
    
#     #else:
#        # print("Não entendi")

    
#     return True




import actions

intent_dict = {
        r"\b[Vv][áa](?:\spara)?\s?[oa]?\s(.+)": actions.go_to,
        r"^(Quero|Preciso|Estou|Onde encontro|procuro)\s+[a-zA-Z\s]+$":actions.control
        }




# command = input("Digite o seu comando: ")
# for key, function in intent_dict.items():
#     pattern = re.compile(key)
#     point = pattern.findall(command)
#     if point:
#         print("Encontrei uma intenção! Computando...")
#         function(point[0])
#         break

def solicite(valor):
    for key, function in intent_dict.items():
        pattern = re.compile(key)
        point = pattern.findall(valor)
        if point:
            print("Encontrei uma intenção! Computando...")
            function(point[0])
            break
    return False


def main():
    sair = True
    while sair:
        sair = solicite(input("Solicite algo ?"))

if __name__ == "__main__":
    main()





