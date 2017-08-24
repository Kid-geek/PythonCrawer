from urllib import request

if __name__ == '__main__':
    url='http://www.whatismyip.com.tw'
    proxy = {'http': '39.71.57.200:8118'}
    proxy_support=request.ProxyHandler(proxy)
    opener=request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    # 安装OPener
    request.install_opener(opener=opener)
    # 使用自己安装好的Opener
    response = request.urlopen(url)
    html = response.read().decode("utf-8")
    # 打印信息
    print(html)