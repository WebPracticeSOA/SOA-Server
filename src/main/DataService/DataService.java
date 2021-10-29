package main.DataService;

import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.internal.OSSHeaders;
import com.aliyun.oss.model.*;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.sql.*;

import javax.jws.WebService;
import java.io.File;
import java.util.List;

@WebService(name = "DataService", endpointInterface = "main.DataService.DataServicePort")
public class DataService implements DataServicePort {
    private String endpoint = "http://oss-cn-beijing.aliyuncs.com";
    private String accessKeyId = "LTAI5tNVfKmpK9XDyvcyWX6f";
    private String accessKeySecret = "730eX85eAqYEKPBzLTWE5EK2CosA0q";
    private String bucketName = "internet-practice";
    @Override
    public String getAllData() {
        OSS ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessKeySecret);
        ObjectListing objectListing = ossClient.listObjects(bucketName);
        List<OSSObjectSummary> sums = objectListing.getObjectSummaries();
        StringBuilder stringBuilder = new StringBuilder();
        for (OSSObjectSummary s : sums) {
            try{
                stringBuilder.append("https://internet-practice.oss-cn-beijing.aliyuncs.com/").append(URLEncoder.encode(s.getKey(), "UTF-8")).append("\n");
            } catch (UnsupportedEncodingException e){
                e.printStackTrace();
                return "Encoding Error";
            }
        }
        return stringBuilder.toString();
    }
}
