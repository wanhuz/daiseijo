from module.converter import Converter
from module.zip import Zip
from module.util import Util
import os, shutil

def main():
    
    print('Input zip path: ')
    zip_path = input()
    zip_path = Util.clean_drag_and_drop_quote(zip_path)

    print('Unzipping ' + zip_path + '...')
    unzip_path = Zip.unzip(zip_path)

    print('Converting to JPG...')
    for filename in os.listdir(unzip_path):
        filepath = unzip_path + '/' + filename
        Converter.convert_to_jpg(filepath)

    print('Removing temporary file...')
    for filename in os.listdir(unzip_path):
        filepath = unzip_path + '/' + filename
        if ('avif' in filename):
            os.remove(filepath)

    print('CBZipping file...')
    Zip.cbzip(unzip_path)
    shutil.rmtree(unzip_path)

    input('Press any key to exit.')


if __name__ == "__main__":
    main()