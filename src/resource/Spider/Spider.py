from selenium import webdriver
import time
from time import sleep
import requests
import oss2
import os

urlStatitory="http://www.pbc.gov.cn/tiaofasi/144941/144953/index.html"
urlRegulation="http://www.pbc.gov.cn/tiaofasi/144941/144957/index.html"
urlNormative="http://www.pbc.gov.cn/tiaofasi/144941/3581332/index.html"
urlOthers="http://www.pbc.gov.cn/tiaofasi/144941/144959/index.html"
path="C:\\Users\\Administrator.DESKTOP-CGIO78B\\Downloads"

typeStatitory="行政法规"
typeRegulation="部门规章"
typeNormative="规范性文件"
typeOthers="其他文件"
DownloadedPath='C:\\Users\\Administrator.DESKTOP-CGIO78B\\Downloads\\'
link1='http://www.pbc.gov.cn/tiaofasi/resource/cms/2021/06/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E4%BA%BA%E6%B0%91%E5%B8%81%E7%AE%A1%E7%90%86%E6%9D%A1%E4%BE%8B.docx'
xpathOfdateFHalf="/html/body/div[4]/table[2]/tbody/tr/td[3]/table/tbody/tr/td/div/div/div[2]/div[1]/table/tbody/tr[2]/td/table["
xpathOfdateSHalf="]/tbody/tr/td[2]/span"


browser = webdriver.Chrome()


def nameRecord(path,name):
    with open(path, "a") as f:
        f.write(name+"\n")

#上传pdf
def download_pdf(url,name):
    r = requests.get(url)
    f = open(name+'', 'wb')
    f.write(r.content)
    f.close()


#上传本地
def upload_oss_file(typeFile,path,oldName,newName,postfix):
    endpoint = 'http://oss-cn-beijing.aliyuncs.com'
    auth = oss2.Auth('LTAI5tNVfKmpK9XDyvcyWX6f', '730eX85eAqYEKPBzLTWE5EK2CosA0q')
    bucket = oss2.Bucket(auth, endpoint, 'internet-practice')
    current_fold = time.strftime('%Y-%m-%d', time.localtime())
    # 上传
    result=bucket.put_object_from_file(typeFile+"/"+newName+postfix, path+oldName+postfix)
    print('http status: {0}'.format(result.status))

#上传link
def upload_oss_file_by_link(typeFile,name,link):
    endpoint = 'http://oss-cn-beijing.aliyuncs.com'
    auth = oss2.Auth('LTAI5tNVfKmpK9XDyvcyWX6f', '730eX85eAqYEKPBzLTWE5EK2CosA0q')
    bucket = oss2.Bucket(auth, endpoint, 'internet-practice')
    current_fold = time.strftime('%Y-%m-%d', time.localtime())
    # 上传
    result=bucket.put_object(typeFile+"/"+name, requests.get(link))
    print('http status: {0}'.format(result.status))

#上传字符串
def upload_oss_file_by_str(typeFile,name,str):
    endpoint = 'http://oss-cn-beijing.aliyuncs.com'
    auth = oss2.Auth('LTAI5tNVfKmpK9XDyvcyWX6f', '730eX85eAqYEKPBzLTWE5EK2CosA0q')
    bucket = oss2.Bucket(auth, endpoint, 'internet-practice')
    current_fold = time.strftime('%Y-%m-%d', time.localtime())
    # 上传
    result=bucket.put_object(typeFile+"/"+name, str)
    print('http status: {0}'.format(result.status))

#判断日期是否符合规定
def betweenDate(date):
    time=date.split("-")
    if(int(time[0])>2021 or int(time[0])<2016):
        return False
    else:
        if(time[0]=="2021" and int(time[1])>8):
            return False
        else:
            return True

