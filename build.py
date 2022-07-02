import os
import zipfile
import re

def is_excluded(file):
    exclude = [
        '.\.zip',
        'build\.py',
        '.\.pyc'
    ]
    for pattern in exclude:
        if re.search(rf"{pattern}", file): return True
    return False


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for file in files:
            if not is_excluded(file):
                ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('cycal.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('./', zipf)
    zipf.close()