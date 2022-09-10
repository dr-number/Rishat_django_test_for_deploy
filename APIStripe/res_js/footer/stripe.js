const stripe = Stripe("pk_test_51LgR6IHVRJovbZDJEifEzGWqm5oSz8d6XlLpLMHYrdRPi5NeZb251Vqe7SzwouLYhtlvBYZIebzm6hnDPfK5jPNT00NNFTs3Zl")

document.getElementById("checkout-button").addEventListener("click", function() {
    fetch("/item/", {
        method: "GET"
    })
    .then(function(response){
        return response.json();
    })
    .then(function(session){
        return stripe.redirectToCheckout(sessionId=session.id);
    })
    .then(function(result){

        if(result.error){
            alert(result.error.message);
        }
    })
    .catch(function(error){
        console.error("Error: ", error);
    });
});