#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Employee:
   '����Ա���Ļ���'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
      
      
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()

"���� Employee ��ĵ�һ������"
emp1 = Employee("Zara", 2000)
"���� Employee ��ĵڶ�������"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

emp1.age = 7  # ���һ�� 'age' ����
if(hasattr(emp1, 'age')):
    print "������ age"    # ������� 'age' ���Է��� True��
    
class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "����"
 
pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3) # ��ӡ�����id
del pt1
del pt2
del pt3


class Parent:        # ���常��
   parentAttr = 100
   def __init__(self):
      print "���ø��๹�캯��"
 
   def parentMethod(self):
      print '���ø��෽��'
 
   def setAttr(self, attr):
      Parent.parentAttr = attr
 
   def getAttr(self):
      print "�������� :", Parent.parentAttr
 
class Child(Parent): # ��������
   def __init__(self):
      print "�������๹�췽��"
 
   def childMethod(self):
      print '�������෽��'
 
c = Child()          # ʵ��������
c.childMethod()      # ��������ķ���
c.parentMethod()     # ���ø��෽��
c.setAttr(200)       # �ٴε��ø���ķ��� - ��������ֵ
c.getAttr()          # �ٴε��ø���ķ��� - ��ȡ����ֵ