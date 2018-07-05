import glob
import os


DOIT_CONFIG = {'default_tasks': ['notebook']}


def task_notebook():
    for fname in glob.glob('*.ipyml'):
        name = os.path.splitext(fname)[0]
        dest = name + '.ipynb'
        yield {
            'name': name,
            'actions': [
                'ipyaml --no-output {src} {dest}'.format(src=fname, dest=dest)
            ],
            'file_dep': [fname],
            'targets': [dest],
            'clean': True,
        }
