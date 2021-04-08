class=>blueprint,desgin pattern,plan,temp
object=>realworld entity







class pesron {

    setperson(name, age) {

        this.name = name;

        this.age = age

    }
    printperson() {
        console.log(this.name);      //this is used for finding instant variable
        console.log(this.age);

    }
}
var obj = new person()
obj.setperson("karthika", 23)
obj.printperson()


class Student{

    setStudent(name,age){
        this.name=name;
        this.age=age
    }
    printStudent(){
        console.log(this.name);
        console.log(this.age);
    }
}
var obj = new Student()
obj.setStudent("Aravind", 23)
obj.printStudent()





