Escreva uma função que receba o número de dados e o número de faces de cada dado e imprima o histograma relativo a 10,000 lançamentos. Represente o histograma para os seguintes valores: 5d2; 2d5; 4d6; 2d100; 100d2;*Click here* to edit me!

~~~~
//Exercício 1

//Função que recebe o número de dados e as faces de cada dado e devolve a soma dos lançamentos
var funcaof = function(nd,faces){
  var prob_faces = mapN(function(){return 1/faces},faces)  //lista com as probabilidades
  var resultados = multinomial({ps:prob_faces, n:nd})  //Distribuição multinomial
  var results = mapIndexed(function(indice,valor){return (indice+1)*valor},resultados)
  return sum(results)
}

//Estas funções servem apenas para se poder fazer o repeat
var fivedtwo = function(){return funcaof(5,2)}
var twodfive = function(){return funcaof(2,5)}
var fourdsix = function(){return funcaof(4,6)}
var twodhundred = function(){return funcaof(2,100)}
var hundreddtwo = function(){return funcaof(100,2)}

//Os lançamentos para cada um dos casos (5d2,2d5,etc)
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

//Função que filtra a lista dos resultados removendo elementos repetidos
var myfilter = function(x){
  if (x == 0 || x == 1){
    return x
  }
  else if (x > 1){
    return 1
  }
}

/*Esta função é igual à do exercício anterior mas agora aplicamos a função myfilter à lista
dos resultados para remover os dados repetidos*/
var funcaof = function(nd,faces){
  var prob_faces = mapN(function(){return 1/faces},faces)
  var resultados = multinomial({ps:prob_faces, n:nd})
  var resultadosf = map(myfilter,resultados)
  var results = mapIndexed(function(indice,valor){return (indice+1)*valor},resultadosf)
  return sum(results)
}

//Função para podermos fazer o repeat
var funcaof2 = function(nd,faces){
  return function(){funcaof(nd,faces)}
}

//Os lançamentos para cada um dos casos
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

//Valores das 10 faces para cada dado
var valores = [1,2,3,4,5,6,7,8,9,10]

//Função que lança um dado
var dado = function(){
  return categorical({vs:valores})
}

/*Função que lança um dado e, se esse dado for 10, repete a função até ao dado explodir
(não sair 10) e devolve o valor final*/
var exploding_dices = function(){
  var dado1 = dado()
  if (dado1 == 10){
    return 10 + exploding_dices()
  }
  else{
    return dado1
  }
}

/*Função que recebe 2 argumentos (traits e skills) e lança x dados, ordena a lista
dos resultados dos lançamentos e depois remove da lista os menores elementos, mantendo
apenas y dados na lista. Depois, devolve a soma desses y dados*/
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

/*Função que lança nd dados, cria uma lista com os sucessos e uma com os fracassos.
Assim, o comprimento da lista de sucessos é o número de sucessos e o comp. da lista
de fracassos é o número de fracassos. Depois, devolve o nº total de 
sucessos = sucessos-fracassos*/
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

/*Função igual à alínea anterior mas agora escolhe um TN à sorte entre 2 e 10 e
lança 10 dados, devolvendo uma lista com o TN e o total de sucessos para o heatmap*/
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

//Faz o heatmap
viz.heatMap(Infer(WoD))
~~~~

Represente um heatmap com o nº de dados vs o nº de sucessos para o TN de 9

~~~~
//Exercício 6

var valores = [1,2,3,4,5,6,7,8,9,10]

var dado = function(){
  return categorical({vs:valores})
}

