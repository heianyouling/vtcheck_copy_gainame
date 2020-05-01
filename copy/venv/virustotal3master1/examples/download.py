import os
import sys
sys.path.append('..')
import virustotal3.core
#virustotal3.path.append("..")

#API_KEY = os.environ['VT_API']
vt = virustotal3.core.Files('0703c8673d85549f143f9bc0e845ba9d255bfc10a9c7140923d4a63651807a83')
vt.download('8e362026eee42eb73184f88a7b76806c406d99cd', '~/samples')