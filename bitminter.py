import time
import requests
import logging

REFRESH_TIME_SECONDS=60


### LOGGING CONF################################
logging.basicConfig(filename='bitminter.log')
logger = logging.getLogger('bitminter.py')
logger.setLevel('DEBUG')
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
#################################################

def go():
	while True:
		h = {
		'Authorization': 'key=0FBQIY3BXF4UYMPHPXR0D1PZFZRRCPHL'
		}
		r = requests.get('https://bitminter.com/api/users', headers=h)
		data = 'ResponseCode="%s" Result=%s' % (r.status_code, r.text)
		logger.info(data)
		time.sleep(REFRESH_TIME_SECONDS)



if __name__=="__main__":
	print 'Running Bitminter Logger...'
	go()


