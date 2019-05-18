$codes = Invoke-RestMethod -Uri "nukacrypt.com/codes.json"

Write-Host Alpha: $codes.alpha`nBravo: $codes.bravo`nCharlie: $codes.charlie
