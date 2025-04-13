<html>

<!-- Name: Kevin Olenic -->
<!-- Username: ko19af -->
<!-- St#: 6814974 -->

<head>

<title>Product_1 - Ditto</title>

<meta name="viewport" content="width=device-width, inital-scale=1">

<script>

window.addEventListener('load',loadList)

</script>

</head>

<body>

<h1>Product_1 - Ditto</h1>

<img src="Images/Ditto.png" alt="Product_1">

<pre>
Details:

Price: $1899.99
LifeSpan: 800 years
Enviroment: any
Color(s): purple
Other Details: PolyMorph, prone to homicidal tendencies.

<!-- This button will add the product to local storage and activate other related functions-->
<button id="Button_Ditto" onclick="saveToStorage('Ditto')">Add To Wishlist</button>

</pre>

<p>
Watch our product in action, courtesey of Smosh videos.
</p>

<!-- This creates a viewable video on the webpage -->
<iframe width="420" height="345" src="https://www.youtube.com/embed/N_nXG8-yLbc">
</iframe>

<!-- This will show the object that are wishlisted and hold the buttons for adding and removing products -->
<pre id="wishList">Products In WishList:

</pre>
