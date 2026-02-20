import sys
import argparse
from pathlib import Path
from blob import create_blob
class GitRepo:
    def __init__(self, path='.'):
        if path == '.' or path.strip() == '':
            base_path = Path.cwd()
        else:
            base_path = Path(path)

        self.mygit_path = base_path / ".mygit"
        self.objects_path = self.mygit_path / "objects"
        self.refs_path = self.mygit_path / "refs"
        self.heads_path= self.refs_path / "heads"
        self.tags_path= self.refs_path / "tags"
        self.HEAD_path= self.mygit_path
        self.index_path = self.mygit_path
    def init(self):
        try:
            if self.mygit_path.exists():
                if (self.HEAD_path / 'HEAD').exists():
                    print(f'''
                        Mygit already initialized at {self.mygit_path}
                    ''')
                    sys.exit()
            self.mygit_path.mkdir(exist_ok=True)
            self.objects_path.mkdir(exist_ok=True)
            self.refs_path.mkdir(exist_ok=True)
            self.heads_path.mkdir(exist_ok=True)
            self.tags_path.mkdir(exist_ok=True)

            head_file=self.mygit_path / "HEAD"
            with head_file.open("w") as f :
                f.write('ref: refs/heads/main \n')
            print('Mygit sucessfully initialized!')
        except Exception as e :
            print(f'Error: {e} ') 
            print('error creating files')

            sys.exit()
    def add(self, args):
        print("add")
    def commit(self, args):
        print("commit")
    def logs(self, args):
        print("logs")



def main():
    parser = argparse.ArgumentParser(
        description="""This is my implementation of git.
        It will support a few basic commands."""
    )
    subparsers = parser.add_subparsers(dest='command', title='Commands')

    init_parser = subparsers.add_parser('init', help="Initialize repo")
    add_parser = subparsers.add_parser('add' , help='add file/files to track them')
    add_parser.add_argument('path')
    commit_parser = subparsers.add_parser('commit', help='Record changes')
    commit_parser.add_argument('-m','--message',required=True,help='message you want for this commit')
    logs_parser = subparsers.add_parser('logs', help='show log  history')


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