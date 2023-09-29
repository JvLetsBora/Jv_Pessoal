# Avaliação P2

Saída esperada após execução do programa:

<img src="./media/tela-front.png" display="flex">

Esse projeto foi divido em três partes, ambas descritas e explicadas no relatório a seguir.

# Relatório

## Frontend
Para a implementação do front utilizei as tecnologias ECS da AWS e apache no ubuntu, o ecs ficou responsável por disponibilizar a aplicação online e o apache por criar um server que facilita a entrega de páginas. Para fazer esse deploy configurei em segurança de redes dentro do AWS a conexão com qual ip. Esse front foi construido do template do Murilo, apenas realizando algumas alterações que possibilitarão o deploy, como a troca das rotas por uma que estivesse online e não mais local.

## Backend
Para a implementação do backend utilizei as tecnologias ECS da AWS, FASTAPI e outras descritas no arquivo requirements.txt na pasta backend, o ecs ficou responsável por disponibilizar a aplicação online e para seu funcionamento foi necessario as instalações do requiments. Para fazer esse deploy configurei em segurança de redes dentro do AWS a conexão com qual ip. Esse backend foi construido do template do Murilo, apenas realizando algumas alterações que possibilitarão o deploy, como a conexão com o banco de dados online.

## Banco de dados
Para a implementação do banco de dados utilizei as tecnologias RDS da AWS e DBeaver, o RDS ficou responsável por disponibilizar a aplicação online e para o funcionamento realizei uma query via dbeaver criando a tabela principal da aplicação. Para fazer esse deploy configurei em segurança de redes dentro do AWS a conexão com qual ip. Esse banco de dados foi construido do template do Murilo, apenas realizando algumas alterações que possibilitarão o deploy.
