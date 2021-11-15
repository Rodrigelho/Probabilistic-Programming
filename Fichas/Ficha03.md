Assuma que 1% da população tem COVID. Dos que têm COVID, 70% tem um teste rápido positivo mas 10% das pessoas que não têm COVID tem um teste rápido positivo. Imprima o histograma correspondente aos positivos;

~~~~
var modelo = function(){
  var covid = flip(0.01)
  var positivos = covid ? flip(0.7) : flip(0.1)
  return positivos
}

viz.table(Infer(modelo))
~~~~

Assuma agora que existe o teste B (em oposição ao teste A referido acima) em que 90% das pessoas com COVID tem um teste positivo enquanto que só 1% das pessoas sem COVID tem um teste positivo. Assuma também que das pessoas que ligam para o Saúde24, 80% das pessoas fizeram o teste A e as restantes fizeram o teste B. Imprima o histograma correspondente aos positivos.

~~~~
var modelo = function(){
  var covid = flip(0.01)
  var positivos_A = covid ? flip(0.7) : flip(0.1)
  var positivos_B = covid ? flip(0.9) : flip(0.01)
  var positivos = flip(0.8) ? positivos_A : positivos_B
  return positivos
}

viz.table(Infer(modelo))
~~~~

Calcule p(COVID|positivo) para a pergunta 1 da ficha 3;

~~~~
var modelo = function(){
  var covid = flip(0.01)
  var positivos = covid ? flip(0.7) : flip(0.1)
  condition(positivos)
  return covid
}

viz.table(Infer(modelo))
~~~~

Se tiver um teste positivo para a pergunta 2 da ficha 3, calcule:
A probabilidade de ter COVID;
A probabilidade de ter feito o teste A;
A probabilidade de ter feito o teste A com teste positivo e COVID;


~~~~
var modelo_a = function(){
  var covid = flip(0.01)
  var positivos_A = covid ? flip(0.7) : flip(0.1)
  var positivos_B = covid ? flip(0.9) : flip(0.01)
  var positivos = flip(0.8) ? positivos_A : positivos_B
  condition(positivos)
  return covid
}

var modelo_b = function(){
  var covid = flip(0.01)
  var feito_teste_A = flip(0.8)
  var positivos_A = covid ? flip(0.7) : flip(0.1)
  var positivos_B = covid ? flip(0.9) : flip(0.01)
  var positivos = feito_teste_A ? positivos_A : positivos_B
  condition(positivos)
  return feito_teste_A
}

var modelo_c = function(){
  var covid = flip(0.01)
  var feito_teste_A = flip(0.8)
  var positivos_A = covid ? flip(0.7) : flip(0.1)
  var positivos_B = covid ? flip(0.9) : flip(0.01)
  var positivos = feito_teste_A ? positivos_A : positivos_B
  condition(positivos && covid)
  return feito_teste_A
}

viz.table(Infer(modelo_a))
viz.table(Infer(modelo_b))
viz.table(Infer(modelo_c))
~~~~