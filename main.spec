# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/home/tt/dev/ojjo/py-seqtest'],
             binaries=[],
             datas=[
              ('resources/fonts/*.ttf', 'resources/fonts'), 
              ('resources/images/*.png', 'resources/images'), 
              ('resources/sounds/*.wav', 'resources/sounds'),
              ('scenery/*', 'scenery'),
              ('lib/*', 'lib'),
              ('results/*', 'results'),
              ('LICENSE', '.'),
             ],
             hiddenimports=['scenery', 'packaging', 'packaging', 'packaging.version', 'packaging.specifiers', 'packaging.requirements'],
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )

import os
os.mkdir("./dist/results")
