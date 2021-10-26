package main.PythonService;

public enum PTResponseEnum {

    SUCCESS("execute the file successfully"),
    FAIL("some problems have happened...");

    private String message;
    PTResponseEnum(String message){
        this.message = message;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
