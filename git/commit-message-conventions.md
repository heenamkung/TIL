# Commit Message Conventions

## Single line commit messages
* Can be executed simply with `git commit -m "Do something"`.
* Capitalize first character.
* Less than 50 characters is best.
* Do NOT end with a period.
* Use imperative mood. Do NOT use past tense. Easy way to do this is by adding "if applied, this commit will" in front of commit message. For example "if applied, this commit will Fix typos".

## Multi line commit messages
* Write message in proper text editor as `-m` is not suitable for it.
* Messages are divided into subject (title) and body.
* Follow Single line commit message convention for subject.
* Separate body and subject with a blank line. `git log --online` or `git shortlog` utilizes this by showing only the subject line.
* Body should contain what, why and how.

```
Simplify serialize.h's exception handling

Remove the 'state' and 'exceptmask' from serialize.h's stream
implementations, as well as related methods.

As exceptmask always included 'failbit', and setstate was always
called with bits = failbit, all it did was immediately raise an
exception. Get rid of those variables, and replace the setstate
with direct exception throwing (which also removes some dead
code).

As a result, good() is never reached after a failure (there are
only 2 calls, one of which is in tests), and can just be replaced
by !eof().

fail(), clear(n) and exceptions() are just never called. Delete
them.
   ```

## Sources
https://cbea.ms/git-commit/#why-not-how

https://github.com/joelparkerhenderson/git-commit-template