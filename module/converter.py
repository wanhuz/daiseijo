from PIL import Image
import pillow_avif

class Converter:

    def convert_to_jpg(avif_fname : str) -> None:
        JPG_fname = avif_fname.replace('.avif', '.jpg')

        AVIFimg = Image.open(avif_fname)
        AVIFimg.save(JPG_fname)
