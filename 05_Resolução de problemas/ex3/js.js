
// var test = {
//     nome: "meuPal",
//     idade: 90
// }


// export function calcular(a){
//     console.log(test)
//     var b = a
//     console.log(b)

// }


function sorte(){
    var sequencia = document.getElementById("input").value // 1,2,33333,4,5666,9
    var valor = document.getElementById("valor").value // 4
    sequencia = sequencia.split(",")
    sequencia.sort()
    var b= "Sua sequência é: "+ sequencia 
    let n =0
    while (sequencia.length>n){
        sequencia.sort()
        if(sequencia[n] != valor){
            n +=1
        }else{break}
        console.log(n+":"+sequencia.length+": valor "+sequencia[n])
    }
    document.getElementById("sequencia").innerHTML = `${b}<p class=\"especial\">O numero sortido está em ${n+1}° posição dessa sequência</p>`
    }




// split()
// sort()