# Platform matrix

## M0 baseline

Linux is the reference development and CI platform. Both GCC and Clang are used to catch accidental compiler dependencies.

## Portability classes

Every systems interface taught should be classified:

| Class | Meaning |
|---|---|
| ISO C | Part of the portable C language/library baseline |
| POSIX | Specified by POSIX and intended to transfer across conforming Unix-like systems |
| Linux | Linux-specific API, behavior or facility |

## Future qualification

The course should later compile selected portable labs on additional POSIX systems such as BSD-family systems and macOS where practical. Linux-specific labs remain explicitly separate.

Passing on Linux is evidence for the Linux baseline; it is not by itself proof of POSIX portability.
