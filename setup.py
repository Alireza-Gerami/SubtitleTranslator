from setuptools import setup

setup(
    name='SubtitleTranslator',
    version='1.0.0',
    py_modules=['SubtitleTranslator'],
    packages=['SubtitleTranslator'],
    url='https://github.com/Alireza-Gerami/SubtitleTranslator',
    install_requires=[
        'click',
        'pysrt',
        'googletrans',
        'tqdm',
    ],
    license='MIT',
    author='Alireza Gerami',
    author_email='alireza.gerami4030@gmail.com',
    description='Python Subtitle Translator as a command-line tool',
    entry_points='''
        [console_scripts]
        subtrans=SubtitleTranslator.SubtitleTranslator:cli
    ''',
)
