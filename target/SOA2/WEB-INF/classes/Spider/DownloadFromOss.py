import oss2
import time
import os
from itertools import islice

endpoint = 'http://oss-cn-beijing.aliyuncs.com'
auth = oss2.Auth('LTAI5tNVfKmpK9XDyvcyWX6f', '730eX85eAqYEKPBzLTWE5EK2CosA0q')
bucket = oss2.Bucket(auth, endpoint, 'internet-practice')
current_fold = time.strftime('%Y-%m-%d', time.localtime())

#从oss上面将internet-practice bucket的所有内容下载下来到本地Files文件夹


for b in oss2.ObjectIterator(bucket):
    print(b.key)
    localPath="./Files/"+b.key
    folder=localPath.replace(localPath.split("/")[-1],"")
    if(not os.path.exists(folder)):
        os.makedirs(folder)
    if(not localPath.endswith("/")):
        bucket.get_object_to_file(b.key, localPath)