from PIL import Image

im = Image.open("C:/Users/Dylan/Desktop/Scripts/Python/steganographie/out.png", 'r')
msg_decode = []
msg_decode_word = []
result = ''

pixVals = list(im.getdata()) #get all pixels from the image

width = im.size[0] #width of the picture
height = im.size[1] #height of the picture


for i in range (0,width*height):
    current_pixVals = pixVals[i]

    get_last_number = current_pixVals[2] #get the last number of the pixel value (R,G,B)
    bin_last_number = bin(get_last_number)[:1] + bin(get_last_number)[2:] #remove b from the binary output

    result = result + bin_last_number[1] #place the last bit of the Blue pixel into the result variable
    if len(result) % 4 == 0: # all the 4 number are placed in a list
        msg_decode.append(result)
        result = "" # and we reset the result variable



print(msg_decode)



msg_decode_word.append(msg_decode[2] + msg_decode[3])

an_integer = int(msg_decode[0] + msg_decode[1], 2)
ascii_character = chr(an_integer) #deocde binary to character

print(pixVals[15])