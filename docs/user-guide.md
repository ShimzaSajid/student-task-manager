# User Guide

## Starting the app
Run `python main.py`. A menu appears with five options.

## 1. Add task
Type a title and press Enter. Empty or space-only titles are rejected with an error message.

## 2. View tasks
Shows all tasks with their ID. `[ ]` means pending and `[x]` means completed.

## 3. Complete task
Enter the ID of a task to mark it completed. An unknown or non-numeric ID shows an error.

## 4. Delete task
Enter the ID of a task to remove it. An unknown or non-numeric ID shows an error.

## 5. Exit
Closes the application. Tasks are kept in memory only, so they are lost on exit.