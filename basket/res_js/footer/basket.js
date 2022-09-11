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

