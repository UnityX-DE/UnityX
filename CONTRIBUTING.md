# Contributing to **UnityX**

---

## Development Environment

Since **UnityX** targets the Wayland protocol, development is best done on a Linux-based system. We recommend a native Linux environment, but WSL2 with WSLg support is a viable alternative for Windows users.

### Prerequisites

| Component | Requirement |
| :--- | :--- |
| **Language** | Python 3.10 or newer |
| **OS (Linux)** | Native Linux environment with Wayland |
| **OS (Windows)** | WSL2 with WSLg support |
| **System Dependencies** | `libwayland-dev`, `libwlroots-dev`, `libxkbcommon-dev` |

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/UnityX-DE/UnityX.git
```

2. **Create and activate a virtual environment:**
```bash
python3 -m venv .venv && source .venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Project Standards
To keep the codebase clean and maintainable, we use automated checks:
> Pylint: Pull requests should aim to maintain the current score (ideally 10/10).   
> Code Style: General Python PEP 8 guidelines are allowed via the `.pylintrc` configuration.

## How to Help
We are looking for assistance with several core components of **UnityX:**

| Component | Responsibility |
| :--- | :--- |
| **Wayland Integration** | Window management using pywlroots. |
| **Architecture** | Interaction design between the panel, launcher, and compositor. |
| **Documentation** | Setup guides and technical specifications. |

If you want to contribute, feel free to check the **Issues** tab or open a new one to discuss a feature you would like to add to **UnityX.**

> **Note:** We advise you try to keep your commit messages descriptive.
