// //inheritance
// class parent{
//     phone(){
//         console.log("have nokia")
//     }
// }
// class child extends parent{

// }
// var ch=new child()
// ch.phone()




//inheritance
class parent{
    m1(){
        console.log("have nokia")
    }
}
class child extends parent {
    m2(){
        console.log("m2 method")
    }
}

class subchild extends child{
    m3(){
        console.log("m3 method")
    }

}
var ch=new subchild()
ch.m3()
ch.m2()
ch.m1()