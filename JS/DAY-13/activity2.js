let nums = [1,2,3,4,5,6,7,8,9,10];

let evennums = nums.filter(nums => nums%2===0);

let findnums = nums.find(nums => nums === 4);

let oddnums = nums.some(nums => nums%2===1);

const total = nums.reduce((sum, num) => {return sum + num;}, 0);


console.log(evennums);
console.log(findnums);
console.log(oddnums);
console.log(total);


// docker run --rm -v ${PWD}:/app -w /app node node index.js 
// use this command to use the docker image for javascript and node.js