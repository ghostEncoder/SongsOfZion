# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Main.py'],
             pathex=['C:\\Users\\jedidiah\\Documents\\pycharmProjects_OLD\\pycharmProjects\\Alpha\\Songs_Of_Zion_Tamil_V1.0'],
             binaries=[],
             datas=[('C:\\Users\\jedidiah\\AppData\\Roaming\\Python\\Python39\\site-packages\\eel\\eel.js', 'eel'), ('Web', 'Web')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='Main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Main')