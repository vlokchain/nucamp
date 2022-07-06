// VARIABLES below are global scope and not block scope because used outside functions

let userGuess = ""; // must initialize after declaring variable + block scope variable only used in runGame function
let userNumber = 0;
let numTries = 0;


function runGame() {

const actualNumber = Math.floor(Math.random() * 5) + 1;  // mfloor removes digits right of decimal point and mrandom generates random number btwn 1-99
let rightAnswer = false;

    do {
        
        userGuess = prompt("I'm thinking of a number in the range 1 to 5.\n\nWhat is the number?"); // rmr prompt function always returns a string
        if (userGuess === null) {                                  // allows prompt dialog cancel button to work
            return;
        }
       
        userNumber = +userGuess;                                    // plus sign used as prefix to variable converts string to number
        numTries += 1;                                               // addition assignment operator used to increase value by 1
        rightAnswer = checkGuess(userNumber, actualNumber);          // checkGuess function being called within the runGame function
        
    } while (!rightAnswer);                                              // do while loop code block runs once before evaluating condition even if condition false

    alert("You got it! The number was " + actualNumber + ".\n\nIt took you " + numTries + " tries to guess correctly.");

}

function checkGuess(userNumber, actualNumber) {                          // function declaration w/ arguments userNumber + actualNumber
    let rightAnswer = false;

    if(isNaN(userNumber)) {                                            //isNaN is a JS function checks if value is valid number or not
        alert("You have not entered a number.\n\nPlease enter a number in the 1 to 5 range.");
    } else if ((userNumber < 1) || (userNumber > 100)) {
        alert("Please enter an integer in the 1-100 range.");
    } else if (userNumber > actualNumber) {
        alert("Your number is too large!")
    } else if (userNumber < actualNumber) {
        alert("Your number is too small.");
    } else {                                                           // will only run if condition is false
        rightAnswer = true;
    }
    return rightAnswer;                                                    // functions always return single value. use the |return| keyword to return a value
}
