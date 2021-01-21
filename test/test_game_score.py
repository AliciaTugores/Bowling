from src.Score import Game_Score

# def test_open_score():
#     assert 60 == Game_Score('12345123451234512345').open_score()

# def test_strike_score():
#     assert 19== Game_Score('X36').strike_score()
#     assert 16 == Game_Score('5X422').strike_score()

# def test_spare_score():
#     assert 8 == Game_Score('4/2').spare_score()

def test_Total_Score():
    assert 60 == Game_Score('12345123451234512345').Total_Score()
    assert 300 == Game_Score('XXXXXXXXXXXX').Total_Score()
    assert 90 == Game_Score('9-9-9-9-9-9-9-9-9-9-').Total_Score()
    assert 150 == Game_Score('5/5/5/5/5/5/5/5/5/5/5').Total_Score()
    assert 133 == Game_Score('8/9-44729-XX8-359/7').Total_Score()
    assert 20 == Game_Score('11111111111111111111').Total_Score()
    assert 122 == Game_Score('8-7-539/9/X8-513/9-').Total_Score()
    assert 175 == Game_Score('X5/X5/XX5/--5/X5/').Total_Score()
    assert 149 == Game_Score('8/549-XX5/53639/9/X').Total_Score()