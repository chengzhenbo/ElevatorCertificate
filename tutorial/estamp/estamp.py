from PIL import Image as pilImage   
import fitz 
from config import settings
from pathlib import Path

HERE = Path(__file__).resolve().parent

class Stamp:
    def __init__(self, 
                 pdf_inputname:str, 
                 pdf_outputname:str,
                 clarity:float = 1.34)->None:
        self.pdf_inputname = pdf_inputname
        self.pdf_outputname = pdf_outputname
        self.pdf_input = HERE / settings.PDF_PATH / self.pdf_inputname
        self.pdf_output = HERE / settings.PDF_PATH / self.pdf_outputname
        self.clarity = clarity 

    def pdf_to_img(self)->None:
        doc = fitz.open(self.pdf_input)
        for pg in range(doc.page_count):
            page = doc[pg]
            rotate = int(0)
            zoom_x = self.clarity
            zoom_y = self.clarity
            trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
            pm = page.get_pixmap(matrix=trans, alpha = False)
            img_file = HERE / settings.PDF_PATH /'1.png'
            pm.save(img_file)
        self.img = img_file
    
    def merge_img(self)->None:

        img1 = pilImage.open(self.img)
        stamp_img = pilImage.open(HERE / settings.ESTAMP_PATH / settings.ESTAMP_XIZHI)
        img1_size = img1.size
        layer = pilImage.new('RGBA', img1.size, (0, 0, 0, 0))
        layer.paste(stamp_img, (img1_size[0]//2, img1_size[1]//2))
        out = pilImage.composite(layer, img1, layer)
        self.merge_path = HERE / settings.PDF_PATH / 'out.png'
        out.save(self.merge_path)
    
    def img_to_pdf(self):
        doc = fitz.open()
        imgdoc = fitz.open(self.merge_path)
        pdfbytes = imgdoc.convert_to_pdf()
        imgpdf = fitz.open('pdf',pdfbytes)
        doc.insert_pdf(imgpdf)
        doc.save(self.pdf_output)
        doc.close()

stamp = Stamp(pdf_inputname='C8950.pdf', pdf_outputname='C8950_out.pdf')
stamp.pdf_to_img()
stamp.merge_img()
stamp.img_to_pdf()