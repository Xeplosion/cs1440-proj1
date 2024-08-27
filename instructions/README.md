# CS 1440 Project 1: Tic-Tac-Toe - Instructions

Since you are still new to using Git, refer to the **Using Git** section of the lecture notes when you need help remembering which command to use to push your work to the server.

Previous Semester Statistics     | Fall 2023 | Spring 2024
--------------------------------:|:---------:|:---------------
Average Hours Spent              | 7.225     | 7.34  
Standard Deviation Hours         | 3.753     | 4.013 
% students thought this was Easy | 21.2%     | 13.4% 
... Medium                       | 40.4%     | 43.8% 
... Hard                         | 26.0%     | 33.3% 
... Too Hard/Did not complete    | 12.5%     | 9.4%  


**You may use AI tools** such as ChatGPT or GitHub Copilot to assist with code and documentation

*   If you do this, explain in your Software Development Plan *which* tools were used, *where* they were used, and *how* they were used
*   Use comments to *clearly* identify which portions of source code were written by the tool
*   Failure to document use of these tools will be regarded as a **violation of academic integrity** and I will pursue sanctions
    *   The same applies to any other resources from outside the class


*   [How to Do This Project](#how-to-do-this-project)
    *   [Phase 0: Requirements Analysis](#phase-0-requirements-analysis)
    *   [Phase 1: Design](#phase-1-design)
    *   [Phase 2: Implementation](#phase-2-implementation)
    *   [Phase 3: Testing and Debugging](#phase-3-testing-and-debugging)
    *   [Phase 4: Deployment](#phase-4-deployment)
    *   [Phase 5: Maintenance](#phase-5-maintenance)
*   [Hints](#hints)
*   [What We Look for When Grading](#what-we-look-for-when-grading)


## How to Do This Project

This project is larger than homework projects in CS 1400 and CS 1410. Do not try to complete this in one sitting.

The flaw in this program is that the optimal AI can lose.  It is your job to find out why.  You will uncover the causes as you study the documentation and the code.  Apart from the AI bug, I am confident this program works as intended.  If you see anything else which looks wrong, **just leave it alone**.  I will make a public announcement if another serious issue is discovered.


### Phase 0: Requirements Analysis
*(20% of your effort)*

0.  Read the [Project Requirements](./Project_Requirements.md) to understand what the project is about.
1.  Study the *Software Development Plans* written by the previous teams to learn what they accomplished.
    *   [AI team's SDP](./AI_Team_Plan.md)
    *   [Game Engine team's SDP](./Engine_Team_Plan.md)
    *   You should understand these documents well enough to find your way around the source code.
    *   Use an AI chat bot (i.e. ChatGPT, Gemini, Claude, Mistral) to assist you with these documents.
    *   Pay special attention to the test cases the previous teams wrote.  After you fix the bug, use these tests to verify your solution.
2.  Run the program several times to identify which functions perform what actions.
    *   Stepping through the program in the debugger is one way to do this.
3.  This project starts with **one** Python file that contains all of the code.
    *   Reorganize the functions into **four** modules.  This will make it easier to understand the program and spot the bug:
        1.  `ttt.py` - the main entry point of the program.
            *   This file will consist of a few import statements and a `__name__ == '__main__'` block.
            *   No functions are defined in this module (i.e. the `def` keyword does not appear in this file).
        2.  `interface.py` - contains functions that take input from the user and create colorful output.
            *   This is the *only* file where the `input()` function is directly called.
            *   Many (but not all) functions that use `print()` belong in this module.
            *   Functions that return *terminal escape sequences* belong here, as do functions that deal with colors.
            *   This module *should not* import any other modules; this helps prevent *circular import* errors.
        3.  `ai.py` - contains the *Look Up Table* (LUT) and the strategy functions which power the CPU opponent.
            *   The strategy functions have names beginning with `strategy_`.
            *   Functions that examine or manipulate the game board do not belong here, but should be imported from another module.
        4.  `engine.py` - is home to functions that drive the main game loop, deal with the game board, or don't belong anywhere else.
            *   There are four different game loops, one for each mode
                1.  CPU vs. CPU
                2.  human vs. CPU
                3.  CPU vs. human
                4.  human vs. human
            *   Code in this module *may* print messages with the help of functions imported from `interface.py`.
            *   Functions that call `input()` do not belong in this module.
            *   Some functions belonging to this module will need to be modified if the format of the game board changes.
    *   Consider every function on its own merits.  Don't keep functions together simply because they were neighbors in the original program.
4.  Fill out **Phase 0** in Plan.md; explain in your *own words* what the program does, how it does it, and what changes you have made so far.
    *   For each function in the program, write one sentence to explain where you placed it and why you think it belongs there.
    *   You will have uncovered redundant and/or duplicated functions.  Answer these questions in the document:
        *   Are these functions exact copies of each other, or is there some difference between them?
        *   Do they agree with how the game's state is kept?
        *   Are there any unnecessary functions?
            *   Do not delete anything now!  Just write down their names and why you think they aren't needed.
5.  The program will no longer work after you finish remodeling it.  Do not despair!  It might feel like you are getting farther away from the goal, but you are making progress.  As the saying goes, *you can't make an omelette without breaking eggs*.  You will tackle the new problems you created in the next phase.  This is a good time to take stock of your situation and understanding of the project.  Here is a preview of the errors you will find:
    *   Moving functions into different modules will result in error messages like this:
        ```
        NameError: name 'logo' is not defined
        ```
        It will be necessary to add `import` statements to restore the program to functionality.
        *   Take care to avoid *circular imports*, which lead to error messages like this:
            ```
            ImportError: cannot import name 'show' from partially initialized module 'interface' (most likely due to a circular import)
            ```
            Circular imports happen when a module ends up importing itself.  For example, a circular import occurs when interface.py imports `engine`, and engine.py imports `interface`.
        *   Circular imports are resolved by breaking the cycle by creating a module that does not import anything else.
6.  Take the **Starter Code Quiz** on Canvas.
    *   Do not worry if you can't answer all of the questions yet
    *   You can re-take the quiz as many times as you want before the project is due
7.  Track your time in Signature.md.
8.  Commit your changes to Git.  Make sure to add untracked files to the repository with `git add`.  Run `git status` to identify such files and check that they are ready to commit.


### Phase 1: Design
*(30% of your effort)*

0.  Resolve the `NameError`s so the program works as well as it did before.
    *   What was the point of all of that work if you're right back where you started?
    *   Now you have seen all of the code and have a better understanding of how and why it works.
1.  Turn back to the duplicated functions you discovered and ponder these questions:
    *   *Why were there two versions of these functions?*
    *   *What does this tell you about each team's conception of the game?*
    *   *How can you untangle the mess they created?*
        *   There are two obvious ways to fix this program:
            1.  Rewrite the functions that embody faulty assumptions about how the game state should be tracked in the program.  Identify the smallest subset of functions that are wrong to avoid rewriting the entire program.
            2.  Write one or two *adapter* functions to translate the game state representation back and forth as needed.
    *   Write answers to these questions in **Phase 1** of Plan.md.
2.  Once you've decided how to fix the problem, sketch out the new/improved functions in *pseudocode* in **Phase 1** of Plan.md.
    *   Walk through the pseudocode in your head, with a pad of paper or a whiteboard to convince yourself that your changes will work.
    *   You may use AI tools to help you understand what each function does.
3.  Consider if any new test cases could be created to ensure the new program will perform correctly.
4.  You should be able to get 100% on the **Starter Code Quiz** by now.
5.  Track your time in Signature.md.
6.  If you haven't already added and committed your changes to Git, this is a good time to do so.


### Phase 2: Implementation
*(15% of your effort)*

0.  You will want to to delete redundant and useless functions.  Before you delete anything, consider:
    *   Are you confident that you know *which* functions should be removed?
    *   Unused AI strategy functions can be kept for testing.
    *   Unused color functions may be kept for future development.
1.  Carefully apply the changes you designed to the source code.  Be patient and take your time.
    *   Don't neglect to rewrite code comments when you change the code they describe.
    *   It is normal to introduce new bugs as you go.  Here are some hints:
        *   Rename variables and functions to improve the readability of the program.  Good names make it easy to spot bugs.
        *   While testing the CPU player set `CPU_DELAY` to a smaller value to speed things up.  Remember to restore it to the original value before you turn in the project.
        *   It is very likely that you will encounter *off-by-one* errors.  Think hard and run lots of tests before you try to fix these.
        *   If you make a change but don't see the result, take another look for duplicated functions.
        *   If you rename a function or add a new function, you may need to add or update your `import` statements.
        *   Ask for help before you get overwhelmed!
        *   Frequently commit your work to Git.  It makes it easier for us when you come for help.
2.  If you think that your changes made things worse, go back to **Phase 1** and design a new approach.  Ask the instructor and TAs for help with Git if you want to undo some of your changes.
3.  If you use AI tools in this phase, be sure to:
    1.  **Cite your sources**
    2.  **Understand why the code works**
    3.  **Make sure your entire program [follows the rules](#what-we-look-for-when-grading)**
    4.  Remember that *how* you arrive at the solution is more important than solving the problem.
4.  By the end of this phase the program is runnable.
    *   **Do not** move on if your program crashes regularly!
5.  Track your time in Signature.md and commit your changes to Git.


### Phase 3: Testing and Debugging
*(30% of your effort)*

0.  Run through the test cases documented by the previous teams in their software plans.
1.  Run through any new test cases that you devised.
2.  If you found bugs in this phase, explain what was wrong and how you fixed it.
3.  Track your time in Signature.md and commit your changes to Git.


### Phase 4: Deployment
*(5% of your effort)*

It is your responsibility to ensure that your program will work on your grader's computer.

*   Code that crashes and *cannot* be quickly fixed by the grader will receive **0 points** on the relevant portions of the rubric.
*   Code that crashes but *can* be quickly fixed by the grader (or crashes only *some* of the time) will receive, at most, **half-credit** on the relevant portions of the rubric.

The following procedure is the best way for you to know what it will be like when the grader runs your code:

0.  Review [How to Submit this Project](./How_To_Submit.md) and make sure that your submission is correct.
1.  Push your code to GitLab, then check that all files and commits are there.
2.  Clone your project into a *different directory* on your computer and re-run your test cases.


### Phase 5: Maintenance

**Before The Due Date**

0.  Review Signature.md and Plan.md one last time.
1.  Make one final commit and push your **completed** Signature.md to GitLab.
2.  Make sure that you are happy with your **Starter Code Quiz** score.

**After You Submit (Can Happen After The Due Date)**

0.  Respond to the **Project Reflection Survey** on Canvas.



## Hints

Here are some tips for when you think you've found the bug in Tic-Tac-Toe but are unsure of the next steps.

*   Don't bother looking for a bug in the LUT.
    *   The bug is that there is an `if` statement that never selects the alternate path.
*   Read both the AI and Engine teams' plans before debugging the program.
    *   After you find the bug, take another look at those documents.  What assumptions does each team make about the game board?
*   After you learn about the REPL and print statement debugging, consider how you can use these techniques to answer the question "why does this happen?"
*   When you re-arrange functions into separate modules, **do not delete anything**.
    *   Instead of deleting unused functions, rename them to make it clear that they are useless:
        *   ```python
            def full(board):
            ```
        *   becomes...
        *   ```python
            def UNUSED_full(board):
            ```
    *   Only delete the `UNUSED_` functions after you are positive that the program works correctly without them.
*   In the past students have lost important pieces of the puzzle when re-arranging the code into modules.  While it is possible to recover the missing code with Git, at this point you haven't been taught all of the necessary commands.
    *   If have lost an important bit of code, you can find it by looking at the original version of ttt.py in my repository: https://gitlab.cs.usu.edu/duckiecorp/cs1440-falor-erik-proj1/-/blob/master/src/ttt.py
    *   As you know, this is a very long file.  Be patient as it will take several seconds to load from the server.



## What We Look for When Grading

**Total points: 90**

*   Repository Structure (10 points)
    *   `.gitignore` is correct and no forbidden files or directories are present
    *   The repository is a clone of the starter code
    *   The repository's GitLab URL follows the naming convention
    *   All required files and directories are in their expected locations
    *   There is at least one Git commit per phase of the project.
*   Quality documentation (15 points)
    *   Plan.md
        *   Each section filled out with a convincing level of detail
        *   No code is pasted from the source files
*   Time management (5 points)
    *   Signature.md contains accurate information about the time you spent on this project
        *   The time reported on the **TOTAL** entry is the sum of the daily entries
    *   The *TODO* message and the placeholder entries have been removed
*   Code quality (40 points)
    *   Functions are organized into the correct modules
    *   No useless variables or constants remain
    *   Useless functions are removed
        *   Exceptions
            *   Unused AI strategy functions *may* be kept for testing
            *   Unused color functions *may* be kept for future development
        *   No duplicated or redundant code remains; each function is present in only one module
    *   Doc strings and comments match the code they describe
    *   Import statements are reasonable
        *   No useless import statements are present
        *   Program *does not* import any modules **except**:
                *   `random`
                *   `time`
                *   `typing`
                *   modules you wrote yourself
        *   No import statement fail due to misspelling or incorrect capitalization.
            *   **Windows users** make sure that the capitalization of file names on GitLab match your `import` statements!
        *   No imports involve the `src.` package; this is the result of a PyCharm misconfiguration
*   Program behavior (20 points)
    *   AI opponent is unbeatable
        *   CPU vs. CPU matches always end in a draw
        *   Human vs. CPU matches end either in a draw or CPU victory
    *   Existing good behavior of program is preserved
        *   The user interface and appearance is unchanged from the starter code
        *   The Easter Egg is still accessible just as it was in the original program
    *   No new bugs
        *   Program doesn't crash
        *   Illegal user input is detected by the program and an appropriate error message is displayed
    *   All test cases work as expected
