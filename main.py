import pandas as pd
import requests
import json
import openai

# Extract

# Importa os ids do usuário
df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

# URL com informações e dados para solicitar
sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'


def get_user(id):
    """
    Com base no id, solicita as informações do usuário na API, retornando em formato json
    """
    response = requests.get(f'{sdw2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

# Transform


# Aplicando get_user para cada usuário
users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

openai_api_key = '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'


openai.api_key = openai_api_key


def generate_ai_news(user):
    """
    Chat Completion - Faz a requisição ao chatGPT com base na versão dele para criar uma resposta com base no
    conteúdo digitado.
    """
    completion = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
        {
            "role": "system",
            "content": "Você é um especialista em markting bancário."
        },
        {
            "role": "user",
            "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos "
                       f"(máximo de 100 caracteres)"
        }
      ]
    )
    return completion.choices[0].message.content.strip('\"')


# Aplicando o generate_ai_news para cada usuário

for user in users:
    news = generate_ai_news(user)
    print(news)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })


# Load


def update_user(user):
    """ Atualiza as informações do usuário na API"""
    response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False


# Aplicando a função para cada usuário
for user in users:
    success = update_user(user)
    print(f"User {user['name']} updated? {success}!")   # Verificando se a ação foi bem sucedida
