//
//javascript ES6 sample
//

//コンソールへの出力
console.log("output " + "text.");

//変数の利用
let value = 20;
console.log(value / 4);

//定数の利用
const feb = 2;
console.log(`Febraryは${feb}月です`);
console.log(feb === 2);
console.log(feb !== 2);

//条件分岐
if(value > 0){
    console.log(`${value}は正の数です。`);
}else if(value === 0){
    console.log(`${value}は0です。`);
}else{
    console.log("負の数です。");
}
switch(value){
    case 1:
        console.log("1");
        break;
    case 2:
        console.log("2");
        break;
    default:
        console.log("bigger than 2.");
        break;
}