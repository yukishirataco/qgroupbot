# -*- coding:utf-8 -*- #
'''
@作者：npfjcg(Yuzhou "Yukino Shiratama npfjcg" Chen)
@语言：Python 3
@运行环境：Ubuntu LTS 16.04 + Docker + Cool Q Pro
@开源协议：GPL v3
'''
import time
import os
import urllib
from cqhttp import CQHttp, Error
from bs4 import BeautifulSoup
import requests
import json
admins = []
# 说明：
# 此处留空，你可以把需要添加的admin的QQ号按照[123456,78901]这样的形式输入进去
if os.path.exists(r'./config'):
    #如果不存在存储
    pass
else:
    print("数据文件夹不存在，建立中...")
    os.mkdir(r'./config')
    print("建立数据文件夹成功...")
if os.path.exists(r'./logs'):
    pass
else:
    print('日志存储目录不存在，建立中...')
    os.mkdir(r'./logs')
    print('建立日志存储目录成功。')
bot = CQHttp(api_root='http://127.0.0.1:5700/',access_token='',)
# 启动机器人的API监听功能,请把access_token换成自己设定的数值，如果没有就留''，
# 具体配置方法可以看https://cqhttp.cc/docs/3.4/#/Configuration
@bot.on_message() 
#当
def handle_msg(context):
    content=context['message']
    #消息内容单独提取成一个变量，否则增大代码量。
    if context['message_type']=='group':
        '''
            变量:
            group_id:群组消息来自的群号
            conf:根据群号生成的群组对应配置json文件路径
            json变量说明；
                blacklist: 类型:list 说明:存储群组内机器人黑名单的列表
                flag: 类型:int 说明:用于存储比如群组的某些参数的保留变量
        '''
        group_id = context['group_id']
        conf = r'./config/'+str(context['group_id'])+'.json'
        if os.path.exists(conf):
            pass
        else:
            print("配置文件不存在，建立中...")
            with open(conf,'w') as def_conf:
                default_conf = { "blacklist" : ['0'] ,"flag" : 0 }
                def_conf.write(json.dumps(default_conf))
                def_conf.close()
                print("写入配置文件成功")
                #如果配置文件不存在，自动写一个新的默认配置文件
        with open(conf,'r') as grp_con:
            #打开配置文件并读取它，然后把dict的内容转存到变量里
            group_cfg = json.load(grp_con)
            blacklist = group_cfg['blacklist']
            flag = group_cfg['flag']
            grp_con.close()
        if str(context['user_id']) in blacklist:
            #XXX
            pass
        else:
            if content.split()[0]=='!laffey':
                #当群消息前缀为'!laffey'时，自动进入指令模式。
                dates = time.strftime('%Y-%m-%d',time.localtime())
                with open('./logs/'+dates+'.log','a') as logging:
                    times = time.strftime("%H:%M:%S",time.localtime())
                    logging.write("["+dates+' '+times+']'+'用户'+str(context['user_id'])+'调用了指令：'+content+'\n')
                    print("["+dates+' '+times+']'+'用户'+str(context['user_id'])+'调用了指令：'+content)
                #先按"./logs/YYYY-MM-DD.log"的形式记录下来，方便追溯滥用等现象，同时也在shell上输出。
                if context['user_id'] in admins:
                    #管理员命令
                    if content.split(' ',3)[1] == 'blacklist':
                        if content.split(' ',3)[2]=='add':
                            '''
                            功能:添加用户至黑名单
                            权限要求：用户位于list admin内
                            QQ群中需要执行的指令:!laffey blacklist add <QQ号>
                            变量：
                            number: 类型:str 说明:参数2，记录下要加入黑名单的用户QQ
                            f_conf_w: 类型:FileIOWrapper 说明：更新群组配置文件使用的文件指针
                            '''
                            number = content.split(' ',3)[3]
                            if number.isdigit():
                                #如果number是一个合法的数字，继续，否则报错退出
                                if number in blacklist:
                                    #如果用户在黑名单里，不添加并返回提示。
                                    bot.send(context,'你要添加到黑名单的用户:'+number+'已存在')
                                else:
                                    blacklist.append(number)
                                    with open(conf,'w') as f_conf_w:
                                        dic_conf = json.dumps(dict(blacklist=blacklist,repeat=repeat,flag=flag))
                                        f_conf_w.write(dic_conf)
                                        f_conf_w.close()
                                    bot.send(context,'用户:'+number+'已被添加至群组:'+str(group_id)+'的黑名单里。')
                            else:
                                bot.send(context,'你输入的用户QQ号不是合法的数字。')
                        elif content.split(' ',3)[2]=='del':
                            '''
                            功能:从黑名单中把用户删除
                            权限要求：用户位于list admin内
                            QQ群中需要执行的指令:!laffey blacklist del <QQ号>
                            变量：
                            number: 类型:str 说明:参数2，记录下要从黑名单移除的用户QQ号
                            f_conf_w: 类型:文件指针（写入） 说明：更新群组配置文件使用的文件指针
                            '''                            
                            number = content.split(' ',3)[3]
                            if number.isdigit():
                                if number in blacklist:
                                    loc = blacklist.index(number)
                                    blacklist.pop(loc)
                                    with open(conf,'w') as f_conf_w:
                                        dic_conf = json.dumps(dict(blacklist=blacklist,repeat=repeat,flag=flag))
                                        f_conf_w.write(dic_conf)
                                        f_conf_w.close()
                                    bot.send(context,'用户'+number+'已从群组:'+str(group_id)+'的黑名单中移除。')
                                
                                else:
                                    bot.send(context,'用户不存在，请查看是否有输入错误。')
                            else:
                                bot.send(context,'你的输入有误，数据不是合法数字。')
                    elif content.split(' ',1)[1]=='status':            
                        '''
                        功能:查看服务器运行状态（仅Linux系统下可用）
                        权限要求：用户位于list admin内
                        QQ群中需要执行的指令:!laffey status
                        变量：
                        略
                        返回内容：
                        内存：已用内存(M)/总内存数量(M)
                        负载：一分钟的平均负载 五分钟的平均负载 十五分钟的平均负载
                        硬盘：已用硬盘空间(M)/可用硬盘空间(M)
                        '''
                        mem = {}
                        f = open("/proc/meminfo")
                        lines = f.readlines()
                        f.close()
                        for line in lines:
                            if len(line) < 2: continue
                            name = line.split(':')[0]
                            var = line.split(':')[1].split()[0]
                            mem[name] = int(var) * 1024.0
                        mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
                        loadavg = {}
                        f = open("/proc/loadavg")
                        con = f.read().split()
                        f.close()
                        loadavg['lavg_1']=con[0]
                        loadavg['lavg_5']=con[1]
                        loadavg['lavg_15']=con[2]
                        loadavg['nr']=con[3]
                        loadavg['last_pid']=con[4]
                        hd={}
                        disk = os.statvfs("/")
                        avahd = disk.f_bsize * disk.f_bavail / (1024*1024)
                        caphd = disk.f_bsize * disk.f_blocks / (1024*1024)
                        frehd = disk.f_bsize * disk.f_bfree / (1024*1024)
                        usedRam = str(int((mem['MemUsed'])/(1024*1024)))
                        topRam = str(int(mem['MemTotal']/(1024*1024)))
                        bot.send(context,"内存:"+usedRam+'M/'+topRam+'M('+str(round(float((mem['MemUsed'])/int(mem['MemTotal']))*100))+'%)\n'+"负载:"+str(loadavg['lavg_1'])+' '+str(loadavg['lavg_5'])+' '+str(loadavg['lavg_15'])+"\n硬盘:"+str(round(caphd-avahd))+'M/'+str(round(caphd))+'M')
                else:
                    pass
                if content.split(' ',1)[1]=='info':
                    '''
                    功能:查看当前群组和用户的信息
                    权限要求：无
                    QQ群中需要执行的指令:!laffey status
                    变量：
                    无
                    返回内容：
                        您的信息：
                        聊天类型：在群组里为'group'
                        消息ID:
                        发送者QQ:
                    '''
                    bot.send(context,'您的信息:\n聊天类型:'+context['message_type']+'\n消息ID:'+str(context['message_id'])+'\n发送者QQ:'+str(context['user_id']))
                elif content.split(' ',1)[1]=='version':
                    '''
                    功能:查看当前群组和用户的信息
                    权限要求：无
                    QQ群中需要执行的指令:!laffey version
                    变量：
                    无
                    返回内容：
                        CQBot Engine build 1805-06，
                        Inside version:Horizon
                        2018 Yukino Shiratama npfjcg
                    '''
                    bot.send(context,'CQBot Engine build 1805-06，\nInside version:Horizon\n2018 Yukino Shiratama npfjcg')
                elif content.split(' ',2)[1]=='blacklist':
                    '''
                    功能:查看当前群组的机器人黑名单（仅非黑名单用户可以查看）
                    权限要求：无
                    QQ群中需要执行的指令:!laffey blacklist
                    变量：
                    无
                    返回内容：
                        群组(群号)内的机器人黑名单查询完毕，共有（数量）项，
                        内容如下：
                        （群组黑名单的list）
                    '''
                    if content.split(' ',3)[2].strip()=='show':
                        #如果不带参数就执行查询，如果带参数就是管理员指令，什么都不做
                        bot.send(context,'群组'+str(group_id)+'内的机器人黑名单查询完毕，共有'+str(len(blacklist))+'项\n内容如下:'+str(blacklist))
                     else:
                        pass
                elif content.split(' ',2)[1]=='baidu':
                    '''
                    功能:百度搜索，使用爬虫获得结果链接并返回结果数量
                    权限要求：无
                    QQ群中需要执行的指令:!laffey baidu <要搜索的内容>
                    变量：
                    略
                    返回内容：
                        百度：
                        https://www.baidu.com/s?wd=(要搜索的内容)
                        百度为您找到相关结果约（数量）个
                    '''
                    content=content.split(' ',2)[2]
                    content.strip()
                    #获得字符串，去除空格
                    content.replace(' ','+')
                    #将字符串的空格换成加号
                    url=r'http://www.baidu.com/s?wd='
                    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
                    source = requests.get(url+content,headers=headers)
                    #Requests获得网页内容
                    source.encoding = 'utf-8'
                    #调整编码，防止乱码
                    soup=BeautifulSoup(source.text,'lxml')
                    #bs4解析
                    tables = soup.find_all(name='div',attrs={"class":"nums"})
                    #找到包含结果数量的标签
                    bot.send(context,'百度:'+url+content+'\n'+str(tables[0])[133:-13])
                elif content.split(' ',2)[1]=='google':
                    '''
                    功能:谷歌搜索，使用官方API获得结果链接并返回结果数量
                    权限要求：无
                    QQ群中需要执行的指令:!laffey google <要搜索的内容>
                    变量：
                    略
                    返回内容：
                        Google：
                        http://www.google.com/search?q=(要搜索的内容)
                        找到约 (数量) 条结果
                    '''
                    content=content.split(' ',2)[2]
                    content.strip()
                    r = requests.get('http://www.google.com/search',
                         params={'q':'"'+content+'"',
                                 "tbs":"li:1"}
                        )
                    soup = BeautifulSoup(r.text,'lxml')
                    bot.send(context,'Google:http://www.google.com/search?q='+content+'\n'+soup.find('div',{'id':'resultStats'}).text)
                elif content.split(' ',2)[1]=='booru':
                    '''
                    功能:Gelbooru查找图片，使用官方API获得结果数量并返回随机一页的随机一张图。
                    权限要求：无
                    QQ群中需要执行的指令:!laffey booru <要搜索的图片tag(s)>
                    变量：
                    tags 类型:str 说明:用户要搜索的图片tag
                    past 类型:float 说明:开始执行指令的时间戳，用于计算指令运行时间
                    num 类型:int 说明:用户请求的tag(s)下有多少图片
                    maxpage 类型:int 说明:请求的图片总共有多少页
                    返回内容：
                        用时（时间)s
                        对于tag:(要搜索的图片tag(s))
                        Gelbooru上有(数量)张图
                        这是随意一张图:
                        (爬取下来的图片)
                    '''
                    tags=content.split(' ',2)[2]
                    past = time.time()
                    source=requests.get(r'http://gelbooru.com/index.php?page=dapi&s=post&q=index&tags='+tags+' rating:safe -highres')
                    soup = BeautifulSoup(source.text, "lxml")
                    #如果API页面能正常打开
                    num = int(soup.find('posts')['count'])
                    #就用bs4解析网页
                    maxpage = int(round(num/100))
                    if maxpage <= 1:
                        page=0
                    else:
                        page=randint(0,maxpage)
                    source=requests.get(r'http://gelbooru.com/index.php?page=dapi&s=post&q=index&tags='+tags+' rating:safe -highres'+'&pid='+str(page))
                    soup = BeautifulSoup(source.text, "lxml")
                    t=soup.find('posts')
                    p=t.find_all('post')
                    if num < 100:
                        pic=p[randint(0,num-1)]
                    elif page==maxpage:
                        pic=p[randint(0,num%100-1)]
                    else:
                        pic=p[randint(0,99)]
                    if num > 0:
                        bot.send(context,'用时'+str(round(time.time()-past))+'s\n对于tag：'+tags+'\n'+'Gelbooru上有'+str(num)+'张图\n这是随机一张图:')
                        bot.send(context,[{"type": "image","data": {"file": pic['sample_url']}}])
                    elif num ==0:
                        bot.send(context,'对于tag：'+tags+'\n'+'Gelbooru上没有找到图片')
                elif content.split(' ',2)[1]=='help':
                    if content.split(' ',2)[2]=='help':
                        bot.send(context,'指令说明:\n!laffey version\n查看bot的版本号。')
                    elif content.split(' ',2)[2]=='baidu':
                        bot.send(context,'指令说明:\n!laffey baidu <内容>\n百度搜索，返回搜索链接和结果数量。')
                    elif content.split(' ',2)[2]=='google':
                        bot.send(context,'指令说明:\n!laffey google <内容>\nGoogle搜索，返回搜索链接和结果数量。')
                    elif content.split(' ',2)[2]=='booru':
                        bot.send(context,'指令说明:\n!laffey booru <tags>\nGelbooru,返回随机一张图的链接。')
                    elif content.split(' ',2)[2]=='info':
                        bot.send(context,'指令说明:\n!laffey info\n查看您当前信息。（仅用于调试。）')
                    elif content.split(' ',2)[2]=='blacklist':  
                        bot.send(context,'指令说明:\n!laffey blacklist show\n(仅非黑名单用户)查询黑名单内容')  
                    else:
                        pass
                else:
                    pass
            else:
                pass
bot.run(host='127.0.0.1', port=8080)        
