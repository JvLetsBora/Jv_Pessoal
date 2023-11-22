from openai import OpenAI
import re
import dotenv
from actions import go_to, control
import os


dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

# print(os.environ["key"])  # outputs "value"
# os.environ["key"] = "newvalue"
#print(os.environ['OPENAI_API_KEY'])  # outputs 'newvalue'

# # Write changes to .env file.
# dotenv.set_key(dotenv_file, "key", os.environ["key"])







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
        
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )

    print(completion.choices[0].message)


if __name__ == "__main__":
    main()





