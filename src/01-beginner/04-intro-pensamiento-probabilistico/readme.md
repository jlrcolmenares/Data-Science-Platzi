![](https://joseluisramoncolmenares.files.wordpress.com/2020/06/joseluiramon-diploma-probabilistica.png)

## Introducción a Pensamiento Probabilístico 

**Prof. David Aroesti**

## Unidad 1. Probabilidad condicional

Cuando pensamos en juego de azar, nosotros estamos pensando en probabilidad independiente, en donde los eventos no están relacionados uno con otros (caso moneda, o caso ruleta de casino). No siempre esas prob. son útiles. Cuando calculamos probabilidades independientes nuestra responsabilidad es contar el caso que no interesa y dividir entre el total. 

Cuando tenemos probabilidad condicionales, tenemos que tomar en consideración la influencia de que un eventos suceda en sucesión con otro. Cuando pensamos en probabilidades condicionales. 

### Teorema de Bayes

[AGREGAR IMÁGENES DEL TEOREMA DE BAYES]



==Queremos calcular cual es la probabilidad de tener cancer si no tienes síntomas==. La calculamos en Python

```python
def calc_bayes(prior_A, prob_B_dado_A, prob_B):
    return (prior_A * prob_B_dado_A)/prob_B

# ahora lo tenemos que calcular los eventos que le pasaremos a la función a partir de la tabla
if __name__ == '__main__':
    prob_cancer = 1 / 100000 #prob A
    prob_sintoma_dado_cancer = 1 # prob B|A
    prob_sintoma_dado_no_cancer = 10 / 99999 # prob B|'no A'
    prob_no_cancer = 1 - prob_cancer # prob 'no A'
   	# prob B, a continuación:
    prob_sintoma = (prob_sintoma_dado_cancer*prob_cancer) \
    + (prob_sintoma_dado_no_cancer*prob_no_cancer)
    
    #lo que nos interesa
    prob_cancer_dado_sintoma = calc_bayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma)
    
    print('La probabilidad de tener cancer dado síntoma es ',prob_cancer_dado_sintoma
    # 0.09090909090909091
```

## Unidad 2. Mentiras estadísticas

Resgos cognitivos: https://es.wikipedia.org/wiki/Anexo:Sesgos_cognitivos

## Unidad 3. Introducción a Machine Learning

* Machine learning se utiliza cuando:
  * Programa un algoritmo es imposible
  * El problema es muy complejo o no se conocer algoritmos para resolverlo
  * Ayuda a los humanos a entender patrones (data mining)
* Aprendizaje supervisado vs no supervisado vs Semi-supervisado
* Batch (el modelo se genera una vez y se aplica siempre) vs Online learning (el modelo se va actualizando)