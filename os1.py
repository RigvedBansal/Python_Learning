import os,shutil
f =  open('practice.txt','w+')
f.write('This is a test string')
f.close()
print(os.getcwd())
print(os.listdir('F:\Programming\Python'))
shutil.move('F:\Programming\Python\Pythonprojects\practice.txt','F:\Programming\Python')
print(os.listdir('F:\Programming\Python'))
os.unlink('F:\Programming\Python\practice.txt')
for folder,sub_folder,files in os.walk('F:\Programming'):
    print(f"Currently looking at {folder}")
    print('\n')
    print('The subfolders are: ')
    for sub_fold in sub_folder:
        print(f"Subfolder : {sub_fold}")
    print('\n')
    print("The files are: ")
    for f in files:
        print(f"File: {f}")
    print("\n") 