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
          name='seqtest',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          icon='resources/images/seqtest.ico',
          console=True )

import os
import sys
import shutil

if not os.path.exists("./dist/results"):
  os.mkdir("./dist/results")

shutil.copyfile('README.md', '{0}/README.md'.format("./dist"))
shutil.copyfile('LICENSE', '{0}/LICENSE'.format("./dist"))
shutil.copyfile('SOP.txt', '{0}/SOP.txt'.format("./dist"))

if sys.platform == 'darwin':
   app = BUNDLE(exe,
                name='seqtest.app',
                icon='resources/images/seqtest.png')
