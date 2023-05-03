"""ALL pre-rendering and pre-preparation of docs should occur in this file.

Note: make no assumptions about the working directory
from which this script will be called.
"""
import platform
import sys
from pathlib import Path

DOCS = Path(__file__).parent.parent.absolute()
NPE2 = DOCS.parent.absolute() / 'npe2'

def prep_npe2():
    #   some plugin docs live in npe2 for testing purposes
    from subprocess import check_call

    if platform.system() == 'Windows':
        delete = 'cmd /c rmdir /s /q'
    else:
        delete = 'rm -rf'

    render = str(NPE2 / '_docs' / 'render.py')
    if NPE2.exists():
        check_call(f"{delete} {NPE2}".split())
    check_call(f"git clone https://github.com/napari/npe2 {NPE2}".split())
    check_call([sys.executable, render, str(DOCS / 'plugins')])
    check_call(f"{delete} {NPE2}".split())


def main():
    prep_npe2()
    __import__('update_preference_docs').main()
    __import__('update_event_docs').main()


if __name__ == "__main__":
    main()
