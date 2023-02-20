# optimalLineup

Uses the stats of 9 baseball players to create an optimal batting lineup. Uses object oriented programming and web scraping.

Webscrapes data off of https://www.mlb.com/stats/ by default. You can manually input stats as well.
```
Calculation Details:
Lineup:
    1. Highest OBP
    2. Highest OPS
    3. Highest SLG
    4. Highest OPS
    5. Highest SLG
    6. Highest OPS
    7. Highest OPS
    8. Highest OPS
    9. Highest OPS
Priority: 2,4,1,5,3,6,7,8,9
```

# How to Run

## Create a virtual environment
1. Start by navigating to the project directory
2. Create the virtual environment
```console 
python3 -m venv ./venv
```
3. Activate the virtual environment
```console 
/venv/Scripts/activate.bat
```
## Install dependencies
```console 
pip install -r requirements.txt
```
## Run the executable
```console 
python optimalLineup.py
```
