let cardColors = ["#0d6efd", "#fd7e14", "#428370", "#dc3545", "#6f42c1", "#d63384"] 

// randomize sequence of colors
let randomizer = new Date(); 
randomizer = randomizer.getSeconds();

// get all cards
let permCards = document.querySelectorAll('.card')

// change background color of cards and words
for (let i = 0; i < permCards.length; i++) {
    // change card header background color
    permCards[i].querySelector('.card-header').style.background = cardColors[(i + randomizer) % cardColors.length];

    // get all words of a card
    let permWords = permCards[i].querySelectorAll('.card-body li');
    // change card words background color
    for (let j = 0; j < permWords.length; j++) {
        permWords[j].style.background = cardColors[(i + randomizer) % cardColors.length];
    }
}
