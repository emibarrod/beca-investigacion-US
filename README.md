# **Proyecto para analizar datos de la Red Eléctrica Española**

El proyecto se divide en varias fases:

1. Descarga y procesado de datos
2. Análisis de datos
3. Clustering de datos
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
 
