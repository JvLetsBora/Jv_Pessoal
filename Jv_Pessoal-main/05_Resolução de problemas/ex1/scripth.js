var x="";
var y=0;
var res =0;
var porta = false;
var v = false;
var opera = "";

function numero(a){
    if(v == false){
        document.getElementById("res").value = "";
        v = true;
    }
    if( porta == false){
         x = a;
         document.getElementById("res").value += x;
         
    }else{ y = a; document.getElementById("res").value += y;}
}

function resultado(){
//     if(opera == "+"){
//         res = parseInt(x)+parseInt(y)  
//     }
//     else if (opera == "-"){
        
//         res = parseInt(x)-parseInt(y);
//     }
//     else if (opera == "*"){
//         res = parseInt(x)*parseInt(y);
//     }
//     else if (opera == "%"){
//         res = parseInt(x)%parseInt(y);
//     }
//     else{res = x/y;
//     document.getElementById("res").value += "/";
//     res = parseInt(x)/parseInt(y);
// }
// document.getElementById("res").value = res;
// v = false;
res = eval(document.getElementById("res").value)
document.getElementById("res").value = res;


}

function operacao(a){
    porta = true;
    opera = a;
    document.getElementById("res").value += a;
}