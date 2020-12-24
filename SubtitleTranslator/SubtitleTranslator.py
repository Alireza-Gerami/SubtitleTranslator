from SubtitleTranslator.Translator import Translator
from SubtitleTranslator.constants import LANGUAGES
from multiprocessing.pool import ThreadPool
import click
import os


@click.group()
def cli():
    """Python Subtitle Translator as a command-line tool"""
    pass


@cli.command(help='Translate subtitle file.')
@click.argument('filename', type=click.Path(exists=True))
@click.option('--src', '-s', default='en', show_default=True,
              type=click.Choice(LANGUAGES.keys(), case_sensitive=False),
              help='The source language you want to translate.')
@click.option('--dest', '-d', default='fa', show_default=True,
              type=click.Choice(LANGUAGES.keys(), case_sensitive=False),
              help='The destination language you want to translate.')
@click.option('--processes', '-p', default=10, type=int, show_default=True,
              help='Number of processes.')
def translate(filename, src, dest, processes):
    basename, extension = os.path.splitext(filename)
    if extension == '.srt':
        translator = Translator(basename, src, dest)
        ThreadPool(processes).map(translator.translate_subtitle, translator.subtitles)
        translator.subtitles.save(f'{basename}.{dest}.srt')
    else:
        click.echo(f'Error : {filename} is not a valid subtitle srt file. (Valid Example is file.srt)')


@cli.command(help='Show available languages to translate.')
def show_lang():
    for key in LANGUAGES:
        click.echo(f'{key} = {LANGUAGES[key]}')
