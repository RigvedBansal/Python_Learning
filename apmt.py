import os
import re
import shutil
import zipfile
#dir_for_extract_result = r'F:\Programming\Python\zipto'
#output_filename = r'C:\Users\HP\Downloads\unzipme.zip'
# shutil.unpack_archive(output_filename,dir_for_extract_result,'zip')

pattern = r'\d{3}-\d{3}-\d{4}'
def search(file, pattern = r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return None


results = []
for folder, sub_folder, files in os.walk('F:\Programming\Python\zipto'):

    for f in files:
        full_path = folder + '\\'+f
        results.append(search(full_path))
for r in results:
    if r != None:
        print(r.group())