const express = require('express'); 
const bodyParser = require('body-parser');
const urlencodedParser = bodyParser.urlencoded({ extended: false })
require("dotenv").config();
const jwt = require("jsonwebtoken");
//const hostname = '127.0.0.1';

const cookieParser = require('cookie-parser');
const port = process.env.PORT || 3000;
const path = require("path")
const sqlite3 = require('sqlite3').verbose();
const app = express();
const DBPATH = 'backend/dbteste.db';

app.use(express.static(path.join(__dirname,"../frontend")));
app.use(express.json());
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

	var db = new sqlite3.Database(DBPATH); // Abre o ban	co
 	var sql = 'SELECT * FROM main ORDER BY id';
	db.all(sql, [],  (err, rows ) => {
		if (err) {
		    throw err;
		
		}
	res.json(rows)
	});
	db.close(); // Fecha o banco
});

// Insere um registro 
app.post('/add', urlencodedParser, (req, res) => {
	res.statusCode = 200;
	res.setHeader('Access-Control-Allow-Origin', '*'); // Isso é importante para evitar o erro 

	sql = `INSERT INTO main (titulo, body_) VALUES ('${req.body.titulo}', '${req.body.body_}')`;
	var db = new sqlite3.Database(DBPATH); // Abre o banco
	console.log(sql);
	db.run(sql, [],  err => {
		if (err) {
		    throw err;
		}
		else console.log(sql);
	});
	db.close(); // Fecha o banco
	res.end();
});

// Atualiza um registro 
app.patch('/atualizar', urlencodedParser, (req, res) => {
	res.statusCode = 200;
	res.setHeader('Access-Control-Allow-Origin', '*'); // Isso é importante para evitar erro

	sql = `UPDATE main SET titulo = '${req.body.titulo}', body_ = '${req.body.body_}' WHERE id = ${req.body.id}`;
	var db = new sqlite3.Database(DBPATH); // Abre o banco
	db.run(sql, [],  err => {
		if (err) {
		    throw err;
		}
		res.end();
	});
	db.close(); // Fecha o banco
});


// Exclui um registro
app.delete('/deletar', urlencodedParser, (req, res) => {
	res.statusCode = 200;
	res.setHeader('Access-Control-Allow-Origin', '*'); // Isso é importante para evitar erro 

	sql = `DELETE FROM main WHERE id = ${req.body.id}`;
	var db = new sqlite3.Database(DBPATH); // Abre o banco
	db.run(sql, [],  err => {
		if (err) {
		    throw err; 
		}
		res.end();
	});
	db.close(); // Fecha o banco
});






app.post("/auth/login", async (req, res) => {
    const { username, password } = req.body;

    // Validações
    if (!username || !password) {
        return res.status(422).json({ msg: "O username e a senha são obrigatórios!" });
    }

    try {
        const sql = `SELECT * FROM users WHERE username = '${username}'`;
        const db = new sqlite3.Database(DBPATH); // Abre o banco

        db.get(sql, [], (err, user) => {
            if (err) {
                throw err;
            }

            if (user && user.password === password) {
                const secret = process.env.SECRET;
                const token = jwt.sign({ id: username }, secret);
				  // Armazene o token em um cookie seguro
				res.cookie('authToken', token, {
					maxAge: 3600000, // Tempo de vida do cookie em milissegundos (1 hora neste caso)
				});

                res.status(200).json({ msg: "Autenticação realizada com sucesso!", token });
            } else {
                res.status(401).json({ msg: "Credenciais inválidas!" });
            }

            db.close(); // Fecha o banco
        });
    } catch (error) {
        res.status(500).json({ msg: "Erro interno do servidor." });
    }
});






/* Inicia o servidor */
app.listen(port, () => {
  console.log(`BD server running at port ${port}`);
});





const db_user = process.env.USER_
const db_password = process.env.PASSWORD_