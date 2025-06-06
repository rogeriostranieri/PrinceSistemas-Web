from rest_framework import viewsets
from django.db.models import Q, Func, F, Value
from .models import Socio
from .serializers import SocioSerializer

class SocioViewSet(viewsets.ModelViewSet):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer

    def get_queryset(self):
        queryset = Socio.objects.all()
        cpf = self.request.query_params.get('cpf')
        query = self.request.query_params.get('q')

        # Filtro por CPF exato (ignorando pontos/traços)
        if cpf:
            cpf_num = ''.join(filter(str.isdigit, cpf))
            # Remove tudo que não é número do campo cpf no banco e compara
            from django.db.models.functions import Replace
            queryset = queryset.annotate(
                cpf_numeros=Replace(Replace(Replace(F('cpf'), Value('.'), Value('')), Value('-'), Value('')), Value(' '), Value(''))
            ).filter(cpf_numeros=cpf_num)
            return queryset

        # Filtro por busca geral (q)
        if query:
            queryset = queryset.filter(
                Q(nomecompleto__icontains=query) | Q(cpf__icontains=query)
            )
        return queryset