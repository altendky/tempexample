import click


@click.command()
@click.option('-t', '--test', required=False)
def main(test):
    click.echo(f'i was executed: {test}')
