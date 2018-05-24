import random
def roll(times,types):
    output = ['抽卡获得的舰船:']
    l_normal = ['如月','卯月','兰利','博格','突击者',
                '竞技神','奥利克','富特','小猎兔犬',
                '大斗犬','斯彭斯','小天鹅','新月','彗星',
                '狐提','奥马哈','罗利','卡尔斯鲁厄','柯尼斯堡',
                '睦月','利安得','唐斯','卡辛','长良',
                ]
    #普通轻型舰船
    l_rare = ['长岛','本森','谷风','天后',
            '哈曼','西姆斯','弗莱彻','撒切尔',
            '夕暮','布鲁克林','菲尼克斯','亚特兰大',
            '阿基里斯','阿瑞托莎','阿贾克斯','加拉蒂亚',
            '格里德利','命运女神','女将','贝利',
            '莱比锡','神风','松风',
            ]
    #稀有轻型舰船
    l_srare = ['吸血鬼','萤火虫','夕张','欧若拉','黑暗界',
                '恐怖','克利夫兰','吹雪','逸仙','平海',
                '宁海','爱丁堡','圣路易斯','标枪','拉菲',
                '丹佛','女灶神','Z23','绫波','独角兽',
                '查尔斯·奥斯本','莫里',
                ]
    #精锐轻型舰船
    l_ssrare = ['圣地亚哥','贝尔法斯特','蒙彼利埃','明石',]
    #超稀有轻型舰船
    h_normal = [ '彭萨科拉','内华达','青叶','衣笠',
                '俄克拉荷马','奥马哈','罗利','利安得',
                '卡尔斯鲁厄','科隆','柯尼斯堡']
    #普通重型舰船
    h_rare = ['苏塞克斯','波特兰','萨福克','芝加哥',
                '阿瑞托莎','加拉蒂亚','阿基里斯','亚特兰大',
                '反击','宾夕法尼亚','田纳西','加利福尼亚',
                '北安普敦','诺福克','什罗普郡','肯特',
                '布鲁克林','菲尼克斯','阿贾克斯']
    #稀有重型舰船
    h_srare = ['阿贝克隆比','印第安纳波利斯','海伦娜','克利夫兰',
                '夕张','爱丁堡','黑暗界','声望','恐怖','威奇塔',
                '亚利桑那','伊丽莎白女王','纳尔逊','罗德尼',
                '多塞特郡','埃克塞特','约克','伦敦','休斯敦',
                '德意志']
    #精锐重型舰船
    h_ssrare = ['欧根亲王','胡德','厌战','高雄','爱宕'
                ,'圣地亚哥','贝尔法斯特','威尔士亲王']
    #超稀有重型舰船
    s_normal = ['兰利','博格','突击者','竞技神',
                '奥马哈','罗利','利安得','卡尔斯鲁厄',
                '科隆','柯尼斯堡','彭萨科拉']
    #普通特型舰船
    s_rare = ['长岛','波特兰','萨福克','芝加哥',
                '北安普敦','诺福克','什罗普郡','阿瑞托莎'
                '加拉蒂亚','阿基里斯','阿贾克斯','肯特',
                '亚特兰大','布鲁克林','菲尼克斯','朱诺']
    #稀有特型舰船
    s_srare = ['夕张','海伦娜','克利夫兰','爱丁堡',
                '独角兽','皇家方舟','女灶神','威奇塔',
                '多塞特郡','伦敦','约克','大黄蜂',
                '约克城','列克星敦','萨拉托加','黑暗界',
                '恐怖','休斯敦','埃克塞特','印第安纳波利斯']
    #精锐特型舰船
    s_ssrare = ['光辉','圣地亚哥','明石','欧根亲王',
                '企业','贝尔法斯特','高雄','爱宕']
    #超稀有特型舰船

    if times >= 10:
        times = 10
        #超过10次抽卡自动降为10次
    if types == 'l':
        for i in range(0,times):
            f = random.randint(0,100)
            if f > 0 and f <= 55:
                res = random.choice(l_normal)
                output.append("普通："+res)
            elif f > 55 and f <= 81:
                res = random.choice(l_rare)
                output.append("稀有："+res)
            elif f > 81 and f <= 93:
                res = random.choice(l_srare)
                output.append("精锐："+res)
            elif f > 93 and f <= 100:
                res = random.choice(l_ssrare)
                output.append("超稀有："+res)   
    elif types == 'h':
        for i in range(0,times):
            f = random.randint(0,100)
            if f > 0 and f <= 30:
                res = random.choice(h_normal)
                output.append("普通："+res)
            elif f > 30 and f <= 81:
                res = random.choice(l_rare)
                output.append("稀有："+res)
            elif f > 81 and f <= 93:
                res = random.choice(l_srare)
                output.append("精锐："+res)
            elif f > 93 and f <= 100:
                res = random.choice(l_ssrare)
                output.append("超稀有："+res)  
    elif types == 's':
        for i in range(0,times):
            f = random.randint(0,100)
            if f > 0 and f <= 30:
                res = random.choice(s_normal)
                output.append("普通："+res)
            elif f > 30 and f <= 81:
                res = random.choice(s_rare)
                output.append("稀有："+res)
            elif f > 81 and f <= 93:
                res = random.choice(s_srare)
                output.append("精锐："+res)
            elif f > 93 and f <= 100:
                res = random.choice(s_ssrare)
                output.append("超稀有："+res)  
    else:
        pass
    return '\n'.join(output)
    #输出使用join函数重新构建

             
if __name__ == '__main__':
    time = input('请输入模拟抽卡的次数(最大10次！):')
    types = input('请输入抽卡类型(l(轻型舰) or h(重型舰) or s(特型舰)):')
    out = roll(int(time),types)
    print(out)

    
    