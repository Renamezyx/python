
import os
import zipfile


def zip_subdirectories(directory_path):
    # 获取目录下的一级子目录
    subdirectories = [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]

    # 遍历每个子目录，创建对应的压缩包
    for subdir in subdirectories:
        subdir_path = os.path.join(directory_path, subdir)
        zip_filename = f"{subdir}.zip"
        zip_file_path = os.path.join(directory_path, zip_filename)
        if os.path.exists(zip_file_path):
            os.remove(zip_file_path)
        with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
            # 将子目录下的所有文件添加到压缩包中
            for root, dirs, files in os.walk(subdir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arc_name = os.path.relpath(file_path, subdir_path)
                    zip_file.write(file_path, arcname=arc_name)
        print(f"Compressed '{subdir}' into '{zip_filename}'.")


if __name__ == '__main__':
    dir_path = r'C:\Users\Admin\Downloads\original-data(2)'
    zip_subdirectories(dir_path)
