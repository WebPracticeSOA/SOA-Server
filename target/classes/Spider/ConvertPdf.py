from pdf2image import convert_from_path
from aip import AipOcr
import os

proPath="./Files\\"
resPath="./Files\\csv\\"
path1="行政法规"
path2="部门规章"
path3="规范性文件"
path4="其他文件"

APP_ID = '25044054'
API_KEY = 'nmzFHP6vrjpWHA6g43tNZEH4'
SECRET_KEY = 'oabxXfM1MqwboMp03ZQV6vsFibNpixvD'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
global count
count=0

def baidu_ocr(filePath,fname):
	global count
	if(os.path.exists(filePath+"\\"+fname[0:-4]+".txt")):
		return False
	f = open(filePath+"\\"+fname[0:-4]+".txt", 'w', encoding='utf-8')
	dirname = "./Images\\"+fname.rsplit('.', 1)[0]
	if not os.path.exists(dirname):
		os.mkdir(dirname)
	images = convert_from_path(filePath+"\\"+fname, fmt='png', output_folder=dirname)

	for img in images:
		with open(img.filename, 'rb') as fimg:
			img = fimg.read() # 根据'PIL.PngImagePlugin.PngImageFile'对象的filename属性读取图片为二进制
			msg = client.basicGeneral(img)
			try:
				for i in msg.get('words_result'):
					f.write('{}\n'.format(i.get('words')))
				f.write('\f\n')
			except TypeError:
				f.write(fname)
				print("'NoneType' object is not iterable")
	f.close()
	count+=1
	print(count)
	# os.remove(dirname)



def convertToTxt(proPath,pathtype):
	filePath=proPath+pathtype
	pathDir = os.listdir(filePath)
	for allDir in pathDir:
		if(allDir!="附件" and allDir.endswith(".pdf")):
			baidu_ocr(filePath,allDir)


if(not os.path.exists("Images")):
	os.mkdir("Images")
convertToTxt(proPath,path2)
convertToTxt(proPath,path3)