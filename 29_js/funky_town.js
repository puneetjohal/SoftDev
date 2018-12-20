var fibonacci = (n) => {
  if (!n)
    return 0;
  if (n == 1)
    return 1;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

var gcd = (a, b) => {
  if (!b)
    return a;
  return gcd(b, a % b); //reverses the order of a and b
}

var students = ["luke", "leia", "han", "r2d2", "c3po", "anakin", "obi-wan", "yoda"];

var randomStudent = () => {
  var index = Math.floor(Math.random() * students.length);
  return students[index];
}

//--------------------------------K29 Functions---------------------------------

//fibonacci
var fibButton = function() {
  var p_fib = document.getElementById("retFib");
  p_fib.innerHTML = fibonacci(30);
  console.log(p_fib.innerHTML);
}

//gcd
var gcdButton = function() {
  var p_gcd = document.getElementById("retGcd");
  p_gcd.innerHTML = gcd(63,14);
  console.log(p_gcd.innerHTML);
}

//randomStudent
var randButton = function() {
  var p_rand = document.getElementById("retRand");
  p_rand.innerHTML = randomStudent();
  console.log(p_rand.innerHTML);
}

//Event Listeners

var button_fib = document.getElementById("fib");
button_fib.addEventListener( "click", fibButton );

var button_gcd = document.getElementById("Gcd");
button_gcd.addEventListener( "click", gcdButton );

var button_rand = document.getElementById("rand");
button_rand.addEventListener( "click", randButton );
