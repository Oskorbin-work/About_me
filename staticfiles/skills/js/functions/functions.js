


var CardBack = document.querySelectorAll('[id^=card_back_]');
var CardFront = document.querySelectorAll('[id^=card_front_]');

for (let i = 0; i < CardBack.length; i++) {
    CardBack[i].style.display = "none"
    CardBack[i].addEventListener("click", () => {
        CardBack[i].style.display = "none"
        CardFront[i].style.display = "block"
    })
 }

for (let i = 0; i < CardFront.length; i++) {
    CardFront[i].addEventListener("click", () => {
        CardFront[i].style.display = "none"
        CardBack[i].style.display = "block"

})
 }


