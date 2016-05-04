# -*- mode: python -*-

block_cipher = None


a = Analysis(['pong.py'],
             pathex=['/home/sophia/Dropbox/Programming/gitrepos/Python_PONG/Human_Game'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas += [('paddle.png','/home/sophia/Dropbox/Programming/gitrepos/Python_PONG/Human_Game/paddle.png','DATA'),('ball.png','/home/sophia/Dropbox/Programming/gitrepos/Python_PONG/Human_Game/ball.png','DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pong',
          debug=False,
          strip=False,
          upx=True,
          console=True )
