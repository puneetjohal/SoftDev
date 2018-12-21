//Generals - Puneet Johal, William Lu
//SoftDev1 pd7
//K30 -- Sequential Progression III: Season of the Witch
//2018-12-21

//----------------------------------PHASE III-----------------------------------

//getting elements and setting vars
var addButton = document.getElementById("b");
var list = document.getElementById("thelist");
var items = document.getElementsByTagName("li");
var heading = document.getElementById("h");
var ogHead = heading.innerHTML;

//adding event listeners

//event listeners for each list element
var listElementPriming = (listElement) => {
  //hovering over list elements changes the heading
  listElement.addEventListener( 'mouseover', function() {
    heading.innerHTML = this.innerHTML;
  });

  //not hovering over the list changes the headding back to original
  listElement.addEventListener( 'mouseout', function() {
    heading.innerHTML = ogHead;
  });

  //remove list elememt if clicked on
  listElement.addEventListener( 'click', function() {
    this.remove();
  });
}

//setting the event listeners for all original list items
for (i = 0; i<items.length; i++)
  listElementPriming(items[i]);

//clicking the button adds list elements
addButton.addEventListener( 'click', function() {
  var newListElement = document.createElement("li");
  newListElement.innerHTML = "WORD";
  listElementPriming(newListElement);
  list.appendChild(newListElement);
});

//----------------------------------PHASE IV-----------------------------------

//functions needed for buttons

//fibonacci
var fibonacci = (n) => {
  if (!n)
    return 0;
  if (n == 1)
    return 1;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

//factorial
var fact = (n) => {
  if (!n)
    return 1
  return n * fact(n-1);
}


//getting elements and setting vars
var fibButton = document.getElementById("fb");
var fibList = document.getElementById("fiblist");
var fibCount = 1;
var factButton = document.getElementById("factb");
var factList = document.getElementById("factlist");
var factCount = 1;

//adding event listeners

//clicking the fib button adds list elements with the next fib value
fibButton.addEventListener( 'click', function(){
  var newListElement = document.createElement("li");
  newListElement.innerHTML = fibonacci(fibCount);
  fibList.appendChild(newListElement);
  fibCount++;
});

//clicking the fact button adds list elements with the next fact value
factButton.addEventListener( 'click', function(){
  var newListElement = document.createElement("li");
  newListElement.innerHTML = fact(factCount);
  factList.appendChild(newListElement);
  factCount++;
});
