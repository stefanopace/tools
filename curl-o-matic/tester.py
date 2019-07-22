import os
import glob
from subprocess import check_output


def check_same():
    curl_path = 'test-data/requests/'
    responses_path = 'test-data/responses/'
    for curl_filename in glob.glob(os.path.join(curl_path, '*.curl')):
        curl_output = check_output(['bash', './' + curl_filename]).decode('utf-8')
        response_name = curl_filename.split('/')[-1].replace('.curl', '.response')
        response_filename = responses_path + response_name
        print('Checking: ' + response_name)
        with open(response_filename, 'r') as response_file:
            oracle = response_file.read()
            try:
                assert(oracle == curl_output)
            except AssertionError:
                print('FAIL! Response changed for ' + curl_filename)
