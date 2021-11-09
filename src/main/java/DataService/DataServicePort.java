package DataService;

import javax.jws.WebService;

@WebService(name = "DataServicePort")
public interface DataServicePort {
    public String getAllData();
}
