Escreva uma função que receba o número de dados e o número de faces de cada dado e imprima o histograma relativo a 10,000 lançamentos. Represente o histograma para os seguintes valores: 5d2; 2d5; 4d6; 2d100; 100d2;*Click here* to edit me!

~~~~
//Exercício 1

var funcaof = function(nd,faces){
  var prob_faces = mapN(function(){return 1/faces},faces)
  var resultados = multinomial({ps:prob_faces, n:nd})
  var results = mapIndexed(function(indice,valor){return (indice+1)*valor},resultados)
  return sum(results)
}

var fivedtwo = function(){return funcaof(5,2)}
var twodfive = function(){return funcaof(2,5)}
var fourdsix = function(){return funcaof(4,6)}
var twodhundred = function(){return funcaof(2,100)}
var hundreddtwo = function(){return funcaof(100,2)}

var lancamentos = repeat(10000,fivedtwo)
var lancamentos2 = repeat(10000,twodfive)
var lancamentos3 = repeat(10000,fourdsix)
var lancamentos4 = repeat(10000,twodhundred)
var lancamentos5 = repeat(10000,hundreddtwo)

viz(lancamentos)
viz(lancamentos2)
viz(lancamentos3)
viz(lancamentos4)
viz(lancamentos5)
~~~~

Crie uma nova função onde os dados repetidos são removidos;

~~~~
var myfilter = function(x){
  if (x == 0 || x == 1){
    return x
  }
  else if (x > 1){
    return 1
  }
}

var funcaof = function(nd,faces){
  var prob_faces = mapN(function(){return 1/faces},faces)
  var resultados = multinomial({ps:prob_faces, n:nd})
  //console.log(resultados)
  var resultadosf = map(myfilter,resultados)
  //console.log(resultadosf)
  var results = mapIndexed(function(indice,valor){return (indice+1)*valor},resultadosf)
  //console.log(results)
  return sum(results)
}

var fivedtwo = function(){return funcaof(5,2)}
var twodfive = function(){return funcaof(2,5)}
var fourdsix = function(){return funcaof(4,6)}
var twodhundred = function(){return funcaof(2,100)}
var hundreddtwo = function(){return funcaof(100,2)}

var lancamentos = repeat(1,fivedtwo)
var lancamentos2 = repeat(10000,twodfive)
var lancamentos3 = repeat(10000,fourdsix)
var lancamentos4 = repeat(10000,twodhundred)
var lancamentos5 = repeat(10000,hundreddtwo)


viz(lancamentos)
viz(lancamentos2)
viz(lancamentos3)
viz(lancamentos4)
viz(lancamentos5)
~~~~

Crie uma função para o sistema Roll & Keep. Represente o histograma para 1k1; 3k1; 5k1; 7k2; 9k4*Click here* to edit me!

~~~~
var funcaof = function(nd,faces){
  var prob_faces = mapN(function(){return 1/faces},faces)
  var resultados = multinomial({ps:prob_faces, n:nd})
  //console.log(resultados)
  var resultadosf = map(myfilter,resultados)
  //console.log(resultadosf)
  var results = mapIndexed(function(indice,valor){return (indice+1)*valor},resultadosf)
  //console.log(results)
  return sum(results)
}
~~~~