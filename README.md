
# 🤖 Utilizando o chatGPT em um Pipeline de ETL

O projeto tem como objetivo enviar mensagens personalizadas para os clientes através da integração com a API do chatGPT. Para isso, será feito todo o processo de Extração, Transformação e Carregamento dos dados para que o chat entenda o perfil da pessoa e, assim, possa enviar uma mensagem para cada cliente.

##  📁Extract
  
O arquivo CSV possui os números dos usuários cadastrados no sistema da [API do Santander](https://sdw-2023-prd.up.railway.app/swagger-ui/index.html). Esta API é fictícia e faz o cadastro de usuários em formato .json com as informações de id, nome e dados bancários.

Primeiramente, foi utilizada a biblioteca “pandas” para passar o arquivo "SDW2023.csv" para um dataframe e, posteriormente, para uma lista, em que os valores serão [957, 958, 959].

Biblioteca requests para efetuar chamadas http e a biblioteca json para verificar o retorno das requisições. Foi criada uma função get_user baseada no id para retornar em formato .json se o status code do request for bem sucedida (==200). Os usuários serão incluídos numa lista caso não sejam nulos.

## 💱 Transform

Nesta etapa, será utilizada a biblioteca do chatGPT chamada “openAI”. Ela consome créditos por requisição e é necessário que se insira a chave pessoa nela. Na [Documentação do chatGPT](https://platform.openai.com/docs/api-reference/chat/create), aba “Chat Completion” é possível criar frases de solicitação para o chat no “content” tanto para a “role”:”system” quanto para a “role”:”user”. Para cada usuário, será colocada a informação de “descrição” onde a mensagem aparecerá.

## ⬆️ Load

Para carregar o dado transformado, foi utilizada a função “requests.put”, com a informação do usuário em formato .json.


### Conecte-se comigo


LinkedIn             |  Discord | GitHub
:-------------------------:|:-------------------------:|:-------------------------:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0E76A8?style=for-the-badge&logo=linkedin&logoColor=FFFFFF)](https://www.linkedin.com/in/alex-pilar/)  |  [![Discord](https://img.shields.io/badge/Discord-9E1EA8?style=for-the-badge&logo=discord&logoColor=FFFFFF)](discordapp.com/users/alekaolindo) | [![Twitter](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github)](https://github.com/AlexPilar)