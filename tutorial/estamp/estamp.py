
import fitz 
import os
import img2pdf
from PIL import Image as pilImage   
from pathlib import Path
from os.path import splitext
from dataclasses import dataclass

from config import settings

HERE = Path(__file__).resolve().parent

@dataclass
class PageCountError(Exception):
    page_count:int 
    def __str__(self) -> str:
        return f"页面数{self.page_count}不能小于等于0."
    
@dataclass
class StampPageError(Exception):
    stamp_page:str 
    def __str__(self) -> str:
        return f"加盖签章类型 {self.stamp_page} 不在可选的['F', 'L', 'A']范围中."

class Stamp:
    def __init__(self, 
                 pdf_inputname:str, 
                 pdf_outputname:str = '',
                 stamp_page:str = 'L', # 'F'表示第1页，'L'表示最后一页，'A'表示所有页
                 clarity:float = 1.34,
                 file_extention:str = '.png')->None:
        self.pdf_inputname = pdf_inputname
        self.pdf_outputname = pdf_outputname
        self.stamp_page = stamp_page
        self.clarity = clarity 
        self.file_extention = file_extention
        self._set_file_path()

    def _set_file_path(self):
        """设置缺省输出文件名"""
        if len(self.pdf_outputname) == 0:
            pdf_inputname = splitext(self.pdf_inputname)
            self.pdf_inputname_first = pdf_inputname[0]
            self.pdf_outputname = pdf_inputname[0]+'_out'+pdf_inputname[1]
        # 设置完整的读入和输出文件
        self.pdf_input = HERE / settings.PDF_PATH / self.pdf_inputname
        self.pdf_output = HERE / settings.PDF_PATH / self.pdf_outputname
        # 存储临时文件
        self._temp_path = Path(HERE / settings.PDF_PATH / 'temp')
        self._temp_path.mkdir(parents=True, exist_ok=True)
        

    def pdf_to_imgs(self)->int:
        doc = fitz.open(self.pdf_input)
        self.page_count = doc.page_count
        for pg in range(self.page_count):
            page = doc[pg]
            rotate = int(0)
            zoom_x = self.clarity
            zoom_y = self.clarity
            trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
            pm = page.get_pixmap(matrix=trans, alpha = False)
            file_name = str(pg)+self.file_extention
            img_file = self._temp_path / file_name
            pm.save(img_file)
    
    def merge_imgs(self)->None:
        """将公章加盖到指定的页面"""
        if self.page_count <= 0:
            raise PageCountError(self.page_count)
        
        if self.stamp_page == 'F':
            img_filename = str(0)+self.file_extention
            self.merge_img(img_filename)
        elif self.stamp_page == 'L':
            img_filename = str(self.page_count-1)+self.file_extention
            self.merge_img(img_filename)
        elif self.stamp_page == 'A':
            for i in range(self.page_count):
                img_filename = str(i)+self.file_extention
                self.merge_img(img_filename)
        else:
            raise StampPageError(self.stamp_page)

    def merge_img(self,img_filename)->None:
        img1 = pilImage.open(self._temp_path/img_filename)
        stamp_img = pilImage.open(HERE / settings.ESTAMP_PATH / settings.ESTAMP_XIZHI)
        img1_size = img1.size
        layer = pilImage.new('RGBA', img1.size, (0, 0, 0, 0))
        layer.paste(stamp_img, (img1_size[0]//2, img1_size[1]//2))
        out = pilImage.composite(layer, img1, layer)
        self.merge_path = self._temp_path/img_filename
        out.save(self.merge_path)
    
    def imgs_to_pdf(self):
        dirname = self._temp_path
        imgs = []
        for i in range(self.page_count):
            fname = str(i)+self.file_extention
            path = os.path.join(dirname, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        with open(self.pdf_output,"wb") as f:
            f.write(img2pdf.convert(imgs))

    def run(self)->str:
        self.pdf_to_imgs()
        self.merge_imgs()
        self.imgs_to_pdf() 
        path = Path(self.pdf_output)
        if path.is_file():
            return path
        else:
            return None
        



