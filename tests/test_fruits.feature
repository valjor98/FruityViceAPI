Feature: Fetch and export fruits data to CSV

    # Implemented tests
    Scenario: Fetch fruits by family
        Given I have a valid base URL
        When I request fruits from the family "Rosaceae"
        Then I should receive a list of fruits from that family

    Scenario: Fetch fruits by genus
        Given I have a valid base URL
        When I request fruits from the genus "Malus"
        Then I should receive a list of fruits from that genus

    # other tests
    Scenario: Fetch fruits by ID range
        Given I have a valid base URL
        When I request fruits with ID range 1 to 10
        Then I should receive a list of fruits that fall within that ID range

    Scenario: Fetch fruits by family and genus
        Given I have a valid base URL
        When I request fruits from the family "Rosaceae" and genus "Malus" 
        Then I should receive a list of fruits that belong to both that family and genus

    Scenario: Fetch fruits by family, genus, and ID range
        Given I have a valid base URL
        When I request fruits from the family "Rosaceae" and genus "Malus" and ID range 1 to 10
        Then I should receive a list of fruits that belong to both that family and genus and be within range

    Scenario: Fetch all available fruits
        Given I have a valid base URL
        When I request all available fruits
        Then I should receive a list of all fruits

    Scenario: Invalid base URL
        Given I have an invalid base URL
        When I attempt to fetch fruits
        Then I should receive an error message

    Scenario: No fruits found
        Given I have a valid base URL
        When I request fruits from the family "NonExistentFamily"
        Then I should receive an empty list of fruits

    Scenario: Fetch fruits and validate CSV structure
        Given I have a valid base URL
        When I request fruits from the family "Rosaceae"
        Then the generated CSV file should have valid headers and rows

    Scenario: Fetch fruits by family and save on DB
        Given I have a valid base URL
        When I request fruits from the family "Rosaceae"
        Then I should receive a list of fruits from that family in the database