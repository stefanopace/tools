import os
import glob
from subprocess import check_output


def store_responses():
    curl_path = 'test-data/requests/'
    responses_path = 'test-data/responses/'
    for curl_filename in glob.glob(os.path.join(curl_path, '*.curl')):
        curl_output = check_output(['bash', './' + curl_filename]).decode('utf-8')
        response_name = curl_filename.split('/')[-1].replace('.curl', '.response')
        response_filename = responses_path + response_name
        print('Saving: ' + response_name)
        with open(response_filename, 'w') as response_file:
            response_file.writelines(curl_output)
