name: middle
class: middle
layout: true

---
class: center, inverse
# Embracing `git`
# `commit`-ment

---
## Embracing `git commit`-ment
Have you ever put off committing because your code "wasn't clean enough", "doesn't have tests", or "doesn't compile"?

---
class: center, inverse
## Commit more often with less thought!

???
Today we are going to build our skills so that we can commit fearlessly without overthinking!

---
## When to rewrite history?

- Tests are failing
- Commit is too big, incomplete, excessive
- Coded tired

???
When should we rewrite history?
When tests are failing
When a commit is
- too big to understand
- missing a relevant change
- has stray comments, dead code, or other onise
When we were coding tired

---
## When to leave history as-is?

- Reality has changed
- Already published

???
If the requirements have changed, the history should reflect that decision - you'll see this in the workshop scenario.
If other people have checked out the branch, rewriting history is likely to cause confusion.

---
class: center, inverse
## Embrace 
## "Stream of Consciousness"
## commits

???
While I was preparing this workshop, Ryan referred to their workflow as "commit a stream of conciousness, then clean up later". I really like this.

---
## Scenario

- First few values of the Fibonacci sequence
- Tests
- Status: Mostly done

## To Do:
- Fix any remaining bugs
- Clean up your commit history

???
You've been tasked with creating a file containing the first few values of the Fibonacci sequence and appropriate tests.
Late yesterday, you got to "mostly done" (perhaps).
Today, you need to fix any remaining bugs and clean up your commit history before opening a PR.

---
## Getting the `git lol` alias

Include provided `project.gitconfig` in your `.git/config`:

```bash
git config --local include.path ../project.gitconfig
```

???
For convenience, useful git aliases are provided in `project.gitconfig`. Use this command to include them into your local repository.

---
class: center, inverse
# Demo: Getting Started

???
I'm going to walk through the first steps now to explain what they look like and what they mean.

```
git checkout -b my-branch
git lol --patch origin/base..HEAD
git config --local include.path ../project.gitconfig
git rebase --interactive --autosquash origin/base
```

---
## Getting Started

```bash
git checkout -b my-branch
```

Inspect your work:
```bash
git lol --patch origin/base..HEAD
```

Rewrite History!
```bash
git rebase --interactive --autosquash origin/base
```
- `squash!` commit message: comment out unwanted lines

---
class: center
# Preliminary Q&A

---
## Continue independently

Follow the step-by-step in the README

Ask for help!

???
If you run into any trouble, please share your screen so we can learn together.

---
layout: false
## Amend a copy-paste error

Change

```python
self.assertEqual(len(triples), len(self.values) - 1)
```

to

```python
self.assertEqual(len(triples), len(self.values) - 2)
```

Since this only affects your most recent commit (check `git lol -1 --patch`), just `git commit --amend` this change.

---
## Fix tests

`./test_fib.py` to run the tests

Suggested fixes:

- Change `self.assertLess()` to `self.assertLessEqual()`
- Correct the final line in `fib.txt`

---
## Commit `fib.txt` fix

`git add --patch` to stage the change to `fib.txt`

`git annotate HEAD -- fib.txt` to determine which commit to fix

`git commit --fixup <commit hash>`

---
## Commit `test_fib.py` fix

`git add --patch` to stage the change

`git annotate HEAD -- test_fib.py` to determine which commit to fix

`git commit --squash <commit hash>`

(write an updated commit message below the `squash! ...` line)

---
## Rewrite History!

Inspect your work:

```bash
git lol --patch origin/base..HEAD
```

Autosquash your fixes into history:

```bash
git rebase --interactive --autosquash origin/base
```

---
## Reorder commits

Use
```bash
git rebase --interactive
```
to move the `test_fib.py` changes to the beginning of your history.

---
## Run tests on each commit

Verify that each of the corrected commits passes all the tests by doing:


```bash
git rebase -i origin/base --exec './test_fib.py'
```

---
class: middle, center
# More Q&A

---
class: inverse, middle, center
# Other Git challenges?

---
## Follow-up

- Try splitting a commit into two or more commits (see [Git - Rewriting History (git-scm.com)](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History) for details)

- Try some convenience tooling such as:
  - [`git undo` with git-branchless](https://github.com/arxanas/git-branchless?tab=readme-ov-file#about)
  - [inline `amend` with lazygit](https://github.com/jesseduffield/lazygit?tab=readme-ov-file#amend-an-old-commit)

---
class: middle
### Thanks!

Inspiration: swan and Anna

Tool Talk Time: Wolf, Ryan, and Clint

???
I'd like to thank swan and Anna for inspiring this workshop.
And the Tool Talkers helped me get the ideas in order.

Thank you!