# import modules
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import glob


# convert month numbers to names
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


# open images folder
images = []
dates = []

print("Loading files...")

for f in glob.glob("./inputdir/*"):
    images.append((Image.open(f)))
    dates.append(f[21:23]+" "+months[int(f[19:21])-1])

print("Done")
print("Starting image processing...")

for i in range (len(images)):
    image = images[i]
    print("Processing:" + str(image.fp.name))

    # creating a copy of original image
    watermark_image = image.copy()
    
    # Image is converted into editable form using
    # Draw function and assigned to draw
    draw = ImageDraw.Draw(watermark_image)
    
    # ("font type",font size)
    font = ImageFont.truetype("Lato-Regular.ttf", 150)
    
    # calculate the position for the text
    coordX = image.size[0] - 640
    coordY = image.size[1] - 250

    # Decide the text location, color and font
    # (255,255,255)-White color text
    draw.text((coordX, coordY), dates[i], (255, 255, 255), font=font)
    
    watermark_image.save("./outputdir/img"+str(i)+"_"+dates[i].replace(" ","")+".jpg")
    print("Processing done. Saved as "+"./outputdir/img"+str(i)+"_"+dates[i].replace(" ","")+".jpg")

print("All tasks done.")