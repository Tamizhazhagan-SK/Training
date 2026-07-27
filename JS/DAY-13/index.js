console.log("Hello, World!");

var oldStyle = "I am new to Javascript(forgot the syntax :D)"



let a = 1000;
let b = 234;
let c = a + b;

let ok = true;

let names = "TamizhSK";
names = "Harris";

// let name = "TamizhSK, A optimist";

// var oldStyle = "Hi, I am new to Javascript(forgot the syntax :D)"

console.log("Hi,"+ "I'm " + names,oldStyle);

console.log("=================================================");

console.log(c);

console.log("=================================================");

const PI = 3.14;
console.log(PI);
console.log("=================================================");

console.log(10/0);
console.log("=================================================");

let div = 0;
console.log(a/div);

console.log("=================================================");

let val;

console.log(val);
console.log("=================================================");

const largeInt = 32434234234234234234234234234234324234234234234234234234234;

console.log(largeInt);

let age = 24;

let price = 123.123

console.log(typeof largeInt, typeof age, typeof price);

let x = 10;
let y = "20";

console.log(typeof a);
console.log(typeof b);


console.log(x+y);
console.log("=================================================");

let person = null; //understands as object

let managers;

let employee = []; //understands as object : Array

let students = {}; //understands as object : Map

let company = {
    "name":"BTI",
    "location":"Chennai",
    "email":"bti@gmail.com",
    "phone number":9876543210
}


console.log(typeof person);
console.log(typeof managers);
console.log(typeof employee);
console.log(typeof students);
console.log(typeof company);
console.log("=================================================");
let str1 = "123";

console.log(str1++); //string is converted to num and performs unary operation

console.log(+str1);  //it should increment but no; it is not creating any errors

let ab = 10;
let ba = "10";

{
if (ab==ba){ //compares the data; not the type
    console.log("equal");
}
else{
    console.log("not equal");
}
}

{
if (ab===ba){ //compares the data and also the type
    console.log("equal");
}
else{
    console.log("not equal");
}
}


console.log("=================================================");


{
if (isNaN(ab)==true){
    console.log("true");
}
else{
    console.log("false");
}

  str2 = "2344.8fcuk"  //when starting with number; it will show the correct numbers
    let pf = parseFloat(str2)
    console.log(typeof pf, pf)
 
    let pi = parseInt(str2)
    console.log(typeof pi, pi)

  str3 = "d2344.8fcuk"  //when starting with character; it will show the data type
    let pf1 = parseFloat(str3)
    console.log(typeof pf1, pf1)
 
    let pi1 = parseInt(str3)
    console.log(typeof pi1, pi1)

str4 = "2344_.8fcuk"  //when starting with character; it will show the data type
    let pf2 = parseFloat(str4)
    console.log(typeof pf2, pf2)
 
    let pi2 = parseInt(str4)
    console.log(typeof pi2, pi2)



}


console.log("=================================================");


let nums = [10,20,30,40,50];

let array2d = [[10,20],[30,40],[50,60]];

console.log(nums);
console.log("=================================================");
console.log(array2d);

nums.push(60);
console.log("=================================================");

console.log(nums);

array2d.push([70,80]);
console.log("=================================================");
console.log(array2d);


let sum = 0;
for (let i=0; i<nums.length;i++){
    sum+=nums[i];
}
console.log("=================================================");
console.log("sum: " + sum);

nums.forEach(function(value){
    sum+=value;
    console.log(value);
});


console.log("sum: " + sum);

console.log("=================================================");

let doubles = nums.map(n=>n*2);
console.log(doubles);















































































