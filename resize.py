from PIL import Image
from glob import glob
import os

image_size = 600


def rotateImage(img, orientation):
    """
    画像ファイルをOrientationの値に応じて回転させる
    """
    #orientationの値に応じて画像を回転させる
    if orientation == 1:
        pass
    elif orientation == 2:
        #左右反転
        img_rotate = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 3:
        #180度回転
        img_rotate = img.transpose(Image.ROTATE_180)
    elif orientation == 4:
        #上下反転
        img_rotate = img.transpose(Image.FLIP_TOP_BOTTOM)
    elif orientation == 5:
        #左右反転して90度回転
        img_rotate = img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90)
    elif orientation == 6:
        #270度回転
        img_rotate = img.transpose(Image.ROTATE_270)
    elif orientation == 7:
        #左右反転して270度回転
        img_rotate = img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270)
    elif orientation == 8:
        #90度回転
        img_rotate = img.transpose(Image.ROTATE_90)
    else:
        pass

    return img_rotate


def rotate_img(img: Image) -> Image:
    try:
        #exif情報取得
        exifinfo = img._getexif()
        #exif情報からOrientationの取得
        orientation = exifinfo.get(0x112, 1)
        #画像を回転
        img = rotateImage(img, orientation)
    except:
        pass
    return img


def scale_down(path: str) -> Image:
    img = Image.open(path)
    img = rotate_img(img)
    width, height = img.size
    down_rate = image_size / max(width, height)
    resized = img.resize((int(width * down_rate), int(height * down_rate)),
                         Image.BILINEAR)
    return resized


def fill_backgound(img: Image) -> Image:
    filled_img = Image.new("RGB", (image_size, image_size), (256, 256, 256))
    size = img.size
    if size[0] >= size[1]:    # width >= height
        margin = (image_size - min(size)) // 2
        filled_img.paste(img, (0, margin))
    else:
        margin = (image_size - min(size)) // 2
        filled_img.paste(img, (margin, 0))

    return filled_img


if __name__ == "__main__":
    exts = ("jpg", "JPG")
    files = []
    for ext in exts:
        files += glob(f"回収物品写真/*.{ext}")
    for file in files:
        no_ext_filename = os.path.splitext(os.path.basename(file))[0]
        dst = os.path.join("static/img", no_ext_filename + ".jpg")
        if os.path.exists(dst):
            continue
        else:
            fill_backgound(scale_down(file)).save(dst)