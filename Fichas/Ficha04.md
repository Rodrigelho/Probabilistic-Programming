# Crie uma função sondagens(tamanho) que gere sondagens baseada nas probabilidades dadas abaixo

~~~~
var perc = {"ps":36.34,"psd":27.76,"cdu":6.33,"cds":4.22, "be":9.52,
  "pan":3.32,"chega":1.29,"il":1.29, "livre":1.09, "indecisos":8.84}

var pares = _.toPairs(perc)
var tuplo = _.unzip(pares)

var tamanho = 1000

var sondagens = function(tamanho){
  var result = multinomial({ps:map(function(x) {return x/100},_.values(perc)),n:tamanho})
  var sondagem_resultado =_.fromPairs(_.zip(tuplo[0], result))
  return sondagem_resultado
}

sondagens(tamanho)
~~~~

## Utilizando os resultados da sondagem, crie um modelo para as probabilidades de um eleitor votar em cada partido

~~~~
var perc = {"ps":36.34,"psd":27.76,"cdu":6.33,"cds":4.22, "be":9.52,
  "pan":3.32,"chega":1.29,"il":1.29, "livre":1.09, "indecisos":8.84}

var tamanho = 5000

var sondagens = function(tamanho){
  var result = multinomial({ps:map(function(x) {return x/100},_.values(perc)),n:tamanho})
  var sondagem_resultado =_.fromPairs(_.zip(_.keys(perc), result))
  return sondagem_resultado
}

var lista = sondagens(tamanho)

var modelo = function(){
  var probs = repeat(_.values(perc).length,function(){uniform({a:0,b:1})})
  var probs_normalizadas = map(function(x){return x/sum(probs)},probs)
  var dist = Multinomial({ps:probs_normalizadas,n:tamanho})
  observe(dist,_.values(lista))
  return _.fromPairs(_.zip(_.keys(lista),probs_normalizadas))
}

viz.marginals(Infer({method:'MCMC',samples: 5000},function(){modelo()}))
~~~~

Use o estimador do High Density Interval para estimar o intervalo da probabilidade para cada partido

~~~~
var perc = {"ps":36.34,"psd":27.76,"cdu":6.33,"cds":4.22, "be":9.52,
  "pan":3.32,"chega":1.29,"il":1.29, "livre":1.09, "indecisos":8.84}

var tamanho = 5000

var sondagens = function(tamanho){
  var result = multinomial({ps:map(function(x) {return x/100},_.values(perc)),n:tamanho})
  var sondagem_resultado =_.fromPairs(_.zip(_.keys(perc), result))
  return sondagem_resultado
}

var lista = sondagens(tamanho)

var modelo = function(){
  var probs = repeat(_.values(perc).length,function(){uniform({a:0,b:1})})
  var probs_normalizadas = map(function(x){return x/sum(probs)},probs)
  var dist = Multinomial({ps:probs_normalizadas,n:tamanho})
  observe(dist,_.values(lista))
  return _.fromPairs(_.zip(_.keys(lista),probs_normalizadas))
}

var dist = Infer({method:'MCMC',samples: 5000},function(){modelo()})
viz.marginals(dist)

var estimar_intervalo = function(dist, margem, low, high) {
  expectation(marginalize(dist, margem), function(p) {low < p && p < high})
}

var HDI = function(dist, margem, low, high, delta) {
  var p = estimar_intervalo(dist, margem, low, high)
  if (p <= 0.95) return [low, high]
  var A  = estimar_intervalo(dist, margem, low + delta, high)
  var B  = estimar_intervalo(dist, margem, low, high - delta)
  return A > B ? HDI(dist, margem, low + delta, high, delta) : HDI(dist, margem, low, high - delta, delta)
}

var print_intervals = function(dist, margens) {
  map(function(m) {
    print(m + ": " + HDI(dist, m, 0, 1, 0.005))
  }, margens)
}
  
var dummy = print_intervals(dist, _.keys(lista))
~~~~