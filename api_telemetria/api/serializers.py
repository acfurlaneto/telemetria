from rest_framework import serializers
from api_telemetria import models

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.marca
        fields = "__all__"

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.modelo
        fields = "__all__"

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.veiculo
        fields = "__all__"

class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.unidade_medida
        fields = "__all__"

class MedicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.medicacao
        fields = "__all__"

class MedicacaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.medicacao_veiculo
        fields = "__all__"