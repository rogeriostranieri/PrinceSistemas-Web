# git-diario.ps1

# Navegar para o diretório do repositório (ajuste conforme seu caminho)
# Set-Location "D:\0000000000000000000000000\PrinceSistemaPY"

# Função para commit e push com mensagem de data/hora atual
function Git-Diario {
    $dataAtual = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$dataAtual] Iniciando commit e push automáticos..." -ForegroundColor Cyan

    # Adicionar todas as mudanças (incluindo submódulos)
    git add .

    # Commit com mensagem contendo data e hora
    git commit -m "Commit diário automático em $dataAtual" 2>$null

    if ($LASTEXITCODE -eq 0) {
        Write-Host "Commit realizado com sucesso."
    } else {
        Write-Host "Nenhuma alteração para commitar."
    }

    # Push para o branch main (ou outro, se preferir)
    git push origin main

    if ($LASTEXITCODE -eq 0) {
        Write-Host "Push realizado com sucesso."
    } else {
        Write-Host "Falha ao fazer push."
    }

    # Mostrar status final
    git status
}

# Executar a função
Git-Diario
