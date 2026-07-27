{
let a = 123.123;
let b = 123;

let c = "123.123";
let d = "123";


let e = true;
if (e=true){
    e=1;
}
else{
    e=0;
}

// let e = true;
// e = e ? 1 : 0;

x = a+b+parseFloat(c)+parseInt(d)+e
console.log(x.toFixed(2));

}

// docker run --rm -v ${PWD}:/app -w /app node node index.js 
// use this command to use the docker image for javascript and node.js