import os
import shutil

source_dir = './storage'
print('目录 %s 下有文件:'% source_dir)
for name in os.listdir(source_dir):
    print(name)

print()

result_dir = './result'
if not os.path.exists(result_dir):
    os.makedirs(result_dir)
for i, name in enumerate(os.listdir(source_dir)):
    basename, ext = os.path.splitext(name)
    new_name ='%03d' % i + ext
    print('正在重命名:%20s -->%s' % (name,new_name))

result_dir = './result'
if not os.path.exists(result_dir):
    os.makedirs(result_dir)
for i, name in enumerate(os.listdir(source_dir)):
    basename, ext = os.path.splitext(name)
    new_name ='%03d'% i + ext
    print('正在重命名:%20s --> %s'% (name,new_name))

    old_path = os.path.join(source_dir, name)
    new_path = os.path.join(result_dir, new_name)
    shutil.copy(old_path, new_path)
