pyinstaller "EFK.spec" --distpath "EFKLauncher"
rsync -r config/ EFKLauncher/config/ --exclude 'config.json'
rsync EFKLauncher/config/EFKLauncher/version.txt  EFKLauncher/ 
rsync "EFK Launcher.ico" "EFKLauncher/" 
cd EFKLauncher
zip -r EFKlauncher.zip  "EFK Launcher" "EFK Launcher.ico" "./config" 
rm -rf  "EFK Launcher" "EFK Launcher.ico" "./config"
