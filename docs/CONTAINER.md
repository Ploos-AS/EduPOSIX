# Container development environment

The Debian-based container provides a reproducible Linux/POSIX learning environment with GCC, Clang, GDB and strace.

Build:

    docker build -t eduposix .

Run:

    docker run --rm -it -v "$PWD:/course" eduposix

Some later systems-programming labs may need additional container permissions or may be better run directly on a Linux host. Such requirements must be documented per lab rather than hidden in the base container.
