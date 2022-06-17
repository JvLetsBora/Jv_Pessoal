
function troca(){
    var pessoas = parseInt(document.getElementById("m1").value)
    for (let i = 0; i < pessoas; i++) {
        document.getElementById("contener").innerHTML += "<div class=\"alunos\"><h2>Aluno"+i+"</h2><input type=\"number\" id=\"prova"+i+"\" placeholder=\"nota prova\"><input type=\"number\" id=\"trablho"+i+"\" placeholder=\"nota trabalho\"></div>"
        
    }
}

