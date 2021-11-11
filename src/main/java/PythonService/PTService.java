package PythonService;

import java.io.*;

import javax.jws.WebService;

import static PythonService.PTResponseEnum.FAIL;
import static PythonService.PTResponseEnum.SUCCESS;

@WebService(
        name = "PTService",
        endpointInterface = "PythonService.PTServicePort"
)
public class PTService implements PTServicePort {

    public String trans() {
        Process proc;
        try {
//            String[] cmd = {"cmd","/C","python D:\\Web-final\\SOA-Part\\src\\Spider\\Spider.py"};
            proc = Runtime.getRuntime().exec("python3 /usr/local/tomcat/apache-tomcat-7.0.108/webapps/SOA-Part/WEB-INF/classes/Spider/Spider.py");// 执行py文件
            //用输入输出流来截取结果
            printMessage(proc.getInputStream());
            printMessage(proc.getErrorStream());
            int value = proc.waitFor();
            System.out.println(value);
            //TODO:如果想要下载的话把这一段注释去掉
//            proc = Runtime.getRuntime().exec("python D:\\Web-final\\SOA-Part\\src\\resource\\Spider\\DownloadFromOss.py");// 执行py文件
//            //用输入输出流来截取结果
//            printMessage(proc.getInputStream());
//            printMessage(proc.getErrorStream());
//            value = proc.waitFor();
//            System.out.println(value);
        }catch (Exception e){
            System.out.println(e.getMessage());
            return FAIL.getMessage();
        }
        return SUCCESS.getMessage();
    }

    private static void printMessage(final InputStream input) {
        new Thread(new Runnable() {
            public void run() {
                Reader reader = new InputStreamReader(input);
                BufferedReader bf = new BufferedReader(reader);
                String line = null;
                try {
                    while ((line = bf.readLine()) != null) {
                        System.out.println(line);
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }
}
