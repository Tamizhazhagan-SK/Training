let arrays = [[[10,20,30],[40,50,60]],[[70,80,90],[100,110,120]]]


sum=0;
for(let i=0;i<arrays.length;i++){
    for(let j=0;j<arrays[i].length;j++){
        for(let k=0;k<arrays[i][j].length;k++){
        sum+=arrays[i][j][k];
    }
}
}

console.log(sum);