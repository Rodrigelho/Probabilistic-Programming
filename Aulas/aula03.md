~~~~
var dado = function(){
  return randomInteger(6) + 1
}

var modelo = function(){
  var d1 = dado()
  var d2 = dado()
  condition( d1 + d2 == 8)
  return {d1,d2}
}

viz.table(Infer(modelo))
~~~~

~~~~
//Se um dos dados for 3 ou mais, qual é a probabilidade da soma ser <6

var dado = function(){
  return randomInteger(6) + 1
}

var modelo = function(){
  var d1 = dado()
  var d2 = dado()
  condition(d1 >=3 || d2>=3)
  condition(d1 + d2 < 6)
  return {d1,d2}
}

viz.table(Infer(modelo))
~~~~

~~~~
//Blackjack

//Se eu tirar 2 cartas, qual é a probabilidade de tirar 16 ou mais?

var valores = mapN(function(x){return x+2},9).concat([10,10,10,11])
var cartas = valores.concat(valores).concat(valores).concat(valores)
var carta = function(){return categorical({vs:cartas})}

var modelo = function(){
  var c1 = carta()
  var c2 = carta()
  var totalp = c1+c2
  var total = totalp == 22 ? 12: totalp
  return total >=16
}

viz.table(Infer(modelo))
~~~~

~~~~
//Blackjack

//Se eu tirar mais uma carta, qual é a probabilidade de a mão inicial rebentar?

var valores = mapN(function(x){return x+2},9).concat([10,10,10,11])
var cartas = valores.concat(valores).concat(valores).concat(valores)
var carta = function(){return categorical({vs:cartas})}

var modelo = function(){
  var c1 = carta()
  var c2 = carta()
  var c3 = carta()
  var totalp = c1+c2
  var total2 = totalp == 22 ? 12: totalp
  var total3 = total2 +c3 > 21 && c3 == 11 ? total2 +1 :total2 + c3
  condition(total3>21)
  return total2
}

viz.table(Infer(modelo))
~~~~

~~~~
//Blackjack

//Se o dealer tem um 10 visível, qual é a probabilidade de eu ganhar sem pedir uma carta?

var valores = mapN(function(x){return x+2},9).concat([10,10,10,11])
var cartas = valores.concat(valores).concat(valores).concat(valores)
var carta = function(){return categorical({vs:cartas})}

var modelo = function(){
  var c1 = carta()
  var c2 = carta()
  var c3 = carta()
  var totalp = c1+c2
  var total2 = totalp == 22 ? 12: totalp
  var totalD = 10 + c3
  return {ganhar: total2 > totalD,cartas: total2}
}

viz(Infer(modelo))
~~~~