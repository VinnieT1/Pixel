let updateButtons = document.getElementsByClassName('update-cart');

for (let i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click', function(){
        let productId = this.dataset.product;
        let action = this.dataset.action;
        
        if (user !== 'AnonymousUser') {
            updateUserOrder(productId, action);
        }
        else {
            window.location.href = "/users/login";
        }
    });
}

function updateUserOrder(productId, action) {
    let url = '/cart/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        location.reload()
    })
}