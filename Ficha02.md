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
//Exercício 2

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
  var resultadosf = map(myfilter,resultados)
  var results = mapIndexed(function(indice,valor){return (indice+1)*valor},resultadosf)
  return sum(results)
}

var funcaof2 = function(nd,faces){
  return function(){funcaof(nd,faces)}
}

var lancamentos = repeat(10000,funcaof2(5,2))
var lancamentos2 = repeat(10000,funcaof2(2,5))
var lancamentos3 = repeat(10000,funcaof2(4,6))
var lancamentos4 = repeat(10000,funcaof2(2,100))
var lancamentos5 = repeat(10000,funcaof2(100,2))

viz(lancamentos)
viz(lancamentos2)
viz(lancamentos3)
viz(lancamentos4)
viz(lancamentos5)
~~~~

Crie uma função para o sistema Roll & Keep. Represente o histograma para 1k1; 3k1; 5k1; 7k2; 9k4*Click here* to edit me!

~~~~
//Exercicio 3

var valores = [1,2,3,4,5,6,7,8,9,10]

var dado = function(){
  return categorical({vs:valores})
}


var exploding_dices = function(){
  var dado1 = dado()
  if (dado1 == 10){
    return 10 + exploding_dices()
  }
  else{
    return dado1
  }
}

var RollandKeep = function(x,y){
  var valores = repeat(x,exploding_dices)
  var valores_ord = sort(valores)
  //console.log("lançamentos: ",valores_ord)
  valores_ord.splice(0,valores_ord.length-y)
  //console.log("y a manter: ",valores_ord)
  return(sum(valores_ord))
}

var f_repeat = function(x,y){
  return function(){return RollandKeep(x,y)}
}

//var onekone = RollandKeep(1,1)
//var threekone = RollandKeep(3,1)
//var fivekone = RollandKeep(5,1)
//var sevenktwo = RollandKeep(7,2)
//var ninekfour = RollandKeep(9,4)

var lancamentos = repeat(10000,f_repeat(1,1))
var lancamentos2 = repeat(10000,f_repeat(3,1))
var lancamentos3 = repeat(10000,f_repeat(5,1))
var lancamentos4 = repeat(10000,f_repeat(7,2))
var lancamentos5 = repeat(10000,f_repeat(9,4))

viz(lancamentos)
viz(lancamentos2)
viz(lancamentos3)
viz(lancamentos4)
viz(lancamentos5)
~~~~

Crie uma função para o sistema WoD. Represente o histograma do nº de sucessos para vários nºs de dados e TN;

~~~~
//Exercício 4

var valores = [1,2,3,4,5,6,7,8,9,10]

var dado = function(){
  return categorical({vs:valores})
}

var WoD = function(nd,TN){
  var valores = repeat(nd,dado)
  //console.log(valores)
  var lista_sucessos = filter(function(x){return x>=TN},valores)
  var sucessos = lista_sucessos.length
  var lista_fracassos = filter(function(x){return x == 1},valores)
  var fracassos = lista_fracassos.length
  var total = sucessos - fracassos
  //console.log("O jogador teve " + sucessos + " sucessos e "+fracassos+ " fracassos, logo terminou com um total de",total)
  return total
}

var f_repeat = function(nd,TN){
  return function(){return WoD(nd,TN)}
}


var lancamentos = repeat(10000,f_repeat(1,2))
var lancamentos2 = repeat(10000,f_repeat(1,7))
var lancamentos3 = repeat(10000,f_repeat(5,5))
var lancamentos4 = repeat(10000,f_repeat(7,2))
var lancamentos5 = repeat(10000,f_repeat(9,4))
                          
viz(lancamentos)
viz(lancamentos2)
viz(lancamentos3)
viz(lancamentos4)
viz(lancamentos5)
~~~~

Represente graficamente o nº de sucessos para os vários TN usando um heatmap quando se lançam 10 dados;

~~~~
//Exercício 5

var valores = [1,2,3,4,5,6,7,8,9,10]

var dado = function(){
  return categorical({vs:valores})
}

var WoD = function(){
  var TN = randomInteger(9) + 2
  var valores = repeat(10,dado)
  //console.log(valores)
  var lista_sucessos = filter(function(x){return x>=TN},valores)
  var sucessos = lista_sucessos.length
  var lista_fracassos = filter(function(x){return x == 1},valores)
  var fracassos = lista_fracassos.length
  var total = sucessos - fracassos
  //console.log("O jogador teve " + sucessos + " sucessos e "+fracassos+ " fracassos, logo terminou com um total de",total)
  return [TN,total]
}


viz.heatMap(Infer(WoD))
~~~~

Represente um heatmap com o nº de dados vs o nº de sucessos para o TN de 9

~~~~
var valores = [1,2,3,4,5,6,7,8,9,10]

var dado = function(){
  return categorical({vs:valores})
}

var WoD = function(){
  var nd = randomInteger(20)+1
  var TN = 9
  var valores = repeat(10,dado)
  //console.log(valores)
  var lista_sucessos = filter(function(x){return x>=TN},valores)
  var sucessos = lista_sucessos.length
  var lista_fracassos = filter(function(x){return x == 1},valores)
  var fracassos = lista_fracassos.length
  var total = sucessos - fracassos
  //console.log("O jogador teve " + sucessos + " sucessos e "+fracassos+ " fracassos, logo terminou com um total de",total)
  return [nd,total]
}

viz.heatMap(Infer(WoD))
~~~~

Represente graficamente contested rolls de Roll & Keep; veja o impacto dos Traits e Skills;

~~~~
//Exercicio 7

var valores = [1,2,3,4,5,6,7,8,9,10]

var dado = function(){
  return categorical({vs:valores})
}


var exploding_dices = function(){
  var dado1 = dado()
  if (dado1 == 10){
    return 10 + exploding_dices()
  }
  else{
    return dado1
  }
}

var RollandKeep = function(x,y){
  var valores = repeat(x,exploding_dices)
  var valores_ord = sort(valores)
  //console.log("lançamentos: ",valores_ord)
  valores_ord.splice(0,valores_ord.length-y)
  //console.log("y a manter: ",valores_ord)
  return(sum(valores_ord))
}

var ContestedRolls = function(){
  var jogador1 = RollandKeep(2,5)
  var jogador2 = RollandKeep()
}
~~~~