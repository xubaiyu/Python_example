# -*- coding: UTF-8 -*-
 
a = 21
b = 10
c = 0
 
c = a + b
print "1 - c ��ֵΪ��", c
 
c = a - b
print "2 - c ��ֵΪ��", c 
 
c = a * b
print "3 - c ��ֵΪ��", c 
 
c = a / b
print "4 - c ��ֵΪ��", c 
 
c = a % b
print "5 - c ��ֵΪ��", c
 
# �޸ı��� a ��b ��c
a = 2
b = 3
c = a**b 
print "6 - c ��ֵΪ��", c
 
a = 10
b = 5
c = a//b 
print "7 - c ��ֵΪ��", c


a = 21
b = 10
c = 0
 
if ( a == b ):
   print "1 - a ���� b"
else:
   print "1 - a ������ b"
 
if ( a != b ):
   print "2 - a ������ b"
else:
   print "2 - a ���� b"
 
if ( a <> b ):
   print "3 - a ������ b"
else:
   print "3 - a ���� b"
 
if ( a < b ):
   print "4 - a С�� b" 
else:
   print "4 - a ���ڵ��� b"
 
if ( a > b ):
   print "5 - a ���� b"
else:
   print "5 - a С�ڵ��� b"
 
# �޸ı��� a �� b ��ֵ
a = 5
b = 20
if ( a <= b ):
   print "6 - a С�ڵ��� b"
else:
   print "6 - a ����  b"
 
if ( b >= a ):
   print "7 - b ���ڵ��� a"
else:
   print "7 - b С�� a"
   
   
a = 21
b = 10
c = 0
 
c = a + b
print "1 - c ��ֵΪ��", c
 
c += a
print "2 - c ��ֵΪ��", c 
 
c *= a
print "3 - c ��ֵΪ��", c 
 
c /= a 
print "4 - c ��ֵΪ��", c 
 
c = 2
c %= a
print "5 - c ��ֵΪ��", c
 
c **= a
print "6 - c ��ֵΪ��", c
 
c //= a
print "7 - c ��ֵΪ��", c

a = 10
b = 20
 
if ( a and b ):
   print "1 - ���� a �� b ��Ϊ true"
else:
   print "1 - ���� a �� b ��һ����Ϊ true"
 
if ( a or b ):
   print "2 - ���� a �� b ��Ϊ true��������һ������Ϊ true"
else:
   print "2 - ���� a �� b ����Ϊ true"
 
# �޸ı��� a ��ֵ
a = 0
if ( a and b ):
   print "3 - ���� a �� b ��Ϊ true"
else:
   print "3 - ���� a �� b ��һ����Ϊ true"
 
if ( a or b ):
   print "4 - ���� a �� b ��Ϊ true��������һ������Ϊ true"
else:
   print "4 - ���� a �� b ����Ϊ true"
 
if not( a and b ):
   print "5 - ���� a �� b ��Ϊ false��������һ������Ϊ false"
else:
   print "5 - ���� a �� b ��Ϊ true"
   
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
 
if ( a in list ):
   print "1 - ���� a �ڸ������б��� list ��"
else:
   print "1 - ���� a ���ڸ������б��� list ��"
 
if ( b not in list ):
   print "2 - ���� b ���ڸ������б��� list ��"
else:
   print "2 - ���� b �ڸ������б��� list ��"
 
# �޸ı��� a ��ֵ
a = 2
if ( a in list ):
   print "3 - ���� a �ڸ������б��� list ��"
else:
   print "3 - ���� a ���ڸ������б��� list ��"
   
a = 20
b = 20
 
if ( a is b ):
   print "1 - a �� b ����ͬ�ı�ʶ"
else:
   print "1 - a �� b û����ͬ�ı�ʶ"
 
if ( a is not b ):
   print "2 - a �� b û����ͬ�ı�ʶ"
else:
   print "2 - a �� b ����ͬ�ı�ʶ"
 
# �޸ı��� b ��ֵ
b = 30
if ( a is b ):
   print "3 - a �� b ����ͬ�ı�ʶ"
else:
   print "3 - a �� b û����ͬ�ı�ʶ"
 
if ( a is not b ):
   print "4 - a �� b û����ͬ�ı�ʶ"
else:
   print "4 - a �� b ����ͬ�ı�ʶ"
   
   
flag = False
name = 'luren'
if name == 'python':         # �жϱ�����Ϊ'python'
    flag = True          # ��������ʱ���ñ�־Ϊ��
    print 'welcome boss'    # �������ӭ��Ϣ
else:
    print name              # ����������ʱ�����������
    
    
num = 5     
if num == 3:            # �ж�num��ֵ
    print 'boss'        
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:           # ֵС����ʱ���
    print 'error'
