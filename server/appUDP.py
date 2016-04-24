#conding:utf-8
import os
import io
import time,datetime
import socket

reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()
UPLOAD_FOLDER = abspath+'/static/uploads'

def saveImg(byteArray):
	image = Image.open(io.BytesIO(byteArray))
	time_ = str(datetime.datetime.now()).replace(' ', '_')
	time_ = time_.replace(':','_')
	new_img_name = time_ + str(random.randint(10000, 1000000)) + '.jpg'
	image.save(UPLOAD_FOLDER+'/'+new_img_name)
	return '/static/uploads/'+new_img_name