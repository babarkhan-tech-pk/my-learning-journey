import java.util.Scanner;
class Person{
    String name;
    int age;
    Scanner Sc = new Scanner(System.in);
    void showRule(){
        System.out.println("Your are a person.");
    }
    void inputAge(){
        System.out.print("Enter your age : ");
        age = Sc.nextInt();
    }
    void inputName(){
        System.out.print("Enter your name : ");
        name = Sc.nextLine();
    }
    void showAge(){
        System.out.println("Your age is : " + age);
    }
    void showName(){
        System.out.println("Your name is : " + name);
    }
}

class Doctor extends Person{
    void showRule(){
        System.out.println("Your are a Doctor.");
    }
}

class Teacher extends Person{
    void showRule(){
        System.out.println("Your are a Teacher.");
    }
}

class ProgramTwo{
    public static void main(String[] args){
        Person p = new Person();
        p.showRule();
        Doctor d = new Doctor();
        d.showRule();
        d.inputName();
        d.showName();
        Teacher t = new Teacher();
        t.showRule();
        t.inputAge();
        t.showAge();
    }
}