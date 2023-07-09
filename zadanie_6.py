from pathlib import Path
from collections import namedtuple
import logging
import os

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename="TesT_15/zadanie_6.log", encoding="utf-8", level=logging.INFO)

logger = logging.getLogger("zadanie_6.py")

class FileScan:

    def __init__(self) -> None:
        self.FileInfo = namedtuple('FileInfo',['name','ext','type','parent'])

    def scan_dir(self, target: Path, res_list: list)->int:
        size_f = 0
        for path in Path(target).iterdir():
            if path.is_dir():
                size_f = size_f + self.scan_dir(path, res_list)
            else:
                size_f = size_f + path.stat().st_size
            filename, fileextension = os.path.splitext(path.name)
            f = self.FileInfo(filename, fileextension, "file" if path.is_file() else "directory", path.parent.name)
            logger.info(f)
            res_list.append(f)
        return size_f


if __name__ == "__main__":
    scun_dir = Path(__file__).parent.parent
    print(scun_dir)
    s = FileScan()
    res = []
    size = s.scan_dir(scun_dir, res)
