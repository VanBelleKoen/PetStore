@wip
Feature: Modification pet Creation

    Background: No pet with those Id's found
        Given The database is cleared

    Scenario: Create New Pets
        Given Create a new pet
        Then The new pet can be found
        When Modify the new pet
        Then The modified pet can be found