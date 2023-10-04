const express = require('express');
const bodyParser = require('body-parser');
const urlencodedParser = bodyParser.urlencoded({ extended: false })
require("dotenv").config();
const jwt = require("jsonwebtoken");

const cookieParser = require('cookie-parser');
const port = process.env.PORT || 3000;
const path = require("path")



const client = require('pg').Client; 
const app = express();


app.use(express.static(path.join(__dirname,"../frontend")));
app.use(express.json());

var confTable =  async(res) => {
	try {
		const new_client = new client({
		user:"postgres",
			password:"senha",
			host: "db",
			port:"5432",
			database:"postgres"
		})
		new_client.connect()
		// Criação da tabela no PostgreSQL
		await new_client.query(`
		CREATE TABLE IF NOT EXISTS users (
			id SERIAL PRIMARY KEY,
			username VARCHAR(100) NOT NULL,
			password VARCHAR(100) UNIQUE NOT NULL
		);
		CREATE TABLE IF NOT EXISTS main (
			id SERIAL PRIMARY KEY,
			titulo VARCHAR(100) NOT NULL,
			body VARCHAR(100) UNIQUE NOT NULL
		);
		`).finally(()=>{
		new_client.end()
	});
	console.log("Deu bom")
  } catch (error) {
		console.error('Erro ao criar tabela:', error);
  }
  try {
	const new_client = new client({
		user:"postgres",
		password:"senha",
		host: "db",
		port:"5432",
		database:"postgres"
	})
	const sql = 'INSERT INTO users (username, password) VALUES ($1, $2)';
	await new_client.connect()
	await new_client.query(sql, ["teste", "teste123"])
		.then(() => {
		new_client.end()
		})
	console.log("User teste criado!")
  } catch (error) {
	console.error('Erro ao criar tabela:', error);
  }
}



confTable()

app.use(cookieParser());


// Definição das rotas 
app.get('/app',checkToken, (req, res) => {
    // Acesse o caminho do arquivo HTML que deseja servir
    const htmlFilePath = path.join(__dirname, '../frontend/', 'app.html');
	
    // Envie o arquivo HTML como resposta
    res.sendFile(htmlFilePath);
});

function checkToken(req, res, next) {
	const token = req.cookies.authToken;
  
	if (!token) return res.status(401).json({ msg: "Acesso negado!" });
  
	try {
	  const secret = process.env.SECRET;
  
	  jwt.verify(token, secret);
  
	  next();
	} catch (err) {
	  res.status(400).json({ msg: "O Token é inválido!" });
	}
  }


// Retorna todos registros 
app.get('/all', (req, res) => {
	res.statusCode = 200;
	res.setHeader('Access-Control-Allow-Origin', '*'); // Isso é importante para evitar o erro de CORS
	const new_client = new client({
		user:"postgres",
		password:"senha",
		host: "db",
		port:"5432",
		database:"postgres"
	})
	new_client.connect()
	new_client.query("SELECT * FROM main")
	.then(dado=>{
		let dados = dado.rows
		res.json(dados)
	})
	.finally(()=>{
		new_client.end()
	});
	
});

// Insere um registro 
app.post('/add', urlencodedParser, async (req, res) => {
	res.statusCode = 200;
	res.setHeader('Access-Control-Allow-Origin', '*'); // Isso é importante para evitar o erro 
	const new_client = new client({
		user:"postgres",
		password:"senha",
		host: "db",
		port:"5432",
		database:"postgres"
	})
	const sql = 'INSERT INTO main (titulo, body) VALUES ($1, $2)';
	await new_client.connect()
	await new_client.query(sql, [req.body.titulo, req.body.body_])
		.then(() => {
		res.end();
		new_client.end()
		})
		res.end();
});

// Atualiza um registro 
app.patch('/atualizar', urlencodedParser, async (req, res) => {
	res.statusCode = 200;
	res.setHeader('Access-Control-Allow-Origin', '*'); // Isso é importante para evitar erro

	sql = `UPDATE main SET titulo = $1, body = $2 WHERE id = $3`;
	const new_client = new client({
		user:"postgres",
		password:"senha",
		host:"db",
		port:"5432",
		database:"postgres"
	})
	await new_client.connect()
	await new_client.query(sql, [req.body.titulo, req.body.body_, req.body.id])
		.then(() => {
		res.end();
		new_client.end()
		})
		res.end();
});


// Exclui um registro
app.delete('/deletar', urlencodedParser, async (req, res) => {
	res.statusCode = 200;
	res.setHeader('Access-Control-Allow-Origin', '*'); // Isso é importante para evitar erro 

	sql = `DELETE FROM main WHERE id = $1`;
	const new_client = new client({
		user:"postgres",
		password:"senha",
		host:"db",
		port:"5432",
		database:"postgres"
	})
	await new_client.connect()
	await new_client.query(sql, [req.body.id])
		.then(() => {
		res.end();
		new_client.end()
		})
});






app.post("/auth/login", async (req, res) => {
    const { username, password } = req.body;

    // Validações
    if (!username || !password) {
        return res.status(422).json({ msg: "O username e a senha são obrigatórios!" });
    }

    try {
		const new_client = new client({
			user:"postgres",
			password:"senha",
			host:"db",
			port:"5432",
			database:"postgres"
		})
		new_client.connect()
		new_client.query("SELECT * FROM users WHERE username = $1",[username])
		.then(dado=>{
			let dados = dado.rows 
			if (dados[0].username && dados[0].password === password) {
                const secret = process.env.SECRET;
                const token = jwt.sign({ id: username }, secret);
				  // Armazene o token em um cookie seguro
				res.cookie('authToken', token, {
					maxAge: (3600*100), // Tempo de vida do cookie em milissegundos (1 hora neste caso)
				});

                res.status(200).json({ msg: "Autenticação realizada com sucesso!", token });
            } else {
                res.status(401).json({ msg: "Credenciais inválidas!" });
            }
		})
		.finally(()=>{
			new_client.end()
		});

    } catch (error) {
        res.status(500).json({ msg: "Erro interno do servidor." });
    }
});






/* Inicia o servidor */
app.listen(port, () => {
  console.log(`Backend server running at port ${port}`);
});

