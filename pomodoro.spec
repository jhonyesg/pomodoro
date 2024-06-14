# pomodoro.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['temporizador.py'],
    pathex=['C:\\Users\\jhony\\Music\\pomodoro'],
    binaries=[],
    datas=[
        ('C:\\Users\\jhony\\Music\\pomodoro\\tomato.png', '.'),
        ('C:\\Users\\jhony\\Music\\pomodoro\\sonido.mp3', '.')
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='temporizador_pomodoro_tomate',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='C:\\Users\\jhony\\Music\\pomodoro\\tomato.ico'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='temporizador_pomodoro_tomate'
)

app = BUNDLE(coll,
             name='temporizador_pomodoro_tomate',
             format='ONEFILE',
             icon='C:\\Users\\jhony\\Music\\pomodoro\\tomato.ico'
             )
