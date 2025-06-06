import subprocess
from django.http import FileResponse, HttpResponse
from django.conf import settings
import os
import tempfile
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def backup_database(request):
    """Gera um backup do banco de dados PostgreSQL."""
    try:
        # Criar pasta temporária se não existir
        temp_dir = os.path.join(settings.BASE_DIR, 'temp')
        os.makedirs(temp_dir, exist_ok=True)
        
        # Nome do arquivo com timestamp
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dump_file = os.path.join(temp_dir, f'backup_prince_{timestamp}.sql')
        
        # Configurar comando pg_dump
        cmd = [
            'pg_dump',
            '-U', settings.DATABASES['default']['USER'],
            '-h', settings.DATABASES['default']['HOST'],
            '-p', str(settings.DATABASES['default']['PORT']),
            '-d', settings.DATABASES['default']['NAME'],
            '-f', dump_file
        ]
        
        # Definir variável de ambiente para senha
        env = os.environ.copy()
        env['PGPASSWORD'] = settings.DATABASES['default']['PASSWORD']
        
        # Executar comando
        result = subprocess.run(cmd, env=env, capture_output=True, text=True)
        
        if result.returncode != 0:
            return HttpResponse(f"Erro ao gerar backup: {result.stderr}", status=500)
        
        # Preparar resposta
        response = FileResponse(
            open(dump_file, 'rb'),
            as_attachment=True,
            filename=f'backup_prince_{timestamp}.sql'
        )
        
        # Adicionar cabeçalhos para evitar problemas de CORS
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        
        return response
        
    except Exception as e:
        return HttpResponse(f'Erro ao gerar backup: {str(e)}', status=500)