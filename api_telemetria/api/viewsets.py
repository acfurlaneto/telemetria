from rest_framework import viewsets
from api_telemetria import models
from api_telemetria.api import serializers

class MarcaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MarcaSerializer
    queryset = models.Marca.objects.all()

class ModeloViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ModeloSerializer
    queryset = models.Modelo.objects.all()

class VeiculoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VeiculoSerializer
    queryset = models.Veiculo.objects.all()

class UnidadeMedidaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UnidadeMedidaSerializer
    queryset = models.UnidadeMedida.objects.all()

class MedicacaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MedicacaoSerializer
    queryset = models.Medicacao.objects.all()

class MedicacaoVeiculoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MedicacaoVeiculoSerializer
    queryset = models.MedicacaoVeiculo.objects.all()