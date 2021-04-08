class Student{
    constructor(name,age){
        this.name=name;
        this.age=age
    }
    printStudent(){
        console.log(this.name);
        console.log(this.age);
    }
}
var obj=new Student("Aravind",23)
obj.printStudent()




