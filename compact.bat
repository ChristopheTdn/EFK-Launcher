pyinstaller EFK.py --distpath "EFKLauncher" 
Robocopy.exe "./config" "./EFKLauncher/config" /E /MIR /Z /DCOPY:T  /TIMFIX /R:0 /W:0 /XF "config.json"
cd "EFKLauncher"
WinRAR a EFKLauncher.zip  "EFK Launcher.exe" "./config"

