import random


class Headers(object):
    def __init__(self, referer='http://www.mzitu.com/'):
        self.referer = referer
        self.user_agent = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
            "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
            "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
            "Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11",
            "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)",
            "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)",
            "Mozilla/5.0(iPhone;U;CPUiPhoneOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5",
            "Mozilla/5.0(Linux;U;Android2.3.7;en-us;NexusOneBuild/FRF91)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
            "Mozilla/4.0(compatible;MSIE6.0;)Opera/UCWEB7.0.2.37/28/999",
            "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"
        ]

    def get_headers(self, referer):
        return {
            'User-Agent': random.choice(self.user_agent),
            'Referer': self.referer
        }
