#coding:utf8
#python模拟百度蜘蛛登录新浪
'''
网易 yodao 有道： Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/ ; )
Goolgle ： Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
baidu： Baiduspider+(+http://www.baidu.com/search/spider.htm)
msn： msnbot/1.1 (+http://search.msn.com/msnbot.htm)
sogou： Sogou Orion spider/3.0(+http://www.sogou.com/docs/help/webmasters.htm#07)
'''
import requests
def simulated_BaiduSpider(url):
    headers={"User-Agent":"Baiduspider+(+http://www.baidu.com/search/spider.htm)"}
    html=requests.get(url,headers=headers).content
    print (html)

if  __name__=="__main__":
    url='http://www.sina.com.cn/'
    simulated_BaiduSpider(url)
