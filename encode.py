from PIL import Image 

im = Image.open(r"C:/Users/Dylan/Desktop/Scripts/Python/steganographie/black-img.png")  

pixVals = list(im.getdata()) #get all pixels from the image

width = im.size[0] #width of the picture
height = im.size[1] #height of the picture

x = 0#counter for pixel in the image's width
i = 0 #counter for pixel in the image's width
n = 0 #counter for number of pixel in the image


word = "0110100001101001" #hi HEX h = 68/ i = 69


while(x < len(word)-1):
    
    current_pixVals = pixVals[n]


    get_last_number = current_pixVals[2]
    bin_last_number = bin(get_last_number)[:1] + bin(get_last_number)[2:] #remove b from the binary output


    bin_last_number_modify = bin_last_number[:3] + word[n] #change the last bit to the first number of the secret word


    last_number_modify = int(bin_last_number_modify , 2)

    m_list = list(current_pixVals)
    m_list.pop(2)
    m_list.append(last_number_modify)
    m_list = tuple(m_list)

    im.putpixel((x, i), m_list)

    x = x + 1
    n = n + 1
    
    if x == width:
	    x = 0
	    i = i + 1

im.save("out.png")

im2 = Image.open(r"C:/Users/Dylan/Desktop/Scripts/Python/steganographie/out.png") 
pixVals2 = list(im2.getdata())

print(pixVals2[15])