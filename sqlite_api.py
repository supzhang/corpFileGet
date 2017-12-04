import sqlite3
import os,time
path = os.getcwd() + '\\db.db'
conn = sqlite3.connect(path)
cursor = conn.cursor()


def data_insert(table_name,table_values):  #table_values = {'key1':'value1','key2':'values2'}
    segs_list = []
    values_list = []
    #构建字段名及数值
    for key in table_values:
        segs_list.append(key)
        values_list.append(table_values[key])
    segs =  ','.join(segs_list)

    #获取问号数量
    wen = []
    for x in range(len(table_values)):
        wen.append("?")
    wens = ','.join(wen)
    #插入数据
    try:
        sql = 'insert into ' + table_name + ' (' + segs + ') values (' + wens + ')'
        print(sql)
        print(values_list)
        cursor.execute(sql, values_list)
        conn.commit()
        return 1
    except Exception as e:
        print(str(e))
        return 0

def data_update(table_name,table_values):  #table_values = {'primarys:['id','xxx'.....],datas:{'data1':data1,'data2',data2....}
    values = []
    wherevalues = []
    where_list = []
    set_list = []
    for datakey in table_values['datas']:
        if datakey in table_values['primarys']:
            where_list.append(datakey + ' = ' + '?')
            wherevalues.append(table_values['datas'][datakey])
        else:
            set_list.append(datakey + ' = ' + '?')
            values.append(table_values['datas'][datakey])
    values = values + wherevalues
    where = ' where ' + ' and '.join(where_list)
    set = ' set ' + ','.join(set_list)
    sql = 'update ' + table_name +  set + where
    try:
        cursor.execute(sql, values)
        conn.commit()
        return 1
    except Exception as e:
        print(str(e))
        return 0

def data_delete(table_name,table_values):  #table_values={'字段1':'data',.....}
    values = []
    segs = []
    where_list = []
    for datakey in table_values:
        where_list.append(datakey + ' = ' + '?')
        values.append(table_values[datakey])
    where = ' and '.join(where_list)
    try:
        sql = 'delete from ' + table_name + ' where ' + where
        cursor.execute(sql,values)
        conn.commit()
        return 1
    except Exception as e:
        print(e)
        return 0







# t = int(time.time())
# table_name = 'logs'
# v = {
#     'dt':t,
#     'logstat':'成功',
#     'pcid':2,
#     'logs':'这是一个LOG'
# }
# l = data_insert(table_name,v)
# print(l)
v = {
    'primarys':['pcid','logs'],
    'datas':{
        'pcid':2,
        'dt':12312312123,
        'logs':'这是一个LOG',
        'logstat':'测试'
    }
}
r = data_update('logs',v)

deletev = {
    'pcid':'2',
    'logstat':'测试'
}
t = data_delete('logs',deletev)
print(t)