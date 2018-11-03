import random
import rps
import pytest
import subprocess
import sys

def test_rock_is_valid_play():
    assert rps.is_valid_play("rock") is True
    
def test_paper_is_valid_play():    
    assert rps.is_valid_play("paper") is True
    
def test_scissors_is_valid_play():
    assert rps.is_valid_play("scissors") is True
    
def test_lizard_is_invalid_play():
    assert rps.is_valid_play("lizard") is False

def test_fuck_is_invalid_play():
    assert rps.is_valid_play("fuck") is False
        
def test_computer_play_is_valid():
    for _ in range(5000):
        play = rps.generate_computer_play()
        assert rps.is_valid_play(play)    
        
def test_computer_plays_randomly():
    plays = [rps.generate_computer_play() for _ in range(5000)]
    assert plays.count('rock') > 1200
    assert plays.count('paper') > 1200
    assert plays.count('scissors') > 1200
    
    
# muzu si printnout neco, v pripade, ze to vse selze, print se vypise
# v pripade ze testy projdou, nechci to printovat (captured)

def test_game_returns_tie():
    assert rps.evaluate_game('rock', 'rock') == "tie"
    assert rps.evaluate_game('paper', 'paper') == "tie"
    assert rps.evaluate_game('scissors', 'scissors') == "tie"
    
def test_paper_beats_rock():
    result = rps.evaluate_game("paper", "rock") 
    assert result == "human"
    
def test_rock_beats_scissors():
    result = rps.evaluate_game("rock", "scissors") 
    assert result == "human"
    
def test_scissors_beats_paper():
    result = rps.evaluate_game("scissors", "paper") 
    assert result == "human"
    
def test_paper_beats_rock2():
    result = rps.evaluate_game("rock", "paper") 
    assert result == "computer"
    
def test_rock_beats_scissors2():
    result = rps.evaluate_game("scissors", "rock") 
    assert result == "computer"
    
def test_scissors_beats_paper2():
    result = rps.evaluate_game("paper", "scissors") 
    assert result == "computer"

"""
################## MONKEYPATCH #######################                
def input_faked_rock(prompt):
    print(prompt)
    return "rock"

def test_full_game(capsys, monkeypatch): #monkeypatch v argumentu je jen pro jeden test
    monkeypatch.setattr("builtins.input", input_faked_rock)
    rps.main()
    captured = capsys.readouterr()
    assert "rock, paper, scissors? " in captured.out
        
def input_faked_paper(prompt):
    print(prompt)
    return "paper"

@pytest.fixture    # pokud chci mit treba 20 testu, ktere budou testovat stejny monkeypatch,
#muzu si nastavit takto fixture - misto toho jak mam vyse monkeypatch 
def fake_input_rock(monkeypatch):  #fixture
    monkeypatch.setattr("builtins.input", input_faked_rock)
            
def test_full_game2(capsys, fake_input_rock): #monkeypatch je jen pro jeden test
    rps.main()
    captured = capsys.readouterr()
    assert "rock, paper, scissors? " in captured.out        
    
def input_faked_scissors(prompt):
    print(prompt)
    return "scissors"
    
def test_full_game3(capsys, monkeypatch): #monkeypatch je jen pro jeden test
    monkeypatch.setattr("builtins.input", input_faked_scissors)
    rps.main()
    captured = capsys.readouterr()
    assert "rock, paper, scissors? " in captured.out      

"""

################## DEPENDENCY INJECTION ##########################
def input_faked_rock(prompt):
    print(prompt)
    return "rock"
    
def test_full_game(capsys): 
    rps.main(input=input_faked_rock)
    captured = capsys.readouterr()
    assert "rock, paper, scissors? " in captured.out      
    
def input_faked_paper(prompt):
    print(prompt)
    return "paper"
    
def test_full_game2(capsys):
    rps.main(input=input_faked_paper)
    captured = capsys.readouterr()
    assert "rock, paper, scissors? " in captured.out     
    
def input_faked_scissors(prompt):
    print(prompt)
    return "scissors"
    
def test_full_game3(capsys):
    rps.main(input=input_faked_scissors)
    captured = capsys.readouterr()
    assert "rock, paper, scissors? " in captured.out     

################ SUBPROCESS ###################################

def test_wrong_play_results_in_repeated_question():
    cp = subprocess.run([sys.executable, 'rps.py'],  #"python" misto sys.executable
                        encoding="utf-8",
                        stdout=subprocess.PIPE, # chci to v citelne podobe pro python
                        input="dragon\nrock\n",
                        check=True)  # pokud program skonci chybou, test failne
    
    assert cp.stdout.count("rock, paper, scissors? ") == 2 #kolikrat se objevi otazka
    
""" NEFUNGUJE
def test_human_play_rock_computer_play_paper_results_in_computer_wins():
    cp = subprocess.run([sys.executable, 'rps.py'],  #"python" misto sys.executable
                        encoding="utf-8",
                        stdout=subprocess.PIPE, # chci to v citelne podobe pro python
                        input="rock\n",
                        check=True)  # pokud program skonci chybou, test failne
    if cp.stdout("rock"):
        assert cp.stdout.count("computer won") == 1
   
"""


        
