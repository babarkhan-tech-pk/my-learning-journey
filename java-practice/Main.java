class Person{
    String name;
    int age;
    Person(String n, int a){
        name= n;
        age = a;
    }
}
class Employee extends Person{
    int salary;
    Employee(int s, String n, int a){
        super(n,a);
        salary = s;
    }
}
class SoftwareEngineer extends Employee{
    String programmingLanguage;
    SoftwareEngineer(String pl, String n, int a, int s){
        super(s, n, a);
        programmingLanguage = pl;
    }
    void show(){
        System.out.println("Name = " + name);
        System.out.println("Age = " + age);
        System.out.println("Salary = " + salary);
        System.out.println("Programming language = " + programmingLanguage);
    }
}
class Main{
    public static void main(String[] args) {
        SoftwareEngineer se = new SoftwareEngineer("Java", "Ali", 20, 3000);
        se.show();
    }
}