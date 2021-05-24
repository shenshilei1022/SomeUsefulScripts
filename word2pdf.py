import os
import comtypes.client

def d2p(doc_name, pdf_name):
	in_file = doc_name
	out_file = pdf_name
	# create COM object
	word = comtypes.client.CreateObject('Word.Application')
	doc = word.Documents.Open(in_file)
	doc.SaveAs(out_file,FileFormat=17)
	doc.Close()
	word.Quit()
	# 创建好pdf文件，删除文件夹中的word文件
	os.remove(doc_name)
    

if __name__ == "__main__":
    file_path = input("请输入文件夹路径：")
    file_list = os.listdir(file_path)
    for word_path in file_list:
        doc_name = file_path + "\\" + word_path
        pdf_name = file_path + "\\" + word_path.split(".")[0]+".pdf"
        
        print(doc_name)
        # 判断文件名后缀是否是docx或doc
        if word_path.split(".")[-1] == "docx" or word_path.split(".")[-1] == "doc":
            d2p(doc_name,pdf_name)
            print(pdf_name)
        else:
            continue
