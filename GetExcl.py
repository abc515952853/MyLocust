#!/user/bin/env python
#coding=utf-8
import requests
import datetime
import time

from xlrd import xldate_as_tuple

import xlrd
import xlwt

class read_excl():
    #获取excl数据
    def get_excl_data(self):
        readbook = xlrd.open_workbook(r'userinfo\testcase.xlsx')
        sheet = readbook.sheet_by_name('UserName')

        row = sheet.row_values(0)
        rowNum  = sheet.nrows
        colNum = sheet.ncols 
        
        cls = []
        curRowNo = 1
        while self.has_next(rowNum,curRowNo):
            s = {}  
            col = sheet.row_values(curRowNo)  
            i = colNum  
            for x in range(i):
                s[row[x]] = self.conversion_cell(sheet,curRowNo,x,col[x])
            cls.append(s)  
            curRowNo += 1
        return cls

    def has_next(self,rownum,curRowNo):  
        if rownum == 0 or rownum <= curRowNo :  
            return False  
        else:  
            return True 

    def conversion_cell(self,sheet,curRowNo,curColNo,cell):
        #判断python读取的返回类型  0 --empty,1 --string, 2 --number(都是浮点), 3 --date, 4 --boolean, 5 --error  
        if sheet.cell(curRowNo,curColNo).ctype == 2:
                no = int(cell)          
        elif sheet.cell(curRowNo,curColNo).ctype == 3:
            # 转成datetime对象
            date = datetime(*xldate_as_tuple(cell, 0))
            no = date.strftime('%Y-%m-%d')
        else:
                no = cell
        return no

    def chose_data(self,data,num):
        return data[num]['phone']

