# -*- coding: utf-8 -*-
import base64
import json
from pathlib import Path

from jinja2 import Environment, select_autoescape, FileSystemLoader

env = Environment(
    loader=FileSystemLoader(Path(__file__).parent / 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


class Reporter(object):
    def __init__(self, name, stat_json: dict, outdir: Path, plot=None, img=None):
        self.name = name
        self.stat_json = stat_json
        self.outdir = outdir
        self.plot = plot
        self.img = img
        self.get_report()

    def get_report(self):
        template = env.get_template('base.html')
        json_file = self.outdir / '.data.json'
        if not json_file.exists():
            data = {}
        else:
            with open(json_file, encoding='utf-8', mode='r') as f:
                data = json.load(f)

        data[self.name + '_summary'] = self.stat_json

        if self.plot:
            data[self.name + '_plot'] = self.plot

        if self.img:
            data[self.name + '_img'] = {}
            for name in self.img:
                with open(self.img[name], 'rb') as f:
                    data[self.name + '_img'][name] = base64.b64encode(f.read()).decode()

        with open(self.outdir / 'report.html', encoding='utf-8', mode='w') as f:
            html = template.render(data)
            f.write(html)

        with open(json_file, encoding='utf-8', mode='w') as f:
            json.dump(data, f)
