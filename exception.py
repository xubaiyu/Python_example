# -*- coding: UTF-8 -*-
try:
    fh = open("testfile", "w")
    fh.write("����һ�������ļ������ڲ����쳣!!")
except IOError:
    print "Error: û���ҵ��ļ����ȡ�ļ�ʧ��"
else:
    print "����д���ļ��ɹ�"
    fh.close()
    
    
    
