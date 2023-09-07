Feature: Fetch and export fruits data to CSV

  Scenario: Fetch fruits by family
    Given I have a valid base URL
    When I request fruits from the family "Rosaceae"
    Then I should receive a list of fruits from that family

  Scenario: Fetch fruits by genus
    Given I have a valid base URL
    When I request fruits from the genus "Malus"
    Then I should receive a list of fruits from that genus
