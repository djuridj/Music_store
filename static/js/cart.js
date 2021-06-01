var updateBtnsGrid = document.getElementsByClassName('update-cart-grid');
console.log("gridCollection:", updateBtnsGrid)
for (i = 0; i < updateBtnsGrid.length; i++) {
    updateBtnsGrid[i].addEventListener("click", function(){
        var albumId = this.dataset.album
        var action = this.dataset.action
        console.log('albumId:', albumId, 'action:', action)
        console.log('USER', user)

        if(user == 'AnonymusUser'){
            console.log('Not logged in')
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

        if(user == 'AnonymusUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(albumId, action)
        }
    })
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