#-*- coding: UTF-8 -*-
# ���庯��
def printme( str ):
   "��ӡ�κδ�����ַ���"
   print str;
   return;
 
# ���ú���
printme("��Ҫ�����û��Զ��庯��!");
printme("�ٴε���ͬһ����");
printme("xuby");

def ChangeInt( a ):
    a = 10

b = 2
ChangeInt(b)
print b # ����� 2

# ��д����˵��
def changeme( mylist ):
   "�޸Ĵ�����б�"
   mylist.append([1,2,3,4]);
   print "������ȡֵ: ", mylist
   return
 
# ����changeme����
mylist = [10,20,30];
changeme( mylist );
print "������ȡֵ: ", mylist

#��д����˵��
def printinfo( name, age ):
   "��ӡ�κδ�����ַ���"
   print "Name: ", name;
   print "Age ", age;
   return;
 
#����printinfo����
printinfo( age=50, name="miki" );

# ��д����˵��
def printinfo( arg1, *vartuple ):
   "��ӡ�κδ���Ĳ���"
   print "���: "
   print arg1
   for var in vartuple:
      print var
   return;
 
# ����printinfo ����
printinfo( 10 );
printinfo( 70, 60, 50 );

total = 0; # ����һ��ȫ�ֱ���
# ��д����˵��
def sum( arg1, arg2 ):
   #����2�������ĺ�."
   total = arg1 + arg2; # total�������Ǿֲ�����.
   print "�������Ǿֲ����� : ", total
   return total;
 
#����sum����
sum( 10, 20 );
print "��������ȫ�ֱ��� : ", total 