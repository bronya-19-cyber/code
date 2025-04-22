import tkinter as tk
import random
import re
gua=['坤','☷','☷','坤']

def draw_lottery():
    # 随机选择一个选项
    result = random.choice(options)
    #获取标签
    mack = options.index(result)
    #查找对应解释
    mean = means[mack]
    # 更新结果标签
    result_label.config(text=f"抽签结果:\n{result}",font=("Arial", 32))
    mean_label.config(text=f"\n{mean}",font=("Arial",20))
    atta_label.config(text=f"请点击变爻按钮",font=("Arial", 32))
    bmean_label.config(text=f"",font=("Arial",20))
    global gua
    gua = result.split("\n")


#处理卦象，并进行转换
def c_gua():
    global gua
    visgua = gua[1]
    owngua = gua[2]
    visgua = basgua[visgua]
    owngua = basgua[owngua]
    tolgua = [visgua,owngua]
    return tolgua

#将卦象编码转换为卦象图
def tra_gua(tolgua1,tolgua2,number):
    lis=[]
    tolgua1[0] = next((k for k ,v in basgua.items() if v == tolgua1[0]),None)
    tolgua1[1] = next((k for k ,v in basgua.items() if v == tolgua1[1]),None)
    keyword1 = "\n"+str(tolgua1[0])+'\n'+str(tolgua1[1])+"\n"
    tolgua2[0] = next((k for k ,v in basgua.items() if v == tolgua2[0]),None)
    tolgua2[1] = next((k for k ,v in basgua.items() if v == tolgua2[1]),None)
    keyword2 = "\n"+str(tolgua2[0])+'\n'+str(tolgua2[1])+"\n"
    lis=[s for s in options if keyword1 in s]
    if lis !=[]:
        result=lis[0]
        #获取标签
        mack = options.index(result)
        #查找对应解释
        mean = means[mack]
        bmean_label.config(text=f"\n{mean}",font=("Arial",12))
        atta_label.config(text=f"变第{number}爻:\n{result}",font=("Arial", 32))
    elif len(lis) <=1:
        lis=[]
        lis=[s for s in options if keyword2 in s]
        result=lis[0]
        #获取标签
        mack = options.index(result)
        #查找对应解释
        mean = means[mack]
        atta_label.config(text=f"变第{number}爻:\n{result}",font=("Arial", 32))
        bmean_label.config(text=f"\n{mean}",font=("Arial",12))
    else:
        atta_label.config(text=f"无",font=("Arial", 32))
    

#变卦匹配
def gua_find(number):
    tolgua = c_gua()
    visgua = list(tolgua[0])
    owngua = list(tolgua[1])
    #6-4杠变化匹配
    if number == '6':
        visgua[0] = str(1^int(visgua[0]))
    elif number == '5':
        visgua[1] = str(1^int(visgua[1]))
    elif number == '4':
        visgua[2] = str(1^int(visgua[2]))
    #3-1杠变化匹配
    elif number == '3':
        owngua[0] = str(1^int(owngua[0]))
    elif number == '2':
        owngua[1] = str(1^int(owngua[1]))
    elif number == '1':
        owngua[2] = str(1^int(owngua[2]))
    else:
        print("操作失败")
    tolgua1=[
            visgua[0]+visgua[1]+visgua[2],
            owngua[0]+owngua[1]+owngua[2]
            ]
    tolgua2=[
            owngua[2]+owngua[1]+owngua[0],
            visgua[2]+visgua[1]+visgua[0]
            ]
    tra_gua(tolgua1,tolgua2,number)
    


#基础卦字典
basgua={
"☰":"111","☱":"011","☲":"101","☴":"110","☷":"000","☶":"100","☵":"010","☳":"001"
}

