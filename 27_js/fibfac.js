// Team Ruff: Ivan Yeung, Andrew Piatetsky
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2023-04-04t
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn

// fact
function fact(a) {
    if (a == 1) {
        return a
    }
    return (a*fact(a-1))
}

// fib
function fib(a) {
    if (a < 2) {
        return a
    }
    return (fib(a-1)+fib(a-2))
}

// ;(fact 1) ;"...should be  1"
// (fact 2) ;"...should be  2"
// (fact 3) ;"...should be  6"
// (fact 4) ;"...should be  24"
// (fact 5) ;"...should be  120"

// ;(fib 0) ;"...should be  0"
// ;(fib 1) ;"...should be  1"
// ;(fib 2) ;"...should be  1"
// ;(fib 3) ;"...should be  2"
// ;(fib 4) ;"...should be  3"



//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
