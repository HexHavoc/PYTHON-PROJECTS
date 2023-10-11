from PIL import Image, ImageFont, ImageDraw
import pandas as pd


def main():
    print("Initializing Script!")
    names = pd.read_csv('participants.csv') 
    for i,row in names.iterrows():
        print(i)
        name = str(row['NAME'])
        name = name.title()
        certificate = Image.open("certificate.jpg")
        font_size = 110
        font = ImageFont.truetype("Roboto-Bold.ttf")
        font = ImageFont.truetype("Roboto-Bold.ttf",font_size)
        image_editable = ImageDraw.Draw(certificate)
        image_editable.multiline_text((390,470), name, (35, 57, 75), font=font)
        certificate.save("{}.jpg".format(name.replace(" ", "_")))
    print("Process Complete!")

if __name__ == "__main__":
    main()