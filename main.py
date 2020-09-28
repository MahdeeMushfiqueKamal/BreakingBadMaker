from PIL import Image, ImageFilter
list = ['al','ar','as','at','b','ba','be','br','c','cl','co','cr','cu','db','dy','eu','f','fe','ga','ge','h','he','i','k','kr','li','mg','mo','n','na','nb','ne','ni','o','p','pd','rb','s','se','si','sr','ti','u','v','w','xe','y','zn','zr']
bg = Image.open('data/src/bbbg.jpg')
first = input('Enter First name: ')
last =  input('Enter Last  name: ')
firstname= []
lastname= []

for chm in list:
    c1=first.find(chm)
    if(c1 != -1):
        c2=c1+len(chm)
        str1 = first[0:c1]
        str2 = first[c2:]
        print(str1+ " " + chm + " "+str2)
        firstname.append((str1,chm,str2))
for chm in list:
    c1=last.find(chm)
    if(c1 != -1):
        c2=c1+len(chm)
        str1 = last[0:c1]
        str2 = last[c2:]
        print(str1+ " " + chm + " "+str2)
        lastname.append((str1,chm,str2))

def findlen(text):
    ans= 0
    for i in text:
        temp = Image.open('data/letter/'+ i +'.png')
        ans= ans + temp.size[0]
    return ans
# (str1, chm, str2) (fn[0],fn[1],fn[2])
count = 0
for fn in firstname:
    #print('Working with', fn)
    for ln in lastname:
        im1=bg.copy()
        y = int(190)
        x = int(405 - findlen(fn[0]))
        for i in range(len(fn[0])):
            im2=Image.open('data/letter/'+fn[0][i]+'.png')
            im1.paste(im2,(x,y),im2)
            x=x+im2.size[0]
        im2=Image.open('data/chm/'+fn[1]+'.png')
        im1.paste(im2,(x,y),im2)
        x=x+100
        for i in range(len(fn[2])):
            im2=Image.open('data/letter/'+fn[2][i]+'.png')
            im1.paste(im2,(x,y),im2)
            x=x+im2.size[0]

        y = int(270)
        x = int(480 - findlen(ln[0]))
        for i in range(len(ln[0])):
            im2=Image.open('data/letter/'+ln[0][i]+'.png')
            im1.paste(im2,(x,y),im2)
            x=x+im2.size[0]
        im2=Image.open('data/chm/'+ln[1]+'.png')
        im1.paste(im2,(x,y),im2)
        x=x+100
        for i in range(len(ln[2])):
            im2=Image.open('data/letter/'+ln[2][i]+'.png')
            im1.paste(im2,(x,y),im2)
            x=x+im2.size[0]
        filename = str(count)+ '.png'
        im1.save(filename)
        count=count+1




print ('huh!')
