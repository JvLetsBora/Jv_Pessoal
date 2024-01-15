function clicou(){
    alert("Houve um click");
    prompt("Empresa", "Tarefa");
}

function clicou(){
        alert(( (1.69-1.69)**2+ (1.62-1.69)**2+ (1.66-1.69)**2+ (1.64-1.69)**2+ (1.81-1.69)**2+ (1.66-1.69)**2+ (1.73-1.69)**2+ (1.69-1.69)**2+ (1.74-1.69)**2+ (1.66-1.69)**2)/10);
        var a = prompt("Empresa", "Tarefa");
        document.write("<div id=\"span\"><h1>\"${a}\"</h1><h2>Competências:</h2><ol><li class=\"efect\">Pacote Adobe</li><li class=\"efect\">Pacote Ofice</li><li class=\"efect\">Inlgles <i>Basíco</i></li><li class=\"efect\"><p>7 Anos de Estudos Sobre<a href=\"https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img\">Design</a></p></li></ol><div class=\"moreEfec\"><h2><button onclick=\"clicou()\">Referencias Profissionais:</button></h2></div><ul id=\"itens\"><li><p><h3>StorIn</h3><strong>Arte Finalista</strong><br>Era responsável por elaborar peças gráficas para o site StorIn.com e produtos para o público infantil<br><h3>Inteli</h3><strong>Estágiario de Marketing</strong><i> trabalho atual</i><br>Elaboro peças visuais e ajudo com ideias para Marketing.</p></li></ul><a href=\"https://www.linkedin.com/in/jo%C3%A3o-vitor-oliveira-3b8253219/\"><img src=\"logolinkedin.png\" alt=\"linkedin\"></a></div><footer><p>@ JV Compane 2022 <br> me mande sua <a href=\"https://wa.me/11948701514whatsapp?text=urldamensagempront\">menssagem</a> </p></footer>");


    }
 
        var i = 1;
        var k = 0;
        var j = 0;
        function jq(){
            if( i == 1){
                $("li").css("color","tomato");
                $("#jq").css("color","violet");
                i -=1;
                k += 1;
                j += 1;
            }else{
                $("li").css("color","black");
                $("#jq").css("color","black");
                i = 1;
                k += 1;
            }
            if(k>=10){
                let seg = prompt("Quantos segundos?")
                let b = 0;
                while(b <= (parseInt(seg)*600)){
                    $("li").css("color","violet");
                    $("#jq").css("color","violet");
                    $("li").css("color","black");
                    $("#jq").css("color","black");
                    b +=1;
                }
                alert("Egg, Numero de click: "+j);
                k = -10;

            }
                
        }
