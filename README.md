# EduPOSIX

**Systems programming in C for POSIX, with Linux as the primary reference platform.**

EduPOSIX builds on [EduC](https://github.com/Ploos-AS/EduC) and teaches how real programs interact with a POSIX operating system.

The course deliberately distinguishes between **ISO C**, **POSIX**, and **Linux-specific interfaces** so learners understand both portability and platform-specific power.

## Prerequisites

Learners should first be comfortable with the material in EduC, especially pointers, structs, memory, files, multi-file programs, debugging, and undefined behavior.

## Goals

By the end of the course, the learner should be able to:

- use POSIX file descriptors and low-level I/O
- understand processes, `fork()`, `exec()` and process lifecycles
- use pipes, signals and other IPC mechanisms
- work with terminals and pseudo-terminals
- write network programs with sockets
- use threads and synchronization primitives
- build daemons and long-running services
- understand permissions, users, groups and process credentials
- debug system programs with tools such as gdb, strace and sanitizers
- write robust programs that handle partial I/O, interruption and failure correctly
- recognize where Linux APIs extend beyond POSIX

## Course structure

1. From ISO C to POSIX
2. The Unix process model
3. File descriptors and low-level I/O
4. Files, directories and metadata
5. Permissions, users and groups
6. Processes and process creation
7. `exec()` and program loading
8. Waiting, exit status and process trees
9. Signals
10. Pipes and FIFOs
11. IPC overview
12. Memory mapping and shared memory
13. Terminals and job control
14. Sockets and network programming
15. Name resolution
16. Threads
17. Mutexes, condition variables and synchronization
18. Time and timers
19. Daemons and services
20. Robust error handling
21. Debugging with gdb and strace
22. Linux-specific extensions
23. Secure systems programming
24. Capstone projects

## Capstone direction

Planned projects include a small shell, a daemon, a network service, a terminal-oriented program, and other utilities that force learners to combine several POSIX concepts.

## Relationship to EduAmigaC

EduPOSIX and [EduAmigaC](https://github.com/Ploos-AS/EduAmigaC) are sister courses. Where useful, both courses will solve comparable systems-programming problems so learners can contrast the POSIX and AmigaOS models.

## Languages and publishing

The course is intended for both **English and Norwegian** editions and for publication through the Ploos publishing toolchain.

## Status

**M0 — Project foundation**

The curriculum and repository structure are being established.

## License

Course material and documentation will use an appropriate Creative Commons license. Source code examples are intended to use the MIT license unless otherwise stated.
