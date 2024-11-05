# Harbor Retention Policy and Project Management Script

This script allows user to manage retention policies and projects in Harbor, a container registry. It utilizes the `harborapi` library to interact with Harbor's API and perform the following actions:

- Add or update retention policies for projects.
- Create projects in Harbor.

## Getting Started

### Prerequisites

- Python 3.x
- The `harborapi` library. Install it using:

  ```bash
  pip install harborapi
  ```

### Usage

1. Clone this repository or download the script `main.py`.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script with the required command-line arguments:

   ```bash
   python main.py --url <Harbor_URL> --username <Username> --secret <Secret>
   ```

   Replace `<Harbor_URL>`, `<Username>`, and `<Secret>` with your Harbor instance's URL, your username, and your secret.

4. The script will perform the following actions:

   * Check and update retention policies for existing projects.
   * Create new projects with the specified names.

### Configuration

* project_names: Add your desired project names to the `project_names` list in the script.

* Retention Policy Settings: The script includes retention policy settings such as `algorithm`, `rules`, and `trigger`. Adjust these settings as needed for your use case.
