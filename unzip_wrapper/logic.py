from zipfile import ZipFile

from common.logic import user_home


class Properties:
    archives: list = []
    source_path: str = user_home
    target_path: str = user_home


properties = Properties()


def unzip_archives() -> bool:
    for file_name in properties.archives:
        with ZipFile(file_name, "r") as zf:
            zf.printdir()
            print('Extracting all the files now...')
            tp: str = properties.target_path
            zf.extractall(path=tp)
            print('Done!')
            return True
    return False

