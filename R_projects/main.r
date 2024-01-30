# main

while (TRUE) {
  print("Hello, what would you like to do")
  print("Type 1 if you want to order a pizza")
  print("Type 2 if you want to play Rock Sicssor Paper")
  x <- TRUE
  while (x) {
    user_choice <- as.numeric(readLines("stdin", n = 1))
  for (answer in c(1,2)) {x<- FALSE}
  }
  if (user_choice == 1) {
    source("order_pizza.r")
  } else {
    source("pao_yin_chub.r")
  } 
  
  print("Do you want to exit? (yes/no)")
  quit <- readLines('stdin', n=1)
  if (quit == 'yes') {
    print("-----------------------Exit--------------------------")
    break
  }
  print("-----------------------------------------------------")
}