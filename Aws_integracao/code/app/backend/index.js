const express = require('express');
const bodyParser = require('body-parser');
const urlencodedParser = bodyParser.urlencoded({ extended: false })
require("dotenv").config();
const jwt = require("jsonwebtoken");
const request = require("request")
const cookieParser = require('cookie-parser');
const port = process.env.PORT || 3000;
const path = require("path")


const { Client } = require('pg');
const app = express();
const hostname = 'http://3.209.136.147/predict?';

app.use(express.static(path.join(__dirname,"../frontend")));
app.use(express.json());
app.use(cookieParser());


const dbConfig = {
	user: process.env.DB_USER || "postgres",
	password: process.env.DB_PASSWORD || "aws12345",
	host: process.env.DB_HOST || "db.cydjxbu1izwa.us-east-1.rds.amazonaws.com",
	port: process.env.DB_PORT || "5432",
	database: process.env.DB_NAME || "",
	ssl: {
	  rejectUnauthorized: false
	}
};

const client = new Client(dbConfig);

async function connectToDatabase() {
try {
	await client.connect();
	console.log("Connected to the database");
} catch (error) {
	console.error("Error connecting to the database:", error);
}
}

connectToDatabase();

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
	  const secret = "process.env.SECRET";
  
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
	const new_client = new Client(dbConfig);
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
	const sql = 'INSERT INTO main (titulo, body) VALUES ($1, $2)';
	const new_client = new Client(dbConfig);
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
	const new_client = new Client(dbConfig);
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
	const new_client = new Client(dbConfig);
	await new_client.connect()
	await new_client.query(sql, [req.body.id])
		.then(() => {
		res.end();
		new_client.end()
		})
});


function tratamento(str) {
	var tratado = str.split(":")
	return tratado[0]
}


app.post("/predict", async (req, res) => {
	const {titulo,body_} = req.body
	request(`${hostname}titulo=${titulo}&body_=${body_}`, async (err, res, body)  => {
		const sql = 'INSERT INTO main (labels, y , x) VALUES ($1, $2, $3)';
		const new_client = new Client(dbConfig);
		await new_client.connect()
		await new_client.query(sql, [req.body.titulo, tratamento(req.body.body_), body])
			.then(() => {
			new_client.end()
			})
		
	});
	res.status(200).send("deu bom!")

});



app.post("/auth/login", async (req, res) => {
    const { username, password } = req.body;

    // Validações
    if (!username || !password) {
        return res.status(422).json({ msg: "O username e a senha são obrigatórios!" });
    }

    try {
		const new_client = new Client(dbConfig);
		new_client.connect()
		new_client.query("SELECT * FROM users WHERE username = $1",[username])
		.then(dado=>{
			let dados = dado.rows 
			if (dados[0].username && dados[0].password === password) {
                const secret = 'process.env.SECRET';
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

