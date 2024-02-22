pyinstaller "EFK_onefile.spec" --distpath "EFKLauncher" 
Robocopy.exe "./config" "./EFKLauncher/config" /E /MIR /Z /DCOPY:T  /TIMFIX /R:0 /W:0 /XF "config.json"
Robocopy.exe "./" "./EFKLauncher/" /MOV "EFK Launcher.exe"
cd "EFKLauncher"
Robocopy.exe "./config/EFKLauncher" "./" "version.txt"
winrar a EFKLauncher.zip  "EFK Launcher.exe" "./config"


