library(rvest)
library(dplyr)
library(httr)

# Function to fetch and parse the NFL schedule grid for a given year
fetch_schedule_data <- function(year) {
  # URL for the NFL Schedule Grid on ESPN for the given year
  url <- paste0("https://www.espn.com/nfl/schedulegrid/_/year/", year)
  
  # Fetch the HTML content of the page with custom headers to mimic a browser
  page <- read_html(GET(url, user_agent("Mozilla/5.0")))
  
  # Find the schedule grid table
  table_node <- page %>%
    html_node("table")
  
  # Check if the table node was found
  if (is.null(table_node)) {
    stop("Schedule table not found for the year ", year)
  }
  
  # Extract the data table
  table <- table_node %>%
    html_table(fill = TRUE)
  
  # Remove any empty columns if present
  table <- table[, colSums(is.na(table)) < nrow(table)]
  
  # Use the second row as column headers and remove the first two rows
  colnames(table) <- paste0("Week", table[2, ])
  table <- table[-c(1, 2), ]
  
  # Ensure the first column is named "Team"
  colnames(table)[1] <- "Team"
  
  # Remove any column with NA as its name
  table <- table[, !is.na(colnames(table))]
  
  # Remove any column named "WeekNA"
  table <- table[, !grepl("^WeekNA$", colnames(table))]
  
  # Return the cleaned table as a DataFrame
  return(table)
}

# Loop through the years 2013 to 2023 and fetch the schedule grid for each year
schedules <- list()
for (year in 2013:2023) {
  tryCatch({
    # Fetch the schedule data
    df <- fetch_schedule_data(year)
    
    # Store the DataFrame in the list with the year as the name
    schedules[[as.character(year)]] <- df
    
    # Save the DataFrame to a CSV file with the desired filename format
    csv_filename <- paste0("NFLScheduleMatrix", year, ".csv")
    write.csv(df, csv_filename, row.names = FALSE)
    
    cat("Successfully fetched and saved schedule data for", year, "as", csv_filename, "\n")
  }, error = function(e) {
    cat("Failed to fetch data for", year, ":", e$message, "\n")
  })
}

# Example: Access and display the schedule data for a specific year
print(head(schedules[["2013"]]))
print(head(schedules[["2023"]]))

setwd("C:/Users/petew/NFL Attendance Project")

