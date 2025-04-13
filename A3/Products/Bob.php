<html>

<!-- Name: Kevin Olenic -->
<!-- Username: ko19af -->
<!-- St#: 6814974 -->

<head>

<title>Product_5 - Bob</title>

<meta name="viewport" content="width=device-width, inital-scale=1">

<script>

window.addEventListener('load',loadList)

</script>

</head>

<body>

<h1>Product_5 - Bob</h1>

<img src="Images/Bob.png" alt="Product_3">

<pre>
Details:

Price: $499.99
LifeSpan: ? weeks (have yet to see one die)
Enviroment: all terrain
Color(s): blue
Other Details: single eye, no brain, attracted to jello,
smells like ham, easily confused, always hungry.

<!-- This button will add the product to local storage and activate other related functions-->
<button id="Button_Graboid" onclick="saveToStorage('Graboid')">Add To Wishlist</button>

</pre>

<!-- This will show the object that are wishlisted and hold the buttons for adding and removing products -->
<pre id="wishList">Products In WishList:

</pre>
