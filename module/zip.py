import zipfile
from os import listdir

class Zip:

    def unzip(zip_fname : str) -> str:
        unzip_path = zip_fname.replace('.zip', '')

        try:
            with zipfile.ZipFile(zip_fname, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
        except zipfile.BadZipFile:
            print('Not a zip file or corrupted zip file')
        except FileNotFoundError:
            input('Zip file not found or not a zip file') 
            exit()
        
        return unzip_path
    
    def cbzip(dirpath : str) -> None:
        cbz_fpath = dirpath + '.cbz'

        with zipfile.ZipFile(cbz_fpath, 'w') as zip:
            for file in listdir(dirpath):
                filepath = dirpath + '/' + file
                zip.write(filepath, arcname=file)