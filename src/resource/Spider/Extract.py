import os
import docx
from docx import Document
import sys
import pickle
import re
import  codecs
import string
import shutil
from win32com import client as wc
import json
import csv
import time
import datetime
from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf



proPath="./Files\\"
resPath="./Files\\csv\\"
path1="行政法规"
path2="部门规章"
path3="规范性文件"
path4="其他文件"



def readPdf(filePath):
    with open(filePath, "rb") as pdf:
        # 创建PDF资源管理器
        resource = PDFResourceManager()
        # 创建一个能在内存中读写str的对象
        rw_str = StringIO()
        # 创建一个PDF参数分析器
        laparam = LAParams()
        # 创建一个PDF设备对象
        device = TextConverter(resource, rw_str, laparams=laparam)
        # 解析PDF文件
        process_pdf(resource, device, pdf)
        device.close()  # 关闭设备对象
        # 获取内存中写入的str
        content = rw_str.getvalue()  # type:str
        rw_str.close()  # 关闭读写对象
        # 获取所有行
        lines = content.split("\n")  # type:list
        print(lines)
        return content

#获取文件的法规文号
def getNum(fileName,content):
     # print(fileName)
     if(fileName[-2]=="号" and fileName[-3]==" "):
        fileName=fileName[0:-3]+"号"
     names=fileName.split(" ")
     for i in range(0,len(names)):
        if(names[len(names)-1-i].find("号")>0):
            temp=names[len(names)-1-i]
            temp2=temp[0:temp.index("号")+1]
            try:
                temp3=temp2[::-1]
                index1=temp3.index("银")
                temp4=temp3[0:index1+1][::-1]
            except:
                    temp4=temp2
            # print(temp4)
            return temp4
     return None

#获取发文部门
def getDepart(fileName):
    departments=""
    if(fileName.find("中国人民银行")>=0):
        departments+="中国人民银行"
        departments+="\n"
    if(fileName.find("海关总署")>=0):
        departments+="海关总署"
        departments+="\n"
    if(fileName.find("改革委员会")>=0):
        departments+="改革委员会"
        departments+="\n"
    if(fileName.find("财政部")>=0):
        departments+="财政部"
        departments+="\n"
    if(fileName.find("中国证券监督管理委员会")>=0):
        departments+="中国证券监督管理委员会"
        departments+="\n"
    if(fileName.find("中国银行业监督管理委员会")>=0):
        departments+="中国银行业监督管理委员会"
        departments+="\n"
    if(fileName.find("发展改革委")>=0):
        departments+=" 发展改革委"
        departments+="\n"
    if(fileName.find("证监会")>=0):
        departments+="中国证券监督管理委员会"
        departments+="\n"
    if(fileName.find("商务部")>=0):
        departments+="商务部"
        departments+="\n"
    if(fileName.find("中国银行业监督管理委员会")>=0):
        departments+="中国银行业监督管理委员会"
        departments+="\n"
    if(fileName.find("银监会")>=0):
        departments+="中国银行业监督管理委员会"
        departments+="\n"
    if(fileName.find("工商总局")>=0):
        departments+="工商总局"
        departments+="\n"
    if(fileName.find("工业和信息化部")>=0):
        departments+="工业和信息化部"
        departments+="\n"
    if(fileName.find("公安部")>=0):
        departments+="公安部"
        departments+="\n"
    if(fileName.find("保监会")>=0 and fileName.find("银保监会")<0):
        departments+="中国银行保险监督管理委员会"
        departments+="\n"
    if(fileName.find("银保监会")>=0):
        departments+="中国银行保险监督管理委员会"
        departments+="\n"
    if(fileName.find("国务院国有资产监督管理委员会")>=0):
        departments+="国务院国有资产监督管理委员会"
        departments+="\n"
    if(fileName.find("中国银行保险监督管理委员会")>=0):
        departments+="中国银行保险监督管理委员会"
        departments+="\n"
    if(fileName.find("国家外汇管理局")>=0):
        departments+="国家外汇管理局"
        departments+="\n"
    if(fileName.find("国家认证认可监督管理委员会")>=0):
        departments+="国家认证认可监督管理委员会"
        departments+="\n"
    if(fileName.find(" 国家税务总局")>=0):
        departments+=" 国家税务总局"
        departments+="\n"
    if(fileName.find("民政部")>=0):
        departments+="民政部"
        departments+="\n"
    if(fileName.find("扶贫办")>=0):
        departments+="扶贫办"
        departments+="\n"
    if(fileName.find("中华人民共和国国家发展和改革委员会")>=0):
        departments+="中华人民共和国国家发展和改革委员会"
        departments+="\n"
    if(fileName.find("人力资源社会保障部办公厅")>=0):
        departments+="人力资源社会保障部办公厅"
        departments+="\n"
    if(fileName.find("国务院")>=0 and fileName.find("国务院国有资产监督管理委员会")<0):
        departments+="国务院"
        departments+="\n"
    if(fileName.find("中华人民共和国")>=0):
        departments+="国务院"
        departments+="\n"
    return departments

#获取实施日期
def getWorkDate(filePath,content):
    if(content==None):
        # print(filePath)
        return None
    date=''
    if(content.find("起实施")>=0):
        index=content.index("起实施")
        temp_index=index
        while(content[temp_index]!="自"):
            temp_index-=1
        date=content[temp_index+1:index]
    elif(content.find("起施行")>=0):
        index=content.index("起施行")
        temp_index=index
        while(content[temp_index]!="自"):
            a=content[temp_index]
            temp_index-=1
        date=content[temp_index+1:index]
    elif(content.find("施行")>=0):
        index=content.index("施行")
        temp_index=index
        while(content[temp_index]!="自"):
            a=content[temp_index]
            temp_index-=1
            if(index-temp_index<=10):
                print("找不到实施日期")
                return None
        date=content[temp_index+1:index]
    else:
        print("找不到实施日期")
        return None
    if(date==''):
        print(filePath)
    if(len(date)>11):
        print("找不到实施日期")
        return None
    return date

