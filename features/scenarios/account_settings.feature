Feature: Account Settings Management

  @change_account_information @uc_012 @logout
  Scenario: Successful Update of Account Information
    Given the user is logged in
    When the user clicks on the Account button
    And the user selects the Settings option
    And the user updates the first name to "John"
    And the user updates the last name to "Doe"
    And the user updates the email to "john.doe@example.com"
    And the user clicks the save button
    Then the user sees a confirmation pop-up indicating the changes have been saved

