# QA Lab — New-System Setup and Migration Guide

**Status:** Working draft
**Purpose:** Rebuild the QA Lab on a new Windows system, including VMware, Linux installation, development tools, and repository restoration.
**Authoritative repository:** `18thSky/my-freecodecamp-portfolio`, branch `main`.
**Last recorded checkpoint:** `054381e` — `test: cover invalid bug API request bodies`.

> Verify current installer versions and licensing terms on official vendor sites. Never commit passwords, tokens, private keys, or populated `.env` files.

## 1. Target architecture

- Windows host computer.
- VMware Workstation installed on Windows.
- Ubuntu Linux guest OS in a VMware virtual machine.
- Python virtual environment and QA tools inside Linux.
- QA Lab cloned from GitHub.
- Database configuration supplied securely at runtime.
- Tests run only against a positively identified disposable or isolated database.

Ubuntu includes its Linux kernel. During a normal Ubuntu installation, you do not separately install a kernel by hand. Kernel updates are managed through Ubuntu's supported package update process.

## 2. Prepare the Windows host

1. Confirm Windows is supported by the current VMware Workstation release.
2. Check available RAM, CPU resources, and free disk space.
3. Confirm hardware virtualization is enabled:
   - Intel: VT-x.
   - AMD: AMD-V / SVM.
4. If disabled, enable it in BIOS/UEFI. The setting name and location vary by manufacturer.
5. Review any Windows Hyper-V / Virtual Machine Platform compatibility notices against current VMware guidance. Do not randomly disable security or virtualization features.

## 3. Install VMware Workstation

1. Visit the official Broadcom portal: https://support.broadcom.com/
2. Sign in or create an account if required.
3. Find the current VMware Workstation download for Windows.
4. Review the current licensing and usage terms.
5. Download the installer from the official source only.
6. Run the installer and follow its prompts.
7. Restart Windows if requested.
8. Launch VMware Workstation and verify it opens.

Record the VMware version, installer source, installation date, and any warnings.

## 4. Download Ubuntu

This guide uses Ubuntu Desktop as the example guest OS.

1. Visit https://ubuntu.com/download/desktop
2. Select an appropriate Ubuntu LTS release.
3. Download the official ISO.
4. Save it in a clearly named folder, such as `Downloads/ISO/`.
5. Verify the published checksum if Ubuntu provides one.

Record the distribution, release, ISO filename, and checksum result.

## 5. Create the Linux VM

1. Open VMware Workstation.
2. Select **Create a New Virtual Machine**.
3. Choose Typical unless custom hardware is needed.
4. Select the Ubuntu ISO as the installer image.
5. If VMware does not detect the OS, select Linux and the appropriate Ubuntu 64-bit guest type.
6. Name the VM `Ubuntu-QA-Lab` or another clear name.
7. Choose a storage location with sufficient free disk space.
8. Create a virtual disk.
9. Review the virtual hardware before booting.

Suggested starting resources (adjust to the host):

| Resource | Starting point |
|---|---:|
| CPU | 2 virtual cores |
| RAM | 4 GB minimum; 8 GB preferred if available |
| Virtual disk | 40–60 GB |
| Network | NAT initially |
| Firmware | VMware/Ubuntu recommended default |

Do not allocate all host CPU or RAM to the VM. Leave resources for Windows.

10. Finish creating the VM.
11. Open VM settings and ensure the ISO is attached to the virtual CD/DVD drive and connected at power-on.

## 6. Boot the VM and install Ubuntu

1. Select the VM and click **Power on**.
2. It should boot from the attached Ubuntu ISO.
3. Select **Install Ubuntu**.
4. Follow the installer:
   - Choose language and keyboard layout.
   - Select appropriate installation options.
   - Configure network access if available.
   - Choose the installation disk inside the VM.
   - Create a Linux username and password.
   - Select the time zone.
5. Carefully confirm the target is the VM's virtual disk, not a physical Windows disk.
6. Complete installation and restart when prompted.
7. Eject/disconnect the ISO when instructed.
8. Boot again and sign in to Ubuntu.

**Safety:** Never select or format a physical Windows host disk during guest OS installation.

