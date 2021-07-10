import os
import json
from urllib.request import urlopen
from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

# Set current directory

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load graphic

img = Image.open("./logo.png")
draw = ImageDraw.Draw(img)

# get api data

try:
  f = urlopen('http://192.168.1.122/admin/api.php')
  json_string = f.read()
  parsed_json = json.loads(json_string)
  adsblocked = parsed_json['ads_blocked_today']
  ratioblocked = parsed_json['ads_percentage_today']
  f.close()
except:
  queries = '?'
  adsblocked = '?'
  ratioblocked = 0

font = ImageFont.truetype(FredokaOne, 32)

inky_display = auto()
inky_display.set_border(inky_display.WHITE)

draw.text((20,20), str(adsblocked), inky_display.BLACK, font)
draw.text((20,50), str("%.1f" % round(ratioblocked,2)) + "%", inky_display.BLACK, font)

inky_display.set_image(img)

inky_display.show()
