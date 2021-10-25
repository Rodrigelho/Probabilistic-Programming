~~~~
var id = function(x) {return x}
var succ = function(x){return x+1}
var prod = function(x,y) {return x*y}
var quad = function (x) {return x*x}
var cubo = function(x) {return x*quad(x)}

viz.line(mapN(succ(100)),mapN(function (x){return quad(succ(x))},100))

var numeros = mapN(function(x){return x-50},100)
viz.line(numeros,map(cubo,numeros))

console.log(map2(prod, [1,2,3], [4,5,6]))

console.log(mapIndexed(prod,[4,5,6,7]))

//Calcula o fatorial de 20

reduce(function(x,acc){return x* acc},1,mapN(succ,20))
~~~~

~~~~
var divisivel = function(num,primos){
  return any(function(p){
       return num %p ==0
             },primos)
}

var iterar = function(x,acc){
  if(divisivel(x,acc)) {
    return acc}
  else{
    return acc.concat(x)
  }
  }

var limite = 100
var numeros_ao_contrario = mapN(function(x){return limite-x}, limite-1)
reduce(iterar,[], numeros_ao_contrario)
~~~~

Exemplos de programação funcional

~~~~
var id = function(x) { return x }
var succ = function(x) { return x + 1 }
var prod = function(x, y) { return x * y }
var quad = function(x) {return x * x }
var cubo = function(x) { return x * quad(x) }

viz.line(mapN(succ, 100), mapN(function(x) {return quad(succ(x))}, 100))

var numeros = mapN(function(x) {return x - 50}, 100)
viz.line(numeros, map(cubo, numeros))

console.log(map2(prod, [1,2,3], [4,5,6]))

console.log(mapIndexed(prod, [4,5,6,7]))

// Calcula o fatorial de 20
reduce(function(x, acc) {return x*x + acc}, 1, mapN(succ, 20))
~~~~

Mais complicado

~~~~
var divisivel = function(num, primos) {
  var D = function(p) {
    return num % p == 0
  }
  return any(D, primos)
}

var iterar = function(x, acc){
  console.log(x, acc)
  if (divisivel(x, acc)) {
    return acc
  } else{
    return acc.concat(x)
  }
}

var limite = 20
var numeros_ao_contrario = mapN(function(x) {return limite - x}, limite - 1)
console.log(numeros_ao_contrario)
reduce(iterar, [], numeros_ao_contrario)
~~~~