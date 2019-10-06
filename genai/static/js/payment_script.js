var stripe;
var checkoutSessionId;

var setupElements = function () {
    fetch("/account/public-key", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(function (result) {
        return result.json();
    })
    .then(function (data) {
        stripe = Stripe(data.publicKey);
    });
};

var createCheckoutSession = function () {
    fetch("/account/create-checkout-session", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(function (result) {
        return result.json();
    })
    .then(function (data) {
        checkoutSessionId = data.checkoutSessionId;
    });
};

setupElements();
createCheckoutSession();

document.querySelector("#submit").addEventListener("click", function (evt) {
    evt.preventDefault();
    // Initiate payment
    stripe
        .redirectToCheckout({
            sessionId: checkoutSessionId
        })
        .then(function (result) {
            console.log(result.error.message);
        })
        .catch(function (err) {
            console.log(err);
        });
});
