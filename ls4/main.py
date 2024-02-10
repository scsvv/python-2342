import os
import subprocess

def find_large_files(start_path="D:\\", min_size_gb=10):
    with open('output.txt', 'a') as result_file:
        for root, dirs, files in os.walk(start_path):
            for file in files:
                file_path = os.path.join(root, file)

                file_size_gb = os.path.getsize(file_path) / 1024 ** 3
                print(f"{file_size_gb:.2f}Gb {file_path}")
                if file_size_gb > min_size_gb:
                    result_file.write(f'{file_path} - {file_size_gb:.2f}Gb\n')


def search_and_open_folder(folder_path, file_name): 
    try:
        for root, dirs, files in os.walk(folder_path):
            if file_name in files:
                file_path = os.path.join(root, file_name)

                print(f"File Founded, {file_path}")
                subprocess.run(['start', root], shell=True)

                return
        print(f"File not Founded")
    except Exception as e:
        print(e)
    


if __name__ == "__main__":
    # find_large_files('D:\Загрузки', 2)
    search_and_open_folder('D:\Schools\Python_scripts\python-2342', 'index.js')