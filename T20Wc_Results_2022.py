from bs4 import BeautifulSoup
import requests, openpyxl

# excel = openpyxl.Workbook()
# sheet = excel.active
# sheet.title = '2022 T20i World-Cup'
# sheet.append(['Date', 'Team 1', 'Team 2', 'Winner', 'Margin', 'Ground', 'Scorecard'])


try:
    response = requests.get("https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450")
    soup = BeautifulSoup(response.text, 'html.parser')
    Results = soup.find('tbody').find_all('tr')

    for Result in Results:
        find_Team_1 = Result.find('td', 'ds-min-w-max').span.text
        find_Team_2_winner_margin_ground_score_elements = Result.find_all('td', 'ds-min-w-max ds-text-right')
    
    # Assuming winner and margin are within different elements, adjust this part accordingly
        if len(find_Team_2_winner_margin_ground_score_elements) >= 5:
            find_Team_2 = find_Team_2_winner_margin_ground_score_elements[0].span.text
            winner = find_Team_2_winner_margin_ground_score_elements[1].span.text
            margin = find_Team_2_winner_margin_ground_score_elements[2].span.text
            Ground = find_Team_2_winner_margin_ground_score_elements[3].span.text
            ScoreCard = find_Team_2_winner_margin_ground_score_elements[4].span.text
        else:
            winner = "N/A"
            margin = "N/A"
    
        date = Result.find('td', 'ds-min-w-max ds-text-right ds-whitespace-nowrap').span.text
    
        print(date, find_Team_1, find_Team_2, winner, margin, Ground, ScoreCard)
        # sheet.append([date, find_Team_1, find_Team_2, winner, margin, Ground, ScoreCard])
    

except Exception as e:
    print(e)

# excel.save("ICC T20I WC-2022.xlsx")
    



# for Result in Results:
    #     find_Team_1 = Result.find('td', 'ds-min-w-max').span.text
    #     find_Team_2 = Result.find_next('td', 'ds-min-w-max ds-text-right').span.text
    #     winner = Result.find_next('td', 'ds-min-w-max ds-text-right').span.text
    #     margin = Result.find_next('td', 'ds-min-w-max ds-text-right').span.text
    #     date = Result.find('td', 'ds-min-w-max ds-text-right ds-whitespace-nowrap').span.text
    #     print(date, find_Team_1, find_Team_2, winner, margin)