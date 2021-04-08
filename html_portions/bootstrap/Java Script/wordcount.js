var text="hello hi how hello"
var words=text.split(" ")
console.log(words);

for(let i of words)
{
    console.log(i)
}
console.log(" ");
var dict={}
for(let word of words){
    if(word in dict)
    {
        dict[word]+=1
    }
    else{
        dict[word]=1
    }
}
console.log(dict);