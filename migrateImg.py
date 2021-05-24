import os
import re

class ReplaceImage:

    path = ''
    lineNum = 0
    # s = r'http[s]?://(?:raw.githubusercontent.com)/.*?(?:jpg|png|JPG)'
    s = r'media/.*?(?:jpg|png|JPG|jpeg)'
    subpath = ''
    failednum = 0

    def __init__(self):
        self.url_re = re.compile(self.s)

    def search(self, path):
        self.path = path
        self.handleDir(path)

    def handleDir(self, path):
        dirs = os.listdir(path)
        for d in dirs:
            subpath = os.path.join(path, d)
            if os.path.isfile(subpath) and subpath.endswith(".md"):
                self.handleFile(subpath)
            elif os.path.isdir(subpath):
                self.handleDir(subpath)

        print("program end")

    def handleFile(self, fileName):
        print("\n")
        print("start read file %s..." % fileName)
        self.subpath = fileName

        # 注意编码
        f = open(fileName, 'r+',encoding="utf-8",errors="ignore")
        self.lineNum = 1
        data = ""
        while True:
            line = f.readline()
            if not line:
                break
            line = self.replaceImage(line)
            self.lineNum = self.lineNum + 1
            data += line
        f.close()

        # 注意编码
        with open(fileName, "w+",encoding="utf-8",errors="ignore") as f:
            f.writelines(data)

    def replaceImage(self, line):

        searchResult = self.searchImage(line)

        if not searchResult:
            return line
        oldline = line

        for result in searchResult:
            # 这里的replace_url就是将要替换的Gitee图床链接
            replace_url = self.uploadImage(result)
            line = self.replaceLine(line, result, replace_url)

        print("before replace is %s" % oldline)
        print("after replace is %s" % line)

        return line

    def searchImage(self, line):
        if self.url_re.search(line):
            all_search = search.url_re.findall(line)
            return all_search
        else:
            return []

    def replaceLine(self, line, search, url):
        return line.replace(search, url)

    #def uploadImage(self, url):
        #subUrl = url.split("master")[1]
        #targetUrl = "https://gitee.com/shenshilei1022/hugo_image_resource/raw/master" + subUrl
        #return targetUrl

    def uploadImage(self, url):
        subUrl = url.split("/")[1]
        targetUrl = "https://gitee.com/shenshilei1022/hugo_image_resource/raw/master/imgs/" + subUrl
        return targetUrl



if __name__ == "__main__":
    search = ReplaceImage()
    dir = input("dir:")
    search.search(dir)