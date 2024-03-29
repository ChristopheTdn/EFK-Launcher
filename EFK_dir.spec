# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['EFK.py'],
    pathex=[],
    binaries=[],
    datas=[('EFK', 'EFK'), ('principale.py', '.'), ('ressources_rc.py', '.'), ('principale_ui.py', '.'),('updater_ui.py', '.'),('updater.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='EFK Launcher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['EFK Launcher.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='EFK',
)
