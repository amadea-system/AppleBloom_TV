# Dev Container Requirements

## Python Version

To update the python version of the Dev Container, first goto [Microsoft Artifact Registry](https://mcr.microsoft.com/en-us/product/devcontainers/python/about) and find the image with the desired python version.
Then update the [.devcontainer.json](../.devcontainer.json) file with the new image link.
Finally, run `Dev Container: Rebuild Container` in the command palette to rebuild the container with the new python version.

## Home Assistant Version & Supporting Python Packages

To configure the desired Home Assistant version and supporting python packages, update the [requirements.txt](../requirements.txt) file with the desired versions.
Then run `Dev Container: Rebuild Container` in the command palette to rebuild the container with the new versions.

### Required Python Package Versions

To find the required python package versions for the desired Home Assistant version:

- colorlog
  - [core/requirements_all.txt at d9dada4fb3d6f61cf84e0aaea9d79f759df64961 · home-assistant/core · GitHub](https://github.com/home-assistant/core/blob/d9dada4fb3d6f61cf84e0aaea9d79f759df64961/requirements_all.txt#L658)
  - [core/requirements_test_all.txt at d9dada4fb3d6f61cf84e0aaea9d79f759df64961 · home-assistant/core · GitHub](https://github.com/home-assistant/core/blob/d9dada4fb3d6f61cf84e0aaea9d79f759df64961/requirements_test_all.txt#L548)
- ruff
  - [core/requirements_test_pre_commit.txt at d9dada4fb3d6f61cf84e0aaea9d79f759df64961 · home-assistant/core · GitHub](https://github.com/home-assistant/core/blob/d9dada4fb3d6f61cf84e0aaea9d79f759df64961/requirements_test_pre_commit.txt#L4)
- pip
  - [core/requirements.txt at 85b453b86c372a56973741de1bb88d2edf371e41 · home-assistant/core · GitHub](https://github.com/home-assistant/core/blob/85b453b86c372a56973741de1bb88d2edf371e41/requirements.txt#L32)
  - [core/homeassistant/package_constraints.txt at 85b453b86c372a56973741de1bb88d2edf371e41 · home-assistant/core · GitHub](https://github.com/home-assistant/core/blob/85b453b86c372a56973741de1bb88d2edf371e41/homeassistant/package_constraints.txt#L45)
  - [core/pyproject.toml at 85b453b86c372a56973741de1bb88d2edf371e41 · home-assistant/core · GitHub](https://github.com/home-assistant/core/blob/85b453b86c372a56973741de1bb88d2edf371e41/pyproject.toml#L57)