import cloudsight as CS
import GenerateVoice as GV
import time
import detector as DT
def Caption(image_name, passs):
	auth = CS.SimpleAuth(passs)
	conn = CS.API(auth)	
	Filter_chocolate = ['chocolate', 'pizza']
	filter_phone=['smartphone', 'phone', 'mobile', 'Smartphone', 'Phone' ,'Mobile']
	filter_cigarette=['cigarette', 'cigarettes', 'smoking', 'smoke']
	with open(image_name, 'rb') as f:
		response = conn.image_request(f, image_name, {
			'image_request[locale]': 'en-US',
		})
	status = conn.wait(response['token'], timeout=30)
	status = conn.image_response(response['token'])
	if status['status'] != CS.STATUS_NOT_COMPLETED:
		try:
			caption = status['name']
			for content in Filter_chocolate:
				if content in caption:
					message = "Warning: Eating %s is injurious to Health...Image Content" %content 
					#GV.speak('Warning: Eating Cholocate is injurious to Health.... Image Content\n')
					message = message+caption
					caption=message
					break
			for content in filter_cigarette:
				if content in caption:
					message = "Warning: Smoking %s is injurious to Health...Image Content. " %content 
					#GV.speak('Warning: Smoking %s is injurious to Health.... Image Content. \n' %content)
					message = message+caption
					caption=message
					break		
			for content in filter_phone:
				if content in caption:
					caption = "Alert: %s Detected.. Filtered Content.." %content

			person = DT.Recognise_Face(image_name)
			if person != 0:
				message = 'You are looking at %s. ' %person
				message = message + caption
				caption = message
			GV.speak(caption)
			return(caption)
		except:
			print('Cannot Process this image')
	else:
		print('Cannot Process Image')

if __name__ == '__main__':
	Caption('try.jpg', '')