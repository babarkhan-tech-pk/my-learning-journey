// AIK CLASS CNIC BNA LI
class CNIC{
    // PROPERTIES OF CNIC CLASS
    int cnic;
    String name;
    int age;
    double dob;
    String city;

    // METHODS FUNCTIONS OF CNIC CLASS
    // 1. TO SHOW THE CNIC NUMBER
    void showCnic(){
        System.out.println("Your CNIC Number is : " + cnic);
    }

    // CONSTRUCTOR
    // 1 . PARAMETRIZED CONSTRUCTOR JIS KO HUM KHUD VALUES DETY HAIN.
    // JAB B AP IS CONSTRUCTOR KO CALL KAREN GAY TU US MA YE PARAMETERS B DENY PRY GAY.
    // IS MAY VARIABLE NAMES KO DIFFERNT KARNY K LIYE SAB KAY SATH AIK S ADD KAR DIYA HAY.
    CNIC(int cnics,String names,int ages,double dobs,String citys){
        // AB IN VALUES KO PHLY SAY MOJOD VARIABLES MA SET KAR DEN GAY.
        cnic = cnics;
        name = names;
        age = ages;
        dob = dobs;
        city = citys;
    }

    // 2. DEFAULT CONSTRUCTORE , JIS MA VALUES PRESET HAIN.
    // FOR EAXMPLE AGAR AP CONSTRCTOR KO CALL KAR KAY KOI VALUE B NAHI DEN GY TU YEH WALA CONSTRUCOR CALL HO GA.
    CNIC(){
        cnic = 1234;
        name = "ALI";
        age = 20;
        dob = 2000;
        city ="Lahore";
    }
}
class ProgramOne{
    public static void main(String[] args)
    {
        // AB HUM CNIC CLASS SAY OBJECTS BNAYEN GAY
        // AUR CONSTRUCTOR MA VALUES PASS KAREN GAY.
        CNIC cnicOne = new CNIC(1000,"Ahmed",30,1990,"Islamabad");
        cnicOne.showCnic();

        // AUR AB KOI VALUE PASS NAHI KRE GY TU YEH DEFAULT VALUE KO PICK KR LY GA.
        CNIC cnicTwo = new CNIC();
        cnicTwo.showCnic();
    }
}