## 7. First boot and Linux kernel verification

Open a terminal inside Ubuntu:

```bash
cat /etc/os-release
uname -r
uname -m
```

Update Ubuntu:

```bash
sudo apt update
sudo apt upgrade
```

Restart if requested:

```bash
sudo reboot
```

After reboot, verify the kernel:

```bash
uname -r
```

Ubuntu installs and maintains the kernel. Do not install an unrelated kernel build for this QA Lab.

## 8. Install VMware guest integration

For Ubuntu:

```bash
sudo apt update
sudo apt install -y open-vm-tools open-vm-tools-desktop
sudo reboot
```

Verify guest integration. Clipboard, display resizing, time synchronization, and shared-folder behavior can depend on VMware and guest configuration.

## 9. Install Linux development tools

```bash
sudo apt update
sudo apt install -y \
  git curl wget build-essential \
  python3 python3-venv python3-pip python3-dev pkg-config
```

Verify:

```bash
python3 --version
python3 -m pip --version
git --version
```

Install an editor using its official instructions and record its version.

## 10. Configure Git and GitHub access

Set your intended Git identity:

```bash
git config --global user.name "YOUR NAME"
git config --global user.email "YOUR GITHUB EMAIL"
```

Verify:

```bash
git config --global --list
```

Configure GitHub authentication using the current official guide: https://docs.github.com/en/authentication

Never share or commit private SSH keys, personal access tokens, or credentials.

## 11. Clone the authoritative repository

Repository:

`https://github.com/18thSky/my-freecodecamp-portfolio`

```bash
cd ~
git clone https://github.com/18thSky/my-freecodecamp-portfolio.git
cd my-freecodecamp-portfolio
git status --short --branch
git log -1 --oneline
```

Follow the repository's current README and project-specific instructions. Verify paths before assuming files exist.

The current workflow treats the Windows repository as authoritative for commits and pushes. The Linux VM is used for development and testing. Do not commit from an incidental or unverified Linux repository.

## 12. Restore the QA Lab Python environment

If the project is under `qa-lab/`:

```bash
cd ~/my-freecodecamp-portfolio/qa-lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip list
```

Do not copy an old `.venv` between computers. Recreate it from the dependency file. If requirements are missing or incomplete, inspect actual imports and verified versions rather than guessing.

## 13. Database configuration and safety

The inspected `database.py` reads these environment variables:

