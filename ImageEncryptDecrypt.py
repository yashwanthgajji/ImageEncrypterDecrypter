class Encrypt:
	def __init__(self,image_path,key,destination_folder):
		self.image_path=image_path
		self.key=key
		self.destination_folder=destination_folder
	def get_name(self):
		location=self.image_path.split("/")
		only_name=location[len(location)-1].split(".")
		enc_name=self.destination_folder+"/"+only_name[0]+"_enc"
		return enc_name
	def convert(self):
		fo=open(self.image_path,"rb")
		image=fo.read()
		fo.close()
		image=bytearray(image)
		for index,value in enumerate(image):
			image[index]=value^self.key
		fo=open(self.get_name()+".jpg","wb")
		fo.write(image)
		fo.close()

class Decrypt:
	def __init__(self,image_path,key,destination_folder):
		self.image_path=image_path
		self.key=key
		self.destination_folder=destination_folder
	def get_name(self):
		location=self.image_path.split("/")
		only_name=location[len(location)-1].split(".")
		dec_name=self.destination_folder+"/"+only_name[0]+"_dec"
		return dec_name
	def convert(self):
		fo=open(self.image_path,"rb")
		image=fo.read()
		fo.close()
		image=bytearray(image)
		for index,value in enumerate(image):
			image[index]=value^self.key
		fo=open(self.get_name()+".jpg","wb")
		fo.write(image)
		fo.close()