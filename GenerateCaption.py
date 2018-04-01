import cloudsight
import GenerateVoice as GV

def caption(image_name, API_KEY):
	auth=cloudsight.SimpleAuth(API_KEY)
	api = cloudsight.API(auth)	
	
	with open(image_name, 'rb') as f:
		response = api.image_request(f, image_name, {
			'image_request[locale]': 'en-US',
		})
	status = api.wait(response['token'], timeout=30)	
	status = api.image_response(response['token'])	
	if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
		try:
			caption = response['name']
			print(caption)
			GV.speak(caption)
		except:
			print('Cannot Process this Image')
	else:
		print('Cannot Process Image')

if __name__ == '__main__':
	caption('try.jpg', 'Cloud Sight API KEY')