Resolves #873

#### Describe the changes you have made in this PR -
- Moved `Notion` and `Prefect` clients from `app/integrations/clients/` to `app/services/`.
- Added backward-compatible shims in the old locations to prevent breaking existing imports.

## Code Understanding and AI Usage
- [ ] No, I wrote all the code myself
- [x] Yes, I used AI assistance (continue below)

**If you used AI assistance:**
- [x] I have reviewed every single line of the AI-generated code
- [x] I can explain the purpose and logic of each function/component I added
- [x] I have tested edge cases and understand how the code handles them
- [x] I have modified the AI output to follow this project's coding standards and conventions

**Explain your implementation approach:**
External service clients belong in `app/services/` rather than the integration layer. I relocated them and provided shims that issue a `DeprecationWarning` when imported from the old path.

## Checklist before requesting a review
- [x] I have added proper PR title and linked to the issue
- [x] I have performed a self-review of my code
- [x] **I can explain the purpose of every function, class, and logic block I added**
- [x] I understand why my changes work and have tested them thoroughly
- [x] I have considered potential edge cases and how my code handles them
- [x] My code follows the project's style guidelines and conventions
