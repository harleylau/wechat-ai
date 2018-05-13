# coding:utf-8
# 导入模块
from wxpy import *
import requests
import json
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

TULING_TOKEN = 'xxxxxx'

def login_c():
    pass

# 初始化机器人，扫码登陆
bot = Bot(console_qr=True, cache_path=True, login_callback=login_c())
# bot = Bot()
bot.enable_puid() # puid 需要手动开启，请将这句话写在登陆登录之后

# 给机器人自己发送消息
# bot.self.send('Hello World!')
# 给文件传输助手发送消息
# bot.file_helper.send('Hello World!')

# friend = bot.friends().search(u'x')[0]
# friend.send(u"老子来啦！!")

# 查到好好友列表的某个好友并向他发送消息
my_friend = bot.friends().search(u'xxx')[0]
print my_friend

# 回复发送给自己的消息，可以使用这个方法来进行测试机器人而不影响到他人
#@bot.register(bot.self, except_self=False)
@bot.register(my_friend, TEXT)
def reply_self(msg):
    print msg.text
    print msg.sender
    print type(msg.sender)
    url_api = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': TULING_TOKEN,
        'info': msg.text,  # 收到消息的文字内容
        'userid': msg.sender.puid,  # 使用群聊中发送者的 puid 作为 userid 传送给图灵接口， 如果是私聊可以使用 msg.sender.puid
    }
    print json.dumps(data)
    # s = requests.post(url_api, data=data).json()
    s = requests.post(url_api, data=json.dumps(data))
    print s  # 打印所获得的json查看如何使用
    print s.text
    info = json.loads(s.text)

    if info['code'] == 100000:
        print info['text']  # 查看回复消息的内容，可省略
        msg.reply(info['text'])  # 回复消息

embed()
