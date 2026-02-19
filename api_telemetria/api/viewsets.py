from rest_framework import viewsets
from api_telemetria import models
from api_telemetria.api import serializers

class MarcaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MarcaSerializer
    queryset = models.marca.objects.all()

class ModeloViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ModeloSerializer
    queryset = models.modelo.objects.all()

class VeiculoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VeiculoSerializer
    queryset = models.veiculo.objects.all()

class UnidadeMedidaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UnidadeMedidaSerializer
    queryset = models.unidade_medida.objects.all()

class MedicacaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MedicacaoSerializer
    queryset = models.medicacao.objects.all()

class MedicacaoVeiculoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MedicacaoVeiculoSerializer
    queryset = models.medicacao_veiculo.objects.all()