/*Função praticamente igual à alínea anterior mas escolhe um nd à sorte entre 1 e 20
para um TN=9 e devolve uma lista com o nd e o total de sucessos para o heatmap*/
var WoD = function(){
  var nd = randomInteger(20)+1
  var TN = 9
  var valores = repeat(nd,dado)
  //console.log("valores: ",valores)
  var lista_sucessos = filter(function(x){return x>=TN},valores)
  //console.log("Lista de sucessos: ",lista_sucessos)
  var sucessos = lista_sucessos.length
  var lista_fracassos = filter(function(x){return x == 1},valores)
  //console.log("Lista de fracassos: ",lista_fracassos)
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

/*2 jogadores jogam um contra o outro e retorna 0 caso o jogador 1 tenha ganho,
1 caso o jogador 2 tenha ganho e 2 caso tenham empatado*/
var contestedRk = function(x1,y1,x2,y2){
  var jogador1 = RollandKeep(x1,y1)
  var jogador2 = RollandKeep(x2,y2)
  if (jogador1 > jogador2){return 0}
  else if (jogador1 == jogador2) {return 2}
  else {return 1}
}

var f_repeat = function(x1,y1,x2,y2){
  return function(){return contestedRk(x1,y1,x2,y2)}
}


console.log("O impacto dos traits e das skills pode ser previsto na maior parte dos casos.")
console.log("Vamos estudar o impacto em casos mais complicados, na gama dos 4 e 5 traits+skills")

var r4k4vsr5k3 = f_repeat(4,4,5,3) //jogador 1 tem 4k4 e jogador 2 tem 5k3
var r4k3vsr5k2 = f_repeat(4,3,5,2)
var r4k2vsr5k1 = f_repeat(4,2,5,1)
var r5k5vsr6k4 = f_repeat(5,5,6,4)
var r6k6vsr7k5 = f_repeat(6,6,7,5)

// 0-Jogador1 ganhou; 1-Jogador2 ganhou;2-Empate
viz(Infer({method:'rejection',samples:5000},r4k4vsr5k3))
viz(Infer({method:'rejection',samples:5000},r4k3vsr5k2))
viz(Infer({method:'rejection',samples:5000},r4k2vsr5k1))

console.log("Quando um jogador tem nkn e o outro tem n+1kn-1, os jogos são equilibrados, como podemos ver pelo primeiro gráfico dos que estão acima")
console.log("Ainda assim, é melhor ter n+1kn-1, embora a diferença seja pequena:")

viz(Infer({method:'rejection',samples:5000},r5k5vsr6k4))
viz(Infer({method:'rejection',samples:5000},r6k6vsr7k5))
~~~~

Represente graficamente contested rolls de WoD; veja o impacto no nº de dados.

~~~~
//Exercício 8

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

/*2 jogadores jogam um contra o outro e retorna 0 caso o jogador 1 tenha ganho,
1 caso o jogador 2 tenha ganho e 2 caso tenham empatado*/
var contestedWoD = function(nd1,nd2,TN){
  var jogador1 = WoD(nd1,TN)
  var jogador2 = WoD(nd2,TN)
  if (jogador1 > jogador2){return 0}
  else if (jogador1 == jogador2) {return 2}
  else {return 1}
}

var f_repeat = function(nd1,nd2,TN){
  return function(){return contestedWoD(nd1,nd2,TN)}
}

var nd5vsnd6TN5 = f_repeat(5,6,5) //jogador 1 tem 5 dados e jogador 2 tem 6 dados para um TN de 5
var nd5vsnd6TN2 = f_repeat(5,6,2) //padrão igual ao de cima
var nd5vsnd6TN9 = f_repeat(5,6,9)
var nd3vsnd7TN9 = f_repeat(3,7,9)
var nd1vsnd10TN10 = f_repeat(1,10,10)

//0-Jogador1 ganhou; 1-Jogador2 ganhou;2-Empate
viz(Infer({method:'rejection',samples:5000},nd5vsnd6TN2))
viz(Infer({method:'rejection',samples:5000},nd5vsnd6TN5))
viz(Infer({method:'rejection',samples:5000},nd5vsnd6TN9))

console.log("De uma forma geral, quantos mais dados se tiver, maior é a probabilidade de ganhar.")
console.log("No entanto, o impacto do número de dados é maior para um TN baixo")

console.log("Só para um TN muito alto é que pode compensar ter menos dados, mas tem de ser uma diferença grande, como podemos ver neste caso entre 1 e 10 dados para um TN de 10")

viz(Infer({method:'rejection',samples:5000},nd1vsnd10TN10))
~~~~