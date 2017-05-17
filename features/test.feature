Feature: Win game in battle ship

  Scenario: Open main page
    Given I open battleship main page
    Then I should see main title

  Scenario: Play a game
    Given I place ships randomly
    Given I click start
    Given I wait for opponent
    Then I use algorythm
    Then I should win