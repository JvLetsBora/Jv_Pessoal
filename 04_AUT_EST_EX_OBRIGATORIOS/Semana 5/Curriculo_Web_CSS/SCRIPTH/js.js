function clicou(){
    alert("Houve um click");
    prompt("Empresa", "Tarefa");
    
}


 // Requisição por Ajax
 function atualizarItens(){
     //Objeto request
     let request = new XMLHttpRequest(); 
     //Criar a função do pedido
     request.onload = function(){
         let MyJson = JSON.parse(this.responseText)// [{Key:value},{Key:value},{Key:value}]
         let MyJsonSize = MyJson.length
         for(let i = 0; i < MyJsonSize; i++ ){ // <div class="conteudo" MyJson[i].id> <div> MyJson[i].id </div> <div> Nome: MyJson[i].name </div> <div> Numero MyJson[i].date </div> <a href="#" class="btndelete" > Remover </a></div>
             document.getElementById("Meu-TR").innerHTML += "<div class=\"conteudo\"" + MyJson[i].id +"> <div>"+ MyJson[i].id+" </div> <div> Nome: "+MyJson[i].name +"</div> <div> Numero: "+ MyJson[i].date +"</div> <a href=\"#\" class=\"btndelete\" > Remover </a></div>"
         }
         console.log(JSON.parse(this.responseText))
     }

     //Faz o pedido
     url = "http://localhost:3063/acessos"
     request.open("GET", url, true);
     request.send();
 }

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