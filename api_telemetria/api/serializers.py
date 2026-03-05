from rest_framework import serializers
from api_telemetria import models

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = "__all__"
        extra_kwargs={
            "id": {"help_text": "Identificador da Marca do Veiculo, no Get da Api veículo"},
            "nome": {"help_text":"Nome da marca do veículo (ex: Case, Chevrolet)"},
        }

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Modelo
        fields = "__all__"
        extra_kwargs={
            "id": {"help_text": "Identificador do Modelo do Veiculo, no Get da Api veículo"},
            "nome": {"help_text": "Nome/Modelo da máquina agrícola (ex: 5078E, CR 8.90, TM 150, MF 275)"},
            "marca": {"help_text": "Marca/fabricante associada a este modelo (referência à tabela de Marcas)"},
        }

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Veiculo
        fields = "__all__"
        extra_kwargs={
            "id": {"help_text": "Identificador do veículo, no Get da Api veículo"},
            "descricao": {"help_text": "Nome ou identificação interna da máquina agrícola (ex: Trator Principal Quadra 5, Colheitadeira Soja 2023)"},
            "marca": {"help_text": "Marca da máquina agrícola (referência à tabela Marca)"},
            "modelo": {"help_text": "Modelo específico da máquina agrícola (referência à tabela Modelo)"},
            "ano": {"help_text": "Ano de fabricação ou modelo da máquina (ex: 2022)"},
            "horimetro": {"help_text": "Horímetro atual da máquina (horas de motor registradas"},
        }

class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UnidadeMedida
        fields = "__all__"
        extra_kwargs={
            "id": {"help_text": "Identificador da Unidade de Medida, no Get da Api veículo"},
            "nome": {"help_text": "Unidade de medida usada nas telemetrias (ex: ha, rpm, bar, km/h)"},
        }

class MedicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicacao
        fields = "__all__"
        extra_kwargs={
            "id": {"help_text": "Identificador da Medição, no Get da Api veículo"},
            "tipo": {"help_text": "Tipo de medição/telemetria realizada na máquina agrícola (ex: Consumo Combustível, Velocidade de Trabalho, Área Colhida, Rotação Motor, Pressão Óleo, Temperatura Água)"},
            "unidade_medida": {"help_text": "Unidade de medida associada a este tipo de medição (referência à tabela UnidadeMedida)"},
        }

class MedicacaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicacaoVeiculo
        fields = "__all__"
        extra_kwargs={
            "id": {"help_text": "Identificador da Medição do veículo, no Get da Api veículo"},
            "veiculo": {"help_text": "Identificador do veículo. Buscar no Get da API Medição"},
            "medicacao": {"help_text": "Identificador da automação / tipo de medição realizada, essa informação deve vir da automação"},
            "data": {"help_text": "Data e hora da medição realizada, essa informação deve vir da automação"},
            "valor": {"help_text": "Valor medido na automação."},
        }
        