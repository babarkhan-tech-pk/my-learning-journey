class Person{
    private String name;
    final int age = 20;
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }
    void show(){
        System.out.println("Name is " + name + " and Age is " + age);
    }
    static void print(String a){
        System.out.println(a);
    }
}
class Learn{
    public static void main(String[] args){
        Person P1 = new Person();
        // P1.name = "ALI"; ERROR ACCESING PRIVATE VARIABLE
        P1.setName("Babar");
        String n = P1.getName();
        P1.show();
        P1.print(n);
    }
}