# -*- coding: UTF-8 -*- 

open('bangumi.data','a').close()

def load():
    f = open('bangumi.data','r')
    s = f.read()
    f.close()
    
    b_list = []
    l = s.split(sep = '\n')
    if l != [''] :
        for i in l:
            i = i.split()
            if i != []:
                b = Bangumi(i[0],i[1],i[2])
                b_list.append(b)

    return b_list



class Bangumi:
    def __init__(self,name,episode,time) :
        self.name = name
        self.episode = episode
        self.time = time
        self.datastr = self.name + ' ' + self.episode + ' ' + self.time + '\n'
        self.showstr = self.name + '\t' + self.episode + '\t' + self.time

    def new(self):
        l = load()
        is_in = False
        for i in l:
            if i.name == self.name:
                print(self.name,'已经在列表里了哦？')
                is_in = True
        
        if not is_in:
            f = open('bangumi.data','a')
            f.write(self.datastr)
            f.close()
            print('番剧',self.name,'创造成功！')


def mark(name,change_type,n_val):
    l = load()
    is_in = False
    for i in l:
        if i.name == name:
            b_index = l.index(i)
            is_in = True
        
    if is_in:
        exec('l[b_index].' + change_type + ' = \'' + n_val + '\'')
        l[b_index] = Bangumi(l[b_index].name,l[b_index].episode,l[b_index].time)
        s = ''
        for i in l:
            s += i.datastr
        f = open('bangumi.data','w')
        f.write(s)
        f.close()
        print('标记成功！')
    else:
        print('列表中还没有',name,'这部番剧！')
        
def check(name):
    l = load()
    is_in = False
    for i in l:
        if i.name == name:
            is_in = True
            b_index = l.index(i)
    if is_in:
        print(name,'的信息为：')
        print(l[b_index].showstr)
    else:
        print('番剧',name,'不在列表中！')

def allegretto(bangumi):
    l = load()
    is_in = False
    for i in l:
        if i.name == bangumi.name:
            l[l.index(i)] = bangumi
            is_in = True
    if is_in:
        s = ''
        for i in l:
            s += i.datastr
        f = open('bangumi.data','w')
        f.write(s)
        print('记录成功')
    else:
        bangumi.new()
    
def delete(name):
    l = load()
    is_in = False
    for i in l:
        if i.name == name:
            b_index = l.index(i)
            is_in = True
    if is_in:
        really = input('真的吗？删除 '+name+' 输入Y/N\n>>>(Y/N?) ')
        if really == 'Y': really = True
        elif really == 'N': really = False
        else: really = False;print('Y、N，大写的哦？重新输入命令吧')
        if really:
            l.pop(b_index)
            s = ''
            for i in l:
                s += i.datastr
            f = open('bangumi.data','w')
            f.write(s)
            f.close()
            print('删除成功orz')
    else:
        print('番剧',name,'还不在列表中哦')


def version():
    print('allegretto! A bangumi recorder by moimo233.\nversion 14!')

def help():
    print('输入exit并回车退出，剩余请查看项目目录下README.md！')


def get_order():
    global s,order
    s = input('>>> ').split()
    order = s[0]

order = 'wtf why there isn\'t do-while in python'

print('allegretto！番剧进度记录系统！')
while order != 'exit':
    get_order()
    if order == 'new':
        if len(s) == 2:
            Bangumi(s[1],'unknown','unknown').new()
        elif len(s) == 4:
            Bangumi(s[1],s[2],s[3]).new()
        else:
            print('命令输入有误！\nnew [name]   OR \nnew [name] [episode] [time]')

    elif order == 'mark':
        l = load()
        if len(s) == 4:
            b_index = 0
            mark(s[1],s[2],s[3])
        else:
            print('命令输入有误！\nmark [name] [change_type] [new_val]')

    elif order == 'check':
        l = load()
        if len(s) == 2:
            check(s[1])
        else:
            print('命令输入有误！\ncheck [name] OR\ncheck-all')

    elif order == 'check-all':
        if len(s) == 1:
            l = load()
            for i in l:
                print(i.showstr)
        else:
            print('命令输入有误！只需要输入check-all')
    
    elif order == 'allegretto' or order == 'al':
        if len(s) == 4:
            allegretto(Bangumi(s[1],s[2],s[3]))
        else:
            print('命令输入有误！\nallegretto [name] [episode] [time]   OR\nal [name] [episode] [time]')

    elif order == 'delete':
        if len(s) == 2:
            delete(s[1])
        else:
            print('命令输入有误！\ndelete [name]')



    elif order == 'version':
        version()
    
    elif order == 'help':
        help()

    elif order == 'exit':
        break

    else:
        print('诶？打错啦？没有',order,'这个命令哦')
print('Bye')
input()