# 抽签选项列表
options = [
"屯\n☵\n☳\n蒙", "需\n☰\n☵\n讼", "师\n☷\n☵\n比", "小畜\n☴\n☰\n履", "泰\n☷\n☰\n否",
"同人\n☰\n☲\n大有", "谦\n☷\n☶\n豫", "随\n☱\n☳\n蛊", "观\n☴\n☷\n临", "噬嗑\n☲\n☳\n贲",
"剥\n☶\n☷\n复", "无妄\n☰\n☳\n大畜", "大过\n☱\n☴\n大过", "咸\n☱\n☶\n恒", "遁\n☰\n☶\n大壮",
"晋\n☲\n☷\n明夷", "家人\n☴\n☲\n睽", "蹇\n☵\n☶\n解","损\n☶\n☱\n益", "夬\n☱\n☰\n姤",
"萃\n☱\n☷\n升", "困\n☱\n☵\n井", "革\n☱\n☲\n鼎","渐\n☴\n☶\n归妹", "丰\n☳\n☲\n旅",
"涣\n☴\n☵\n节", "小过\n☳\n☶\n小过", "既济\n☲\n☵\n未济","乾\n☰\n☰\n乾", "坤\n☷\n☷\n坤",
'坎\n☵\n☵\n坎','离\n☲\n☲\n离','震\n☳\n☳\n艮',"巽\n☴\n☴\n兑","颐\n☴\n☱\n颐",
"中孚\n☶\n☳\n中孚"
]
#挂意列表
means = [
"屯卦象征事物初生时的艰难与混乱，充满生机但面临重重阻碍\n蒙卦表示蒙昧无知，需要启蒙教育来开启智慧\n二者分别从起始的艰难和懵懂状态两个角度描述事物开端",
"需卦讲的是等待时机，在条件不成熟时耐心蓄积力量\n讼卦则代表争讼、纠纷，是等待过程中可能因利益冲突引发的状况",
"师卦象征军队、战争，强调领导者要以正道带领众人作战\n比卦寓意亲密团结、互助协作，是战争之后或避免战争所期望达到的和平共处状态",
"小畜卦表示小有积蓄、小有成就，但力量还不够强大\n履卦意味着小心行动、履行职责，在有一定积累后要谨慎行事",
"泰卦象征通泰、吉祥，上下交融，万物亨通\n否卦代表闭塞、不通，上下隔阂，诸事不顺\n二者是事物发展的两种相反状态",
"同人卦体现和同于人、团结协作，强调志同道合者的聚合\n大有卦表示大获所有、富有，是团结协作之后取得的成果",
"谦卦寓意谦虚、退让，谦虚者能得到各方助力\n豫卦有安乐、愉悦之意，但也提醒要居安思危\n二者从不同态度方面影响着人的境遇",
"随卦代表随从、追随，倡导顺应时势、灵活应变\n蛊卦象征整治、革新，是在随顺过程中发现问题后进行的变革",
"观卦表示观察、审视，通过观察来了解情况以更好地统治或自我提升\n临卦有监督、统治之意，强调领导者要关怀民众",
"噬嗑卦寓意咬合、刑罚，通过强制手段来维护秩序\n贲卦象征文饰、修饰，注重外在形式和内在品质的统一，一个重秩序规范，一个重外在美化",
"剥卦代表剥落、侵蚀，形势逐渐恶化\n复卦表示回复、回归，象征生机的重现和希望的到来，是事物从衰败到复兴的过程体现。",
"无妄卦寓意不妄为、遵循正道，否则将遭遇灾祸\n大畜卦有大量蓄积、培养贤能之意，遵循正道才能更好地蓄积力量",
"大过卦表示过度、超越常规，调养过度或行事过度都会带来问题",
"咸卦寓意感应、交感，强调人与人之间的情感交流和相互影响\n恒卦表示恒久、持久，倡导坚守正道持之以恒，情感感应需持久维护",
"遁卦代表退避、隐居，当形势不利时及时退避\n大壮卦象征强盛、壮大，但要防止过于刚强而引发危险，是进与退的不同策略",
"晋卦有前进、晋升之意，鼓励人们积极进取\n明夷卦表示光明受损、艰难困苦，此时应韬光养晦，是进取与受挫的不同阶段",
"家人卦体现家庭、家族，强调家庭的秩序和成员间的责任\n睽卦代表乖离、分离，家庭中也可能出现矛盾分离的情况",
"蹇卦寓意艰难、险阻，需在困境中寻找突破之道\n解卦象征缓解、解除困难，是从困境到解脱的转变",
"损卦有减损、自我牺牲之意，通过适当舍弃换取更大利益\n益卦表示增益、受益，积极行动会带来好处\n二者体现了得失的辩证关系",
"夬卦代表决断、决裂，要果断去除不良因素\n姤卦寓意相遇、邂逅，象征新的机遇和缘分，是去除旧有迎来新生的过程",
"萃卦有聚集、聚合之意，如物以类聚人以群分\n升卦表示上升、进步，象征事业和地位的提升，聚集是上升的基础",
"困卦代表困穷、困境，此时要坚守内心信念\n井卦象征水井、滋养，寓意提供稳定支持和帮助，在困境中期待滋养解脱",
"革卦表示变革、革新，当旧制度不适应时要勇于变革\n鼎卦寓意鼎新、稳定，象征建立新的秩序和权威，变革之后需要稳定",
"渐卦表示渐进、逐步发展，强调做事循序渐进\n归妹卦有女子出嫁之意，涉及婚姻和家庭关系，生活中很多事包括婚姻都需渐进发展",
"丰卦象征丰盛、繁荣，但要防止因满而盈\n旅卦代表旅行、旅居，寓意在漂泊中寻找归宿，繁荣时可能会有漂泊不定之感",
"涣卦有涣散、离散之意，需要凝聚力量避免瓦解\n节卦表示节制、节俭，提醒合理控制欲望，防止因过度而离散",
"小过卦代表小有过失，出现小偏差时要及时纠正，诚信缺失可能导致过失",
"既济卦象征成功、完成，但要警惕功成之后的懈怠\n未济卦表示未完成、有待继续努力，提醒永远保持进取之心，成功只是阶段，永远有未完成之事",
"乾为天，纯阳之卦，刚健不已",
"坤为地，纯阴之卦，柔顺承载",
"坎卦代表险陷、困难，提醒人们在困境中坚定信念",
"离卦象征附着、光明，如日高悬照亮万物，是从困境走向光明的对比",
"震卦代表震动、震惊，提醒人们保持警觉\n艮卦象征静止、止息，教导人们适时停止避免过度\n一动一静相互平衡",
"巽卦表示顺从、谦逊，通过柔顺方式达成目标\n兑卦象征喜悦、和悦，倡导积极乐观态度，顺从往往能带来和悦",
"颐卦表示春暖万物养育，依时养贤育民。阳实阴虚，实者养人，虚者为人养。自食其力",
"中孚卦指出了主方应当与客方和谐共处"
]


