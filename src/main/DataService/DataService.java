package main.DataService;

import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.internal.OSSHeaders;
import com.aliyun.oss.model.CannedAccessControlList;
import com.aliyun.oss.model.ObjectMetadata;
import com.aliyun.oss.model.PutObjectRequest;
import com.aliyun.oss.model.StorageClass;

import java.io.IOException;
import java.sql.*;

import javax.jws.WebService;
import java.io.File;

@WebService(name = "DataService", endpointInterface = "main.DataService.DataServicePort")
public class DataService implements DataServicePort {
    static final String USER = "root";
    static final String PASS = "czh13935748710.";
    static final String DBName = "exampledb6";
    static final String TableName = "spittle";
    static final String SaveAddress = "data.sql";

    private String endpoint = "https://oss-cn-shanghai.aliyuncs.com";
    private String accessKeyId = "LTAI5tJRq93hFiZS5u6YGhvi";
    private String accessKeySecret = "U4Y2xGsuTLyCQ5zRN1obRaASqj0zbE";
    private boolean hasStore = false;
    @Override
    public String getAllData() {
        if(!hasStore){
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.append("mysqldump -u ").append(USER).append(" --password=").append(PASS);
            stringBuilder.append(" -h localhost ").append("-P 3306 ").append(DBName).append(" ").append(TableName);
            stringBuilder.append(" -r ").append(SaveAddress);
            try{
                System.out.println(stringBuilder.toString());
                Process process = Runtime.getRuntime().exec(stringBuilder.toString());
                int ret = process.waitFor();
                if (ret == 0){
                    System.out.println("success");
                    OSS ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessKeySecret);
                    PutObjectRequest putObjectRequest = new PutObjectRequest("bankdata", "data.sql", new File(SaveAddress));
                    ObjectMetadata metadata = new ObjectMetadata();
                    metadata.setHeader(OSSHeaders.OSS_STORAGE_CLASS, StorageClass.Standard.toString());
                    metadata.setObjectAcl(CannedAccessControlList.PublicRead);
                    putObjectRequest.setMetadata(metadata);
                    ossClient.putObject(putObjectRequest);
                    ossClient.shutdown();
                }
                else {
                    System.out.println(ret);
                    return "Export Failed";
                }
            } catch (IOException e){
                System.out.println("IOException");
                return "Export Failed";
            } catch (InterruptedException e){
                System.out.println("InterruptedException");
                return "Export Failed";
            }
        }
        return "https://bankdata.oss-cn-shanghai.aliyuncs.com/data.sql";
    }
}
