
function troca(){
    var pessoas = parseInt(document.getElementById("m1").value)
    var escolha = document.getElementById("escolha").value
    var preco = 0
    if(pessoas > 50 && escolha == "diurno"){
        preco = (pessoas*(200*0.4))
    }else if(escolha == "diurno"){
        preco = pessoas*200
    }else if(pessoas > 50 && escolha == "noturno"){
        preco = (pessoas*(100*0.2))
    }else{preco = pessoas*100 }
    document.getElementById("m2").innerHTML = "O preço total deu: "+preco
}

