source("./global.R")

# Define server logic
server <- function(input, output,session) {
  session$onSessionEnded(function() {
    session$reload()
  })
  
  output$data_table <- renderDataTable({
    # Use global_dat data frame to render the data table
    global_dat
  })
  
  output$random_number <- renderText({
    # Generate a random number between 1 and 100
    random_num <- sample(1:100, 1)
    random_num
  })
}