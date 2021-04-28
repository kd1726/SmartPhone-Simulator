function sleep(ms){
  return new Promise(resolve => setTimeout(resolve,ms))
}

async function greeting(){
  let words = ['Hi!',"I'm guessing a number between 0 and 10.", "Take a guess!"]
  for(let i = 0; i<words.length; i++){
    var element = document.querySelector("#question")
    var newItem = document.createElement('h2')
    newItem.innerHTML = words[i]
    newItem.id = "question"
    element.parentNode.replaceChild(newItem,element)
    await sleep(2000)
  }
  var buttons = document.getElementsByClassName("numbers")
  for(let x = 0; x<buttons.length; x++){
    buttons[x].style.visibility = "visible"
  }

}
let game_map = {
  "score":0
}
function pick_number(number){
  var buttons = document.getElementsByClassName("numbers")
  var numbers = [0,1,2,3,4,5,6,7,8,9,10]
  var computerchoice = Math.floor(Math.random()*numbers.length)
  let correct_choice = numbers[computerchoice]
  let your_choice = number
  if (your_choice === correct_choice){
    game_map["score"]+=5
  }else if(your_choice === correct_choice -1 || your_choice === correct_choice +1){
    game_map["score"]+=2
  }else if(your_choice === correct_choice -2 || your_choice === correct_choice +2){
    game_map["score"] = game_map["score"]
  }else{
    game_map["score"]-=2
  }
  var replace = document.querySelector("#question")
  var newi = document.createElement('h2')
  newi.innerHTML = `I chose ${correct_choice}. You chose ${your_choice}.`
  newi.id = "question"
  replace.parentNode.replaceChild(newi,replace)
  var element = document.querySelector("#points")
  var newItem = document.createElement('h1')
  newItem.id = "points"
  newItem.innerHTML = `Points: ${game_map["score"]}`
  element.parentNode.replaceChild(newItem,element)
  resetbutton()
}

function resetbutton(){
  var button = document.createElement("button")
  button.className = "login-button"
  button.style.padding = "5px 12px 5px 12px;"
  button.style.borderRadius = "50%";
  button.classList.add("ml-3")
  button.onclick = function(){resetpoints()}
  button.innerHTML = "Reset"
  document.querySelector("#points").appendChild(button)
}

function resetpoints(){
  game_map["score"] = 0
  var element = document.querySelector("#points")
  var newItem = document.createElement('h1')
  newItem.id = "points"
  newItem.innerHTML = "Points: 0"
  element.parentNode.replaceChild(newItem,element)
  var buttons = document.getElementsByClassName("numbers")
  for(let x = 0; x<buttons.length; x++){
    buttons[x].style.visibility = "hidden"
  }
  greeting()
}
