from setuptools import setup

setup(
    name='SubtitleTranslator',
    version='1.0.0',
    py_modules=['SubtitleTranslator'],
    packages=['SubtitleTranslator'],
    url='https://github.com/Alireza-Gerami/SubtitleTranslator',
    download_url='https://github.com/Alireza-Gerami/SubtitleTranslator/archive/main.tar.gz',
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
    keywords=['TRANSLATE', 'TOOLS', 'SUBTITLE'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
