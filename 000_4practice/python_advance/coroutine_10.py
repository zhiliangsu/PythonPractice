import gevent
import urllib.request
from gevent import monkey

monkey.patch_all()


def download_img(img_url, img_name):
    try:
        print(img_url)
        response = urllib.request.urlopen(img_url)
        with open(img_name, 'wb') as img_file:
            while True:
                img_data = response.read(1024)
                if img_data:
                    img_file.write(img_data)
                else:
                    break
    except Exception as e:
        print('图片下载异常：', e)
    else:
        print('图片下载成功：%s' % img_name)


if __name__ == '__main__':
    img_url1 = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.jj20.com%2Fup%2Fallimg%2F1115%2F092621094420%2F210926094420-8-1200.jpg&refer=http%3A%2F%2Fimg.jj20.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1662640192&t=40001c4a8ae3cef21139227dd66f4a72"
    img_url2 = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.jj20.com%2Fup%2Fallimg%2F1115%2F092621094420%2F210926094420-2-1200.jpg&refer=http%3A%2F%2Fimg.jj20.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1662640192&t=c827d9e94cd23ec928e0b82d335254a5"
    img_url3 = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F8%2F56208e059f6ed.jpg%3Fdown&refer=http%3A%2F%2Fpic1.win4000.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1662640192&t=ed796ba8d50787b0fec543443cc83b5f"

    g1 = gevent.spawn(download_img, img_url1, '1.jpg')
    g2 = gevent.spawn(download_img, img_url2, '2.jpg')
    g3 = gevent.spawn(download_img, img_url3, '3.jpg')

    gevent.joinall([g1, g2, g3])