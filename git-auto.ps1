# Navega até a pasta do projeto
cd "D:\0000000000000000000000000\PrinceSistemaPY"

# Inicializa git (se já tiver .git ignora)
if (-not (Test-Path .git)) {
    git init
    git remote add origin https://github.com/rogeriostranieri/PrinceSistemas-Web.git
}

# Adiciona tudo
git add .

# Commit com mensagem padrão ou argumento passado
param(
    [string]$msg = "Atualização automática"
)
git commit -m $msg

# Push branch main (renomeie aqui se for outro branch)
git push -u origin main
