var p = parseInt(document.getElementById("inP").value)



function pMais(){
    p = parseInt(document.getElementById("inP").value) + 1
    document.getElementById("inP").value = p 
    console.log(p)
    atualizar()
}

function vMais(){
    p = parseInt(document.getElementById("inP").value) - 1
    document.getElementById("inP").value = p
    console.log(p)
    atualizar()
}

function atualizar(){
    var v = document.getElementById("inV").value
    var res = document.getElementById("res")
    res.innerHTML = "Ficou: "+eval("p * v")
}