Feature: Manage To-Do Items Section

  @manage_to_do_items @uc_004 @logout
  Scenario: Successful Access to "Manage To-Do Items" Section
    Given the user is logged in
    When the user clicks on the Manage To-Do Items button
    Then the user is redirected to the Manage To-Do Items page
    And the user sees the option to create a new to do item

  @manage_to_do_items @uc_009 @logout
  Scenario: Successful Creation of a To-Do Item
    Given the user is logged in
    When the user clicks on the Manage Folders button
    And the user clicks on the Create new Folder button
    And the user enters the folder name "Test"
    And the user clicks the Save button
    And the user saves the folders id of "Test" folder
    And the user clicks on the Home button
    And the user clicks on the Manage To-Do Items button
    And the user clicks on the Create new To-Do Item button
    And the user enters the title "NewTask" in the title field
    And the user enters the description "This is a test task" in the description field
    And the user selects the folder "Test" for the to-do item
    And the user clicks the Save button
    Then the to-do item "NewTask" appears in the to-do items list

  @manage_to_do_items @uc_010 @logout
  Scenario: Successful Deletion of a To-Do Item
    Given the user is logged in
    When the user clicks on the Manage Folders button
    And the user clicks on the Create new Folder button
    And the user enters the folder name "Test"
    And the user clicks the Save button
    And the user saves the folders id of "Test" folder
    And the user clicks on the Home button
    And the user clicks on the Manage To-Do Items button
    And the user clicks on the Create new To-Do Item button
    And the user enters the title "NewTask" in the title field
    And the user enters the description "This is a test task" in the description field
    And the user selects the folder "Test" for the to-do item
    And the user clicks the Save button
    And the user clicks on the Delete option of the to do item named "NewTask"
    And the user confirms the deletion by clicking the delete button in the popup
    Then a message is displayed confirming the deletion
    And the to do item named "NewTask" no longer appears in the list of to do items

  @manage_to_do_items  @uc_011 @logout
  Scenario: Successful Editing of a To-Do Item
    Given the user is logged in
    When the user clicks on the Manage Folders button
    And the user clicks on the Create new Folder button
    And the user enters the folder name "Test"
    And the user clicks the Save button
    And the user saves the folders id of "Test" folder
    And the user clicks on the Home button
    And the user clicks on the Manage To-Do Items button
    And the user clicks on the Create new To-Do Item button
    And the user enters the title "NewTask" in the title field
    And the user enters the description "This is a test task" in the description field
    And the user selects the folder "Test" for the to-do item
    And the user clicks the Save button
    And the user clicks on the edit option of the to do item named "NewTask"
    And the user updates the title to "UpdatedTaskTitle"
    And the user updates the description to "UpdatedTaskDescription"
    And the user clicks the Save button
    Then the to-do item "TaskToEdit" no longer appears in the to-do items list
    And the user sees a confirmation message indicating the changes were successful
    And a to-do item named "UpdatedTaskTitle" appears in the list with the updated data
