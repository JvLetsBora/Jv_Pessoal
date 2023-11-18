
function troca(){
    var m1 = document.getElementById("m1").value
    var m2 = document.getElementById("m2").value
    var m3 = document.getElementById("m3").value
    var lista = [m1,m2,m3]
    document.getElementById("res").innerHTML = lista.sort()
}
