# -*- coding: UTF-8 -*-
# ���庯��
def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "����û�а�������\n", Argument

# ���ú���
temp_convert("xyz");

# ���庯��
def mye( level ):
    if level < 1:
        raise Exception,"Invalid level!"
        # �����쳣�󣬺���Ĵ���Ͳ�����ִ��
try:
    mye(0)            # �����쳣
except Exception,err:
    print 1,err
else:
    print 2