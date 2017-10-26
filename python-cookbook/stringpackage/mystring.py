# string对象的split()只适应非常简单的字符串分割
import re
import os


line = "111,222, 333;444,555, 666"
print(line.split(","))

print(re.split(r'[;,\s]\s*', line))



if line.startswith("11"):
    print(line)

if line.endswith("66"):
    print(line)

filenames = os.listdir('.')
print(filenames)

for name in filenames:
    if name.endswith('.py'):
        print(name)

# find
print(line.find('333'))

print(re.findall('3', line))

line = line.replace("111", "7777")
print(line)
