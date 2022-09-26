import multiprocessing
import os
import shutil


def copy_work(src_dir, dst_dir, file_name):
    pid = multiprocessing.current_process()
    print(pid)

    src_file_path = os.path.join(src_dir, file_name)
    dst_file_path = os.path.join(dst_dir, file_name)

    with open(dst_file_path, 'wb') as dst_file:
        with open(src_file_path, 'rb') as src_file:
            while True:
                src_file_data = src_file.read(1024)
                if src_file_data:
                    dst_file.write(src_file_data)
                else:
                    break

if __name__ == '__main__':
    src_dir = '000_4practice'
    dst_dir = './test'

    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)

    os.mkdir(dst_dir)
    file_name_list = os.listdir(src_dir)
    pool = multiprocessing.Pool(3)
    for file_name in file_name_list:
        pool.apply_async(copy_work, args=(src_dir, dst_dir, file_name))

    pool.close()
    pool.join()