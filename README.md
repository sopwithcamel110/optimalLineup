# optimalLineup
Uses the stats of 9 baseball players to create an optimal batting lineup. Uses object oriented programming and web scraping.

Webscrapes data off of https://www.mlb.com/stats/ by default. You can manually input stats as well.

Calculation Details:
order:
    1. Highest OBP
    2. Highest OPS
    3. 2nd Highest SLG
    4. 2nd Highest OPS
    5. Highest SLG
    6. 3rd Highest OPS
    7. 4th Highest OPS
    8. 5th Highest OPS
    9. 6th Highest OPS
priority: 2,4,1,5,3,6,7,8,9
