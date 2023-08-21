import io
import base64
import os
from pathlib import Path

from PIL import Image
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, SquareModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask, SquareGradiantColorMask

# router = APIRouter(tags=["qrcode"], prefix="/api")
router = APIRouter()

HERE = Path(__file__).resolve().parent
# 生成一个base64格式的二维码，可以直接在网页中被使用
def generate_qrcode_base64(url: str) -> str:
    if len(url.rstrip().lstrip()) == 0:
        url = 'params values is empty!'

    qr = qrcode.QRCode(
        version=1,
        # error_correction=qrcode.constants.ERROR_CORRECT_L,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )
    url = url.encode('utf-8')
    qr.add_data(url)

    # 下面这段不告诉你，可能真要累坏你
    # creates qrcode base64
    out = io.BytesIO()
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(out, 'PNG')

    # 如果语句最后不加上decode('ascii')，生成的base64会前后会
    # 各带有一个b&#39; 在页面中是无法转化成图像的
    return "data:image/png;base64," + base64.b64encode(out.getvalue()).decode('ascii')


def generate_qrcode(url: str) -> str:
    # 获取当前项目路径
    # print(os.getcwd())
    # print(os.path.abspath('.'))
    # print(os.path.dirname(__file__))
    # 获取上级目录
    # print(os.path.abspath(os.path.join(os.getcwd(), "..")))
    # 获取上上级目录
    # print(os.path.abspath(os.path.join(os.getcwd(), "../..")))
    embeded_image_path_url = HERE / 'resource'/'pic'/'zjts.png'
    left_img_url = HERE / 'resource'/'pic'/'qrcode_word.png'
    # embeded_image_path_url = os.path.join(os.getcwd(), r'resource/pic/zjts.png')
    # left_img_url = os.path.join(os.getcwd(), r"resource/pic/qrcode_word.png")
   
    # print(embeded_image_path_url)
    # print(left_img_url)

    if len(url.rstrip().lstrip()) == 0:
        url = 'params values is empty!'

    qr = qrcode.QRCode(
        version=7,
        # error_correction=qrcode.constants.ERROR_CORRECT_L,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    # 像素计算：(21 + (version - 1) * 4 + border * 2) * box_size
    url = url.encode('utf-8')
    qr.add_data(url)
    qr.make(fit=True)

    # 下面这段不告诉你，可能真要累坏你
    # creates qrcode base64
    out = io.BytesIO()
    qrcode_img = qr.make_image(fill_color="black", back_color="white")

    # 添加图标-start

    # 修改二维码形状
    img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
    # 修改二维码颜色
    img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=SquareGradiantColorMask())
    # 嵌入图像
    img_3 = qr.make_image(image_factory=StyledPilImage,
                          embeded_image_path=embeded_image_path_url)
    # 嵌入图像
    img_4 = qr.make_image(fill_color="black", back_color="white", image_factory=StyledPilImage,
                          module_drawer=SquareModuleDrawer(),
                          embeded_image_path=embeded_image_path_url)

    left_img = Image.open(left_img_url)

    result_image = Image.new(img_4.mode, (left_img.width + left_img.height, left_img.height))
    result_image.paste(left_img, (0, 0))
    result_image.paste(img_4, (left_img.width, 0))
    print(left_img.size)
    print(img_4.size)

    # 添加图标-end
    result_image.save(out, 'png')
    out.seek(0)
    result = out

    # 如果语句最后不加上decode('ascii')，生成的base64会前后会
    # 各带有一个b&#39; 在页面中是无法转化成图像的
    return result


@router.get('/qrcode')
def qrcode_show():
    img_stream = generate_qrcode('http://tsgz.zjamr.zj.gov.cn/ecode/300200033110103932023Z1803')
    return StreamingResponse(content=img_stream, media_type='image/png')
