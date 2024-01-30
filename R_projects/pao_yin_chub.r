#pao_yin_chub

print("Let's play Rock Scissor Paper!")

# create shapes
shapes <- c('rock','scissor','paper')

#create score collectors
lose <- 0; win <- 0; draw <-0

# Let's player choose their shape
x <- TRUE
while (x){
  y <- TRUE
  while(y){
    print("Choose your shape (Rock/Scissor/Paper)")
    my_shape <- tolower(readLines('stdin', n = 1))
    for (shape in shapes) {
      if (shape == my_shape) {y <- FALSE}
    }
  }
  bot_shape <- sample(shapes, size =1)
  print(paste("You:",my_shape,"VS","Bot:",bot_shape))
  ## Battle
  if (my_shape != bot_shape){
    ## user win
    if ((my_shape == 'rock' & bot_shape == 'scissor') |
        (my_shape == 'scissor' & bot_shape == 'paper') |
        (my_shape == 'paper' & bot_shape == 'rock')){
      print("You win")
      win <- win + 1
        } else {
      print("You lose")
      lose <- lose + 1
        }
  } else {
    print("Draw!!")
    draw <- draw + 1
  }
  z <- TRUE
  while (z){
    print("Play again? (yes/no)")
    end_game <- tolower(readLines('stdin',n=1))
    for (answer in c('yes','no')) {
      if (answer == end_game) {z <- FALSE}
    }  
  if (end_game == 'no') {x<- FALSE}
  }
}

# total wins/loses
print("Here is the scoreboard")
stat <- list(Win = win, Lose = lose, Draw = draw)
stat_show <- data.frame(stat)
print(stat_show,row.names = FALSE)

