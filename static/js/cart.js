var updateBtnsGrid = document.getElementsByClassName('update-cart-grid');
console.log("gridCollection:", updateBtnsGrid)
for (i = 0; i < updateBtnsGrid.length; i++) {
    updateBtnsGrid[i].addEventListener("click", function(){
        var albumId = this.dataset.album
        var action = this.dataset.action
        console.log('albumId:', albumId, 'action:', action)
        console.log('USER', user)

        if(user == 'AnonymousUser'){
            addCookieItem(albumId, action)
        }else{
            updateUserOrder(albumId, action)
        }
    })
}

var updateBtnsList = document.getElementsByClassName('update-cart-list');
console.log("listCollection:", updateBtnsList)
for (i = 0; i < updateBtnsList.length; i++) {
    updateBtnsList[i].addEventListener("click", function(){
        var albumId = this.dataset.album
        var action = this.dataset.action
        console.log('albumId:', albumId, 'action:', action)
        console.log('USER', user)

        if(user == 'AnonymousUser'){
            addCookieItem(albumId, action)
        } else {
            updateUserOrder(albumId, action)
        }
    })
}

var updateBtnsList = document.getElementsByClassName('update-cart-grid-by-price');
console.log("listCollection:", updateBtnsList)
for (i = 0; i < updateBtnsList.length; i++) {
    updateBtnsList[i].addEventListener("click", function(){
        var albumId = this.dataset.album
        var action = this.dataset.action
        console.log('albumId:', albumId, 'action:', action)
        console.log('USER', user)

        if(user == 'AnonymousUser'){
            addCookieItem(albumId, action)
        } else {
            updateUserOrder(albumId, action)
        }
    })
}

var updateBtnsList = document.getElementsByClassName('update-cart-grid-by-price-reversed');
console.log("listCollection:", updateBtnsList)
for (i = 0; i < updateBtnsList.length; i++) {
    updateBtnsList[i].addEventListener("click", function(){
        var albumId = this.dataset.album
        var action = this.dataset.action
        console.log('albumId:', albumId, 'action:', action)
        console.log('USER', user)

        if(user == 'AnonymousUser'){
            addCookieItem(albumId, action)
        } else {
            updateUserOrder(albumId, action)
        }
    })
}

var updateBtnsList = document.getElementsByClassName('update-cart-grid-by-artist-name');
console.log("listCollection:", updateBtnsList)
for (i = 0; i < updateBtnsList.length; i++) {
    updateBtnsList[i].addEventListener("click", function(){
        var albumId = this.dataset.album
        var action = this.dataset.action
        console.log('albumId:', albumId, 'action:', action)
        console.log('USER', user)

        if(user == 'AnonymousUser'){
            addCookieItem(albumId, action)
        } else {
            updateUserOrder(albumId, action)
        }
    })
}


function addCookieItem(albumId, action){
    console.log('user is not authenticated')
    if(action == 'add'){
        if(cart[albumId] == undefined){
            cart[albumId] = {'quantity':1}
        } else {
            cart[albumId]['quantity'] += 1
        }
    }
    if(action == 'remove'){
        cart[albumId]['quantity'] -= 1

        if(cart[albumId]['quantity'] <= 0){
            console.log('remove item')
            delete cart[albumId]
        }
    }
    console.log('cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

    location.reload()
}

function updateUserOrder(albumId, action){
    console.log('user logged in')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'albumId': albumId, 'action': action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}