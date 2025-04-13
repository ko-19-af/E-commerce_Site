// Name: Kevin Olenic
// Username: ko19af
// St#: 6814974

// this function saves an item to the local storage
// and creates a p to show the element is in the list
// and creates the remove button
function saveToStorage(product){
	
	// if their is a p with the "none" tag in the wishlist
	if(document.getElementById("none") !== null){
		
		// remove it
		document.getElementById("none").remove();
	}
	
	// add it to local storage
	localStorage.setItem(product, product);

	// remove product from server side storage
	serverList("add",product);

	// get the ith key from local storage and assign it as the text for variable t (text)	
	var t = product;
			
	// create paragraph element
	let p = document.createElement('p');
			
	// set the contents to variable t
	p.innerHTML = t;
			
	// this sets the id of the p to the product
	p.setAttribute('id',t);
			
	// append the item to the body of the document
	document.getElementById("wishList").append(p);
			
	// button still needs to be finished
	let btn = document.createElement("button");
			
	btn.innerHTML = "Remove From Wishlist";
			
	// add an event listener to the button to remvoe the desired product from local storage
	btn.addEventListener("click", function(){removeFromStorage(t)});
			
	// this adds the button to the pre
	document.getElementById(t).appendChild(btn);
	
	// disable adder button when product added to local storage
	document.getElementById("Button_" + product).disabled = true;
	
	// add class to button
	document.getElementById("Button_" + product).classList.add("unclickable");
}

function removeFromStorage(product){
	
	if(localStorage.getItem(product)){
	
		// remove from local storage
		localStorage.removeItem(product);

		// remove product from server side storage
		serverList("remove",product);

	
		// remove item from wishlist
		document.getElementById(product).remove();
	
		// re-enable adder button when product removed from local storage(if it exist on the page)
		if(document.getElementById("Button_" + product) !== null){
			// re-enable the button
			document.getElementById("Button_" + product).disabled = false;
			// remove class from button
			document.getElementById("Button_" + product).classList.remove("unclickable");
		}
	}
	
	else{
		// do nothing
	}
}

// load the printable wishlist
function load(){
		
	// if no elements in local storage
	if(localStorage.length === 0){
		
		// create paragraph element
		let p = document.createElement('div');
	
		// set the contents to variable t
		p.innerHTML = "There are no items In your Wishlist";
	
		// this sets the id of the p to the product
		p.setAttribute('id',"none");
	
		// append the item to the body of the document
		document.getElementById("wishList").append(p);
	}

	else{

		for(var i = 0; i < localStorage.length; i++){
		

			// get the ith key from local storage and assign it as the text for variable t (text)	
			var t = localStorage.getItem(localStorage.key(i));
			
			// create paragraph element
			let p = document.createElement('div');
		
			// set the contents to variable t
			p.innerHTML = t;
			
			// this sets the id of the p to the product
			p.setAttribute('id',t);
			
			// append the item to the body of the document
			document.getElementById("wishList").append(p);
		}
	}
}


// this function loads the items from local storage for the wish list page
function loadList(){
		
	// if no elements in local storage
	if(localStorage.length === 0){
		
		// create paragraph element
		let p = document.createElement('p');
	
		// set the contents to variable t
		p.innerHTML = "There are no items In your Wishlist";
	
		// this sets the id of the p to the product
		p.setAttribute('id',"none");
	
		// append the item to the body of the document
		document.getElementById("wishList").append(p);
	}
	
	// if there are elements in local storage
	else{

	
	// for every element in local storage
	for(var i = 0; i < localStorage.length; i++){
		
		(function(){

			if(localStorage.length == 0){
				// do nothing
			}

			else{

				// get the ith key from local storage and assign it as the text for variable t (text)	
				var t = localStorage.getItem(localStorage.key(i));
			
				// create paragraph element
				let p = document.createElement('p');
			
				// set the contents to variable t
				p.innerHTML = t;
			
				// this sets the id of the p to the product
				p.setAttribute('id',t);
			
				// append the item to the body of the document
				document.getElementById("wishList").append(p);
			
				// create button
				let btn = document.createElement("button");
			
				btn.innerHTML = "Remove From Wishlist";
			
				// add an event listener to the button to remvoe the desired object from local storage
				btn.addEventListener("click", function(){removeFromStorage(t)});
				
				// this adds the button to the pre
				document.getElementById(t).appendChild(btn);			
			
				// if the buttons are on the page when loading
				if(document.getElementById("Button_" + t) !== null){
			
					// disable adder button
					document.getElementById("Button_" + t).disabled = true;
			
					// add class to button
					document.getElementById("Button_" + t).classList.add("unclickable");
				}
			}
			
			}());
		}
	}
}

// function that add/removes files
function serverList(action, product){
	call = new XMLHttpRequest();
	call.open("GET","utils.cgi?id=" + action + "&product=" + product, true);
	call.send();
}

// function to copy localStorage wishlist to serverside wishlist
function serverSave() {
	for (i = 0; i < localStorage.length; i++) {
		serverList("add",localStorage.key(i));
	}
}

