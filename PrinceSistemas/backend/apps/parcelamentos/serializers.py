from rest_framework import serializers
from .models import Parcelamento, models

class ParcelamentoSerializer(serializers.ModelSerializer):
    razaosocial = serializers.CharField(source='razao_social', required=False, allow_null=True, allow_blank=True)
    cnpjcpf = serializers.SerializerMethodField()

    class Meta:
        model = Parcelamento
        fields = '__all__'
        extra_kwargs = {
            field.name: {'required': False, 'allow_null': True, 'allow_blank': True}
            for field in Parcelamento._meta.fields
            if isinstance(field, (models.CharField, models.EmailField))
        }
        # Para campos de data:
        extra_kwargs.update({
            field.name: {'required': False, 'allow_null': True}
            for field in Parcelamento._meta.fields
            if isinstance(field, models.DateField)
        })

    def get_cnpjcpf(self, obj):
        if not obj.cnpj:
            return None
        doc = ''.join(filter(str.isdigit, obj.cnpj))
        if len(doc) == 14:
            return f"{doc[:2]}.{doc[2:5]}.{doc[5:8]}/{doc[8:12]}-{doc[12:]}"
        elif len(doc) == 11:
            return f"{doc[:3]}.{doc[3:6]}.{doc[6:9]}-{doc[9:]}"
        return obj.cnpj

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Campos de checkbox
        checkbox_fields = [
            "mei", "inss_antigo", "inss_novo", "inss_procur",
            "para_fazer", "atraso_parcela_mei", "atraso_parcela_inss_antigo",
            "atraso_parcela_inss_novo", "atraso_parcela_inss_procu"
        ]
        for field in checkbox_fields:
            valor = data.get(field)
            data[field] = valor == "Checked"
        return data

    def to_internal_value(self, data):
        checkbox_fields = [
            "mei", "inss_antigo", "inss_novo", "inss_procur",
            "para_fazer", "atraso_parcela_mei", "atraso_parcela_inss_antigo",
            "atraso_parcela_inss_novo", "atraso_parcela_inss_procu"
        ]
        for field in checkbox_fields:
            if field in data:
                # Aceita true/false ou "Checked"/"Unchecked"
                if data[field] in [True, "Checked", "checked", "True", "true", 1]:
                    data[field] = "Checked"
                else:
                    data[field] = "Unchecked"
        return super().to_internal_value(data)
