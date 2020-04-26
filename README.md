# **Proyecto para analizar datos de la Red Eléctrica Española**

El proyecto se divide en varias fases:

1. Descarga y procesado de datos
2. Análisis y clústering de datos
3. Reglas de asociación
4. Predicciones sobre los datos

 Debemos hacer todo esto para los datos de 2017, 2018 y 2019.  
 El plazo del proyecto es de 3 semanas.

 ---
 
 ## **Primera fase: Descarga y procesado de datos**
 
 ### Primer paso: Entender la API
 Antes de nada, debía familiarizarme con la API.  
 Lo primero a tener en cuenta es que no podemos descargar más de un mes de datos en cada request a la API, por lo tanto
habrá que hacer un request por cada mes de cada año.  
 Lo segundo, es que hay datos que la API nos proporciona y no necesitamos. Solo nos interesan los datos reales de
demanda y precio, los demás los descartaremos.  

 ### Segundo paso: Entender las requests a la API
 #### Para demanda:
 La URL tiene este formato:  
 ```https://apidatos.ree.es/es/datos/demanda/demanda-tiempo-real?start_date=2018-01-01T00:00&end_date=2018-01-31T23:50&time_trunc=hour```  
 Este ejemplo descargaría los datos de Enero de 2018. Una cosa importante a tener en cuenta para las requests de demanda
es que no nos devuelve los datos de hora en hora, lo hace de 10 minutos en 10 minutos.  
 Teniendo esto en cuenta, deberemos parsear con cuidado la URL.
 
 #### Para precio:
 La URL tiene este formato:  
 ```https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?start_date=2018-01-01T00:00&end_date=2018-01-31T23:00&time_trunc=hour```  
 Este ejemplo descargaría los datos de Enero de 2018, de hora en hora.  
 Teniendo esto en cuenta, deberemos parsear con cuidado la URL.
 
 ### Tercer paso: Implementación
 Teniendo en cuenta todo lo anterior, procedo a la implementación.  
 El código está debidamente comentado, por lo que aquí solo haré un pequeño resumen de los archivos y las funciones.  
 
 * #### recoleccionDatosMes.py
 Es un archivo que no usaremos. Es la primera versión que hice para recolectar datos. Te devuelve dos carpetas, una con
los datos por mes durante los tres años para demanda y otra con lo mismo pero para precio. No he visto necesario
comentar este archivo puesto que no lo usaremos.

 * #### recoleccionDatosAnyos.py
 Archivo que usamos para la recolección de los datos. Contiene la función que nos genera dos archivos json, uno para 
demanda y otro para precio. En los archivos que genera solo tenemos los datos que nos interesa. Están incluidos todos 
los meses de los tres años. Como ejemplo de output de la función, tenemos los archivos ```demanda.json``` y 
```precio.json``` generados por dicha función.

 * #### procesadoDatosDemandaString.py
 Archivo que contiene la función que nos genera un DataFrame conteniendo los datos de la demanda. Los índices de
columnas y filas son String. El archivo que usa para sacar los datos es el generado por la función contenida en
```recoleccionDatosAnyos.py```.

 * #### procesadoDatosDemandaTime.py
 Archivo que contiene la función que nos genera un DataFrame conteniendo los datos de la demanda. Los índices de
columnas son TimeDelta y los 'indices de filas son DateTime. El archivo que usa para sacar los datos es el generado por
la función contenida en ```recoleccionDatosAnyos.py```.

 * #### procesadoDatosPrecioString.py
 Archivo que contiene la función que nos genera un DataFrame conteniendo los datos del precio. Los índices de
columnas y filas son String. El archivo que usa para sacar los datos es el generado por la función contenida en
```recoleccionDatosAnyos.py```.

 * #### procesadoDatosPrecioTime.py
 Archivo que contiene la función que nos genera un DataFrame conteniendo los datos del precio. Los índices de
columnas son TimeDelta y los 'indices de filas son DateTime. El archivo que usa para sacar los datos es el generado por
la función contenida en ```recoleccionDatosAnyos.py```.

 ### Problemas encontrados:
 * Encuentro un gran problema, y es que nunca he trabajado con APIS para descargar datos ni con archivos json. Aún así he 
investigado y aprendido lo suficiente para completar con éxito la tarea.  
 
 * El manejo del DataFrame con la función ```pd.concat()``` me ha dado muchos problemas ya que no me concatenaba bien las
columnas que quería.  
 
 * La lectura y escritura de archivos Json. Al ser algo nuevo no terminaba de entender cómo funcionaba.
 
 * El manejo de DateTime y TimeDelta me ha costado porque no estaba acostumbrado a trabajar con datos de esos tipos.
 
 ---
 
  ## **Segunda fase: Análisis y clústering**
 Para hacernos una idea de cómo son nuestros datos, tenemos que analizarlos. Para ello aplicaremos técnicas de  
clústering, visualizaremos los datos y veremos la correlación entre algunas variables.

 Vamos a aplicar el algoritmo de K-medias. Para obtener el número óptimo de clústers vamos a usar la función silhouette.  
