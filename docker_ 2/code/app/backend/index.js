const express = require('express'); 
const bodyParser = require('body-parser');
const urlencodedParser = bodyParser.urlencoded({ extended: false })
//const hostname = '127.0.0.1';

const port = process.env.PORT || 3000;
const path = require("path")
const sqlite3 = require('sqlite3').verbose();
const app = express();
const DBPATH = 'dbteste.db';

app.use(express.static(path.join(__dirname,"../frontend")));
app.use(express.json());


/* Definição das rotas  


// Retorna todos registros
app.get('/profissionais', (req, res) => {
	res.statusCode = 200;
	res.setHeader('Access-Control-Allow-Origin', '*'); // Isso é importante para evitar o erro de CORS

	var db = new sqlite3.Database(DBPATH); // Abre o ban	co
 	var sql = 'SELECT * FROM PROFISSIONAIS ORDER BY idFunc';
	db.all(sql, [],  (err, rows ) => {
		if (err) {
		    throw err;
		
		}
	res.json(rows)
	});
	db.close(); // Fecha o banco
});

// Insere um registro 
app.post('/alocacao/adicionar', urlencodedParser, (req, res) => {
	res.statusCode = 200;
	res.setHeader('Access-Control-Allow-Origin', '*'); // Isso é importante para evitar o erro 

	sql = `INSERT INTO ALOCACAO (idFunc, idProject, horasAlocadasProjeto, mes, ano) VALUES (${req.body.idFunc}, ${req.body.idProject}, ${req.body.horasAlocadasProjeto}, '${req.body.mes}', ${req.body.ano})`;
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
app.patch('/alocacao/atualizar', urlencodedParser, (req, res) => {
	res.statusCode = 200;
	res.setHeader('Access-Control-Allow-Origin', '*'); // Isso é importante para evitar erro

	sql = `UPDATE ALOCACAO SET horasAlocadasProjeto = ${req.body.horasAlocadasProjeto}, mes = '${req.body.mes}', ano = ${req.body.ano} WHERE idAlocacao = ${req.body.idAlocacao}`;
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
app.delete('/alocacao/deletar', urlencodedParser, (req, res) => {
	res.statusCode = 200;
	res.setHeader('Access-Control-Allow-Origin', '*'); // Isso é importante para evitar erro 

	sql = `DELETE FROM ALOCACAO WHERE idAlocacao = ${req.body.idAlocacao}`;
	var db = new sqlite3.Database(DBPATH); // Abre o banco
	db.run(sql, [],  err => {
		if (err) {
		    throw err; 
		}
		res.end();
	});
	db.close(); // Fecha o banco
});


*/

/* Inicia o servidor */
app.listen(port, () => {
  console.log(`BD server running at port ${port}`);
});