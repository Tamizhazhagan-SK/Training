arr1 = [10,4,10,3,5,6,7,3,4,7,8,9,10,4,5,2,1,10,5,6,7,3,5];


//using .reduce()

// const count = arr1.reduce((arr, arr1) => {
// arr[arr1] = (arr[arr1] || 0) + 1;
// return arr;
// }, {});

//using Map

let count={};
 
for(let num of arr1){
    count[num]=(count[num] || 0) + 1;
}

console.log(count);