# 创建主窗口
root = tk.Tk()
atta = tk.Toplevel(root)
atta.attributes('-topmost',True)
#设置窗体的大小
xsize=1200
ysize=800
root.geometry(str(xsize)+"x"+str(ysize))
atta.geometry(str(xsize//2)+"x"+str(ysize//2))
root.title("今日卦象")
atta.title("卦象变卦")
# 创建结果标签
result_label = tk.Label(root, text="抽签结果:\n未抽签", font=("Arial", 32))
result_label.pack(pady=20)
atta_label = tk.Label(atta, text="请先抽签", font=("Arial", 32))
atta_label.pack(pady=20)
#创建一个解释标签
mean_label = tk.Label(root)
mean_label.pack(pady=5)
bmean_label = tk.Label(atta)
bmean_label.pack(pady=10)
# 创建抽签按钮
draw_button = tk.Button(root, text="开始抽签", font=("Arial", 14), command=draw_lottery)   
draw_button.pack(pady=10)
draw_button.place(x=xsize/2,y=ysize*3/4+ysize/10)
atta_button = tk.Button(root,text="变第壹爻",font=("Arial",14),command=lambda:gua_find('1'))
atta_button.pack(pady=10)
atta_button.place(x=10,y=-ysize/100+ysize/20*6)
atta_button = tk.Button(root,text="变第贰爻",font=("Arial",14),command=lambda:gua_find('2'))
atta_button.pack(pady=10)
atta_button.place(x=10,y=-ysize/100+ysize/20*5)
atta_button = tk.Button(root,text="变第叁爻",font=("Arial",14),command=lambda:gua_find('3'))
atta_button.pack(pady=10)
atta_button.place(x=10,y=-ysize/100+ysize/20*4)
atta_button = tk.Button(root,text="变第肆爻",font=("Arial",14),command=lambda:gua_find('4'))
atta_button.pack(pady=10)
atta_button.place(x=10,y=-ysize/100+ysize/20*3)
atta_button = tk.Button(root,text="变第伍爻",font=("Arial",14),command=lambda:gua_find('5'))
atta_button.pack(pady=10)
atta_button.place(x=10,y=-ysize/100+ysize/20*2)
atta_button = tk.Button(root,text="变第陆爻",font=("Arial",14),command=lambda:gua_find('6'))
atta_button.pack(pady=10)
atta_button.place(x=10,y=-ysize/100+ysize/20*1)


# 运行主循环
root.mainloop()
