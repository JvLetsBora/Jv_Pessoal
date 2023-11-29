import openai

# Sua chave da OpenAI
api_key = "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"

# Configurar a chave da API
openai.api_key = api_key

# Testar a chave fazendo uma solicitação simples
response = openai.Completion.create(
  engine="text-davinci-003",  # Substitua pelo motor apropriado
  prompt="Testando minha chave OpenAI.",
  max_tokens=5
)

# Exibir a resposta
print(response)
