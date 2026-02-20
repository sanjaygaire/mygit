import hashlib
import hashlib
import zlib
from pathlib import Path

def create_blob(file_path, objects_dir):
    file_content = file_path.read_bytes()

    blob_header = f'blob {len(file_content)}\0'.encode()
    blob = blob_header + file_content

    sha1 = hashlib.sha1(blob).hexdigest()
    compressed = zlib.compress(blob)

    objects_dir.mkdir(parents=True, exist_ok=True)

    folder_name = sha1[:2]
    file_name = sha1[2:]

    # print(f'folder {folder_name}')
    # print(f'file {file_name}')

    folder_path = objects_dir / folder_name
    folder_path.mkdir(exist_ok=True)

    object_file = folder_path / file_name
    object_file.write_bytes(compressed)

    # print(sha1)
    return sha1


if __name__ == '__main__':
    create_blob(Path('C:/Users/LOQ/Desktop/100 Weeks of code/mygit/hello.txt'),Path('C:/Users/LOQ/Desktop/100 Weeks of code/mygit/.mygit/objects'))

