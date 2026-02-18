import sys
import argparse
from pathlib import Path

class GitRepo:
    def __init__(self, path='.'):
        if path == '.' or path.strip() == '':
            base_path = Path.cwd()
        else:
            base_path = Path(path)

        self.mygit_path = base_path / ".mygit"
        self.objects_path = self.mygit_path / "objects"
        self.refs_path = self.mygit_path / "refs"

    def init(self):
        ...
def main():
    parser = argparse.ArgumentParser(
        description="""This is my implementation of git.
        It will support a few basic commands."""
    )
    subparsers = parser.add_subparsers(dest='command', title='Commands')

    init_parser = subparsers.add_parser('init')
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('path')
    commit_parser = subparsers.add_parser('commit')
    commit_parser.add_argument('-m')
    logs_parser = subparsers.add_parser('logs')

    args = parser.parse_args()
    git = GitRepo()

    if args.command == 'init':
        git.init()
    elif args.command == 'add':
        git.add(args)
    elif args.command == 'commit':
        git.commit(args)
    elif args.command == 'logs':
        git.logs(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()