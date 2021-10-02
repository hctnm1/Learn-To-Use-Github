// Question1: Write a function which generates a secret code from a given string, by shifting characters of alphabet by N places.

const alphabets = [
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z"
];
const encodeString = (string, num) => {
  const encodedString = [];
  for (let i = 0; i < string.length; i++) {
    encodedString.push(alphabets[alphabets.indexOf(string[i]) + num]);
  }
  return encodedString.join("");
};
// console.log(encodeString("javascript", 2));
