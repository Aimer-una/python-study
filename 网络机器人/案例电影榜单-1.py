import requests
from lxml import html

# 常量
BASE_URL = 'https://ssr1.scrape.center'


def get_movie_info(movie_url):
    pass



def save_all_movies(all_movies):
    pass


def main():
    # 1. 发起请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    # ✅ 修正点：必须写成 headers=headers
    response = requests.get(BASE_URL, headers=headers, timeout=10)

    # 检查状态码
    if response.status_code == 200:
        print("✅ 请求成功！")

        # 2. 解析数据
        document = html.fromstring(response.text)

        # ✅ 修正点：不要直接 print(document)，那样只能看到内存地址
        # 我们可以直接开始提取数据来验证是否成功

        # 这个网站的电影列表在 class="item" 的 div 里

        movie_list = document.xpath('//div[@class="el-card__body"]')

        print(f"🎬 共找到 {len(movie_list)} 部电影：\n")

        # 遍历电影列表获取电影详情
        all_movies = []
        for movie in movie_list:
            # 电影详情的url
            urls = movie.xpath("./div/div[@class = 'el-col el-col-24 el-col-xs-8 el-col-sm-6 el-col-md-4']/a/@href")
            if urls:
                movie_url = BASE_URL + urls[0]
                print(movie_url)
                # 发起请求，获取电影详情数据
                movie_info = get_movie_info(movie_url)
                all_movies.append(movie_info)

        # 保存到csv文件
        save_all_movies(all_movies)
if __name__ == '__main__':
    main()