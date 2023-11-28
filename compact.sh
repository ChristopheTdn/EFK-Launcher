pyinstaller "EFK.spec" --distpath "EFKLauncher" ; rsync -r config/ EFKLauncher/config/ --exclude 'config.json' ; rsync EFKLauncher/config/EFKLauncher/version.txt  EFKLauncher/ 
cd EFKLauncher
zip -r EFKlauncher.zip  "EFK Launcher" "./config" 
rm -rf  "EFK Launcher" config/
