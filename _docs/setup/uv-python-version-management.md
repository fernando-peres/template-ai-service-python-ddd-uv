## 📝 Python Version Management with `uv`

When using `uv`, it's important to ensure that your **project’s Python version** is aligned with the **active interpreter** being used in your virtual environment.

| Action                     | Command                                   |
|----------------------------|-------------------------------------------|
| List available versions    | `uv python list --available`              |
| Install a Python version   | `uv python install 3.11`                  |
| Pin version to project     | `uv python pin 3.11`                      |
| List installed versions    | `uv python list`                          |
| Uninstall a Python version | `uv python uninstall 3.11`                |


---

### 🔍 Check the Project Python Version

Inside your project, open the `pyproject.toml` file and look for the `requires-python` field under `[project]`. For example:

```toml
[project]
name = "my-app"
requires-python = ">=3.10,<3.12"
```

### 🧠 Check the Active Python Version

To see the currently active Python version managed by uv, use:

```
 uv python pin
```

You can check the insatlled versions of Python by running:

```bash
uv python list
```

This command will show:
	•	System and uv-managed Python versions
	•	The currently active interpreter
	•	Installed paths and metadata

### 📌 Pin a Specific Python Version

To ensure uv always uses a specific version (e.g., Python 3.13), run:

```bash
uv python pin cpython-3.13.2-macos-aarch64-none
```
This creates a `.python-version` file in your project directory, pinning the environment to Python 3.13. This ensures consistency across machines and CI/CD pipelines.

## 🐍 Installing Python Versions with `uv`

The `uv` CLI includes built-in tooling to **install and manage Python versions**, similar to `pyenv` — but faster and more portable.

Here's how to add and manage Python interpreters with `uv`:

---

### 🔍 List Available Python Versions

To see what versions are available to install via `uv`:

```bash
uv python list
```

### 📥 Install a Python Version

To install a specific version of Python (e.g., Python 3.11):

```bash
uv python install <version>
```

### 📌 Pin a Specific Python Version

Once installed, you can pin a version for a project:

```bash
uv python pin <version>
```

This will:
	•	Create a `.python-version `file in your project
	•	Ensure uv uses that version when creating or activating the venv
	•	Align with your pyproject.toml if requires-python is set


### 🧼 Uninstall a Python Version

To remove an installed Python version:

```bash
uv python uninstall <version>
```
