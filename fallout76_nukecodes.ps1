$codes = Invoke-RestMethod -Uri "https://nukacrypt.com/codes.json?r="

ForEach ($silo in $codes) {
    $alpha = $silo.alpha; $bravo = $silo.bravo; $charlie = $silo.charlie }

Write-Host "Alpha: $alpha`nBravo: $bravo`nCharlie: $charlie"
