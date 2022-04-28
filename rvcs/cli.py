import argparse

from . import __version__


def _get_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'cmd', type=str,
        help='Valid commands: run'
    )
    parser.add_argument(
        '-v', '--version',
        action='version', version=f'%(prog)s {__version__}',
        help='Show the version number and exit'
    )
    return parser.parse_args()


def entry_point() -> None:
    args = _get_arguments()

    if args.cmd == 'run':
        from .app import App
        App().run()
