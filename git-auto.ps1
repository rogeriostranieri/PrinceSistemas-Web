# -*- coding: utf-8 -*-
param(
    [string]$msg = "Atualizacao automatica"
)

# força CP-65001 e encoding UTF-8 antes de qualquer saída
chcp 65001 | Out-Null
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
[Console]::InputEncoding  = [System.Text.UTF8Encoding]::new()

Set-Location -Path "D:\0000000000000000000000000\PrinceSistemaPY"

if (-not (Test-Path .git)) {
    git init
    git remote add origin https://github.com/rogeriostranieri/PrinceSistemas-Web.git
}

Write-Host "Adicionando todas as alteracoes..."
git add -A

if (-not (git diff --cached --quiet)) {
    Write-Host "Criando commit: '$msg'"
    git commit -m "$msg"
} else {
    Write-Host "Nenhuma alteracao para commitar."
}

Write-Host "Enviando para o repositorio remoto..."
git push -u origin main