/*
https://pt.stackoverflow.com/questions/307418/limitar-valor-r-em-campo-input-com-html5-e-css3-com-javascript
*/

function mascara(o, f) {
    v_obj = o
    v_fun = f
    setTimeout("execmascara()", 1)
}

function execmascara() {
    v_obj.value = v_fun(v_obj.value)
}

function mreais(v) {
    v = v.replace(/\D/g, "") //Remove tudo o que não é dígito
    v = v.replace(/(\d{2})$/, ",$1") //Coloca a virgula
    v = v.replace(/(\d+)(\d{3},\d{2})$/g, "$1.$2") //Coloca o primeiro ponto
   
    return v
}

