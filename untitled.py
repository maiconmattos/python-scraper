tweet = "LATEST (half-time): All-Ireland SFC Qualifier Round 1A - @Doiregaa 0-11 @WaterfordGAA 0-92."

def parseLatest(text):
    text = " " + text + " "
    print("TWEET : " + text)
    
    event = "LATEST"
    print("EVENT : " + event)
    
    time = text[ text.find("(") : (text.find(")") + 1) ]
    print("TIME : " + time)
    
    textFromTeam1Name = text[text.find("@"):]
    team1NameFinalPos = textFromTeam1Name.find(" ")
    team1Name = textFromTeam1Name[0:team1NameFinalPos]
    print ("TEAM1_NAME " + team1Name)

    textFromTeam1Score = textFromTeam1Name[team1NameFinalPos+1:]
    team1ScoreFinalPos = textFromTeam1Score.find(" ")
    team1Score = textFromTeam1Score[0:team1ScoreFinalPos]
    print ("TEAM1_SCORE " + team1Score)

    textFromTeam2Name = textFromTeam1Score[team1ScoreFinalPos+1:]
    team2NameFinalPos = textFromTeam2Name.find(" ")
    team2Name = textFromTeam2Name[0:team2NameFinalPos]
    print ("TEAM1_NAME " + team2Name)

    textFromTeam2Score = textFromTeam2Name[team2NameFinalPos+1:]
    team2ScoreFinalPos = textFromTeam2Score.find(" ")
    team2Score = textFromTeam2Score[0:team2ScoreFinalPos + 1]
    print ("TEAM2_SCORE " + team2Score)
    print("---------------")


parseLatest(tweet)