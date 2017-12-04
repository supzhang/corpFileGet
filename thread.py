import os
import shutil
import zipfile
import re
from PyQt5.QtCore import pyqtSignal,QThread

class zipThread(Qthread):
    progress = pyqtSignal(list)
    def __init__(self):
        super().__init__()

    def run(self):
        pass





    def zipdir(file, disPath):  # file 文件或文件夹 dispath压缩文件存放位置及文件名
        zipext = ['7z', 'rar', 'zip', 'bz', 'gz']
        r = re.search('^[cdefghijCDEFGHIJ]:.*\.([a-zA-Z0-9]{1,5})', file)  # 检查是否为文件

        try:
            if os.path.exists(file):
                if r:  # 如果是文件
                    filesize = os.path.getsize(file)
                    ext = r.group(1)
                    # filename = re.search(r'.*\\(.*)',file).group(1)
                    if ext in zipext:
                        shutil.copy(file, disPath)
                        ok = 1
                    else:
                        f = zipfile.ZipFile(disPath, 'w', zipfile.ZIP_DEFLATED)
                        f.write(file)
                        f.close()
                        ok = 1
                    self.progress.emit([filesize, filesize])
                else:  # 文件夹处理
                    f = zipfile.ZipFile(disPath, 'w', zipfile.ZIP_DEFLATED)
                    filesize = 0
                    for dirpath, dirnames, filenames in os.walk(file):
                        for filename in filenames:
                            size = os.path.getsize(os.path.join(dirpath, filename))
                            filesize += size

                    zipsize = 0
                    for dirpath, dirnames, filenames in os.walk(file):
                        for filename in filenames:
                            p = os.path.join(dirpath, filename)
                            f.write(p)
                            zipsize += os.path.getsize(p)
                            self.progress.emit([zipsize, filesize])
                    f.close()
                    ok = 1
            else:
                ok = 0
        except Exception as e:
            ok = 0
            print(e)
        return ok

    # f = r'D:\\EFI'
    # f1 = r'D:\\b.zip'
    #
    # a = zipdir(f, f1)
    # print(a)