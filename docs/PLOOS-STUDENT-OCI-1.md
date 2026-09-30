# PLOOS-STUDENT-OCI-1

EduPOSIX adopts the PLOOS-STUDENT-OCI-1 student environment contract. The course repository plus a standard OCI runtime must provide the supported learning environment without private Ploos infrastructure.

Stable interface:

- workspace: `/course`
- `student-env-info`: report environment/tool versions
- `student-check`: verify the course checkout
- default command: `student-check`

The image must contain only redistributable dependencies, work with Docker and Podman, support non-interactive CI, and be versioned with published course releases. Labs requiring unusual Linux privileges must declare those privileges explicitly and must not silently weaken the base container.

Canonical cross-course contract/reference implementation: EduC `docs/PLOOS-STUDENT-OCI-1.md`.