Esta función nos sirve como medida interna y externa para la obtención del número de clústers.
 
 Para visualizar los datos usamos ```visualizacion.py```, que nos imprime una gráfica por pantalla:
 
 ![visualizacion demanda](https://github.com/theesmoxDEV/beca-investigacion-US/blob/master/images/visualizacion%20demanda.png?raw=true)
 
 El análisis con la función Silhouette y la elección de k están en los archivos ```clustering_por_dias_demanda.ipynb``` y  
 ```clustering_por_dias_precio.ipynb```
 Al aplicar la función Silhouette para la demanda a distintos números para K, obtenemos:
 
 ![silhouette demanda](https://github.com/theesmoxDEV/beca-investigacion-US/blob/master/images/silhouette.png?raw=true)

 Por lo que la función nos dice  que el mejor número para K es 6 (cogemos la segunda joroba de la gráfica).
 Lo siguiente que hacemos son unas tablas de contingencia con los días que pertenecen a invierno y verano y los que no.  
Estas tablas están en el archivo ```tablas.xslx```. Dentro también está la prueba del CHI cuadrado, que nos sale muy pequeña,  
por lo que intuimos que es una buena suposición de clustering.

Para el precio tenemos la siguiente gráfica de la función silhouette:

 ![silhouette precio](https://github.com/theesmoxDEV/beca-investigacion-US/blob/master/images/silhouette%20precio.png?raw=true)
 
  ### Problemas encontrados:
 * No había usado mucho técnicas de clústering, por lo que he encontrado dificultad a la hora de conseguir el número de
 clústers óptimos usando la función Silhouette. 
 
 * La gráfica es muy mejorable, pero por mucho que cambiaba cosas e intentaba mejorarla no lo he conseguido.
 
 * El cálculo del CHI cuadrado y las tablas de contingencia han sido cosas completamente nuevas para mí, por lo que he
 encontrado dificultad al principio para entender estos conceptos.
 
 ---
 
 ## **Tercera fase: Reglas de asociación**
 Vamos a ver si podemos extraer algunas reglas del conjunto de datos. Para ello vamos a aplicar un algoritmo llamado
algoritmo a priori. Pero antes de eso tenemos que comprobar si existe correlaciñón entre las variables, y si es así, 
ver en cuáles la correlación es mayor para usar en nuestras reglas.

### Primer paso: Ver correlaciones entre variables
 Para ello podemos ver el archivo ```correlacion.ipynb```, donde se usan las funciones de ```correlacion.py``` para
analizar la correlación entre variables.

 He encontrado algunas correlaciones entre la demanda y el precio, en la siguiente gráfica podemos ver la correlación
entre la demanda hasta 24 horas antes y el precio a determinada hora:

 ![correlacion](https://github.com/theesmoxDEV/beca-investigacion-US/blob/master/images/correlacion.png?raw=true)
 
 Aquí vemos que la correlación una hora antes y 24 horas antes de la demanda con el precio tiene un valor que podríamos
considerar como bueno. Esto nos va a servir para ver qué usar en las reglas de asociación.
 
 También he encontrado que esta correlación se repite a lo largo de una semana:
 
 ![correlacion semana](https://github.com/theesmoxDEV/beca-investigacion-US/blob/master/images/correlacion_semana.png?raw=true)
 
### Segundo paso: Hacer las reglas
 Para hacer las reglas de asociación vamos a usar el algoritmo a priori, discretizando los valores mediante kmeans haciendo
uso del archivo ```reglasAsociacion.py```. El resto lo hacemos en el archivo ```reglas.ipynb```.
 
 Hemos intentado sacar reglas con las demandas 24, 23, 2 y 1 hora antes al precio. Este es el conjunto de items que hemos
obtenido:

![items reglas](https://github.com/theesmoxDEV/beca-investigacion-US/blob/master/images/items-reglas.png?raw=true)

 Y estas las reglas que hemos obtenido a partir de ese conjunto:
 
![reglas](https://github.com/theesmoxDEV/beca-investigacion-US/blob/master/images/reglas.png?raw=true)

 Como vemos hemos conseguido algunas reglas con bastante soporte y confianza.
 
  ### Problemas encontrados:
 * No acabo de entender las reglas de asociación al 100%.
 
 * La forma de discretizar y de hacer las reglas creo que no están totalmente bien.
 
 ---
 
 ## **Cuarta fase: Predicciones**
 Vamos a intentar predecir los precios para las demandas de septiembre de 2019.
 Todo está en el archivo prediccion.ipynb
 
### Primer paso: Preprocesado de datos
 Tenemos que separar los datos en entrenamiento y test, y poner los precios separados de la demanda.
Luego normalizamos los datos y los preparamos de forma en la que se los podamos pasar a la red neuronal.

### Segundo paso: Construir la red
 He creado una red neuronal bastante simple paar hacer una aproximación sencilla. Es una red de 4 capas con 256 unidades
en cada capa (menos en la última que solo hay una). Las funciones de activación son funciones ReLu, y en la última capa
es una función linear para obtener la regresión. Usamos el algoritmo ADAM (versión "mejorada" del descenso por el gradiente).
La función pérdida que usamos es MAE.

### Tercer paso: Computar las predicciones
 Predecimos los precios de septiembre de 2019 usando la demanda desde el 31 de agosto hasta el 29 de septiembre. Siempre
usando 24 horas y 1 hora antes (así nos aseguramos que no haya data leak).

 Vemos que las predicciones no son del todo buenas (de hecho son malas), pero es una aproximación al problema que se
puede mejorar haciendo uso de alguna otra arquitectura de la red (como por ejemplo LTSM o convolucionales) y cogiendo
más datos, no solo los de 24 y 1 hora antes para cada precio. También podríamos incluir datos meteorológicos ya que
estoy casi seguro de que tiene que influir en el precio de la electricidad.