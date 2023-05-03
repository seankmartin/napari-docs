"""ALL pre-rendering and pre-preparation of docs should occur in this file.

Note: make no assumptions about the working directory
from which this script will be called.
"""
import platform
import sys
from pathlib import Path

docs = Path(__file__).parent.parent.absolute()
npe = docs.parent.absolute() / 'npe2'

def prep_npe2():
    #   some plugin docs live in npe2 for testing purposes
    from subprocess import check_call

    if platform.system() == 'Windows':
        delete = 'cmd /c rmdir /s /q'
    else:
        delete = 'rm -rf'

    render = str(npe / '_docs' / 'render.py')
    if npe.exists():
        check_call(f"{delete} {npe}".split())
    check_call(f"git clone https://github.com/napari/npe2 {npe}".split())
    check_call([sys.executable, render, str(docs / 'plugins')])
    check_call(f"{delete} {npe}".split())


def main():
    prep_npe2()
    __import__('update_preference_docs').main()
    __import__('update_event_docs').main()


if __name__ == "__main__":
    main()
