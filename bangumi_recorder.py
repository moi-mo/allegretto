# 番剧进度记录 by moimo233
# 锟斤拷问题暂时无解

#规定每个番剧class对应4个变量：
class Bangumi :
    def __init__(self,name,episode,time) :
        self.name = name
        self.episode = episode
        self.time = time
#########################################

# load
# 格式为name episode time，中间用空格分开，不同的项目之间是\n
def load():
    f = open('bangumi_recorder/data.data','r')
    s = f.read()
    f.close()

    bangumi_list = s.split(sep = '\n')
    bangumi_detail_list = []
    for i in bangumi_list :
        i = i.split()
        if i != []:   # 列表要不为空才可以使用l[0]
            na = i[0]
            ep = i[1]
            ti = i[2]
            bangumi_detail_list.append(Bangumi(na,ep,ti))
    return bangumi_detail_list
###########################################

# new
# open(xxx,'a')，即在data文件后追加
def new(bangumi):
    l = load()
    is_in = False
    for i in l:
        if i.name == bangumi.name:
            is_in = True
    if is_in:
        print('错误！这部番已经在列表里了哦？')
    else:
        f = open('bangumi_recorder/data.data','a')
        f.write(bangumi.name+' '+bangumi.episode+' '+bangumi.time+'\n')
        f.close()
        print('番剧',bangumi.name,'新建成功！')
###########################################

# mark
# 本质上是覆盖
def mark(name,change_type,new_val):
    l = load()
    is_in = False
    for i in l:
        if i.name == name:
            is_in = True
            bangumi_index = l.index(i)
    if not is_in:
        print('错误！本番剧还未新建！\n打错了吗？')
    else:
        # change_type和new_val都是str
        exec('l[bangumi_index].'+change_type+'=new_val')
        s = ''
        for i in l:
            s += i.name+' '+i.episode+' '+i.time+'\n'
        f = open('bangumi_recorder/data.data','w')
        f.write(s)
        f.close()

# check_all
def check_all():
    l = load()
    print('name\tepisode\ttime')
    for i in l:
        print(i.name,'\t',i.episode,'\t',i.time,'\n')
###############################################

# check
def check(name):
    l = load()
    is_in = False
    for i in l:
        if name == i.name:
            print(i.name,'\t',i.episode,'\t',i.time)
            is_in = True
    if not is_in:
        print('该番剧还不在列表中，打对了吗？')
        

# help
# 写完main了写
##################################################

# version
def version():
    print('version 12!Bangumi Recorder by moimo233')


# 希望有如下功能：
# 1 新建番剧    new
# 2 改变番剧中的变量    mark
# 3 查看已有内容    check_all
#############以下是程序运行的main：

print('Hi~喜欢今天看的番剧吗？\n开始记录吧w，如有疑问请查阅README.md或者输入help')

def get_order():
    global l,order
    s = input('>>> ')
    l = s.split()
    order = l[0]

get_order()

while order != 'exit':
    if order == 'new':
        if len(l) == 2:     #new [name]
            b = Bangumi(l[1],'null','null')
            new(b)
        elif len(l) == 4:   #new [name] [episode] [time]
            b = Bangumi(l[1],l[2],l[3])
            new(b)
        else:
            print('命令格式错误！\nnew [name]，或者\nnew [name] [episode] [time]')
        get_order()

    elif order == 'mark':
        if len(l) == 4:     #mark [name] [change_type] [new_val]
            mark(l[1],l[2],l[3])
            print('记录成功！')
        else:
            print('命令格式错误！\nmark [name] [change_type] [new_val]')
        get_order()

    elif (order == 'br') or (order == 'BangumiRecorder'):
        if len(l) == 4:
            mark(l[1],'episode',l[2])
            mark(l[1],'time',l[3])
            print('记录成功！')
        else:
            print('命令格式错误！\nbr [name] [episode] [time] (BangumiRecorder=br)')
        get_order()

    elif order == 'check':
        if len(l) == 2 and l[1] == 'all':     #check all
            check_all()
        elif len(l) == 2:
            check(l[1])
        else:
            print('命令格式错误！\ncheck all\n或check [name]')
        get_order()
    
    elif order == 'version':
        version()
        get_order()