- `DB_HOST`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`

The inspected `app.py` imports `get_connection` directly. The `POST /bugs` route validates title, severity, and status before calling `get_connection()`. If validation succeeds, it connects to MySQL, inserts a row, and commits. On an exception, it rolls back.

### Current environment finding

During the November 2026 inspection, the following were checked without printing their values:

- `DB_HOST`: NOT SET
- `DB_USER`: NOT SET
- `DB_NAME`: NOT SET

`DB_PASSWORD` was intentionally not displayed. The database target has **not** been established. Do not run the test suite, send POST requests, or attempt database writes until the target is positively identified.

### Database restrictions

Never write to these protected/shared databases:

- `hitwicket_qa`
- `racing_db`
- `racing_game`
- shared `qa_lab`

Do not create or drop schemas on a shared server for this exercise.

For persistence testing, use only a positively verified disposable database or a test connection/fixture that the route itself will actually use. If safe isolation cannot be established, stop and document the blocker.

### Secrets handling

- Keep the real `.env` file out of Git.
- Ensure `.env` is listed in `.gitignore`.
- Commit only a sanitized `.env.example` with placeholders.
- Never print passwords or tokens in shared logs or terminal output.
- Never put secrets in README instructions, screenshots, or Git history.

Example placeholders only (not real credentials):

```dotenv
DB_HOST=127.0.0.1
DB_USER=replace_with_test_user
DB_PASSWORD=replace_with_test_password
DB_NAME=replace_with_disposable_test_database
```

This example does not establish that such a database exists or is safe.

## 14. Run QA Lab tests

Only after the database target and isolation are verified:

```bash
cd ~/my-freecodecamp-portfolio/qa-lab
source .venv/bin/activate
pytest -q
```

Record the exact command, isolation strategy, non-secret database identifier, test count, pass/fail/skip totals, warnings, and files changed. Never claim a test passed unless it was actually run.

## 15. VM backup and migration

Before returning or replacing the current hardware:

1. Push intended code and documentation changes from the authoritative Windows repository.
2. Confirm GitHub contains the latest commit.
3. Confirm no required work exists only on the old machine.
4. Back up important non-secret project files.
5. Record VM CPU, RAM, disk, firmware, and network settings.
6. Decide whether to export/copy the VM or recreate it from this guide.
7. Do not export protected/shared databases.
8. Recreate secrets securely on the new machine; keep them out of VM archives and GitHub.
9. On the new system, install VMware, create the Linux VM, install Ubuntu and tools, clone GitHub, and recreate the Python environment.
10. Verify the QA Lab using an isolated test target before declaring migration complete.

A VM-folder copy is not automatically a complete backup. Shut down the VM, include all required virtual disk/configuration files, and verify the backup can be restored.

## 16. Current QA Lab progress

### Completed — 26 October 2026

- Added tests for malformed JSON, JSON arrays, strings, and `null`.
- Preserved existing validation and summary tests.
- `app.py` unchanged.
- Linux VM result: **15 passed, 1 existing deprecation warning**.
- Windows syntax compilation passed; Windows runtime tests were not rerun.
- Documentation updated in `qa-lab/QA_LAB_EXACT_STEPS.md`.
- Commit pushed to `main`: `054381e` — `test: cover invalid bug API request bodies`.

### Next persistence-testing milestone

Objective: prove invalid `POST /bugs` requests do not create database records, using a verified isolated test environment.

1. Inspect repository and code.
2. Trace the route's actual database connection.
3. Establish safe database isolation before running tests or sending POST requests.
4. Capture a starting record count with a read-only query.
5. Submit an invalid request through FastAPI `TestClient`.
6. Capture a second count using an appropriate fresh read connection.
7. Assert the count is unchanged.
8. Extend to representative invalid cases only if the first test is safe and passes.
9. Run tests and document evidence.
10. Do not commit from an incidental Linux VM repository.

### Linux VM inspection already completed

- Project directory: `/home/sky/qa-lab`.
- Incidental Git repository: branch `master`, no commits; files are untracked. It is not authoritative.
- `test_api.py`, `database.py`, and `app.py` were inspected.
- No `conftest.py`, `pytest.ini`, `pyproject.toml`, `setup.cfg`, or `.env.example` was found by a search at depth 2.
- The route imports `get_connection` directly, so the route uses `app.get_connection` after import.
- No FastAPI database dependency override was identified in the inspected code.
- `initialize_database()` is a no-op; its comment says the existing `qa_lab.bugs` table already exists.
- `DB_HOST`, `DB_USER`, and `DB_NAME` were not set in the shell during inspection.
- No test or POST request was run during that inspection.

**Current safety status:** Database target not verified. Stop before any test or write that could connect to MySQL.

## 17. New-system acceptance checklist

- [ ] VMware Workstation installed from official source.
- [ ] VMware version and licensing terms recorded.
- [ ] Hardware virtualization verified.
- [ ] Ubuntu ISO downloaded from official source.
- [ ] Linux VM created with documented resources.
- [ ] Ubuntu installed and boots successfully.
- [ ] Kernel version recorded with `uname -r`.
- [ ] `open-vm-tools` installed and verified.
- [ ] Linux updates applied.
- [ ] Git, Python, venv, and development tools installed.
- [ ] GitHub authentication configured securely.
- [ ] Repository cloned from GitHub.
- [ ] Python virtual environment recreated from requirements.
- [ ] Database target positively identified and isolated before tests.
- [ ] README and setup documents updated.
- [ ] New-system setup rehearsal completed.
- [ ] GitHub contains required code and documentation.
- [ ] No credentials or protected database data committed.

## 18. Maintenance notes

Update this guide as the actual system is built. Record real versions, settings, command outputs, and deviations. Distinguish completed steps from planned steps; do not mark a step complete without verification.

**Primary repository:** https://github.com/18thSky/my-freecodecamp-portfolio
**Current branch:** `main`
**Last recorded commit:** `054381e`
