with open('reader.txt', 'w') as file:
    file.writelines('Hello world')

print('Reading was succesfully')


my_file=open('reader.txt','w')
my_f=my_file.writelines('Hello world second')
my_file.close()

print('First file was erased and created new one')

