# -*- coding: UTF-8 -*-
if True:
    print "Answer"
    print "True"
else:
    print "Answer"
    # 1û���ϸ���������ִ��ʱ�ᱨ��
    print "False"
    
# ��һ��ע��
print "Hello, Python!";  # �ڶ���ע��

print "��ã�����";
    
'''
���Ƕ���ע�ͣ�ʹ�õ����š�
���Ƕ���ע�ͣ�ʹ�õ����š�
���Ƕ���ע�ͣ�ʹ�õ����š�
'''

"""
���Ƕ���ע�ͣ�ʹ��˫���š�
���Ƕ���ע�ͣ�ʹ��˫���š�
���Ƕ���ע�ͣ�ʹ��˫���š�
"""

raw_input("���� enter ���˳��������������ʾ...\n")

import sys; x = 'xubaiyu'; sys.stdout.write(x + '\n')

x="a"
y="b"
# �������
print x
print y

print '---------'
# ���������
print x,
print y,

# ���������
print x,y

import sys

print sys.argv

counter = 100 # ��ֵ���ͱ���
miles = 1000.0 # ������
name = "John" # �ַ���
 
print counter
print miles
print name

a = b = c = 1
print a
print b
print c

a, b, c = 1, 2, "john"
print a
print b
print c

s = 'ilovepython'
print s[1:5]
	
str = 'Hello World!'
 
print str           # ��������ַ���
print str[0]        # ����ַ����еĵ�һ���ַ�
print str[2:5]      # ����ַ����е������������֮����ַ���
print str[2:]       # ����ӵ������ַ���ʼ���ַ���
print str * 2       # ����ַ�������
print str + "TEST"  # ������ӵ��ַ���

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print list               # ��������б�
print list[0]            # ����б�ĵ�һ��Ԫ��
print list[1:3]          # ����ڶ�����������Ԫ�� 
print list[2:]           # ����ӵ�������ʼ���б�ĩβ������Ԫ��
print tinylist * 2       # ����б�����
print list + tinylist    # ��ӡ��ϵ��б�


tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
 
print tuple               # �������Ԫ��
print tuple[0]            # ���Ԫ��ĵ�һ��Ԫ��
print tuple[1:3]          # ����ڶ�������������Ԫ�� 
print tuple[2:]           # ����ӵ�������ʼ���б�ĩβ������Ԫ��
print tinytuple * 2       # ���Ԫ������
print tuple + tinytuple   # ��ӡ��ϵ�Ԫ��


tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
#tuple[2] = 1000    # Ԫ�����ǷǷ�Ӧ��
list[2] = 1000     # �б����ǺϷ�Ӧ��


dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
 
 
print dict['one']          # �����Ϊ'one' ��ֵ
print dict[2]              # �����Ϊ 2 ��ֵ
print tinydict             # ����������ֵ�
print tinydict.keys()      # ������м�
print tinydict.values()    # �������ֵ