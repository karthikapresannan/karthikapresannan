var student={sid:100,name:"achu",course:"Bcom",total:100}
console.log(student["name"]);
console.log(student["total"]);
console.log("gender" in student);
console.log(" ");
//iteration
for(let k in student)
{
    console.log(k+"->"+student[k]);
}