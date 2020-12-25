import googletrans
from tqdm import tqdm
import httpx
import pysrt


class Translator:
    def __init__(self, basename, src, dest):
        self.src, self.dest = src, dest
        self.subtitles = pysrt.open(f'{basename}.srt')
        self.progressbar = tqdm(total=len(self.subtitles.data), desc='Translating',
                                bar_format='{desc} --> {percentage:3.0f}%|{bar}|{n_fmt}/{total_fmt}')

        self.translator = None

    def translate_subtitle(self, subtitle):
        timeout = httpx.Timeout(10)
        self.translator = googletrans.Translator(service_urls=['translate.google.com', 'translate.google.co.kr'],
                                                 timeout=timeout)
        try:
            subtitle.text = self.translator.translate(subtitle.text, src=self.src, dest=self.dest).text
        except:
            pass
        self.progressbar.update(1)
