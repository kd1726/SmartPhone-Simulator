function sleep(ms){
  return new Promise(resolve => setTimeout(resolve,ms))
}
const handdown = new Audio("/static/Black-Jack/swish.m4a")
async function Start(){
  handdown.play()
  let words = ["Paper!","Scissors!","Says!","Shoot!"]
  let h2  = document.createElement('h2')
  var word = document.createTextNode("Rock!")
  h2.appendChild(word)
  document.querySelector("#who-won").appendChild(word)
  for (let i =0; i<words.length; i++){
    await sleep(500)
    handdown.play()
    let element = document.querySelector("#who-won")
    let newItem  = document.createElement('h2')
    newItem.id = "who-won"
    newItem.style.textAlign = "center"
    newItem.innerHTML = words[i]
    element.parentNode.replaceChild(newItem,element)
    if(i===words.length){
      handdown.play()
      let element = document.querySelector("#who-won")
      let newItem  = document.createElement('h2')
      newItem.id = "who-won"
      newItem.style.textAlign = "center"
      newItem.innerHTML = words[i]
      element.parentNode.replaceChild(newItem,element)
        }
      }
    }
async function rpsgame(input){
  let rock = document.getElementById('rock')
  let paper = document.getElementById('paper')
  let scissor = document.getElementById('scissors')
  let choices = [rock,paper,scissor];
  let choice = input
  let computerchoiceprocess = Math.floor(Math.random()*choices.length)
  let computerchoice = choices[computerchoiceprocess]
  Start()
  await sleep(2500)
  if (choice===rock){
    rock_function()
    frontend()
  }
  else if (choice===paper){
    paper_function()
    frontend()
  }
  else{
    scissors_fucntion()
    frontend()
  }
  function rock_function(){
  if ((choice===rock)&&(computerchoice===rock)) {
      document.getElementById('scissors').remove();
      document.getElementById('paper').remove();
      let element = document.querySelector("#who-won")
      let newItem  = document.createElement('h2')
      newItem.id = "who-won"
      newItem.style.textAlign = "center"
      newItem.innerHTML = "It's a Tie!"
      element.parentNode.replaceChild(newItem,element)
      resetbutton()
    }

  else if ((choice===rock)&&(computerchoice===paper)){
      document.getElementById('scissors').remove()
      let element = document.querySelector("#who-won")
      let newItem  = document.createElement('h2')
      newItem.id = "who-won"
      newItem.style.textAlign = "center"
      newItem.innerHTML = "You Lose!"
      element.parentNode.replaceChild(newItem,element)
      resetbutton()
    }

  else if ((choice===rock)&&(computerchoice===scissor)){
      document.getElementById('paper').remove();
      let element = document.querySelector("#who-won")
      let newItem  = document.createElement('h2')
      newItem.id = "who-won"
      newItem.style.textAlign = "center"
      newItem.innerHTML = "You Win!"
      element.parentNode.replaceChild(newItem,element)
      resetbutton()
  }
  else{
    let h2 = document.createElement('h2');
    let element = document.querySelector("#who-won")
    let newItem  = document.createElement('h2')
    newItem.id = "who-won"
    newItem.style.textAlign = "center"
    newItem.innerHTML = "Something is Not Right!"
    element.parentNode.replaceChild(newItem,element)
    resetbutton()
  }
}
function paper_function(){
  if ((choice===paper)&&(computerchoice===paper)) {
      document.getElementById('scissors').remove();
      document.getElementById('rock').remove();
      let element = document.querySelector("#who-won")
      let newItem  = document.createElement('h2')
      newItem.id = "who-won"
      newItem.style.textAlign = "center"
      newItem.innerHTML = "It's a Tie!"
      element.parentNode.replaceChild(newItem,element)
      resetbutton()
    }

  else if ((choice===paper)&&(computerchoice===scissor)){
      document.getElementById('rock').remove()
      let element = document.querySelector("#who-won")
      let newItem  = document.createElement('h2')
      newItem.id = "who-won"
      newItem.style.textAlign = "center"
      newItem.innerHTML = "You Lose!"
      element.parentNode.replaceChild(newItem,element)
      resetbutton()
    }

  else if ((choice===paper)&&(computerchoice === rock)){
      document.getElementById('scissors').remove()
      let element = document.querySelector("#who-won")
      let newItem  = document.createElement('h2')
      newItem.id = "who-won"
      newItem.style.textAlign = "center"
      newItem.innerHTML = "You Win!"
      element.parentNode.replaceChild(newItem,element)
      resetbutton()
  }
  else{
    let h2 = document.createElement('h2');
    let element = document.querySelector("#who-won")
    let newItem  = document.createElement('h2')
    newItem.id = "who-won"
    newItem.style.textAlign = "center"
    newItem.innerHTML = "Something is Not Right!"
    element.parentNode.replaceChild(newItem,element)
    resetbutton()
  }
}
function scissors_fucntion(){
  if ((choice===scissor)&&(computerchoice===scissor)) {
      document.getElementById('paper').remove();
      document.getElementById('rock').remove();
      let element = document.querySelector("#who-won")
      let newItem  = document.createElement('h2')
      newItem.id = "who-won"
      newItem.style.textAlign = "center"
      newItem.innerHTML = "It's a Tie!"
      element.parentNode.replaceChild(newItem,element)
      resetbutton()
    }

  else if ((choice===scissor)&&(computerchoice===rock)){
      document.getElementById('paper').remove()
      let element = document.querySelector("#who-won")
      let newItem  = document.createElement('h2')
      newItem.id = "who-won"
      newItem.style.textAlign = "center"
      newItem.innerHTML = "You Lose!"
      element.parentNode.replaceChild(newItem,element)
      resetbutton()
    }

  else if ((choice===scissor)&&(computerchoice===paper)){
      document.getElementById('rock').remove()
      let element = document.querySelector("#who-won")
      let newItem  = document.createElement('h2')
      newItem.id = "who-won"
      newItem.style.textAlign = "center"
      newItem.innerHTML = "You Win!"
      element.parentNode.replaceChild(newItem,element)
      resetbutton()
    }

  else{
    let h2 = document.createElement('h2');
    let element = document.querySelector("#who-won")
    let newItem  = document.createElement('h2')
    newItem.id = "who-won"
    newItem.style.textAlign = "center"
    newItem.innerHTML = "Something is Not Right!"
    element.parentNode.replaceChild(newItem,element)
    resetbutton()
  }
}
  function frontend(){
    if (choice===computerchoice){
      let h2 = document.querySelector("#who-won")
      choice.style.boxShadow = "2px 2px 20px green"
      computerchoice.style.boxShadow = "2px 2px 20px green"
      h2.style.color="yellow"
      }
    else{
      choice.style.boxShadow = "2px 2px 20px blue"
      computerchoice.style.boxShadow = "2px 2px 20px red"
    }
  }
}
function resetbutton(){
  var button = document.createElement("button")
  button.className = "login-button"
  button.classList.add("ml-3")
  button.addEventListener('click',resetcontainer)
  button.innerHTML = "Reset"
  document.querySelector("#who-won").appendChild(button)
}

