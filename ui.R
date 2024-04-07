# Define UI
ui <- fluidPage(
  titlePanel("Gas Prices Data Table"),
  fluidRow(textOutput("random_number"),width=2),
  fluidRow(dataTableOutput("data_table"))
)