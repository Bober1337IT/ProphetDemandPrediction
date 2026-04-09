# Project Setup and Guidelines

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <your-repository-url>
    cd <project-folder>
    ```

2.  **Create a virtual environment:**

    ```bash
    py -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **Windows:**

        ```bash
        venv\Scripts\activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Guidelines

*   **Commit Messages:** Commits should clearly describe the changes that were made. Commit messages may be generated automatically using AI tools, but they should remain meaningful and relevant.
*   **Branching Strategy:** Each module of the application should be developed in a separate branch. Branch names should reflect the functionality or module being implemented.
*   **Main Branch Protection:** Do not push directly to the `main` branch. Modules will be integrated together during a shared team session, and only then merged into the `main` branch.