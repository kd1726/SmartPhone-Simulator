function rpsgame(input){
  let rock = document.getElementById('rock')
  let paper = document.getElementById('paper')
  let scissor = document.getElementById('scissors')
  let choices = [rock,paper,scissor];
  let choice = input
  let computerchoiceprocess = Math.floor(Math.random()*choices.length)
  let computerchoice = choices[computerchoiceprocess]
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
      let h2 = document.createElement('h2');
      var result = document.createTextNode("It's a tie!");
      h2.appendChild(result);
      return document.getElementById('who won').appendChild(result);
    }

  else if ((choice===rock)&&(computerchoice===paper)){
      document.getElementById('scissors').remove();
      let h2 = document.createElement('h2');
      var result = document.createTextNode("You lose!");
      h2.appendChild(result)
      return document.getElementById('who won').appendChild(result)
    }

  else if ((choice===rock)&&(computerchoice===scissor)){
      document.getElementById('paper').remove()
      let h2 = document.createElement('h2');
      var result = document.createTextNode("You win!")
      h2.appendChild(result)
      return document.getElementById('who won').appendChild(result)
  }
  else{
    let h2 = document.createElement('h2');
    var result = document.createTextNode("Something is not right")
    h2.appendChild(result)
    return document.getElementById('who won').appendChild(result)
  }
}
function paper_function(){
  if ((choice===paper)&&(computerchoice===paper)) {
      document.getElementById('scissors').remove();
      document.getElementById('rock').remove();
      let h2 = document.createElement('h2');
      var result = document.createTextNode("It's a tie!");
      h2.appendChild(result);
      return document.getElementById('who won').appendChild(result);
    }

  else if ((choice===paper)&&(computerchoice===scissor)){
      document.getElementById('rock').remove();
      let h2 = document.createElement('h2');
      var result = document.createTextNode("You lose!");
      h2.appendChild(result)
      return document.getElementById('who won').appendChild(result)
    }

  else if ((choice===paper)&&(computerchoice === rock)){
      document.getElementById('scissors').remove()
      let h2 = document.createElement('h2');
      var result = document.createTextNode("You win!")
      h2.appendChild(result)
      return document.getElementById('who won').appendChild(result)
  }
  else{
    let h2 = document.createElement('h2');
    var result = document.createTextNode("Something is not right")
    h2.appendChild(result)
    return document.getElementById('who won').appendChild(result)
  }
}
function scissors_fucntion(){
  if ((choice===scissor)&&(computerchoice===scissor)) {
      document.getElementById('paper').remove();
      document.getElementById('rock').remove();
      let h2 = document.createElement('h2');
      var result = document.createTextNode("It's a tie!");
      h2.appendChild(result);
      return document.getElementById('who won').appendChild(result);
    }

  else if ((choice===scissor)&&(computerchoice===rock)){
      document.getElementById('paper').remove();
      let h2 = document.createElement('h2');
      var result = document.createTextNode("You lose!");
      h2.appendChild(result)
      return document.getElementById('who won').appendChild(result)
    }

  else if ((choice===scissor)&&(computerchoice===paper)){
      document.getElementById('rock').remove()
      let h2 = document.createElement('h2');
      var result = document.createTextNode("You win!")
      h2.appendChild(result)
      return document.getElementById('who won').appendChild(result)
  }
  else{
    let h2 = document.createElement('h2');
    var result = document.createTextNode("Something is not right")
    h2.appendChild(result)
    return document.getElementById('who won').appendChild(result)
  }
}
  function frontend(){
    if (choice===computerchoice){
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