#获取发布日期
def getClaimDate(content):
    if(content==None):
        return None
    if(content.find("日印发")>=0):
        end=content.index("日印发")
        start=end
        while(content[start]!="\n"):
            start-=1
        date=content[start+1:end+1]
        return date
    else:
        try:
            for i in range(0,len(content)):
                if(content[i]=="年" and content[i-5]=="\n"):
                    start=i-4
                    end=i
                    while(content[end]!="日"):
                        end+=1
                    date=content[start:end+1]
                    if (len(date)>11):
                        print("找不到发布日期")
                        return None
                    return date
        except IndexError:
            print("找不到发布日期")
            return None
    return None
def writeCsv(filePath,rows):
    f = open(filePath, 'w',newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["字段名称", "字段描述", "录入形式","数据类型","必输项","备注"])
    for row in rows:
        csv_writer.writerow(row)
    f.close()

#读取docx
def readDocx(filePath):
    content = ""
    document = Document(filePath)
    for paragraph in document.paragraphs:
        content+=paragraph.text
        # print(paragraph.text)
    return content


# 读取文件内容
def readTxt(filename):
    content=""
    fopen = open(filename, 'r',encoding='UTF-8') # r 代表read
    for eachLine in fopen:
        content+=eachLine
    fopen.close()
    return content

#读取doc
def readDoc(filePath):
    word = wc.Dispatch('Word.Application')
    doc = word.Documents.Open(filePath)        # 目标路径下的文件
    doc.SaveAs(filePath[0:-3]+".docx", 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件
    readDocx(filePath[0:-3]+".docx")
    doc.Close()
    word.Quit()


def readFile(filePath):
    if (filePath.endswith("txt")):
        return readTxt(filePath)
    if (filePath.endswith("docx")):
        return readDocx(filePath)
    if (filePath.endswith("doc")):
        return readDoc(filePath)
    # if (filePath.endswith("pdf")):
    #     return None

def createCsv(filePath,pathtype):
    # print(filePath)
    fileName=filePath.split("\\")[-1].split(".")[0]
    content=readFile(filePath)
    rows=[]
    temp=[]
    temp.append("法规标题")
    temp.append(fileName)
    temp.append("手工录入")
    temp.append("字符串型")
    temp.append("是")
    temp.append(None)
    rows.append(temp)

    temp=[]
    temp.append("法规文号")
    num=getNum(fileName,content)
    temp.append(num)
    temp.append("手工录入")
    temp.append("字符串型")
    temp.append("可为空")
    temp.append(None)
    rows.append(temp)

    temp=[]
    temp.append("外规类别")
    temp.append(None)
    temp.append(None)
    temp.append(None)
    temp.append(None)
    temp.append(None)
    rows.append(temp)

    temp=[]
    temp.append("发文部门")
    departments=getDepart(fileName)
    temp.append(departments)
    temp.append("选择录入")
    temp.append("字符串型")
    temp.append("是")
    temp.append(None)
    rows.append(temp)

    temp=[]
    temp.append("效力等级")
    temp.append(pathtype)
    temp.append("选择录入")
    temp.append("字符串型")
    temp.append("是")
    temp.append(None)
    rows.append(temp)

    temp=[]
    temp.append("发布日期")
    claim_date=getClaimDate(content)
    print("发布日期:")
    print(claim_date)
    temp.append(claim_date)
    temp.append("选择录入")
    temp.append("字符串型")
    temp.append("是")
    temp.append(None)
    rows.append(temp)

    temp=[]
    temp.append("实施日期")
    work_date=getWorkDate(filePath,content)
    print("实施日期")
    print(work_date)
    if(work_date==None and claim_date!=None):
        work_date=claim_date
    temp.append(work_date)
    temp.append("选择录入")
    temp.append("字符串型")
    temp.append("是")
    temp.append(None)
    rows.append(temp)

    temp=[]
    temp.append("解读部门")
    temp.append(None)
    temp.append(None)
    temp.append(None)
    temp.append(None)
    temp.append("外规内化部门")
    rows.append(temp)

    temp=[]
    temp.append("录入人")
    temp.append("huzihua")
    temp.append("系统生成")
    temp.append("字符串型")
    temp.append("是")
    temp.append("根据当前用户信息生成")
    rows.append(temp)

    temp=[]
    temp.append("录入时间")
    nowtime=str(time.strftime("%Y-%m-%d,%H: %M: %S", time.localtime()))
    temp.append(nowtime)
    temp.append("系统生成")
    temp.append("字符串型")
    temp.append("是")
    temp.append("系统根据当前日期自动生成")
    rows.append(temp)

    temp=[]
    temp.append("正文")
    temp.append(content)
    temp.append("手工录入")
    temp.append("内嵌正文")
    temp.append("是")
    temp.append(None)
    rows.append(temp)


    temp=[]
    temp.append("状态")
    temp.append("1")
    temp.append("系统录入")
    temp.append("字符串型")
    temp.append("是")
    temp.append("0 未发布"+"\n"+"1 已发布")
    rows.append(temp)

    writeCsv(resPath +pathtype+"\\"+fileName + ".csv", rows)

def extract(proPath,pathtype):
    filePath=proPath+pathtype
    pathDir = os.listdir(filePath)
    for allDir in pathDir:
        if(allDir!="附件"):
            childPath = filePath+"\\"+allDir
            # print(allDir)
            createCsv(childPath,pathtype)




extract(proPath,path1)
extract(proPath,path2)
extract(proPath,path3)
extract(proPath,path4)