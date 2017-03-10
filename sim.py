# -*- coding=GBK -*-



tag1 = ["麻枝准","P.A.WORKS","2015年7月","原创","key","TV","Charlotte","夏洛特","2015","校园","大魔王","原创动画","业界良心","2015年","PA","佐仓绫音","超能力","浅井義之","奇幻","动画","内山昂辉","治愈","搞笑","内田真礼","佐倉綾音","浅井义之","烂尾","剧情","季番","関口可奈味"]
tag2 = ["key","J.C.STAFF","2012年10月","GAL改","key社","催泪","Busters!","TV","校园","Little","等得花儿都谢了","緑川光","神作","京阿尼","2012","游戏改","治愈","麻枝准","万分给力","堀江由衣","花泽香菜","友情","搞笑","2012年","山川吉树","LB","LittleBusters!","Little_Busters!","2012十月番"]
#tag1 = ["起亚", "实拍", "汽车", "新闻", "广州车展", "东风", "资讯"]
#tag2 = ["广州", "现场", "汽车", "国际车展", "新闻", "首发", "资讯", "现代", "概念", "北京"]


def similar(tag1,tag2):
    taglist = [([0] * (len(tag2))) for i in range(len(tag1))]
    for a in range(len(tag1)):
        taglist[a][0] = a
    for a in range(len(tag2)):
        taglist[0][a] = a
    for i in range(len(tag1)):
        for j in range(len(tag2)):
            if(tag1[i - 1] == tag2[j - 1]):
                temp = 0
            else:
                temp = 1
            taglist[i][j] = min(taglist[i - 1][j - 1] + temp, taglist[i][j - 1] + 1, taglist[i - 1][j] + 1)
    similarity = 1 - taglist[len(tag1)-1][len(tag2)-1] / float(max(len(tag1), len(tag2)))
    return similarity

print similar(tag1,tag2)
