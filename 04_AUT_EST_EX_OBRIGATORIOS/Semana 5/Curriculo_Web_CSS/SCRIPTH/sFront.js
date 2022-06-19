
const rodape = document.getElementById("rodape")
rodape.onload = geraTabela()

// // Requisição por Ajax
// function geraTabela(){
//     //Objeto request
//     let request = new XMLHttpRequest(); 
//     //Criar a função do pedido
//     request.onreadystatechange = function(){
//         let MyJson = JSON.parse(this.responseText)
//         console.log(MyJson[0].name + "jaisonnnn")
//         let MyJsonSize = MyJson.length
//         document.getElementById("Meu-TR").innerHTML = `<tr><td>id</td><td>Nome</td><td>Data</td></tr>`
//         for(let i = 0; i < MyJsonSize; i++ ){
//             document.getElementById("Meu-TR").innerHTML += '<tr id="' + MyJson[i].id + '"> <td>' + MyJson[i].id +'</td><td>'+ MyJson[i].name +'</td><td>'+ MyJson[i].date +'</td><td>' + '<a href="#" class="btndelete" > Remover </a>'  + '</td> </tr>'
//         }
//         console.log(JSON.parse(this.responseText))
//     }

//     //Faz o pedido
//     url = "http://localhost:3063/acessos"
//     request.open("GET", url, true);
//     request.send();
// }

// Post por ajax
function enviaAcesso(){
    const nameInput = document.getElementById("input1").value
    const dateInput = Number(document.getElementById("input2").value)
    url = "/adicionaracesso"
    $.ajax({
        type: "POST",
        url: url,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify(
            {
                "name": nameInput,
                "date": dateInput
            }
        )
    });
}

// Delete por ajax
$(document).ready(function(){
    $('body').on('click', '.btndelete', function (e) {
        idTable = $(this).closest('tr').attr('id')
      $.ajax({
        url: "/deletaracesso",
        data: { id: idTable},
        type: "Delete",
        dataType: "Json",
      });
      $("#"+idTable).remove();
    });
  });