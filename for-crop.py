from PIL import Image, ImageFilter
im1 = Image.open('Main.png')
for i in range(3):
    for j in range(9):
        left= j*110
        right = left + 110
        top = i *120
        bottom = top + 120
        cropped = im1.crop((left+5, top+20, right-5, bottom-20))
        text = 'data/'+str(i)+str(j)+'.png'
        cropped.save(text)
