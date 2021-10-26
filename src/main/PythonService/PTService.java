package main.PythonService;

import org.python.util.PythonInterpreter;

import javax.jws.WebService;

@WebService(
        name = "PTService",
        endpointInterface = "main.PythonService.PTServicePort"
)
public class PTService implements PTServicePort {

    public void execute() {
        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.execfile("src\\resource\\resource.py");
    }
}
