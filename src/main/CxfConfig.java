package main;

import main.DataService.DataService;
import main.PythonService.PTService;

import javax.xml.ws.Endpoint;

public class CxfConfig {

    public static void main(String[] args) {

        System.out.println("Ready to Start...");

        String address1 = "http://localhost:8080/PTService";
        Endpoint.publish(address1, new PTService());
        System.out.println("PTService Publish Success!");
        System.out.println("Address:" + address1);

        String address2 = "http://localhost:8080/DataService";
        Endpoint.publish(address2, new DataService());
        System.out.println("DataService Publish Success!");
        System.out.println("Address:" + address2);
    }
}
