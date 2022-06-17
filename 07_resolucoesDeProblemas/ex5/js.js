var alunos = new Map(); // alunos.has('chave')

function troca(){
    var pessoas = parseInt(document.getElementById("m1").value)
    for (let i = 0; i < pessoas; i++) {
        document.getElementById("contener").innerHTML += "<div class=\"alunos\"><h2>Aluno"+i+"</h2><input type=\"number\" id=\"prova"+i+"\" placeholder=\"nota prova\"><input type=\"number\" id=\"trablho"+i+"\" placeholder=\"nota trabalho\"></div>"
        alunos.set("aluno"+i,[0,0])
    }
    document.getElementById("m3").innerHTML = "<button onclick=\"media()\">Calcular</button>"
}

function media(){
    console.log(alunos)
    for (let i = 0; i < alunos.size; i++) {
        let teste = eval('"aluno"+i')
        let test2 = eval('"prova"+i')
        let test3 = eval('"trablho"+i')
        var a = alunos.get(teste)[0] = document.getElementById(test2).value
        var b = alunos.get(teste)[1] = document.getElementById(test3).value
        var media = (parseInt(a) + parseInt(b))/2
        document.getElementById("m3").innerHTML += "<div>"+"Media do aluno"+i+": "+media+"</div>"
    }
    
}