Feature: Youtube landing page logo

Scenario: Logo presence on youtube landing page
    Given launch browser
    When user is not youtube landing page
    When presence of logo is verified
    Then close youtube browser