else:
    print 'roadman'     # ������������ʱ���
    
    
num = 9
if num >= 0 and num <= 10:    # �ж�ֵ�Ƿ���0~10֮��
    print 'hello'
# ������: hello
 
num = 10
if num < 0 or num > 10:    # �ж�ֵ�Ƿ���С��0�����10
    print 'hello'
else:
    print 'undefine'
# ������: undefine
 
num = 8
# �ж�ֵ�Ƿ���0~5����10~15֮��
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    
    print 'hello'
else:
    print 'undefine'
# ������: undefine


count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
 
print "Good bye!"

count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"
   
   
for letter in 'Python':     # ��һ��ʵ��
   print '��ǰ��ĸ :', letter
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # �ڶ���ʵ��
   print '��ǰˮ�� :', fruit
 
print "Good bye!"

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print '��ǰˮ�� :', fruits[index]
 
print "Good bye!"

for num in range(10,20):  # ���� 10 �� 20 ֮�������
   for i in range(2,num): # �������ӵ���
      if num%i == 0:      # ȷ����һ������
         j=num/i          # ����ڶ�������
         print '%d ���� %d * %d' % (num,i,j)
         break            # ������ǰѭ��
   else:                  # ѭ���� else ����
      print num, '��һ������'
      
# ��� Python ��ÿ����ĸ
for letter in 'Python':
   if letter == 'h':
      pass
      print '���� pass ��'
   print '��ǰ��ĸ :', letter

print "Good bye!"

a = "Hello"
b = "Python"

print "a + b ��������", a + b 
print "a * 2 ��������", a * 2 
print "a[1] ��������", a[1] 
print "a[1:4] ��������", a[1:4] 

if( "H" in a) :
    print "H �ڱ��� a ��" 
else :
    print "H ���ڱ��� a ��" 

if( "M" not in a) :
    print "M ���ڱ��� a ��" 
else :
    print "M �ڱ��� a ��"

print r'\n'
print R'\n'

print "My name is %s and weight is %d kg!" % ('Zara', 21) 

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
 
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
	
list = []          ## ���б�
list.append('Google')   ## ʹ�� append() ���Ԫ��
list.append('Runoob')
print list

list1 = ['physics', 'chemistry', 1997, 2000]
 
print list1
del list1[2]
print "After deleting value at index 2 : "
print list1

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
 
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
 
 
print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
 
del dict['Name']; # ɾ������'Name'����Ŀ
#dict.clear();     # ��մʵ�������Ŀ
#del dict ;        # ɾ���ʵ�
 
print "dict['Age']: ", dict['Age'];
#print "dict['School']: ", dict['School'];

dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'};
 
print "dict['Name']: ", dict['Name'];

#dict = {['Name']: 'Zara', 'Age': 7};
 
print "dict['Name']: ", dict['Name'];

import time;  # ����timeģ��

ticks = time.time()
print "��ǰʱ���Ϊ:", ticks

localtime = time.localtime(time.time())
print "����ʱ��Ϊ :", localtime

localtime = time.asctime( time.localtime(time.time()) )
print "����ʱ��Ϊ :", localtime

# ��ʽ����2016-03-20 11:45:39��ʽ
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

# ��ʽ����Sat Mar 28 22:24:24 2016��ʽ
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
  
# ����ʽ�ַ���ת��Ϊʱ���
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

import calendar

cal = calendar.month(2016, 1)
print "�������2016��1�·ݵ�����:"
print cal;

Money = 2000
def AddMoney():
   # ����������ȡ������ע��:
   global Money
   Money = Money + 1
 
print Money
AddMoney()
print Money

import math
 
content = dir(math)
 
print content;

list = dir(math)

print list[1]

print "Python ��һ���ǳ��������ԣ�������"

#str = raw_input("�����룺")
#print "�������������: ", str

#str = input("�����룺")
#print "�������������: ", str

# ��һ���ļ�
fo = open("foo.txt", "r+")
print "�ļ���: ", fo.name
print "�Ƿ��ѹر� : ", fo.closed
print "����ģʽ : ", fo.mode
print "ĩβ�Ƿ�ǿ�Ƽӿո� : ", fo.softspace

# ��һ���ļ�
#fo = open("foo.txt", "w")
print "�ļ���: ", fo.name

#fo.write( "www.runoob.com!\nVery good site!\n")

str = fo.read(10)
print "��ȡ���ַ����� : ", str
 
# ���ҵ�ǰλ��
position = fo.tell()
print "��ǰ�ļ�λ�� : ", position
 
# ��ָ���ٴ����¶�λ���ļ���ͷ
position = fo.seek(0, 0)
str = fo.read(10)
print "���¶�ȡ�ַ��� : ", str
# �رմ򿪵��ļ�
fo.close()