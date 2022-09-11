const stripe = Stripe("pk_test_51LgR6IHVRJovbZDJEifEzGWqm5oSz8d6XlLpLMHYrdRPi5NeZb251Vqe7SzwouLYhtlvBYZIebzm6hnDPfK5jPNT00NNFTs3Zl")

document.querySelectorAll(".checkout-button").forEach(button => {
    button.onclick = () => {
        fetch("/buy/" + button.getAttribute("id") + "/", {
            method: "GET"
        })
        .then(function(response){
            return response.json();
        })
        .then(function(session){

            if(!session.error)
                return stripe.redirectToCheckout({sessionId: session.id});
            else
                console.error("Session error: ", session.error);    
        })
        .then(function(result){

            if(result.error){
                alert(result.error.message);
            }
        })
        .catch(function(error){
            console.error("Error: ", error);
        });
    }
})

document.querySelectorAll(".basket-buy-all").forEach(button => {
    button.onclick = () => {

        const array = [];
        let name, price, count, item

        document.querySelectorAll(".product").forEach(product => {

            name = product.querySelector(".name").innerHTML;
            price = Math.round(product.querySelector(".price").innerHTML * 100);
            count = product.querySelector(".count-in-basket").value;

            item = {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                    'name': name,
                    },
                    'unit_amount': price,
                },
                'quantity': count,
            }

            array.push(item);

        })

        const data = {'data' : array};
        runInServerFetch('buy_basket', data)
            .then(function(response){
                return response.json();
            })
            .then(function(session){

                if(!session.error)
                    return stripe.redirectToCheckout({sessionId: session.id});
                else
                    console.error("Session error: ", session.error);    
            })
            .then(function(result){

                if(result.error){
                    alert(result.error.message);
                }
            })
            .catch(function(error){
                console.error("Error: ", error);
            });
    }
})
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getParams(element){
    return JSON.parse(JSON.stringify(element.dataset));
}

function runInServerFetch(url, params=''){

    const head = {
        method: "POST",
        credentials: 'same-origin',
        headers: {
            'Accept' : 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken' : getCookie('csrftoken') //CSRF_TOKEN
        }
    };

    if(params != '')
        head['body'] = JSON.stringify(params);

    return fetch(url, head);
}

function changeBasket(url, button, countElem = undefined){

    runInServerFetch(url, getParams(button))
        .then(function(response){
            return response.json();
        })
        .then(function(result){

            if(result.status == 'success')
                if(countElem && result.count > 0)
                    countElem.value = result.count
            else{
                console.error("Basket error: ", result.error);    
            }
        })
        .then(function(result){

            if(result.error){
                alert(result.error.message);
            }
        })
        .catch(function(error){
            console.error("Error: ", error);
        });

}

document.querySelectorAll(".basket-button").forEach(button => {
    button.onclick = () => {
        changeBasket("basket/change", button);
    }
})

function getCountElem(button){
    return button.parentElement.querySelector(".count-in-basket");
}

document.querySelectorAll(".basket-remove, .basket-add").forEach(button => {
    button.onclick = () => {

        changeBasket("change", button, getCountElem(button));
    
    }
});