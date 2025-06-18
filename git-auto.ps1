# -*- coding: utf-8 -*-
param(
    [string]$msg = "Atualização automática"
)

# força UTF-8 no console
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
[Console]::InputEncoding  = [System.Text.UTF8Encoding]::new()
chcp 65001 | Out-Null

cd "D:\0000000000000000000000000\PrinceSistemaPY"

if (-not (Test-Path .git)) {
    git init
    git remote add origin https://github.com/rogeriostranieri/PrinceSistemas-Web.git
}

Write-Host "Adicionando todas as alterações..."
git add -A

if (-not (git diff --cached --quiet)) {
    Write-Host "Criando commit: '$msg'"
    git commit -m "$msg"
} else {
    Write-Host "Nenhuma alteração para commitar."
}

Write-Host "Enviando para o repositório remoto..."
git push -u origin main