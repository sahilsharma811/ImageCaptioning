import cloudsight as CV
import GenerateVoice as GV
import time
def Caption(image_name, passs):
	auth=CV.SimpleAuth(passs)
	conn = CV.API(auth)	
	Filter_chocolate = ['chocolate', 'pizza']
	filter_phone=['smartphone', 'phone', 'mobile', 'Smartphone', 'Phone' ,'Mobile']
	with open(image_name, 'rb') as f:
		response = conn.image_request(f, image_name, {
			'image_request[locale]': 'en-US',
		})
	status = conn.wait(response['token'], timeout=30)
	status = conn.image_response(response['token'])
	if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
		try:
			caption = status['name']
			for content in Filter_chocolate:
				if content in caption:
					print("Warning: Eating %s is injurious to Health.." %content) 
					GV.speak('Warning: Eating Cholocate is injurious to Health.... Image Content')
					break
			for content in filter_phone:
				if content in caption:
					caption = "Alert: %s Detected.. Filtered Content.." %content
					
			GV.speak(caption)
			return(caption)
		except:
			print('Cannot Process this image')
	else:
		print('Cannot Process Image')

if __name__ == '__main__':
Caption('try.jpg','')