# NFL-Game-Attendance-Predictive-Analysis
## **Abstract**:
The NFL is monetarily driven by those who consume the product. For each of the 32 franchises, one of the main sources of revenue comes from fans attending home games. Teams profit massively from the cost fans pay a ticket to attend a game. Once fans are at games, they are likely to spend money on team clothing/gear, food at concession stands, and most importantly beer. Therefore, for every empty seat a stadium has during a game, the team is losing money from the absence of those in-game purchases. If the front office of a team is able to predict a low turnout for a game, this information is valuable business intelligence. The front office can then take action and find ways to get fans to fill those empty seats. For example, a team can advertise discounts (Dollar Hot Dogs, Giveaways, or Discounted Beer) days before a game in order to avoid lost gains from low fan turnout.

This project is a Machine Learning approach to predict NFL Game Attendance using past attendance data (2013-2023). It was an idea I came up with to combine my love for sports along with my sports business acumen. This model can be used as a tool to predict Attendance of a future NFL Game, given a handful of known variables. A large majority of this project involved scraping the necessary data as well as formatting it to be fed into a machine learning algorithm. I scraped and manipulated data from the following:

## Data Sources:
- [(Stadium Capacity Data)](https://en.wikipedia.org/wiki/List_of_current_NFL_stadiums) 
- [(Team Abbreviation Data for Joins)](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_National_Football_League/National_Football_League_team_abbreviations) 
- [(Attendance Data for Model Training/Testing)](https://www.pro-football-reference.com/years/2023/attendance.htm) 
- [(Schedule Matrix to Remove Away Game Attendance Values)](https://www.espn.com/nfl/schedulegrid/_/year/2023) 
- [(Weekly Matchup Data to Extract Team Records)](https://www.espn.com/nfl/scoreboard/_/week/1/year/2023/seasontype/2) 
- [(Sunday Night Football Game Data for Time of Game Variable)](https://www.nfl.com/schedules/sunday-night-football/2023)
- [(Monday Night Football Game Data for Time of Game Variable)](https://www.nfl.com/schedules/monday-night-football/2023) 
- [(Thursday Night Football Game Data for Time of Game Variable)](https://www.nfl.com/schedules/thursday-night-football/2023) 


Variable to be Predicted: Game Attendance / Maximum Capacity
- I chose to predict percent capacity (Ex: 95%) instead of the attendance (Ex: 50,000) because all stadiums have different maximum capacities.

**3 Algorithms were implemented:**
1. Multiple Linear Regression
2. Decision Tree Regression
3. Random Forest Regression

I plan on continously improving the model and its inputs to achieve greater prediction accuracy. Stay tuned...

Python Libraries Used:
- Beautiful Soup
- Pandas
- Numpy
- Sklearn
