import random
import func.global_variable as glov
def rand_gua():
    # 随机选择一个选项
    result = random.choice(glov.options)
    #获取标签
    mack = glov.options.index(result)
    #查找对应解释
    mean = glov.means[mack]
    # 更新结果标签
    #mean_label.config(text=f"\n{mean}",font=("Arial",20))
    glov.gua = result.split("\n")
    return result,mean

def c_gua():
    visgua = glov.gua[1]
    owngua = glov.gua[2]
    visgua = glov.basgua[visgua]
    owngua = glov.basgua[owngua]
    tolgua = [visgua,owngua]
    return tolgua

def tra_gua(tol,number):
    lis=[]
    tolgua1 = tol[0]
    tolgua2 = tol[1]
    tolgua1[0] = next((k for k ,v in glov.basgua.items() if v == tolgua1[0]),None)
    tolgua1[1] = next((k for k ,v in glov.basgua.items() if v == tolgua1[1]),None)
    keyword1 = "\n"+str(tolgua1[0])+'\n'+str(tolgua1[1])+"\n"
    tolgua2[0] = next((k for k ,v in glov.basgua.items() if v == tolgua2[0]),None)
    tolgua2[1] = next((k for k ,v in glov.basgua.items() if v == tolgua2[1]),None)
    keyword2 = "\n"+str(tolgua2[0])+'\n'+str(tolgua2[1])+"\n"
    lis=[s for s in glov.options if keyword1 in s]
    if lis !=[]:
        result=lis[0]
        #获取标签
        mack = glov.options.index(result)
        #查找对应解释
        mean = glov.means[mack]
    elif len(lis) <=1:
        lis=[]
        lis=[s for s in glov.options if keyword2 in s]
        result=lis[0]
        #获取标签
        mack = glov.options.index(result)
        #查找对应解释
        mean = glov.means[mack]
    else:
        number=-1
        result="无"
        mean="空"
    return result,mean

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
    result = tra_gua([tolgua1,tolgua2],number)
    return result