function runGame(){
/**** A - GENERATE RANDOM NUMBER BTWN 1-100 & STORE AS VARIABLE ****/


    // B - Always initialize values when you declare them otherwise they'll be undefined
    let guessString = "";
    // B - Stores the number of guess(s) from player
    let guessNumber = 0;
    // B - This variable holds boolean value of true or false if guess was correct or not
    let correct = false;
    // D - Initialize varible to keep track number of guess(s) tried by player
    let numTries = 0;

    // A - Creates random noninteger number between 0-99.99 and stores as variable
    const randomNumber = Math.random() * 100;
    // A - Creates an integer (whole number) from the randomNumber call. Output = 0-99
    const randomInteger = Math.floor(randomNumber);
    // A - Creates an integer between 1-100
    const target = randomInteger + 1;
    // A - The code above can be summarized in one line: [ const target = Math.floor(Math.random * 100) + 1 ]


/**** B - GET GUESS FROM PLAYER & STORE AS VARIABLE ****/


    do {
        // B - Prompts player with the text in " brown quotes." Escape sequence =\n\n
        guessString = prompt("I'm thinking of a number from 1 to 100.\n\nWhat is the number?");
        // B - Turns the string into a number
        guessNumber =+guessString;
        // D - Adds 1 every time the loop repeats to number of player guess(s)
        numTries += 1;
        // B - Correct will have a return value of a function called checkGuess with two arguments (function written in section )
        correct = checkGuess(guessNumber, target);
        // B - This allows the loop to repeat as long as answer is false
    } while (!correct);

        //D - Prompts player target was guessed
    alert("You got it! The number was " + target + ".\n\nIt took you " + numTries + " tries to guess correctly");
}

/**** C - SCRIPT CHECKS GUESS ALONG WITH SEVERAL CONDITIONS***/


    // C - Declares checkGuess funtion with two parameters
function checkGuess(guessNumber, target) {
    // C - Sets a local variable of correct ()
    let correct = false;
    
    // C - Checks if the value is a valid number or not
    if (isNaN(guessNumber)) {
    // C - Prompts player with the text in "brown quotes."
        alert("You have not enetered a number.\n\nPlease enter a number in the 1-100 range.");
    // C - Else if checking two conditions
    } else if ((guessNumber < 1) || (guessNumber > 100)) {
    // C - Prompts player with the text in "brown quotes"
        alert("Please enter an integer in the 1-100 range.");
    // C - Checks if guess number is greater or less than the target number
    } else if (guessNumber > target) {
    // C - If true prompts player with the text in "brown quotes"
        alert("Your number is too large.");
    // C - Checks if guess number is greater or less than the target number
    } else if (guessNumber < target) {
    // C - If true prompts player with the text in "brown quotes"
        alert ("Your number is too small");
    } else {
    // C - Set value of correct to true. Only block on the if statement that causes carrect to be true
        correct = true;
    }
    // C Returns value of correct. Value runs back to run game function where checkGuess was called as the return value from checkGuess
    return correct;
}
