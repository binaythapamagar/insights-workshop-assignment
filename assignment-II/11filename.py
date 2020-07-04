filename = 'ReadMe.txt'

print(f'File name is {filename}')
print(f'extension of the file is "{filename[-3:]}"')

findDot = filename.find('.')

print(f'File name is "{filename[0:findDot]}"')