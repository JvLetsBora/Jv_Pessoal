// Obtém o pop-up
const popup = document.getElementById('popup');
const lista = document.getElementById('conteudo');



// Define uma função para mostrar o pop-up
function mostrarPopup() {
    popup.style.display = 'block';
}

// Define uma função para fechar o pop-up
function fecharPopup() {
    popup.style.display = 'none';
}


function deletarNota(a){
    confirm(a)
}

function add(a) {
    const body_add = document.getElementById('body_add');
    const titulo_add = document.getElementById('titulo_add');
    var titulo_ = titulo_ = titulo_add.value
    var body_ = body_ = titulo_add.value
    lista.innerHTML += `<li id="2"> <div class="titulo">${titulo_}</div> <div style="margin: 0px; color: #565656;"> ${body_} </div> <div id="tools"> <div onclick="mostrarPopup()"><img src="https://cdn-icons-png.flaticon.com/512/1827/1827933.png "></div> <div onclick="deletarNota(${a})"><img src="https://cdn-icons-png.flaticon.com/512/484/484611.png "></div> </div> </li>`;
}


function atualiza(params) {
    const body_atualizar = document.getElementById('body_atualizar');
    const titulo_atualizar = document.getElementById('titulo_atualizar');
    let titulo_ = titulo_atualizar.value
    let body_ = body_atualizar.value
}