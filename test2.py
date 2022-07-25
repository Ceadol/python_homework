import random
import re
file=open("hangman词表.txt",'r')
strs=file.readlines()
s=random.choice(strs)
pat='[a-zA-Z]+'
s=re.findall(pat,s)
s=s[0]
file.close()
lenth=len(s)
print("提示：这个单词有"+str(lenth)+"个字母")
print("第1个字母是"+s[0],"最后一个字母是"+s[lenth-1])
print("开始猜测，你将随机猜测"+str(lenth-2)+"个单词中的未知字母，且可能重复。")
for i in range(1,lenth-1):
    ran=random.randint(2,lenth-1)
    while True:
     c=str(input("请猜出第"+str(ran)+"个字母\n"))
     if c==s[ran-1]:
        print("答对了！")
        break
     elif c>s[ran-1]:
         print("正确字母在这个字母之前！")
     elif c<s[ran-1]:
         print("正确字母在这个字母之后！")
     else: continue
    a=int(input("是否继续猜测字母？1.继续 2.结束\n"))
    if a==1:
        continue
    else:
        break
ch=str(input("这个单词是？\n"))
if(ch==s):
    print("正确!")
else:
    print("错误!正确答案是："+s+"!")
