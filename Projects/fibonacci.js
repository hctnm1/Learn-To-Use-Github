// The Fibonacci Sequence.

var sequence = [];
var num = 0;
function fibonacci(times) {
    while (sequence.length < times) {
        if (sequence.length <= 2) {
            sequence.push(num);
            num++;
        } else {
            sequence.push(sequence[sequence.length - 1] + sequence[sequence.length - 2]);
        }
    }
    console.log(sequence);
}
fibonacci(100);