Feature: OrangeHRM logo

Scenario: logo presence on the OrangeHRM portal 
    Given launch chrome browsers
    When open OrangeHRM homepage
    When verify presence of logo on homepage
    Then close browser 