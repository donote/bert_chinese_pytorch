# /usr/bin/env python
# encoding=utf8
# trans from text with format '\t' split to json

import sys
import json
import codecs
import click

@click.command()
@click.option('-i', 'input', type=click.Path(file_okay=True, dir_okay=False, exists=True))
@click.option('-o', 'output', type=click.Path())
def text2json(input, output):
    outfd = codecs.open(output, mode='w', encoding='utf8')
    with open(input) as fd:
        for line in fd:
            line = line.strip()
            terms = line.split('\t')
            if len(terms) < 4:
                continue
            label = terms[2]
            content = terms[3]
            elem = {'label': label, 'question': content}
            elem_str = json.dumps(elem)
            outfd.write(elem_str)
            outfd.write('\n')

if __name__ == '__main__':
    text2json()

