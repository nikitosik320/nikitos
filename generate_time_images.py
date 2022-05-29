import time
from PIL import ImageDraw, Image, ImageFont
from datetime import datetime, timedelta

FONT_SIZE = 60
TEXT_Y_POSITION = 25
TEXT_X_POSITION = 5
Tashkent_UTC = 5 #укажите ваш часовой пояс 

def convert_time_to_string(dt):
    
    dt += timedelta(hours=Tashkent_UTC)
    
    return f"{dt.hour}:{dt.minute:02}"
    
    
    

def change_img():
    start_time = datetime.utcnow()
    text = convert_time_to_string(start_time)
    row = Image.new('RGBA', (200, 200), "gray")# Цвет фона black,white тд
    parsed = ImageDraw.Draw(row)
    font = ImageFont.truetype("HEADPLANE.ttf", FONT_SIZE)#стиль шрифта
    font2 = ImageFont.truetype("HEADPLANE.ttf", 18)
    font3 = ImageFont.truetype("HEADPLANE.ttf", 40)
    
    parsed.text((int(row.size[1]*0.15), int(row.size[1]*0.31)), f'{text}', 
                 align="center", font=font, fill=(3,33,212))
    
    parsed.text((30, 110),'TASHKENT TIME', # подтекст
                 align="center", font=font2, fill=(196,4,4))
    
    parsed.text((35, 140),'N!k!t0$', # подтекст
                 align="center", font=font3, fill=(43,247,2))
    
    row.save(f'time.png', "PNG")

if __name__ == '__main__':
    change_img()
