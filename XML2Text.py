import os, glob, sys
from bs4 import BeautifulSoup

if len(sys.argv) == 1:
    src_path = None
    dst_path = None
else:
    src_path = str(sys.argv[1])
    dst_path = str(sys.argv[2])

print('`src_path`:', src_path)
print('`dst_path`:', dst_path)

assert os.path.exists(src_path), '[ERROR] `src_path` not exists!'
assert os.path.exists(dst_path), '[ERROR] `dst_path` not exists!'

# traverse `src_path`
for r, d, f in os.walk(src_path):
    file_list = [file for file in glob.glob(r + '/*.xml')]
    if len(file_list) > 0:
        for file_path in file_list:
            file_path = os.path.abspath(file_path)
            print('process file `{file_path}`'.format(file_path=file_path))
            id = os.path.basename(file_path).split('.')[0]

            # convert xml to text
            with open(file_path, 'r') as fin:
                text = BeautifulSoup(fin.read(), features='html5lib').text

            # store text
            with open(os.path.join(dst_path, '{id}.txt'.format(id=id)), 'w') as fout:
                fout.write(text)
