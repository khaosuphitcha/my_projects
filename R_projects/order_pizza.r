#order_pizza

print("Welcome! Welcome!")
print("Here is our pizza menu")

#create the menu
names <- c("Tom Yum Kung", "Hawaiian", "Pepporoni", "Chesse & Tomatoes"
           ,"Veggie Italian Pizza")
s_prices <- c(8,6,7,7,8)
m_prices <- c(10,8,9,9,10)
l_prices <- c(12,10,11,11,12)
foods <- data.frame(names, 
                    S = paste0(s_prices, '$'),
                    M = paste0(m_prices, '$'),
                    L = paste0(l_prices, '$'))
drink_names <- c("Cola", "Beer", "Water","Punch","Juice")
drink_prices <- c(2,4,1,3,2)
drinks <- data.frame(names = drink_names,
                     prices = paste0(drink_prices,'$'))

#display the Pizza menu
print(foods)
print("-------------------------------------------------")

# Take an order
x <- TRUE
while (x) {
  print("Choose your Pizza: ")
  my_pizza <- tolower(readLines('stdin', n =1))
  for (name in names) {
    if(my_pizza == tolower(name)) {x <- FALSE}
  }
}
y <- TRUE
while(y) {
  print("Size (S/M/L): ")
  my_size <- toupper(readLines('stdin', n =1))
  for (size in c('S','M','L')) {
    if(my_size == size) {y<- FALSE}
    }
}
u <- TRUE
while(u){
  print("Want any drinks? (type yes or no)")
  have_drink <- tolower(readLines('stdin', n =1))
  for (answer in c('yes','no')) {
    if (have_drink == answer) {u <- FALSE}
  }
}
if (tolower(have_drink)== 'yes'){
  ## display the drinks menu
  print("Here is the drinks menu")
  print(drinks)
  print("-------------------------------------------------")
  z <- TRUE
  while(z){
    print("choose your drink: ")
    my_drink <- readLines('stdin', n =1)
    for (drink_name in drink_names) {
      if(my_drink == tolower(drink_name)) {z <- FALSE}
    }
  }
}

# calculate price
a <- foods[tolower(foods$names) == my_pizza, toupper(my_size)]
piz_bill <- as.numeric(substring(a,1,last = nchar(a)-1))
if (tolower(have_drink)== 'yes'){
  b <- drinks[tolower(drinks$names) == my_drink, "prices"]
  drink_bill <- as.numeric(substring(b,1,nchar(b)-1))
}

# revise order
print("Here is your slip")
if (tolower(have_drink)== 'no'){
    bill <- data.frame('Orders'=c(my_pizza),
                       'Price' = c(a))
    print("***********************")
    print(bill)
    print("***********************")
    print(paste("Total:",a))
}
if (tolower(have_drink)== 'yes'){
    bill <- data.frame('Orders'= c(my_pizza,my_drink),
                     'Price'= c(a,b))
    print("***********************")
    print(bill)
    print("***********************")
    print(paste("Total:",paste0(piz_bill + drink_bill,'$')))
}