import os
import sys
sys.path.append('..')
import virustotal3.enterprise

#API_KEY = os.environ['0703c8673d85549f143f9bc0e845ba9d255bfc10a9c7140923d4a63651807a83']
results = virustotal3.enterprise.search("0703c8673d85549f143f9bc0e845ba9d255bfc10a9c7140923d4a63651807a83", 'evil.exe', order='size-',limit=10)
print(results)