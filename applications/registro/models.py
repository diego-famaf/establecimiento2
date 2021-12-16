
from django.db import models




# Create your models here.
class Oficina(models.Model):
    name = models.CharField("Nombre", max_length=50)
    short_name = models.CharField("Nombre corto", max_length=50)

    class Meta:
        verbose_name = "Despacho"
        verbose_name_plural = "Despacho del establecimiento"
        ordering = ["name"]

    def __str__(self):
        return self.name

    
class Materia(models.Model):#modelo materia
    name = models.CharField("Nombre", max_length=50)#nombre de tipo chart
    short_name = models.CharField("Nombre corto", max_length=50)#nombre corto de tipo chart



    class Meta:#info extra del modelo creado
        verbose_name = "Asignatura" #para que el administrador me lo muestre con el nombre asignatura
        verbose_name_plural = "Asignaturas del establecimiento"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Empleado(models.Model):
    """Model definition for Empleado."""

    CARGO =(
        ("0","Docente"),
        ("1","No Docente"),

    )
    

    first_name = models.CharField("Nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=50)
    full_name = models.CharField("Nombre Completo", max_length=150, blank=True)#blank me permite dejar en blanco el full name
    age = models.IntegerField("Edad")
    job = models.CharField("Cargo", max_length=50, choices = CARGO)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, blank=True, null=True, default='')
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE, blank=True, null=True, default='')
    photo=models.ImageField("foto",upload_to = 'registro',height_field = None, width_field = None, max_length = None, blank=True)
    
    class Meta:
        """Meta definition for Empleado."""

        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """Unicode representation of Empleado."""
        return self.last_name + ' , ' + self.first_name


