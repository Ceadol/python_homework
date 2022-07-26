import re
def char_frequency(strs):
    mydict={}
    for i in strs:
        if i in mydict:
         mydict[i]+=1
        else:
            mydict[i]=1
    return mydict

#字符串为immutable，故需返回修改后的新字符串
def swap_chars(strs,i,j):
    strlist=list(strs)
    temp=strlist[i]
    strlist[i]=strlist[j]
    strlist[j]=temp
    return ''.join(strlist)

def min_str(strs):
    strlist=list(strs)
    strlist.sort()
    return ''.join(strlist)

calltime=0

def permutate(strs):
    n=len(strs)
    dict=char_frequency(strs)
    newdict={}
    for i in dict:
        newdict[i]=0;
    temp=[]
    newstrs=[]
    if n==1:
        return [strs]
    elif n>1:
        for i in range(n):
            if newdict[strs[i]]==0:
                strs=swap_chars(strs,0,i)
                temp.append(strs[0])
                rest=strs[1:n]
                oldstrs=permutate(rest)
                #print(oldstrs)
                for oldstr in oldstrs:
                    temp.append(oldstr)
                    newstr=''.join(temp)
                    temp.pop()
                    newstrs.append(newstr)
                temp.pop()
                strs=swap_chars(strs,i,0)
                newdict[strs[i]]+=1
    return newstrs

def clear_same(list):
    temp=[]
    for i in list:
        if i not in temp:
            temp.append(i)
    return temp
'''
#strs=str(input("请输入一个长度不小于10的字符串，以回车或空格结束：\n"))
#print(strs)
strs='aabcd'
while True:
  pat=r'\s+'
  news=re.split(pat,strs)
  #print(news)
  if len(news)>0:
   news=news[0]
   if len(news)<10:
     strs=str(input(news+"长度小于10，请重新输入:\n"))
     continue
   else:
     print(news)
     lists=permutate(news)
     for i in lists:
         print(i)
     print("共有"+str(len(lists))+"种不同的排列方式！")
     break
'''
s='aabcdeee'
ls=permutate(s)
for i in ls:
 print(i)
print(len(ls))