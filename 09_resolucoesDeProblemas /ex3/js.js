var lista = ["0","1","2","3","4","5","6","7","8","9",")","(","-"]

function troca(){
    let m1 = document.getElementById("m1").value // 12012012012 ( X X ) X X X X X - X X X X 14
    m1.split()
 
    if(m1.length == 14){
        for (let index = 0; index < m1.length; index++) {
            if(lista.indexOf(m1[index]) > -1){
                console.log(index)
                if(m1[0] == "(" && m1[3] == ")" && m1[9] == "-"){
                    deuBom(m1)
                  } else{erro(m1[0]+" caracter não esperdado"); break;} 
            }else{erro("Erro nos caracteres");break}
        }
    }else if(m1.length < 14){
        erro("Está faltando caracteres")
    }else{erro("Erro nos caracteres")}

    
}

function erro(er){
    let erro = er
    document.getElementById("m2").innerHTML = "Erro na formatação: " + er
}

function deuBom(bom){
    let deu = bom
    document.getElementById("m2").innerHTML = "Está tudo certo: " + deu
}
