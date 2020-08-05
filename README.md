# python-side-projects

I wrote simple python scripts to solve some real problems in work:

> Note: My scripts use python3.

- [insert-string.py](/insert-string.py): Append a string (or insert a line) to all markdown files in a given folder

- [find-string.py](/find-string.py): Walk through all markdown files in a given folder and check if each of the file links is in another file (e.g. TOC.md)

- [Adding] Walk through all markdown files in a given folder and print the files that contain or do not contain a specific string

- [Adding] Track all github issues and pull requests in Google Sheet

- [TODO]「Can be a CI integration」 Check all github pull requests that are opened before a specific date and do not have a label that matches the pattern `translation/xxx`

- [TODO]「Can be a CI integration」 Check the aliases in all markdown files and see if there is any duplicate item like [this](https://github.com/pingcap/docs-cn/pull/4109/files#diff-33d7f29af3c798935116f4588fda0824R3).

- [TODO]「Can be a CI integration」 Check if the changed files in a PR include any deleted/relocated/renamed file. If so, check if any alias exists in the PR changes. And if not, CI check fails.

- [TODO]「Can be a CI integration」 Check if the changed files in a PR include any newly added file. If so, check if the doc link exists in TOC.md. And if not, CI check fails.
