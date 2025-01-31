Feature: Youtube search bar

Scenario: working of search bar for a given query
    GIVEN user launches browser
    WHEN user opens youtube homepage
    WHEN user clicks on search bar and enters query "selenium"
    WHEN user clicks the search button with the query
    Then user should be redirected to the search results page
    And user should see videos related to "selenium"
    And close youtube