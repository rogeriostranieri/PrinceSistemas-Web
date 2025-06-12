param(
    [string]$msg = "Atualização automática"
)

# Navega até a pasta do projeto
cd "D:\0000000000000000000000000\PrinceSistemaPY"

# Inicializa git (se já tiver .git ignora)
if (-not (Test-Path .git)) {
    git init
    git remote add origin https://github.com/rogeriostranieri/PrinceSistemas-Web.git
}

# Adiciona tudo
git add .

# Faz o commit com a mensagem recebida
git commit -m $msg

# Push para o branch main
git push -u origin main
