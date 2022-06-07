function calcular(){
    var a = document.getElementById("input").value; // 725
    var b = 0;
    var valor = 0
    var vezes = {
        cem:0,
        cin:0,
        vin:0,
        dez:0,
        cinc:0,
        dos:0,
        um:0
    };
    b=a;
    valor=b;
    if(a % 100 >= 0 ){
        b = valor%100
        vezes.cem = (valor - b)/100
        b = valor - b
        valor = valor - b
    }
    if(b%50 >= 0){
        b = valor%50
        vezes.cin = (valor - b)/50
        b = valor - b
        valor = valor - b
    }
    if(b%20 >= 0){
        b = valor%20
        vezes.vin = (valor - b)/20
        b = valor - b
        valor = valor - b

    }
    if(b%10 >= 0){
        b = valor%10
        vezes.dez = (valor - b)/10
        b = valor - b
        valor = valor - b
    }
    if(b%5 >= 0){
        b = valor%5
        vezes.cinc = (valor - b)/5
        b = valor - b
        valor = valor - b
    }
    if(b % 2 >= 0){
        b = valor%2
        vezes.dos = (valor - b)/2
        b = valor - b
        valor = valor - b
    }
    vezes.um = valor
    if((vezes.um*1) + (vezes.dos*2) + (vezes.cinc*5) + (vezes.dez*10) + (vezes.vin*20) + (vezes.cin*50) + (vezes.cem*100) == a){
        document.getElementById("valor").innerHTML = "Para chegar ao valor de "+"R$ "+a+", você ira precisar de "+"<br>"+vezes.cem+" notas de 100;"+"<br>"+vezes.cin+" notas de 50;"+"<br>"+vezes.vin+" notas de 20;"+"<br>"+vezes.dez+" notas de 10;"+"<br>"+vezes.cinc+" notas de 5;"+"<br>"+vezes.dos+" notas de 2;"+"<br>"+vezes.um+" notas de 1;";
    }else{document.getElementById("valor").innerHTML = "<h3>ERRO:</h3>"+(vezes.um*1) +"; " + (vezes.dos*2) +"; " + (vezes.cinc*5) +"; " + (vezes.dez*10) +"; " + (vezes.vin*20) +"; " + (vezes.cin*50) +"; "+ (vezes.cem*100)}
    
}