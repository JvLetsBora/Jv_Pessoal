// Obtém o pop-up
const popup = document.getElementById('popup');
const lista = document.getElementById('conteudo');
const root = 'http://localhost:3000';


// Define uma função para mostrar o pop-up
function mostrarPopup(a) {
    const body_atualizar = document.getElementById('body_atualizar');
    const titulo_atualizar = document.getElementById('titulo_atualizar');
    titulo_atualizar.value = a[1]
    body_atualizar.value = a[2]
    const corpo_at = document.getElementById('atualizador'); 
    corpo_at.innerHTML = `<button type="submit" onclick="atualiza([${a[0]},'${a[1]}','${a[2]}'])">Atualizar</button>`
    popup.style.display = 'block';
}

// Define uma função para fechar o pop-up
function fecharPopup() {
    popup.style.display = 'none';
}


function deletarNota(a){
    confirm("Tem certeza que quer deletar?")

    const url = `${root}/deletar`; 
    const data = {
        id: a
    };

    fetch(url, {
    method: 'DELETE',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
        throw new Error('Não foi possível completar a requisição.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });

    location.reload(true);

    

}

function add() {
    const body_add = document.getElementById('body_add');
    const titulo_add = document.getElementById('titulo_add');
    // URL para a qual você deseja fazer a solicitação POST
    let url = `${root}/add`;

    // Dados que você deseja enviar no corpo da solicitação POST (no formato JSON)
    const dados = {
    titulo: titulo_add.value,
    body_: body_add.value
    };

    // Configuração da solicitação POST
    const configuracao = {
    method: 'POST', // Método HTTP POST
    headers: {
        'Content-Type': 'application/json' // Tipo de conteúdo JSON
    },
    body: JSON.stringify(dados) // Converte os dados em JSON e os envia no corpo da solicitação
    };

    // Fazendo a solicitação POST usando a API Fetch
    fetch(url, configuracao)
    .then(response => {
        // Verifica se a resposta da solicitação foi bem-sucedida (código de status 200)
        if (!response.ok) {
        throw new Error(`Erro HTTP! Código: ${response.status}`);
        }
        
        // Aqui, você pode processar a resposta, se necessário
        return response.json();
    })
    .then(data => {
        // Aqui, você pode lidar com os dados de resposta, se houver algum
        console.log(data);
    })
    .catch(error => {
        // Lida com erros, se houver algum
        console.error('Ocorreu um erro:', error);
    });
}


function atualiza(lista) {
    const body_atualizar = document.getElementById('body_atualizar');
    const titulo_atualizar = document.getElementById('titulo_atualizar');

    const url = `${root}/atualizar`; 
    const data = {
        id: lista[0],
        titulo: `${titulo_atualizar.value}`,
        body_: `${body_atualizar.value}`
    }; 

    fetch(url, {
    method: 'PATCH',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
        throw new Error('Não foi possível completar a requisição.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });

    fecharPopup()
}




// Fazendo a solicitação GET usando a API Fetch
fetch(`${root}/all`)
  .then(response => {
    // Verifica se a resposta da solicitação foi bem-sucedida (código de status 200)
    if (!response.ok) {
      throw new Error(`Erro HTTP! Código: ${response.status}`);
    }
    
    // Converte a resposta em JSON
    return response.json();
  })
  .then(data => {
    // Aqui, você pode trabalhar com os dados recebidos da resposta
    data.forEach(element => {
        lista.innerHTML += `<li id="${element.id}"> <div class="titulo">${element.titulo}</div> <div style="margin: 0px; color: #565656;"> ${element.body} </div> <div id="tools"> <div onclick="mostrarPopup([${element.id},'${element.titulo}','${element.body}'])"><img src="https://cdn-icons-png.flaticon.com/512/1827/1827933.png "></div> <div onclick="deletarNota(${element.id})"><img src="https://cdn-icons-png.flaticon.com/512/484/484611.png "></div> </div> </li>`;
        
    });
  })
  .catch(error => {
    // Lida com erros, se houver algum
    console.error(`Ocorreu um erro: ${error}`);
  });