def get_info(typeFile,urlType):
    browser.get(urlType)
    uploadCount=0
    uploadAppendixCount=0
    names=[]
    links=[]
    texts=[]
    pagingNormals=[1,2,3,4]
    count=0#帮助判断是不是最后一页
    while ((count==1) or len(pagingNormals)==4) and len(pagingNormals)>1:
        tempnames=[]
        #获取文件的名字
        temp=browser.find_elements_by_class_name('newslist_style')
        for i in range(0,len(temp)):
            time.sleep(0.5)
            date=browser.find_element_by_xpath(xpathOfdateFHalf+str(i+1)+xpathOfdateSHalf).text
            if (int(date.split("-")[0])<2016):
                break
            if(betweenDate(date)):
                print(date)
                title=browser.find_element_by_link_text(temp[i].text).get_attribute('title')
                tempnames.append(temp[i].text)
                print('text:'+temp[i].text)
                names.append(title)
                nameRecord("./FilesList.txt", title)
        #获取文件的link
        for i in tempnames:
            link=browser.find_element_by_link_text(i).get_attribute('href')
            links.append(link)
            #link若是docx下载链接则直接点击下载到本地
            if(str(link).endswith("docx")):
                browser.find_element_by_link_text(i).click()
            if(str(link).endswith("pdf")):
                print("直接点击是pdf链接")
            print('文件链接:'+link)
        pagingNormals=browser.find_elements_by_class_name('pagingNormal')
       # print("pagingNormals is "+str(len(pagingNormals)))
        if(len(pagingNormals)>=2):#判断是不是最后一页
            pagingNormals[-2].click()
        count+=1


    for i in range(0,len(links)):
        #link是docx下载链接则直接上传本地已经下载的docx文件
        if(str(links[i]).endswith("docx")):
            print('遇到docx文件')
            texts.append("none")
            # browser.get(urlType)
            # browser.find_element_by_link_text(names[i]).click()
            time.sleep(2)
            upload_oss_file(typeFile,DownloadedPath,names[i].split("（")[0],names[i].split("（")[0],".docx")
            os.remove(DownloadedPath+names[i].split("（")[0]+".docx")
            uploadCount+=1
            print("已经上传文件数："+str(uploadCount))
        else:
        # browser.find_element_by_link_text(i).click()
        # windows=browser.window_handles
        # browser.switch_to.window(windows[1])
        # time.sleep(3)
            browser.get(links[i])
            zoom=browser.find_element_by_id("zoom")
            tempText=zoom.text
            print('文件内容长度:'+str(len(tempText)))
            #遇到pdf链接则下载到本地再上传pdf文件
            if(len(tempText)<200 and str(tempText).endswith('.pdf')):
                print("遇到pdf文件")
                print(names[i])
                pdfLink = browser.find_element_by_partial_link_text('.pdf')
                print("pdf链接:"+pdfLink.get_attribute('href'))
                download_pdf(pdfLink.get_attribute('href'),pdfLink.text)
                time.sleep(1)
                upload_oss_file(typeFile,'./',pdfLink.text,pdfLink.text,'')
                os.remove("./"+pdfLink.text)
                uploadCount += 1
                print("已经上传文件总数：" + str(uploadCount))
                tempText='none'
            else:
                appendixDocElements=browser.find_elements_by_partial_link_text('.doc')
                appendixPdfElements = browser.find_elements_by_partial_link_text('.pdf')
                if(len(appendixDocElements)>0):
                    print("有doc/docx附件")
                    for docElement in appendixDocElements:
                        docElement.click()
                        time.sleep(2)
                        try:
                            newName=names[i]+"的"
                            if(len(docElement.text)<8):
                                newName+=docElement.text
                            else:
                                newName=docElement.text
                            upload_oss_file(typeFile+"/附件",DownloadedPath,docElement.get_attribute('href').split("/")[-1],newName,'')
                            os.remove(DownloadedPath+docElement.get_attribute('href').split("/")[-1])
                        except FileNotFoundError:
                            newName=names[i]
                            if(len(docElement.text)<8):
                                newName+=docElement.text
                            else:
                                newName=docElement.text
                            upload_oss_file(typeFile+"/附件", DownloadedPath, docElement.text,newName, '')
                            os.remove(DownloadedPath+docElement.text)
                        nameRecord("./AppendixList.txt", docElement.text)
                        uploadAppendixCount+=1
                        uploadCount+=1
                        print("上传附件数:"+str(uploadAppendixCount))
                if(len(appendixPdfElements)>0):
                    print("有pdf附件")
                    for pdfElement in appendixPdfElements:
                        print("pdf附件链接:"+pdfElement.get_attribute('href'))
                        download_pdf(pdfElement.get_attribute('href'), pdfElement.text)
                        time.sleep(1)
                        newName = names[i]+"的"
                        if (len(pdfElement.text) < 8):
                            newName += pdfElement.text
                        else:
                            newName = pdfElement.text
                        upload_oss_file(typeFile+"/附件", './', pdfElement.text,newName, '')
                        nameRecord("./AppendixList.txt", pdfElement.text)
                        os.remove("./"+ pdfElement.text)
                        uploadAppendixCount += 1
                        uploadCount += 1
                        print("上传附件数:" + str(uploadAppendixCount))
            texts.append(tempText)
        # browser.back()

    #非docx和pdf格式的则上传文本到txt格式中
    for i in range(0,len(names)):
        if not (str(links[i]).endswith("docx") or len(texts[i])<=4):
            if(names.count(names[i])>1):
                #名字重复的
                upload_oss_file_by_str(typeFile, names[i] + "("+str(names[0:i].count(names[i])+1)+")"+'.txt', texts[i])
            else:
                upload_oss_file_by_str(typeFile,names[i]+'.txt',texts[i])
            uploadCount+=1
            print("已经上传文件总数："+str(uploadCount))
    print("普通文件总数="+str(len(texts))+","+"附件总数="+str(uploadAppendixCount))


get_info(typeStatitory,urlStatitory)
get_info(typeRegulation,urlRegulation)
get_info(typeNormative,urlNormative)
get_info(typeOthers,urlOthers)
browser.quit()



