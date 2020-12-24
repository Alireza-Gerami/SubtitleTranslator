from setuptools import setup

with open('README.md') as f:
    long_description = f.read()
setup(
    name='subtrans',
    version='1.0.1',
    py_modules=['SubtitleTranslator'],
    long_description=long_description,
    long_description_content_type='text/markdown',
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
