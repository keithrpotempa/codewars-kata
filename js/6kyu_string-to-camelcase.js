// https://www.codewars.com/kata/517abf86da9663f1d2000003/train/javascript

const toCamelCase = (str) => {
  let camelCasedStr = "";
  const splitStr = str.split(/[\_\-]/);
  splitStr.forEach((word, index) => {
    const firstLetter = word.charAt(0);
    if (index === 0 && firstLetter === firstLetter.toLowerCase()) {
      camelCasedStr += word
    } else {
      camelCasedStr += firstLetter.toUpperCase() + word.slice(1);
    }
  })
  return camelCasedStr
}
