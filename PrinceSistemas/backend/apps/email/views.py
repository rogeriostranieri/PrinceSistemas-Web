from rest_framework import viewsets
from .models import Email, Emailcaixadesaida
from .serializers import EmailSerializer, EmailCaixaDeSaidaSerializer
from django.core.mail import EmailMultiAlternatives, get_connection
from rest_framework.response import Response
from rest_framework import status

class EmailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class EmailCaixaDeSaidaViewSet(viewsets.ModelViewSet):
    queryset = Emailcaixadesaida.objects.all()
    serializer_class = EmailCaixaDeSaidaSerializer

    def create(self, request, *args, **kwargs):
        # Salva normalmente no banco
        response = super().create(request, *args, **kwargs)
        data = request.data

        assunto = data.get('assunto', '')
        mensagem = data.get('caixadesaidatexto', '')
        remetente = data.get('emailprincipal', '')
        destinatarios = data.get('emaildestino', '')

        # Busca config do banco pelo e-mail principal
        config = Email.objects.filter(email=remetente).first()
        if not config:
            return Response({'detail': 'Configuração de e-mail não encontrada.'}, status=status.HTTP_400_BAD_REQUEST)

        smtp_host = config.smtpclient or ''
        try:
            smtp_port = int(config.smtpport) if config.smtpport else 587
        except Exception:
            smtp_port = 587
        smtp_user = config.email or ''
        smtp_password = config.senhaemail or ''
        use_tls = str(config.habilitassl or 'True').lower() == 'true'

        # Divide por vírgula e remove espaços
        lista_destinatarios = [e.strip() for e in destinatarios.split(',') if e.strip()]

        try:
            connection = get_connection(
                host=smtp_host,
                port=smtp_port,
                username=smtp_user,
                password=smtp_password,
                use_tls=use_tls,
                fail_silently=False
            )
            email = EmailMultiAlternatives(
                subject=assunto,
                body=mensagem,  # texto puro
                from_email=remetente,
                to=lista_destinatarios,
                connection=connection,
            )
            email.attach_alternative(mensagem, "text/html")
            email.send()
        except Exception as e:
            return Response({'detail': f'Erro ao enviar e-mail: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response