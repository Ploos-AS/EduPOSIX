# 01 — From C to POSIX

## Learning objectives

Understand what POSIX adds to ISO C and how EduPOSIX classifies interfaces.

## Three layers

- **ISO C** defines the language and portable standard library.
- **POSIX** specifies operating-system interfaces shared by Unix-like systems.
- **Linux-specific** interfaces are useful but are not automatically portable to other POSIX systems.

## First lab

Build and run `examples/getpid/getpid.c`. Identify which included header and function come from POSIX rather than ISO C.

## Checkpoint

Explain why a program can be valid C while still not being a portable POSIX program, and why a POSIX program can still contain Linux-specific code.
