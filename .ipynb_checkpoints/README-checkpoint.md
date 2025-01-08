![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Lab | Git Practice: About Me for AI Engineering, Data Analytics & Data Science Students

## Lab Objectives

- Understand the basic Git workflow: fork, clone, commit, push, and create a pull request (PR).
- Write a personal introduction using Python in a Jupyter Notebook.
- Practice submitting work using GitHub.

## Instructions

1. **Fork the Repository**:
   - You are already in the GitHub repository you want to fork.
   - Click the **Fork** button in the upper right corner of the page.
     - Remember, this creates a copy of the repository under your own GitHub account.
   - Confirm that the repository now appears in your account, showing your username in the repository name (e.g., `username/repository-name`).

2. **Clone the Forked Repository**:
   - Navigate to your forked repository on GitHub (you should be already there but make sure you are not still in the original repository you should've forked already)
   - Click the **Code** button and copy the HTTPS or SSH URL.
   - Open your terminal or command prompt and navigate to the directory where you want to store the repository (for now you can even do it on your Desktop).
   - Run the following command to clone the repository:
     ```bash
     git clone <repository-url>
     cd repository-name
     # cd lab-git-practice-data-ai
     ```

3. **Work on the Lab: Edit the Notebook**:
   - Open the repository in your code editor (e.g., VS Code).
   - Open the `about-me.ipynb` file in Jupyter Notebook.
   - Fill in the Python variables:
     ```python
     name = "Jane Doe"
     reason = "I want to learn AI to solve real-world problems like automating processes."
     fun_fact = "I enjoy hiking and working on side projects with Python!"
     ```
    - Run the Notebook: Execute the code cell to display your introduction.
    - Save the updated notebook.

4. **Commit Your Changes**:
   - Stage your changes:
     ```bash
     git add about-me.ipynb
     ```
   - Commit the changes with a meaningful message:
     ```bash
     git commit -m "Added my personal introduction to about-me.ipynb"
     ```

5. **Push Your Changes**:
   - Push your changes directly to your **forked** repository:
     ```bash
     git push
     ```

6. **Create a Pull Request**:
   - Navigate to your forked repository on GitHub.
   - Click **Compare & pull request**.
   - Ensure the base repository is the original repository and the base branch is `main`.
   - Add a title and description for your PR:
     - Example Title: `Lab X Solution Submission`
     - Example Description: *"This pull request includes short summary about myself."*
   - Click **Create Pull Request**.


## Lab Submission Requirements

- Share link to your Pull Request in the submission field on Student Portal.

<br>

## Daily Process for Labs :rocket:

Students will repeat the above steps for each new lab:

1. Fork the original repository (if not already done).
2. Clone the repository (only needed the first time).
3. Work on the lab, commit the changes, and push to their fork.
4. Submit a pull request to the original repository.
5. Paste the URL to your Pull Request in the submission field on Student Portal.