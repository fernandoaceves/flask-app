Para poder ejecutar la imagen, basta con dirigirse al path donde se encuentra el archivo "app.py". Una vez encontrandose ahí, debemos seguir los siguientes pasos:

-Posteriormente podemos aplicar el siguiente comando en nuestra CMD:
“ docker build --tag python-docker . “

-Una vez creada nuestra imagen, la podemos encontrar en nuestras imágenes de docker con el comando:
“ docker images “

-Aplicamos el siguiente comando para poder conectarnos via local a nuestro servidor:
“ docker run --publish 8000:5000 python-docker ”

-Si nos conectamos al puerto http://localhost:8000, entonces podremos observar nuestra aplicación corriendo en el servidor

