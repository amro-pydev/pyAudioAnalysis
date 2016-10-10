try:
    from setuptools import setup #enables develop
except ImportError:
    from distutils.core import setup

setup(name='pyAudioAnalysis',
      version='0.1',
      description='Python Audio Analysis Library',
      author='Theodoros Giannakopoulos, Amro Tork',
      author_email='tyiannak@gmail.com  , amrsfmt@yahoo.com ',
      license='MIT',
      url='https://github.com/amro-pydev/pyAudioAnalysis',
      packages=['pyAudioAnalysis'],
    )
