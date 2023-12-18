from module.converter import Converter
from module.zip import Zip
from module.util import Util
import os, shutil

def main():
    
    print('Input zip file or folder: (Drag and drop compatible)')
    zip_path = input()
    zip_path = Util.clean_drag_and_drop_quote(zip_path)
    is_given_dir = False


    if (Util.is_zip(zip_path)):
        print('Unzipping ' + zip_path + '...')
        unzip_path = Zip.unzip(zip_path)
    elif (os.path.isdir(zip_path)):
        is_given_dir = True
        temp_path = zip_path + '_temp'
        unzip_path = shutil.copytree(zip_path, temp_path)
    else:
        print('Not a valid zip file or directory')
        input('Press any key to exit.')
        exit()


    print('Converting to JPG...')
    for filename in os.listdir(unzip_path):
        filepath = unzip_path + '/' + filename
        Converter.convert_to_jpg(filepath)


    print('Removing temporary file...')
    Util.remove_avif_file_in_directory(unzip_path)


    print('CBZipping file...')
    cbzed_file = Zip.cbzip(unzip_path)
    shutil.rmtree(unzip_path)

    if (is_given_dir):
        new_cbz_name = cbzed_file.replace('_temp', '')
        os.rename(cbzed_file, new_cbz_name)

    input('Press any key to exit.')


if __name__ == "__main__":
    main()