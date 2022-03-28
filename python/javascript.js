console.log(1);
console.log(2);
console.log(3);

// Number
console.log(1);
console.log(1.2);
console.log(1 + 1);
console.log(2 - 1);
console.log(2 * 2);
console.log(6 / 2);
console.log(Math.pow(3, 2));
console.log(Math.random());

// String
console.log('Hello');
console.log('"Hello"');
console.log(`Hello
World
`);
console.log('Hello'.length);
console.log('Hell world'.replace('Hell', 'Hello'));

// Array
let member = ['egoing', 'duru', 'taeho'];
console.log(member[0]);

// Variable
let a = 1;

// Input
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.on('line', line => {
    console.log('가격: ', line);
    let 가격 = line;
    let 부가가치세 = 0.1;
    console.log(가격 * 부가가치세);
    rl.close();
});

rl.on('close', () => {
    process.exit();
});
