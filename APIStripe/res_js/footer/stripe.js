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
    }
)