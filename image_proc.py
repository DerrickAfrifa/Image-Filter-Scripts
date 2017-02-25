from PIL import Image

DIVISION_CONSTANT = 9
img = Image.open("mini.jpg")
pixels = img.load()

kernel = [[1,1,1],
          [1,1,1],
          [1,1,1]]

radius = 1

img1 = Image.new( img.mode, img.size)
pixels_new = img1.load()
for i in range(radius,img1.size[0]-radius):
    for j in range(radius,img1.size[1]-radius):

        accumulator_red = 0
        accumulator_green = 0
        accumulator_blue = 0

        off_row = -1
        off_col = -1
        for row in range(len(kernel)):
            for col in range(len(kernel[0])):
                 red = pixels[i+off_row, j+off_col][0]*kernel[row][col]
                 accumulator_red += red
                 green = pixels[i+off_row, j+off_col][1]*kernel[row][col]
                 accumulator_green += green
                 blue = pixels[i+off_row, j+off_col][2]*kernel[row][col]
                 accumulator_blue += blue
                 off_col += 1
            off_col = -1
            off_row += 1

        new_value = (accumulator_red//DIVISION_CONSTANT, accumulator_green//DIVISION_CONSTANT, accumulator_blue//DIVISION_CONSTANT)
        pixels_new[i, j] = new_value
        #print(str(pixels[i,j]))
        #print(str(new_value))

img.close()
#img.show()
img1.save("new_pic2.tif")
img1.close()