function resetcontainer(){
  var container = document.querySelector("#resetting-id")
  container.remove()
  var div = document.createElement('div')
  div.classList.add("img-container")
  div.classList.add("mt-5")
  div.id = "resetting-id"
  document.getElementById("reset-container").appendChild(div)
  var imgdiv = document.querySelector("#resetting-id")
  let h2 = document.createElement('h2');
  let element = document.querySelector("#who-won")
  let newItem  = document.createElement('h2')
  newItem.id = "who-won"
  newItem.style.textAlign = "center"
  newItem.innerHTML = ""
  element.parentNode.replaceChild(newItem,element)
  var rock = document.createElement('img')
  rock.src= "/static/rps/rock.png"
  rock.id = "rock"
  rock.onclick = function(){rpsgame(this)}
  var paper = document.createElement('img')
  paper.src= "/static/rps/paper.png"
  paper.id = "paper"
  paper.onclick = function(){rpsgame(this)}
  var scissors = document.createElement('img')
  scissors.src= "/static/rps/scissors.png"
  scissors.id="scissors"
  scissors.onclick = function(){rpsgame(this)}
  imgdiv.appendChild(rock)
  imgdiv.appendChild(paper)
  imgdiv.appendChild(scissors)
  var children = document.querySelector("#resetting-id").children
}
