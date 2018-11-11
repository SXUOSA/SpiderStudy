import requests
import uuid
from bs4 import BeautifulSoup
import time

# 保存图片
def save_pic(content):
    # 生成唯一识别码
    unique_uuid = uuid.uuid1()
    # 打开文件, 文件名为唯一识别码 + jpg, 目录在imgs 
    f = open("./imgs/" + str(unique_uuid) + '.jpg', 'wb')
    # 写入数据
    f.write(content)

def get_duowan():
    # 需要获取页面的地址
    base_url = "http://tu.duowan.com/tu"

    # requests进行请求
    result = requests.get(base_url)
    # print(result.text)

    # 解析获得的HTML页面
    soup = BeautifulSoup(result.text, "html.parser")

    # 获得所有的图片标签
    imgs = soup.select("img")

    # 从图片标签中提取地址
    for img in imgs:
        # 请求提取到的地址，并且保存图片
        content = requests.get(img.get('src')).content

        # 保存图片
        save_pic(content)
        

def get_xinxianshi():
    base_url = "http://jandan.net/page/"

    # 遍历二十页
    for i in range(20):

        # 为了模拟人类行为，采取延时手段
        time.sleep(1)

        # 向我们事先分析好的地址发送请求
        result = requests.get(base_url + str(i))

        # 用HTML分析引擎去分析我们爬取下来的结果
        soup = BeautifulSoup(result.text, 'html.parser')

        # 找到所有h2标签中的链接
        for link in soup.find_all("h2"):

            # 对每一个h2标签进行提取
            for xinxianshi in link.contents:

                # 获取新鲜事的标题
                title = xinxianshi.string

                # 获取路径
                href = xinxianshi.get('href')

                # 请求全文页面
                result = requests.get(href)

                # 用beautiful解析新得到的页面
                soup_content = BeautifulSoup(result.text, 'html.parser')

                for j in  soup_content.select(".post p"):
                    print(j.get_text())



if __name__ == '__main__':
    # get_xinxianshi()
    get_duowan()