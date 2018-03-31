import cloudsight
import GenerateVoice as GV

def analyse(image_name, API_KEY):
	auth=cloudsight.SimpleAuth(API_KEY)
	api = cloudsight.API(auth)	
	
	with open(image_name, 'rb') as f:
		response = api.image_request(f, image_name, {
			'image_request[locale]': 'en-US',
		})
	status = api.wait(response['token'], timeout=30)	
	status = api.image_response(response['token'])	
	if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
		caption = response['name']
		print(caption)
		GV.speak(caption)
	else:
		print('Cannot Process Image')

if __name__ == '__main__':
	analyse('try.jpg', 'LKUYuDVfT_MEJN7-gF266g')