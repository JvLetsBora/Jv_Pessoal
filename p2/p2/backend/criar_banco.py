import psycopg2

# Constantes
DB_USER = "postgres"
DB_PASSWORD = "aws123456"
DB_HOST = "database-2.cydjxbu1izwa.us-east-1.rds.amazonaws.com"
DB_PORT = "5432"
DB_NAME = ""

# Conexão com o banco
con = psycopg2.connect(
    database= DB_NAME,
    user= DB_USER,
    password= DB_PASSWORD,
    host= DB_HOST,
    port= DB_PORT
)

# Criação do cursor
cur = con.cursor()

# Roda o comando SQL
cur.execute(
    """DROP TABLE IF EXISTS minhas_notas ;

    CREATE TABLE minhas_notas (
        id SERIAL PRIMARY KEY,
        titulo VARCHAR(255) NOT NULL,
        descricao TEXT NOT null,
        data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );"""
)
print("Criado")

# Fecha a conexão
con.close()