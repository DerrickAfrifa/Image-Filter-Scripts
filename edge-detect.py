from PIL import Image

img = Image.open("mini.jpg")
pixels = img.load()

img1 = Image.new(img.mode, img.size)
pixels_new = img1.load()

threshold = 15

for i in range(img1.size[0]-1):
    for j in range(1,img1.size[1]):

        pixel_luminance = 0
        neighbour_luminance = 0

        pixel_luminance = (pixels[i,j][0] + pixels[i,j][1] + pixels[i,j][2])//3
        neighbour_luminance = pixels[i,j-1][0] + pixels[i,j-1][1] + pixels[i,j-1][2]
        neighbour_luminance += pixels[i+1,j][0] + pixels[i+1,j][1] + pixels[i+1,j][2]
        neighbour_luminance = neighbour_luminance // 6

        if(abs(pixel_luminance-neighbour_luminance) < threshold):
            pixels_new[i,j] = 0
        else:
            pixels_new[i,j] = (255,255,255)

img.close()
#img.show()
img1.save("new_pic3.tif")
img1.close()
