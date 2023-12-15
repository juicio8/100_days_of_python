function getValidWord(s, dictionary) {
  let validWord = [];
  let obj = {};
  // loop and store each letter in s and their index in obj
  for (let i = 0; i < s.length; i++) {
    let key = s[i];
    if (!obj[key]) {
      obj[key] = [i];
    } else {
      obj[key].push(i);
    }
  }

  //check if words in dictionary is a substring of s
  for (let word of dictionary) {
    let i = 0;
    let min = -Infinity;
    let objCopy = JSON.parse(JSON.stringify(obj)); //really bad
    // maybe I should use string and then parse it instead of using array in the object, then I would be able to shallowCopy e.g 'e': '1,2'
    let first;
    let last;

    //check if each letter in a word is present in s and is a substring
    while (i < word.length) {
      let key = word[i];
      if (objCopy[key] && objCopy[key].length) {
        let index = objCopy[key].shift();

        if (index > min) {
          min = index;
          if (i === 0) first = index;
          if (i === word.length - 1) last = index;
        } else {
          break;
        }
      } else {
        break;
      }
      i++;
    }

    if (i === word.length) {
      let value = last - first;
      validWord.push({ value, word });
    }
  }
  console.log("before sort:", validWord);
  validWord.sort((a, b) => a.value - b.value);
  console.log("after sort:", validWord);
  console.log("answer: ", validWord[0].word);
  return validWord[0].word;
}

getValidWord("hgferyjkllkop", ["coffee", "coding", "happy", "hello", "hop"]); //answer should be hello
getValidWord("ocbms", ["rdnothix", "obms", "qhlrplaiv", "ms", "jaupx"]); //answer should be ms
