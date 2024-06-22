Feature: Test Star Wars API People Endpoint

  Scenario: Get details of a person by ID
    Given the SWAPI API is available
    When I request the details for person with ID 1
    Then the response status should be 200
    And the response should contain the name "Luke Skywalker"
