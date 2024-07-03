public class Alarm {
    public static boolean setAlarm(boolean employed, boolean vacation) {
        boolean status;

        if (vacation == true || employed == false) {
            status = false;
        }else{
            status = true;
        }



        return status;
    }

}