import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import VotingRegressor

# Load your pre-trained models
# Ensure you have saved your models using pickle previously
model_paths = {
    "XGBoost": "XGBoost_model.sav",
    "Voting Regressor": "VotingRegressor.sav",
    "Random Forest": "RandomForest_model.sav",
    "Decision Tree": "DecisionTree_model.sav",
}
models = {name: pickle.load(open(path, "rb")) for name, path in model_paths.items()}

# List of NFL teams and their corresponding capacities
nfl_teams = {
    "Arizona Cardinals": 63400, "Atlanta Falcons": 71000, "Baltimore Ravens": 71008,
    "Buffalo Bills": 71608, "Carolina Panthers": 74867, "Chicago Bears": 61500,
    "Cincinnati Bengals": 65515, "Cleveland Browns": 67431, "Dallas Cowboys": 80000,
    "Denver Broncos": 76125, "Detroit Lions": 65000, "Green Bay Packers": 81441,
    "Houston Texans": 72220, "Indianapolis Colts": 67000, "Jacksonville Jaguars": 67838,
    "Kansas City Chiefs": 76416, "Las Vegas Raiders": 65000, "Los Angeles Chargers": 70240,
    "Los Angeles Rams": 70240, "Miami Dolphins": 65326, "Minnesota Vikings": 66655,
    "New England Patriots": 66829, "New Orleans Saints": 73208, "New York Giants": 82500,
    "New York Jets": 82500, "Philadelphia Eagles": 69596, "Pittsburgh Steelers": 68400,
    "San Francisco 49ers": 68500, "Seattle Seahawks": 69000, "Tampa Bay Buccaneers": 69218,
    "Tennessee Titans": 69143, "Washington Football Team": 65000
}

# Define international stadium capacities
international_stadiums = {
    "London (Wembley Stadium)": 86000,
    "London (Twickenham Stadium)": 75000,
    "London (Tottenham Hotspur Stadium)": 62850,
    "Mexico (Estadio Azteca)": 83000,
    "Germany (Alianz Arena)": 70000,
    "Germany (Deutsche Bank Park)": 50500
}

st.markdown("""
    <style>
        .header-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-direction: row;  /* Stack items vertically */
        }
        .header-title {
            font-size: 3em;  /* Increase the size as needed */
            margin: 0;
        }
        .header-image {
            max-height: 120px;  /* Adjust the height as needed */
        }
    </style>
""", unsafe_allow_html=True)

# Add the title and images
st.markdown(f"""
    <div class="header-container">
        <h1 class="header-title">NFL Game Attendance Predictor</h1>
        <img class="header-image" src="https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/National_Football_League_logo.svg/800px-National_Football_League_logo.svg.png" alt="NFL Logo"/>  
    </div>
""", unsafe_allow_html=True)

# Dropdown menu for selecting the model
model_name = st.selectbox("Select the Machine Learning Model", list(models.keys()))

# Input fields for predictor variables
team_selected = st.selectbox("Select the Home Team", list(nfl_teams.keys()))
capacity = nfl_teams[team_selected]

week = st.slider("Week", 1, 18, 1)
away_wins = st.number_input("Away Team Wins", min_value=0, max_value=17, value=0)
home_wins = st.number_input("Home Team Wins", min_value=0, max_value=17, value=0)

international = st.selectbox("Is this an International Game?", ("No", "Yes"))
if international == "Yes":
    stadium_option = st.selectbox("Select Stadium:", list(international_stadiums.keys()))
    capacity = international_stadiums[stadium_option]
international = 1 if international == "Yes" else 0


time_of_game = st.selectbox("Time of Game", ["Sunday (Day Game)", "Sunday Night", "Monday Night", "Thursday Night", "Holiday"])

# Creating dummy variables for time
time_1 = time_2 = time_3 = time_4 = 0
if time_of_game == "Sunday Night":
    time_1 = 1
elif time_of_game == "Monday Night":
    time_2 = 1
elif time_of_game == "Thursday Night":
    time_3 = 1
elif time_of_game == "Holiday":
    time_4 = 1

# Display predictor variables
st.write("## Predictor Variables")
st.write(f"Capacity: {capacity}")
st.write(f"Week: {week}")
st.write(f"Away Team Wins: {away_wins}")
st.write(f"Home Team Wins: {home_wins}")
st.write(f"International Game: {'Yes' if international == 1 else 'No'}")
st.write(f"Time: {time_of_game}")

# Button to make predictions
if st.button("Predict"):
    # Preparing the input data for prediction
    input_data = pd.DataFrame([[capacity, week, away_wins, home_wins, international, time_1, time_2, time_3, time_4]],
                              columns=["Capacity", "Week", "Away Team Wins", "Home Team Wins",
                                       "International", "Time_1", "Time_2", "Time_3", "Time_4"])

    # Selecting and making a prediction with the chosen model
    selected_model = models[model_name]
    prediction = selected_model.predict(input_data)

    # Display the prediction
    st.write(f"### Predicted Attendance: {int(prediction[0]):,}")
