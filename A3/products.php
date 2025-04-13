#!/usr/bin/php-cgi

<html>
<!-- Name: Kevin Olenic -->
<!-- Username: ko19af -->
<!-- St#: 6814974 -->

<body>

<!-- This sets the title of the page -->
<title>Products</title>

<?php

include 'top.php';
include 'bottom.php';

?>

<head>

<title>Products</title>

<meta name="viewport" content="width=device-width, inital-scale=1">

<!-- this sets a specefic style for this page -->
<style>

img:hover{
outline: 4px dashed blue;
}

</style>

<script>

window.addEventListener('load',loadList)

</script>

</head>

<body>

<!-- This will show the object that are wishlisted and hold the buttons for adding and removing products -->
<pre id="wishList">Products In WishList:</pre>

<pre>
Here is a selection of our wonderful products, click on the image of
a product you are interested in to learn more about it.

</pre>

<h1>Product_1 - Ditto</h1>

<!-- This creates a clickable image that leads to the corresponding product -->

<a href="product.php?id=Ditto">

<img src="Images/Ditto.png" alt="Product_1">
</a>

<pre>
Ditto is our number one best seller as it is capable of taking the form of
any living creature it sees making it a higly adaptable and desirable product.

<button id="Button_Ditto" onclick="saveToStorage('Ditto')">Add To Wishlist</button>

</pre>

<h1>Product_2 - Xeno</h1>

<!-- This creates a clickable image that leads to the corresponding product -->

<a href="product.php?id=Xeno">

<img src="Images/Xeno.png" alt="Product_2">
</a>

<pre>
The Xeno is our most lethal product to date with its razor sharp teeth, scorpion like tail,
acid blood and high level of intelligence this model is also capable of traversing any
terrain making it an ideal hunting and killing machine.

<button id="Button_Xeno" onclick="saveToStorage('Xeno')">Add To Wishlist</button>

</pre>

<h1>Product_3 - Graboid</h1>

<!-- This creates a clickable image that leads to the corresponding product -->

<a href="product.php?id=Graboid">

<img src="Images/Graboid.png" alt="Product_3">
</a>

<pre id="Graboid">
The Graboid model is our latest in subterranian monsters it is capable of travelling at
high speeds, and can feel the seismeic activity of its prey, making it our most effective
subterranian hunter.

<button id="Button_Graboid" onclick="saveToStorage('Graboid')">Add To Wishlist</button>

</pre>

<h1>Product_4 - Kraken</h1>

<!-- This creates a clickable image that leads to the corresponding product -->

<a href="product.php?id=Kraken">

<img src="Images/Kraken.png" alt="Product_4">
</a>

<pre>
The kraken is our largest model to date, capable of sinking entire ships with
minimal effort, and eating entire schools (not fish schools actual schools provided
they are close to the ocean).

<button id="Button_Kraken" onclick="saveToStorage('Kraken')">Add To Wishlist</button>

</pre>

<h1>Product_5 - Bob</h1>

<!-- This creates a clickable image that leads to the corresponding product -->

<a href="product.php?id=Bob">

<img src="Images/Bob.png" alt="Product_4">
</a>

<pre>
Bob is our most durable product as it can sustain any type of damage and
maintain his original shape and consistency, despite this product's
indestructible nature it is easily confused and constantly hungry and will
eat whatever he can get his hands on.

<button id="Button_Bob" onclick="saveToStorage('Bob')">Add To Wishlist</button>

</pre>


</body>
</html>
