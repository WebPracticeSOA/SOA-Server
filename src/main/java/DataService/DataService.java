package DataService;

import com.alibaba.fastjson.JSONObject;
import java.sql.*;

import javax.jws.WebService;
import java.io.File;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

@WebService(name = "DataService", endpointInterface = "DataService.DataServicePort")
public class DataService implements DataServicePort {
    static final String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";
    static final String DB_URL = "jdbc:mysql://106.15.42.179:3303/practice?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC";
    static final String USER = "root";
    static final String PASS = "123456";
    @Override
    public String getAllData() {
        Connection conn = null;
        Statement stmt = null;
        List<Map> result = new ArrayList<Map>();
        try{
            Class.forName(JDBC_DRIVER);
            conn = DriverManager.getConnection(DB_URL,USER,PASS);
            stmt = conn.createStatement();
            String sql;
            sql = "SELECT * FROM papers";
            ResultSet rs = stmt.executeQuery(sql);
            while(rs.next()){
                Map<String, Object> line = new LinkedHashMap<String, Object>();
                line.put("id", rs.getInt("id"));
                line.put("title", rs.getString("title"));
                line.put("number", rs.getString("number"));
                line.put("category", rs.getString("category"));
                line.put("department", rs.getString("department"));
                line.put("release_time", rs.getDate("release_time"));
                line.put("implement_time", rs.getDate("implement_time"));
                line.put("grade", rs.getString("grade"));
                line.put("interpret", rs.getString("interpret"));
                line.put("user_id", rs.getInt("user_id"));
                line.put("input_time", rs.getDate("input_time"));
                line.put("content", rs.getString("content"));
                line.put("status", rs.getInt("status"));
                line.put("analyse_id", rs.getInt("analyse_id"));
                result.add(line);
            }
            rs.close();
            stmt.close();
            conn.close();
        }catch(SQLException se){
            System.out.println("sql exception");
            se.printStackTrace();
        }catch(Exception e){
            // ?????? Class.forName ??????
            System.out.println("exception");
            e.printStackTrace();
        }finally{
            // ????????????
            try{
                if(stmt!=null) stmt.close();
            }catch(SQLException se2){
            }// ???????????????
            try{
                if(conn!=null) conn.close();
            }catch(SQLException se){
                se.printStackTrace();
            }
        }
        return JSONObject.toJSONString(result);
    }
}
