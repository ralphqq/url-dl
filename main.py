import os
from urllib.parse import urlsplit

import click
import requests

import config as cfg

def read_and_save(res):
    """Reads content of the accessed file and saves it locally."""
    fname = os.path.split(urlsplit(res.url).path)[-1]
    fpath = os.path.join(cfg.OUTPUT_DIR, fname)
    with open(fpath, 'wb') as f:
        for chunk in res.iter_content(cfg.CHUNK):
            f.write(chunk)

@click.command()
@click.argument('urls', nargs=-1)
def run(urls):
    """Handles program flow."""
    click.echo('Starting...')
    if not urls:
        click.echo('No URLs found. Please provide at least 1 URL.')
    else:
        n_files = len(urls)
        skipped = 0
        downloaded = 0
        errors = 0
        click.echo('Total files to be downloaded: {}'.format(n_files))
        for url in urls:
            click.echo('Processing file {}'.format(url))
            try:
                click.echo(' - Accessing file')
                res = requests.get(url, stream=True)
                s_code = res.status_code
                if s_code == 200:
                    click.echo(' - Reading file...')
                    read_and_save(res)
                    click.echo(' - File saved.')
                    downloaded += 1
                else:
                    click.echo(' - Unable to access: {}'.format(s_code))
                    skipped += 1
            except requests.exceptions.RequestException as e:
                click.echo(e)
                errors += 1
        
        click.echo('Finished.')
        click.echo('Files successfully downloaded: {}'.format(downloaded))
        click.echo('Files skipped: {}'.format(skipped))
        click.echo('Errors: {}'.format(errors))
