import os
from PIL import Image

def img2pdf(img_name, pdf_name):
    img = Image.open(img_name)
    if img.mode == "RGBA":
        img = img.convert('RGB')
    img.save(pdf_name, "PDF", resolution=100.0, save_all=True)
    print("输出文件名称：", pdf_name)
    # 创建好pdf文件，删除文件夹中的img文件
    os.remove(img_name)


if __name__ == "__main__":
    path = input("请输入文件夹路径：")
    file_list = os.listdir(path)
    for img_path in file_list:
        img_name = path + "\\" + img_path
        pdf_name = path + "\\" + img_path.split(".")[0] + ".pdf"

        print(img_name)

        if "jpg" in img_name or "png" in img_name or "jpeg" in img_name:
            img2pdf(img_name, pdf_name)
        else:
            continue

