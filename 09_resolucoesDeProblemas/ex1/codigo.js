



function calcular(){
    var valor = document.getElementById("btn").value
    valor.split()
    var teste = Number( valor[0])
    var resposta = "nulo"
    if(teste % 2 == 0 ){
        resposta = "par, digite outro numero"
    }else(resposta="impar, boa!")
    document.getElementById("res").innerHTML = "O valor da dezena é "+teste+" Logo é "+resposta
}
