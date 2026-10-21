$ExecutePath = $PWD
Set-Location $PSScriptRoot
Set-Location ..

git pull origin master
git add .
git commit -m "update data"
git status
git push origin master
git logs
Write-Host "执行完毕!"

Set-Location $ExecutePath
if ($PSScriptRoot -eq $ExecutePath) {
    # timeout.exe /T -1
}
