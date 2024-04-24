HOME_TEAM_WON=1
def tournamentWinner(competitions, resultS):
   currentBestTeam=""  #setting best team to empty string
   scores={currentBestTeam:0} #setting scores to 0 for the string
   for idx, competition in enumerate(competitions): #iterating through the competitions
       result = resultS[idx] #getting the result of the competition
       homeTeam, awayTeam = competition #getting the home and away team
       winningTeam=homeTeam if result == HOME_TEAM_WON else awayTeam #setting the winning team
       updateScores(winningTeam,3,scores) #updating the scores
       if scores[winningTeam]>scores[currentBestTeam]: #checking if the winning team has more scores than the current best team
           currentBestTeam = winningTeam    #setting the winning team as the current best team
   return currentBestTeam #returning the current best team

def updateScores(team, points,scores): #function to update the scores
    if team not in scores: #checking if the team is not in the scores
        scores[team]=0 #setting the score to 0
 
    scores[team]+=points #adding the points to the score