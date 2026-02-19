from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=100)


class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)


class Veiculo(models.Model):
    descricao = models.CharField(max_length=255, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    ano = models.PositiveIntegerField()
    horimetro = models.PositiveIntegerField(default=0)


class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=50)


class Medicacao(models.Model):
    tipo = models.CharField(max_length=100)
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.PROTECT)


class MedicacaoVeiculo(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    medicacao = models.ForeignKey(Medicacao, on_delete=models.PROTECT)
    data = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
