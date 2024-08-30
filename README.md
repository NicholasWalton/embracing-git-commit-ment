# Embracing `git commit`-ment

Have you ever put off `git commit` because your code "wasn't clean enough", "doesn't have tests", or "doesn't compile"?

In this workshop, we'll practice techniques for cleaning history between `commit` and `push` so that you can commit more often with less thought. I'll share some of the techniques I use to clean up a few (dozen) commits of varying quality.

- [Summary](#summary)
- [Before you start](#before-you-start)
  - [Prerequisites](#prerequisites)
  - [Preparation](#preparation)
  - [Using the aliases](#using-the-aliases)
- [Workshop](#workshop)
  - [Scenario](#scenario)
  - [Step-by-step](#step-by-step)
- [Solutions](#solutions)
- [Follow-up](#follow-up)
- [Acknowledgments](#acknowledgments)

## Summary

We will cover:

- `git add --patch`,
- `--amend`, `--squash`, and `--fixup`,
- and `git rebase --interactive` with both `--autosquash` and `--exec`

so that you can `git commit` now and (over)think later!

## Before you start

### Prerequisites

For this workshop, please have a recent version of Git (>=2.35?) in a bash-like shell ready. If you are on Windows, Windows Terminal with `git-bash` or WSL should be fine. (PowerShell or CMD may overstrain your facilitator's humble faculties).

### Preparation

If you don't use command-line Git on a regular basis, you may want to do the first two exercises in [Version Control (Git) · Missing Semester (mit.edu)](https://missing.csail.mit.edu/2020/version-control/) before this workshop. Skimming the video and notes may also be helpful.

You may find this workshop unnecessary if you regularly use the features documented in [Git - Rewriting History (git-scm.com)](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History) and are comfortable with [git rebase: what can go wrong? (jvns.ca)](https://jvns.ca/blog/2023/11/06/rebasing-what-can-go-wrong-/).

### Using the aliases

For convenience, helpful git aliases including `git lol` and `git lola` are provided in `project.gitconfig`. Do:

```bash
git config --local include.path ../project.gitconfig
```

to add them to your local repo.

## Workshop

### Scenario

You've been tasked with creating a file containing the first few values of the Fibonacci sequence and appropriate tests.
Late yesterday, you got to "mostly done" (perhaps). Today, you need to fix any remaining bugs and clean up your commit history before opening a PR.

### Step-by-step

1. Create your branch from yesterday: `git switch -c my-branch origin/main`
2. Inspect your work, then do a rebase to incorporate the fixes you've made:
    ```bash
    git lol --patch origin/base..HEAD
    git rebase --interactive --autosquash origin/base
    ```
    When prompted to edit the commit message for the `squash!`, comment out any lines that shouldn't be part of your final history.
3. Correct your copy-paste error by changing:
    ```python
    self.assertEqual(len(triples), len(self.values) - 1)
    ```

    to

    ```python
    self.assertEqual(len(triples), len(self.values) - 2)
    ```

    and `git add`.

    Since this only affects your most recent commit (check `git lol -1 --patch`), just `git commit --amend` this change.

4. Run the tests by `./test_fib.py` and fix the mistakes you find. 
   (Change `self.assertLess()` to `self.assertLessEqual()` and correct the final line in `fib.txt`.)

5. Use `git add --patch` to stage the change to `test_fib.py`.

6. Use `git annotate HEAD -- test_fib.py` to determine which commit to fix, then do `git commit --squash <commit hash>` and include an updated commit message below the `squash! ...` line.

7. Use `git add -p` (short for `--patch`) to stage the change to `fib.txt`.

8. Use `git annotate HEAD -- fib.txt` to determine which commit to fix, then do `git commit --fixup <commit hash>`.

9. Apply your fixes by rebasing again.

10. Reorder commits: use `git rebase --interactive` to move the `test_fib.py` changes to the beginning of your history.

11. Do `git rebase --interactive origin/base --exec './test_fib.py'` to verify that each of the corrected commits passes all the tests.

## Solutions

The `final` branch contains all needed commits. The `solution` branch is fully rebased and tested.

## Follow-up

- Try splitting a commit into two or more commits (see [Git - Rewriting History (git-scm.com)](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History) for details)

- Try some convenience tooling such as:

  - [`git undo` with git-branchless](https://github.com/arxanas/git-branchless?tab=readme-ov-file#about)
  - [inline `amend` with lazygit](https://github.com/jesseduffield/lazygit?tab=readme-ov-file#amend-an-old-commit)

## Acknowledgments

Thanks to Anna and swan for inspiring this workshop and to Tool Talkers Wolf, Ryan, and Clint for their input.
