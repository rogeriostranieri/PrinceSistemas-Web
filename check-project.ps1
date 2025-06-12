Write-Host "Procurando vite.config.js..."
Get-ChildItem -Path . -Recurse -Filter vite.config.js -ErrorAction SilentlyContinue | ForEach-Object {
    Write-Host "Encontrado: $($_.FullName)"
}

Write-Host "`nProcurando package.json..."
Get-ChildItem -Path . -Recurse -Filter package.json -ErrorAction SilentlyContinue | ForEach-Object {
    Write-Host "`nArquivo encontrado: $($_.FullName)"
    try {
        $package = Get-Content $_.FullName -Raw | ConvertFrom-Json
        if ($package.dependencies) {
            Write-Host "Dependências (dependencies):"
            $package.dependencies.GetEnumerator() | ForEach-Object { Write-Host " - $($_.Key): $($_.Value)" }
        }
        if ($package.devDependencies) {
            Write-Host "Dependências de Desenvolvimento (devDependencies):"
            $package.devDependencies.GetEnumerator() | ForEach-Object { Write-Host " - $($_.Key): $($_.Value)" }
        }
        if ($package.scripts) {
            Write-Host "Scripts:"
            $package.scripts.GetEnumerator() | ForEach-Object { Write-Host " - $($_.Key): $($_.Value)" }
        }
    }
    catch {
        Write-Host "Erro ao ler $($_.FullName): $_"
    }
}

Write-Host "`nProcurando angular.json..."
Get-ChildItem -Path . -Recurse -Filter angular.json -ErrorAction SilentlyContinue | ForEach-Object {
    Write-Host "`nArquivo encontrado: $($_.FullName)"
    try {
        $angularJson = Get-Content $_.FullName -Raw | ConvertFrom-Json
        Write-Host "Projetos encontrados:"
        $angularJson.projects.PSObject.Properties.Name | ForEach-Object { Write-Host " - $_" }

        Write-Host "Builders de cada projeto:"
        foreach ($projName in $angularJson.projects.PSObject.Properties.Name) {
            $architect = $angularJson.projects.$projName.architect
            if ($architect) {
                Write-Host "`nProjeto: $projName"
                foreach ($target in $architect.PSObject.Properties.Name) {
                    $builder = $architect.$target.builder
                    Write-Host "  Target: $target - Builder: $builder"
                }
            }
        }
    }
    catch {
        Write-Host "Erro ao ler $($_.FullName): $_"
    }
}
