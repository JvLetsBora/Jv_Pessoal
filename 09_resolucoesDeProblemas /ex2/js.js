function troca(){
    let m1 = document.getElementById("m1").value // 123
    m1.split()
    let tamanho = m1.length
    var valor = 0
    for (let i = 0; i < tamanho; i++) {
        valor = valor + Number(m1[i])
    }
    document.getElementById("res").innerHTML = "A soma desses termos é "+valor
}