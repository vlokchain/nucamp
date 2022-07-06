/*

[UNDERSTANDING SCOPE]

 Scope is the region of code where a variable exists and can be accessed
 JavaScript works with lexical scope: meaning scope of variable depends where it was declared

 There are 2 types of scopes
 1. Global Scope and,
 2. Local Scope = Block Scope & Function Scope

[BLOCK SCOPE]

 Variables declared using let and const have block scope and are only available within the code block they are declared in (including child blocks)

 Example of variable declared outside block scope:

 > if (true) {
    let testVar = 1;
 }

 > console.log(testVar);
 > = ERROR

 Inner child if block able to access value of variable as it was declared in parent block:

 > if (true) {
     let testVar = 1;
     if (true) {
         console.log(testVar);
     }
 }
 > = 1
 
 Declaring a variable in the child block would not work as parent block cannot see it:

 > if (true) {
     if (true) {
         let testVar = 1;
     }
     console.log(testVar);
     }
 
 Possible to declare variables with the same name in different code blocks (but avoid reusing variable names/can be confusing):

 > if (true) {
     let testVar = 1;
     if (true) {
         let testVar = 2;
         console.log("In the child block, testVar is", testVar);
     }
     console.log("In the child block, testVar is", testVar);
 }

 > = In the child block, testVar is 2
 > = In the child block, testVar is 1
 
[GLOBAL SCOPE]

 Global scopes are varialbes declared outside of any code block and are available everywhere.

 Pointers:
 1. It's best practice to declare variables where they will be used with local scope
 2. Avoid using global scope as much as possible. Can be confusing and lead to bugs
 3. Constants used in multiple places within code are often set as globals

[FUNCTION SCOPE]
 
 Function scope is another type of local scope but only applies to function blocks
 It is used with variables declared with the |var| keyword that is PRE-ES6

 Example of variable declared inside |if| block it is available outside the |if| block:

 > if (true) {
     var testVar = 1;
 }
 
 > console.log(testVar);
 > = 1

 Example of variable declared inside function block:

 > function testFn() {
     var testVar = 2;
 }

 > console.log(anotherTestVar);
 > = ERROR

[ARRAYS]
 
 Arrays are numerically indexed collections of values
 Can contain: strings, numbers, booleans and other arrays
 
[CREATING AN ARRAY]

 To use an array more than once store it in a variable, example:

 const groceryList = ["eggs", "coffee beans", "salad"];
 or
 let luckyNumbers = [7, 23, 99, 11];
 or
 let anArray = [7, "eggs", 99, "salad"];

[ACCESSING AND MODIFYING ARRAY ITEMS]
 
 Arrays are zero-indexed: it starts at 0
 Use index with brackets [] to modify array

 > const groceryList = ["eggs", "coffee beans", "salad"];
   groceryList [0]   = "bananas";
   groceryList [2]   = "soap";
 > const groceryList = ["bananas", "coffee beans", "soap"]

[ARRAY PROPERTY:LENGTH]
 
 Property length is the total count of items inside an array

 Count of items starts at 1
 Array index starts at 0

 Example:

 > const groceryList = ["eggs", "coffee beans", "salad"];
 > groceryList.length = 3

 The length of the array above is 3 but the index is 0 though 2.

 To access the last item in an array:

 > groceryList[groceryList.length-1]
 > = "soap"

 [ARRAY METHODS:POP() AND PUSH()]

 Pop and push are mutators and return a value
 
 pop() removes item from end of array:

 > const groceryList = ["eggs", "coffee beans", "salad"];
 > groceryList.pop();
 > ["eggs", "coffee beans"];

 push() adds one or more item to end of array:
 > const groceryList = ["eggs", "coffee beans", "salad"];
 > groceryList.push("milk");
 > ["eggs", "coffee beans", "salad", "milk"];

 [ARRAY METHODS:SHIFT() AND UNSHIFT()]

 Both are mutators and they return a value

 shift() removes item from beggining of array:

 > const groceryList = ["eggs", "coffee beans", "salad"];
 > groceryList.shift();
 > ["coffee beans", "soap"];

 unshift() adds one or more items to beggining of array"

 > const groceryList = ["eggs", "coffee beans", "salad"];
 > groceryList.unshift("milk");
 > ["milk", "eggs", "coffee beans", "salad"];

 [ARRAY METHODS:JOIN()]

 Not a mutator and returns string 

 join() takes all array items and returns a string with optional string argument that can be used as seperator (comma used as seperator if no argument provided):

 > const groceryList = ["bananas", "coffee beans", "soap"];
 > const groceries = groceryList.join();
 > grocieries = "bananas, coffee beans, soap"
 or
 > const groceryList = ["bananas", "coffee beans", "soap"];
 > const groceries = groceryList.join("--");
 > grocieries = "bananas--coffee beans--soap"

[ARRAY METHOD:INCLUDES()]
 
 Not a mutator and returns boolean value of true or false

 includes() used to check if item exists inside array:

 > const groceryList = ["bananas", "coffee beans", "soap"];
 > const itemInArray = groceryList.includes("soap");
 > itemInArray = true
 or
 > const groceryList = ["bananas", "coffee beans", "soap"];
 > const itemInArray = groceryList.includes("tea");
 > itemInArray = false

[ARRAY METHOD:INDEXOF()]

Not a mutator and returns index of item if it exists in array

 indexOf() checks if item is in array but instead of true or false it returns index of item if it exists in array:

 > const groceryList = ["bananas", "coffee beans", "soap"];
 > const itemIdx = groceryList.indexOf("soap");
 > itemIdx = 2

 if item does not exist it retuns value of number -1:

 > const groceryList = ["bananas", "coffee beans", "soap"];
 > const itemIdx = groceryList.indexOf("tea");
 > itemIdx = -1

[GENERATING RANDOM NUMBERS]

 |Math| is a built in global object in JavaScript used to access certain math-related functions called methods of the |Math| global object

[Math.random()]

 Math.random() generates a random number between 0 and 1
 The potential value of this number includes 0 but not 1

 To store a number inside a variable use:

 > let randomumber = Math.random();
 > randomNumber = 0.0573750
 or
 > randomNumber = 0.9999999

 To generate a number between 0 and a number higher than 1, multiply the random number
 
 Here is an example of a number generated between 0 thorugh 6 but not including 6

 > let randomumber = Math.random() * 6;
 > randomNumber = 0.0573750
 or
 > randomNumber = 5.9999999

[Math.floor()]

 Math.floor() removes all digits to right of the decimal point from a number

 Example:
 > const anInteger: Math.floor(3.14);
 > anInteger = 3

[Math.floor()&Math.random()]

 If you want a random number between 0 and 6:
 > const randomInteger = Math.floor(Math.random() * 6);
 > then the |randomInteger| could potentially be: 0, 1, 2, 3, 4, 5 but never 6

 If you want a random number between 1 and 6:
 > const randomInteger = Math.floor(Math.random() * 6) + 1;
 > then the |randomIteger| could potentially be: 1, 2, 3, 4, 5 but never 6



*/