from django.db import models, connection


class Product(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    descrip = models.CharField(max_length=255)
    marcaId = models.IntegerField()
    familiaId = models.IntegerField()
    stock = models.IntegerField()
    urlImage = models.CharField(max_length=255)
    proveedor = models.IntegerField()

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.descrip

    @staticmethod
    def obtener_datos():
        """
        Ejecuta el procedimiento almacenado `obtener_datos_productos` con el valor `12`
        y retorna los resultados como una lista de diccionarios.
        """
        with connection.cursor() as cursor:
            # Llama al procedimiento almacenado con el parámetro 12
            cursor.callproc("aqexsbali_divia.obtener_datos_productos", [12])

            # Recupera los resultados y los convierte en una lista de diccionarios
            # Obtiene los nombres de las columnas
            columns = [col[0] for col in cursor.description]
            # Convierte cada fila en un diccionario
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return results
