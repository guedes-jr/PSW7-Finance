from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0)
    
    def __str__(self):
        return self.categoria

class Conta(models.Model):
    banco_choises = (
        ('NU', 'Nubank'),
        ('CE', 'Caixa Econômica'),
        ('BR', 'Banco Bradesco')
    )
    tipo_choises = (
        ('pf', 'Pessoa Física'),
        ('pj', 'Pessoa Jurídica')
    )
    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=2, choices=banco_choises)
    tipo = models.CharField(max_length=2, choices=tipo_choises)
    valor = models.FloatField()
    icone = models.ImageField(upload_to="icones")
    
    def __str__(self):
        return self.apelido
    
    