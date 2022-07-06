/*

[JAVASCRIPT BASICS]

[VARIABLES]

 Variables can have data types: (1) Numbers, (2) String, (3) Boolean, (4) Null, (5) Undefined

 Numbers = a positive/negative or decimal number
 String = characters inside quotes
 Boolean = true or false w/out quotes
 Null = empty/non-existent/intentional absence of a value
 Undefined = given to a declared variable but not initialized

[VARIABLE DECLARATION: LET]

 To declare/create a variable use the |let| keyword and terminate it with a semicolon.
 If a variable is terminated without a value it is considered undefined.
 
 Example: let myScore;

[VARIABLE INITIALIZATION/ASSIGNMENT:]

 The first time you assign a value to a variable after declaring it you are |initializing| the variable

 Example: let myScore = 99;

[VARIABLE REASSIGNMENT]

 To reassign the value of a variable use the variable name only and assign it a new value

 Example: let myScore = 99; *here it is declared and initialized
              myScore = 100; *here it is reassigned using the variable name only

[VARIABLE DECLARATION: CONST]

 Another way to declare a variable is by using the |const| keywork

 Rule #1: You must initialize a const variable after declaring it
 Rule #2: You cannot reassign a const variable

 Example: let myName = "Abraham"

[CONST VS LET]

 Use the |let| keyword for variables that can be reassigned
 Use the |const| keyword for varaible than cannot be reassigned

[CALLING A FUNCTION]

 To call a function use the |function| name followed by () and ;
 Defining a function does not call a function
 You must call a function (like with the onclick event handler)

 A function declaration look like this:

 function sayHello() {
            code to run;
 }

 A function call looks like this:

 sayHello();

[FUNCTION PARAMENTERS + ARGUMENTS]

 A function declaration with parameter |word| looks like this:

 function sayWord(word) {
    alert(word);
 }

 When the function above is called it is declaring a local variable based on its parameter
 The local variable exists only within the function
 You do not need to declare with let or const
 Does not need to be unique to the document
 Cannot be accessed from outside the function block

 A function call w/ argument of |turnip| looks like this:

 sayWord("Turnip");

 Once a function is called the variables from the parameter list determine the value from the argument list.

 To take a look at another function declaration with parameters and its function call see below:

 function getArea(width, length) {
    return width*length;
 }

 getArea(3, 4); 
 alert(area);

 the yielding result would bounce back with "12"

[FUNCTION RETURN VALUES]

 Functions always return a single value.
 If you do not provide that value it returns the value of undefined

 To return a value use the |return| keyword followed by the value.
 This lets you call the function and assigns the return value to a variable

 function getArea(width, length) {
     return width*length;
 }

 let area = getArea(3, 4);



*/