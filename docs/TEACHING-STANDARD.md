# Teaching standard

Every substantive chapter should aim to contain:

1. **Why this matters** — the problem before the mechanism.
2. **Learning objectives** — observable skills, not vague familiarity.
3. **Mental model** — what the learner should picture happening.
4. **Small complete example** — buildable code rather than disconnected fragments where practical.
5. **Walkthrough** — explain important lines and choices.
6. **Under the hood** — memory, ABI, OS or machine behavior when pedagogically useful.
7. **Common mistakes** — including compiler diagnostics and failure modes.
8. **Exercises** — from modification to independent implementation.
9. **Checkpoint** — a concise test of understanding.
10. **Further exploration** — optional deeper material.

## Code quality

Examples favor clarity over cleverness. Warnings are treated seriously. Unsafe patterns may be demonstrated for analysis, but must be clearly identified and followed by the safe/correct approach.

## Learning by observation

Learners should be encouraged to change programs, predict behavior, compile, run, debug and inspect results. When a concept becomes clearer by looking at generated assembly or memory layout, the course should do so rather than hiding the machine.

## Reproducibility

Examples used as milestones should have automated build/run checks whenever the target environment permits it.
