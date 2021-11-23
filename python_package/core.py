from pathlib import Path
import os

TEMPLATE_PATH = Path(__file__).parent.joinpath('templates')
TEMPLATES = [i.replace('.template', '') for i in os.listdir(TEMPLATE_PATH)]


def create_package(name, author):
    base_path = Path.cwd().joinpath(name)
    base_path.mkdir()

    create_file(base_path.joinpath('requirements.txt'))
    create_file(base_path.joinpath("test-requirements.txt"))

    env_path = base_path.joinpath('env')
    env_path.mkdir()
    dot_env_path = env_path.joinpath('.env')
    create_file(dot_env_path)

    src_path = base_path.joinpath(name)
    src_path.mkdir()
    source_files = ['__init__', 'cli']
    for file in source_files:
        file_path = src_path.joinpath(f"{file}.py")
        if file in TEMPLATES:
            create_file_from_template(f"{file}.template", file_path)
        else:
            create_file(file_path)

    create_file_from_template(template='.gitignore.template', dest=base_path.joinpath('.gitignore'))
    create_file_from_template(template='setup.template', dest=base_path.joinpath('setup.py'), name=name, author=author)
    return None


def create_file_from_template(template, dest, **kwargs):
    with open(TEMPLATE_PATH.joinpath(template)) as f:
        template = f.read()

    contents = template.format(**kwargs)

    with open(dest, 'w') as f:
        f.write(contents)

    return None


def create_file(path):
    with open(path, 'a') as f:
        f.write('')
    return None
