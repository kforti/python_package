import click

from .core import create_package


COMMANDS = {
    'create': create_package
}


@click.command()
@click.option('--name', help='package name')
@click.option('--author', help='package author')
@click.argument('command')
def run_command(command, name, author):
    func = COMMANDS[command]
    return func(name=name, author=author)
