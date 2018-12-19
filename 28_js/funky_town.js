//Generals - William Lu, Puneet Johal
//SoftDev1 pd7
//K28 -- Sequential Progression
//2018-12-19

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
