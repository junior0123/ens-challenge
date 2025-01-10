Feature: Manage folders Section

  @manage_folders @uc_005 @logout
  Scenario: Successful Access to "Manage folders" Section
    Given the user is logged in
    When the user clicks on the Manage Folders button
    Then the user is redirected to the Manage Folders page
    And the user sees the option to create a Folder

  @manage_folders @uc_006 @logout
  Scenario: Successful Folder Creation
    Given the user is logged in
    When the user clicks on the Manage Folders button
    And the user clicks on the Create new Folder button
    And the user enters the folder name "Test"
    And the user clicks the Save button
    Then the folder "Test" appears in the folder list

  @manage_folders @uc_007 @logout
    Scenario: Successful Folder Renaming
    Given the user is logged in
    When the user clicks on the Manage Folders button
    And the user clicks on the Create new Folder button
    And the user enters the folder name "Test"
    And the user clicks the Save button
    And the user is on the Folders section
    And the user clicks on the Edit option of the folder named "Test"
    And the user enters the new folder name "NewName" in the Name field
    And the user clicks the Save button
    Then the folder updates its name to "NewName"
    And a popup is displayed with the confirmation of the change
    And the folder appears in the list with the new name "NewName"

  @manage_folders @uc_008 @logout
  Scenario: Successful Folder Deletion
  Given the user is logged in
  When the user clicks on the Manage Folders button
  And the user clicks on the Create new Folder button
  And the user enters the folder name "Test"
  And the user clicks the Save button
  And the user is on the Folders section
  And the user clicks on the Delete option of the folder named "Test"
  And the user confirms the deletion by clicking the Delete button in the popup
  Then a message is displayed confirming the deletion
  And the folder named "Test" no longer appears in the list of folders
