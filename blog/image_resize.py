import PIL
from PIL import Image 
#from blog.models import Blog


"""
http://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio

def resizer(basewidth, img):

	basewidth = 300
	img = Image.open(Blog.image)
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent))
	img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
	img.save(Blog.image)

	return img 

"""


def resizer(path):
	img = Image.open(path)
	img = img.resize((700,450), PIL.Image.ANTIALIAS)
	img.save(path)

