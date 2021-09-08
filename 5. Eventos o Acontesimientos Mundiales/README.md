# 1. Obtención de datos
Para la obtención de los datos acerca de eventos o acontecimientos mundiales se hace uso de la página de Kagle, la misma que nos proporciona los archivos tipo CSV.

# 2. Base de Datos
Se hace la creación de la base de datos en “phpMyAdmin” utilizando XAMP, de esta forma podemos hacer la implementación de forma local. La base de datos se denomina “proyectoad”.
Se hace la importación de archivos de forma manual, cabe resaltar que para realizar esto se debe de tener los datos dentro de un archivo con la extensión .CSV, además para una     mejor organización se asigna la primera fila como el nombre que tendrá cada columna de la tabla del CSV correspondiente.

![image](https://user-images.githubusercontent.com/58042215/132573970-2b7e41e4-9672-4b66-81de-f5180b3449fa.png)

Se realiza este mismo procedimiento con los archivos de datos restantes.

# 3. Elasticearch
Una vez se tenga adicionado todos los archivos de datos en la base de datos se realiza el levantamiento del servidor de “Elasticsearch”, para ello se tiene que hacer la descarga de los archivos de configuración de Elasticsearch y correr el archivo denominado “elasticsearch” (mismo que será una aplicación) en una terminal de Windows.

![image](https://user-images.githubusercontent.com/58042215/132574061-e19a9306-de0e-4bf6-bf3c-d34567649c7c.png)

# 4. Cerebro 
Para realizar la visualización de los datos contenidos en “Elasticserach” se hace uso de la aplicación de “cerebro” siendo así nuestro cliente con el que podremos acceder a nuestro servidor, de igual forma que en el paso anterior, se debe correr la aplicación a través de una terminal de Windows 
Para realizar la visualización de los datos contenidos en ese momento en nuestro servidor de “Elasticserach”, se debe de escribir la dirección de http://localhost:9000 en el navegador, se esta forma se nos redireccionará a la interfaz de usuario de cerebro.

![image](https://user-images.githubusercontent.com/58042215/132574281-61543d9f-dcff-4717-88ea-313234714b67.png)

Dentro de ella se escribirá la dirección donde este levantado nuestro servidor, en este caso, se lo está realizando de forma local por lo que la dirección ingresada será          localhost, con diferencia en que nuestro servidor se hallará levantado en el puerto 9200. Cabe resaltar, que si se lo estuviera realizando con un servidor en la nube de           “elastic-cloud” se colocaría la dirección url en el apartado correspondiente.
Una vez añadida la dirección correspondiente se podrá hacer visualización de los datos que se tengan en dicho momento en nuestro servidor.

![image](https://user-images.githubusercontent.com/58042215/132574472-473f47df-9848-4a9a-b098-d33e849565f4.png)

# 5. Logstash
Para la carga de archivos en nuestro servidor local, se hace uso de la aplicación de “logstash” para ello, primero se hace la descompresión de todos los archivos necesarios para poder correr la aplicación. Una vez realizado esto, se debe de hacer ciertas modificaciones en nuestro archivo de configuración para poder hacer el envío de la información almacena en nuestra base de datos de “phpMyAdmin”.
    * Se debe de hacer la instalación de un conector para poder realizar la conexión con la base de datos de phpMyAdmin. Para ello se hace la utilización del instalador de MySQL         y seguido a esto en el archivo de configuración se debe de indicar la ruta directa en donde se encuentra instalado nuestro conector.
    * Se debe de hacer la creación de un usuario en “phpMyAdmin” colocando todos los permisos de administrador sobre nuestro servidor, esto debido a una serie de permisos que           nuestro usuario root no posee.   
    * Se debe de hacer la especificación de la base de datos que va a ser utilizada y adicional a ello se debe especificar la tabla de la cual se tomarán los datos para ser             enviados a “elasticsearch”. 
    * Finalmente se especificará la url de nuestro servidor de “elasticsearch” incluyendo el puerto en el que estará levantado.

