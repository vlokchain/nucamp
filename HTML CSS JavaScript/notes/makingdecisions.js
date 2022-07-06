/* 

[IF STATEMENTS]
 
 An if statement evaluates a condition and excecutes a block of code

 Example of syntax:

 if (condtion) {
    code to run if condition is true
 }
 Example of an if statement:

 if(password === "SuperSecrePassword") {
     alert("Your password is correct");
 }

 The breakdown of the if statement above:

 The if statement is followed by the condition |password| to be evaluated inside ()
 The triple equals operator compares the value stored inside this variable named password and the string "SuperSecretPassword"
 It returns a boolean value of true if they match
 It returns a false if they do not match

[IF/ELSE STATEMENTS]

 If statements can also have an |else| block following the |if| block
 The |else| block will only run if the condition is false

 Example:

 if(password === "SuperSecretPassword") {
     alert ("Your password is correct!");
     else {
     alert ("Your password is incorrect");
 }

[IF/ELSE STATEMENTS]

 To test more conditions in the same statement use |else if|
 Rule #1 each if statement can only have one if block sand one else block
 Rule #2 you can have as many |else if| blocks in between them

 Example:

 if(color === "red") {
     hexColorCode = "#FF0000";
 } else if (color === "black") {
     hexColorCode = "#000000";
    else if (color === "white") {
     hexColorCode = "#ffffff";
    else {
     hexColorCode = null;
    }
 }

[TRUTHY & FALSY]

 IF conditions operate based on truthy and falsy and do not depend on false or true conditions alone.

 These values are falsy: (1) false, (2) undefined, (3) null, (4) 0, (5) -0, (6) NaN, (7) "" an empty string

 These values are truthy: (1) 3,(2) -3,(3) "0",(4) any non-empty string

[OPERATORS & OPERANDS] 

 This is how an assignment operator is composed: x = 5;

 The operator is      ---> x = 5;
 The left operand is  ---> x
 The right operand is ---> 5

 An operator with 1 left and 1 right operand = binary operator
 An operator with 1 operand                  = unary operator
 An operator with 3 operands                 = ternary operator

[USING MULTIPLE OPERATORS]

 More than one operator can be used in a single statement: x = y + 3
 You can have multiple operators in the same operand:      x = y + 3 * 5

 Rule #1 They follow PEMDAS sequence

[COMPARISON OPERATORS]

 All comparison operators are binary operators
 They compare two values and return a Boolena value of true or false
 There are two types of comparison operators: equality and relational

 Rememeber:
 Javascript converts a values type without explicitly requesting it when using | == | a loose equality/equality/double equals operator
 Type coercion = implicit value type conversion, value type converted without explicit request

 === | strict equality/identity/triple equals operator ---> compares operands value and type
 ==  | loose equality/equality/double equals operator  ---> compares operands value + auto performs type coercion when types do not match
 !== | strict inequality/nonidentity operator          ---> compares operands value and type and + states not equal to value or not equal type
 !=  | loose inequality/inquality operator             ---> states not equal + auto performs type coercion 

 Examples:

 5 === "5"          --> false -> two different data types cannot strictly equal one another: the left operand is a number and the right operand is a string
 5 ==  "5"          --> true  -> the double equals operator will coerce the two value data types to match each other
 
 null === undefined --> false
 null ==  undefined --> true

 5 !== "5"          --> true -> the number 5 does not equal a string of |"5"|

[RELATIONAL OPERATORS]

 With number operands, relational operators work the same as in mathematics.

 < less than ,
 <= less than or equal to,
 > greater than,
 >= greater than or equal to

 String operands are compared in lexicographical order: A is lower + Z is higher
 When string character match compare the next character

 "a"        < "z"        ---> true
 "aardvark" < "anteater" ---> false
 "peony"    > "obeo"     ---> true
 "eefffgg"  > "eefffgh"  ---> false

[LOGICAL OPERATORS]

 There are 3 logical operators in Javascript: (1) &&, (2) ||, (3) !

 && and || are binary: x && y or x || you

 ! is unary: !x

[LOGICAL AND + OR + NOT + DOUBLE NOT OPERATORS]

 Using logical operators write an if statement for:

 A ticket price of $20 for ages over 12 and under 16
 A discounted ticket price of $10 for ages 12 and under or 65 and over 
 
 The if statement for the statement above would look like this:

 if ((age > 12) && (age <65)) {
     ticketPrice = 20;
 }else {
    ticketPrice = 10;
 }

 && = tests if the left operand is truthy or falsy
 If = falsy         --> it returns left operands value
 If = truthy        --> it returns right operands value
 If = both truthy   --> truthy it returns last truthy Value
 If = either falsy  --> falsy it retuns first falsy value

 
 || = tets if the left operand is truthy or falsy
 If = falsy         --> it returns right operands value
 If = truthy        --> it returns left operands value
 If = both truthy   --> it returns first truthy Value
 If = neither falsy --> it retuns last falsy value
 
 ! is a unary operator = has one only one operand
 ! = always returns true or false
 returns false when operand value is truthy
 returns true  when operand value is falsy|

 !type coerces operand to a boolean value then negates the value
 use parenthesis to apply to entire operand

 Boolean() can be used to convert values to boolean data type: Boolean(123) : true
 
 or,
 
 use       ! to coerce a value to boolean and negate it
 then use !! to reverse the negation
 _________________________________________
 Expression               | Return Value  |
 _________________________________________|
 true      && "true"      | "true"        |
 "true"    && true        | true          |
 true      && null        | null          |
 undefined && "true"      | undefined     |
 ""        && null        | ""            |
 null      && undefined   | null          |
 _________________________________________|

 _________________________________________
 Expression               | Return Value  |
 _________________________________________|
 true      || "true"      | true          |
 "true"    || true        | "true"        |
 true      || null        | true          |
 undefined || "true"      | undefined     |
 ""        || null        | null          |
 null      || undefined   | undefined     |
 _________________________________________|

 _________________________________________
 Expression               | Return Value  |
 _________________________________________|
 !true                    | false         |
 !false                   | true          |
 !"cat"                   | false         |
 !(3 > 2)                 | false         |
 !"nucamp" === true       | false         |
 !("nucamo" === true)     | true          |
 _________________________________________|

 REFER TO WEEK 3 EXCERCISE "theater1.html" FOR A BREAKDOWN OF JAVASCRIPT BASICS AND MAKING DECISIONS

[MORE OPERATORS]

 +=    ---->    addition assignment operator
 -=    ---->    subtraction assignment operator
 ++    ---->    increment operator
 --    ---->    decrement operator

 Addition/Subtraction Assignment Operator Example:

 > let x = 1

 > x + 2;
 < x = 3

 > x += 2;
 < x = 5

 > x -+ 2;
 < x = 3

 Increment/Decrement Assignment Operator Example:

 > let y = 1

 > ++y;
 < y = 2

 > --y;
 < y = 1

 > y++    ----> returns value before increment
 < y = 1 

 > y--;
 < y = 2  ----> returns value before decrement

[WHILE LOOPS]

 While loops evaluate a condition that you set
 When condition is true it will continue to loop
 Something must cause condition to be false or loop will continue indefinetly

 Example:

 > let i = 0

 > while (i < 5) {
     i += 1;
     console.log("This is iteration #" + i);
 }

 This is iteration #1
 This is iteration #2
 This is iteration #3
 This is iteration #4
 This is iteration #5

 The code ran 5 times each time incrementing the value by one 
 When the value of the variable was no longer less than 5 the while condition evaluated as false and exited the loop 

[DO WHILE LOOP]

 While loop     = condition evaluated first, if condition false code block does not run
 Do while loop  = code block runs once before evaluating condition

 Example of while loop where code block does not run:

 Code will not run as 5 is not < 5.

 > let i = 5

 > while (i < 5) {
     i += 1;
     console.log("This is iteration #" + i);
 }

 Example of do while loop where code block runs once:
 Condition is false but code block will run one time

 > do {
     i += 1;
 } while (i < 5);
     console.log("This is iteration #" + i);
 
 This is iteration #6

 Example of do while loop where code block loops:
 Code block will continue to loop until user answers "yes"

 > let answer = "";

 > do {
     answer = prompt("Do you like chocolate?")
 } while (answer !== "yes");















*/ 