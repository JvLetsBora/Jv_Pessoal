
function troca(){
    var m1 = parseInt(document.getElementById("m1").value)
    var m2 = parseInt(document.getElementById("m2").value)
    var lista =[]
    for (index=m1; index < m2; index++) {
        lista.push(index)
    }
    document.getElementById("res").innerHTML = "{"+lista+","+m2+"}"
}
