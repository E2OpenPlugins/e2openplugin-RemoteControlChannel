from distutils.core import setup, Extension

pkg = 'Extensions.RemoteControlChannel'
setup (name = 'enigma2-plugin-extensions-remotecontrolchannel',
       version = '0.1',
       description = 'Remote control IR channel selection',
       packages = [pkg],
       package_dir = {pkg: 'plugin'}
      )
