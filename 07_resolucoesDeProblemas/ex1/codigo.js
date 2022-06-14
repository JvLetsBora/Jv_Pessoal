var p = parseInt(document.getElementById("inP").value)
var v = parseInt(document.getElementById("inV").value)


function pMais(){
    p = parseInt(document.getElementById("inP").value)
    document.getElementById("inP").value = p + 1
    console.log(p)
}

function vMais(){
    v = parseInt(document.getElementById("inV").value)
    document.getElementById("inV").value = v + 1
    console.log(v)
}