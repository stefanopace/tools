import os
import glob
from subprocess import check_output
import difflib
import re

def check_same():
    curl_path = 'test-data/requests/'
    responses_path = 'test-data/responses/'
    for curl_filename in glob.glob(os.path.join(curl_path, '*.curl')):
        curl_output = check_output(['bash', './' + curl_filename]).decode('utf-8')
        response_name = curl_filename.split('/')[-1].replace('.curl', '.response')
        response_filename = responses_path + response_name
        print('Checking: ' + response_name)
        with open ('./' + curl_filename, 'r') as curl_file:
            print(curl_file.readline())
        with open(response_filename, 'r') as response_file:
            oracle = response_file.read()
            try:
                oracle = oracle.replace('\r', '')
                curl_output = curl_output.replace('\r', '')
                oracle = re.sub(r'(?m)^\s+', '', oracle)
                oracle = re.sub(r'(?m)\s+$', '', oracle)
                curl_output = re.sub(r'(?m)^\s+', '', curl_output)
                curl_output = re.sub(r'(?m)\s+$', '', curl_output)

                assert(oracle == curl_output)
            except AssertionError:
                d = difflib.HtmlDiff()
                diff = d.make_table(oracle.split('\n'), curl_output.split('\n'), context=True)
                # # with open('./test1.txt', 'w') as test1:
                # #     test1.write(oracle)
                # # with open('./test2.txt', 'w') as test1:
                # #     test1.write(curl_output)
                with open('./diff.html', 'w') as diff_file:
                    diff_file.write(diff)
                print('FAIL! Response changed for ' + curl_filename)
                exit(0)
