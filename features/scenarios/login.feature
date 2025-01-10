Feature: Login
  @login @uc_001
  Scenario: Successful Login with valid credentials
  Given the user is on the login page
  When the user enters valid credentials
  And the user clicks on the Sign In button
  Then the user is redirected to the homepage
  And the user sees a message saying You are logged in as user

  @login @uc_002
  Scenario: Failed Login with invalid credentials
  Given the user is on the login page
  When the user enters invalid credentials
  And the user clicks on the Sign In button
  Then the user sees an error message
  And the user remains on the login page

  @login @successful_logout @uc_003
  Scenario: Successful Logout without any problem
  Given the user is logged in
  When the user clicks on the Account button
  And the user clicks on the Sign Out button
  Then the user sees a confirmation message saying You have been logged out successfully
  And the session is terminated

