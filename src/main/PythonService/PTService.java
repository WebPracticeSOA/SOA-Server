package main.PythonService;

import org.python.util.PythonInterpreter;

import javax.jws.WebService;

import static main.PythonService.PTResponseEnum.FAIL;
import static main.PythonService.PTResponseEnum.SUCCESS;

@WebService(
        name = "PTService",
        endpointInterface = "main.PythonService.PTServicePort"
)
public class PTService implements PTServicePort {

    public String trans() {
        try {
            PythonInterpreter interpreter = new PythonInterpreter();
            interpreter.execfile("src\\resource\\resource.py");
        }catch (Exception e){
            return FAIL.getMessage();
        }
        return SUCCESS.getMessage();
    }
}
