//Black Jack
let blackjack_game = {
  'you':{'scorespan':'#your-score', 'div':'#your-box' , 'score':0},
  'dealer':{'scorespan':'#dealer-score', 'div':'#dealer-box' , 'score':0},
  'cards':['2','3','4','5','6','7','8','9','10','J','K','Q','A'],
  'cardsmap':{'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'K':10,'Q':10,'A':[1,11]},
  'wins':0,
  'losses':0,
  'draws':0,
  'isStand':false,
  'turnsOver':false,
}
const YOU = blackjack_game['you']
const DEALER = blackjack_game['dealer']
const hitsound = new Audio('/static/Black-Jack/swish.m4a')

function blackjackHit(){
  if (blackjack_game['isStand']===false){
    let card =randomCard()
    showcard(YOU,card)
    updateScore(card,YOU)
    showScore(YOU)
  }
}
//to remove async stuff comment out sleep and things labeled async stuff

function blackjackStand(activePlayer=DEALER) {
  blackjack_game['isStand'] =true

  while(DEALER['score']<16 && blackjack_game['isStand']===true){
  let card1 =randomCard()
  showcard(DEALER,card1)
  updateScore(card1,DEALER)
  showScore(DEALER)
  }
//async stuff
blackjack_game['turnsOver'] = true;
let winner = whoWon();
showScore(winner)
/*  if (DEALER['score']>15){
    blackjack_game['turnsOver'] = true;
    let winner = whoWon();
    showScore(winner)
    console.log(blackjack_game['turnsOver'])
  }*/
}

function showcard(activePlayer,card){
  if (activePlayer['score']<21){
    let cardImage = document.createElement('img')
    let player =  activePlayer['div']
    cardImage.src = `/static/Black-Jack/cards/${card}.png`
    document.querySelector(player).appendChild(cardImage)
    hitsound.play()
  }
}

async function blackjackDeal() {
  if (blackjack_game['turnsOver']===true){
    blackjack_game['isStand']=false;
    let yourImages = document.querySelector('#your-box').querySelectorAll('img')
    for (let i = 0; i<yourImages.length; i++){
    yourImages[i].remove()}

    let dealerImages = document.querySelector('#dealer-box').querySelectorAll('img')
    for (let i = 0; i<dealerImages.length; i++){
    dealerImages[i].remove()
  }
    YOU['score'] = 0;
    DEALER['score'] = 0;
    document.querySelector('#your-score').textContent = 0
    document.querySelector('#your-score').style.color='white';

    document.querySelector('#dealer-score').textContent =0
    document.querySelector('#dealer-score').style.color='white';

    await sleep(100)
    document.getElementById('blackjack-result').textContent = "Let's Play!"
    document.getElementById('blackjack-result').style.color="black"
    blackjack_game['turnsOver'] = true;
  }
}

function randomCard(){
  let randomcard = Math.floor(Math.random()*blackjack_game['cards'].length)
  return blackjack_game['cards'][randomcard]
}

function updateScore(card, activePlayer){
  //if adding 11 keept me below 21 add 11, else add 1
  if (card ==='A' && activePlayer['score']<21){
    if (activePlayer['score'] +blackjack_game['cardsmap']['A'][1] <= 21){
      blackjack_game['cardsmap']['A'] = 11
      activePlayer['score'] +=blackjack_game['cardsmap']['A']
    }else if (activePlayer['score'] +blackjack_game['cardsmap']['A'][0] > 21){
      blackjack_game['cardsmap']['A'] = 1
      activePlayer['score'] +=blackjack_game['cardsmap']['A']
    }
  }
  else if (activePlayer['score']>=21){
    activePlayer['score'] =activePlayer['score']
  }
  else{
  activePlayer['score']+=blackjack_game['cardsmap'][card];
  }
}
function showScore(activePlayer){
  if (activePlayer['score']>21 && DEALER['score'] <21){
    document.querySelector(activePlayer['scorespan']).textContent = "BUST!";
    document.querySelector(activePlayer['scorespan']).style.color='red';
    const aww = new Audio("/static/Black-Jack/aww.mp3")
    aww.play()
  }
  else if(activePlayer['score']===21 && activePlayer['score']<DEALER['score']){
    document.querySelector(activePlayer['scorespan']).textContent = "You win!";
    document.querySelector(activePlayer['scorespan']).style.color='green';
    const yes = new Audio("/static/Black-Jack/cash.mp3")
    yes.play()
    }
    else{
    document.querySelector(activePlayer['scorespan']).textContent = activePlayer['score'];
  }
}

function whoWon(){
  let message, messageColor;
  let winner;
  let counter =0;
  let win = document.getElementById('wins')
  let lose = document.getElementById('losses')
  let draw = document.getElementById('draws')
  if (blackjack_game['turnsOver']===true){
    if(YOU['score']<= 21){
      if ((YOU['score']>DEALER['score']) || (DEALER['score']>21)){
        console.log('You Win!')
        const yes = new Audio("/static/Black-Jack/cash.mp3")
        yes.play()
        message = 'You WIN!'
        messageColor = 'green'
        document.getElementById('blackjack-result').textContent = message
        document.getElementById('blackjack-result').style.color = messageColor
        blackjack_game['wins']++
        //counter++
       document.querySelector("#wins").textContent =blackjack_game['wins']
        winner = YOU
      }
      else if(YOU['score']<DEALER['score']){
        const aww = new Audio("/static/Black-Jack/aww.mp3")
        aww.play()
        message = 'You lost!'
        messageColor = 'red'
        console.log('You Lost!')
        document.getElementById('blackjack-result').textContent = message
        document.getElementById('blackjack-result').style.color = messageColor
        blackjack_game['losses']++
        document.querySelector("#losses").textContent =blackjack_game['losses']
        winner =DEALER
      }
      else if (YOU['score'] === DEALER['score']){
        message = 'Draw!'
        messageColor = 'yellow'
        document.getElementById('blackjack-result').textContent = message
        document.getElementById('blackjack-result').style.color = messageColor
        blackjack_game['draws']++
        document.querySelector("#draws").textContent =blackjack_game['wins']
        console.log('draw!')
      }
    }
    else if (YOU['score'] >21 && DEALER['score']<=21){
      const aww = new Audio("/static/Black-Jack/aww.mp3")
      aww.play()
      message = 'You lost!'
      messageColor = 'red'
      console.log('You Lost!')
      document.getElementById('blackjack-result').textContent = message
      document.getElementById('blackjack-result').style.color = messageColor
      console.log('You Lost')
      blackjack_game['losses']++
    //  counter++
      document.getElementById("losses").textContent =blackjack_game['losses']
      winner = DEALER
    }
    else if ((YOU['score'] <21) && (YOU['score']<DEALER['score']<=21)){
      const aww = new Audio("/static/Black-Jack/aww.mp3")
      aww.play()
      message = 'You lost!'
      messageColor = 'red'
      console.log('You Lost!')
      document.getElementById('blackjack-result').textContent = message
      document.getElementById('blackjack-result').style.color = messageColor
      console.log('You Lost')
      blackjack_game['losses']++
    //  counter++
      document.getElementById("losses").textContent =blackjack_game['losses']
      winner = DEALER
    }
    else if ((YOU['score'] > 21) && (DEALER['score']>21)){
      message = 'Draw!'
      messageColor = 'yellow'
      document.getElementById('blackjack-result').textContent = message
      document.getElementById('blackjack-result').style.color = messageColor
      console.log('it is a draw')
      blackjack_game['draws']++
      //counter++
      //console.log(counter)
      document.querySelector("#draws").textContent = blackjack_game['draws']
    }
    console.log('Winner is', winner);
    console.log(blackjack_game)
    return winner;
  }
}
function counter(){
  counter++
  document.querySelector("#wins").textContent =counter
}
