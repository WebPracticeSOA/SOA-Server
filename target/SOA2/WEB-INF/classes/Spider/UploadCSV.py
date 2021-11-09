import oss2
import time
import os
#将生成的csvsc到oss中的bucket底下的csv文件夹
endpoint = 'http://oss-cn-beijing.aliyuncs.com'
auth = oss2.Auth('LTAI5tNVfKmpK9XDyvcyWX6f', '730eX85eAqYEKPBzLTWE5EK2CosA0q')
bucket = oss2.Bucket(auth, endpoint, 'internet-practice')
current_fold = time.strftime('%Y-%m-%d', time.localtime())
count=0
for root, dirs, files in os.walk(r"Files\\csv"):
    for file in files:
        localPath=os.path.join(root, file)
        ossPath=localPath[7:].replace("\\","/")
        print(ossPath)
        # 上传
        result = bucket.put_object_from_file(ossPath, localPath)
        count+=1
        print("成功上传"+str(count))