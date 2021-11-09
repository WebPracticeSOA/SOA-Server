## Readme

Files文件夹存放爬下来的四个类别的文件和一个csv文件夹，其中csv文件夹是将其他四个类别文件转换为csv格式以便后端处理。

Images文件夹存放的是pdf图片，因为爬下来的文件中有些是图片pdf格式而不是文本格式，所以需要将这些pdf先转换为图片，再用ocr识别图片的文字将内容转换为文本格式。其中子文件夹名字对应的是pdf文件名。（之前不小心删除了，但是跑起来后会再生成的）

Appendixlist.txt存放的是所有附件的文件名字

FilesList.txt存放的是所有正文文件的名字

Spider.py是爬虫代码。主要实现从网站上爬取所需的四个类别的文件到本地，再从本地上传的阿里云oss中。（该文件需要配置环境，参考链接[Python selenium + chromedriver 爬取数据_石榴笑了的博客-CSDN博客](https://blog.csdn.net/weixin_42947716/article/details/103398015)）

DownloadFromOss.py是将初步爬下来的原始文件下载到本地的Files文件夹中

ConvertPdf.py主要实现将下载到本地的Files的pdf文件先拆成图片，再用ocr识别成文本。（这个文件跑起来的话要花钱，因为用的是百度的ocr所有尽量别跑这个文件）

Extract.py是从文本文件内容中提取出数据库所需的字段内容，并一一生成一个对应的csv文件，存进csv文件夹。

UploadCSV.py是最后将生成的csv文件夹上传至oss中的csv文件夹



oss用户名：2021Practice@1645483843958325.onaliyun.com

密码：181250047

可以登录阿里云oss上去查看