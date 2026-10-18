# FileFlow — Python File Management System

A modern, interactive file management application built with **Python** and **Streamlit**. FileFlow provides a simple dashboard for creating, reading, updating, renaming, and deleting text files through a clean user interface.

## Overview

FileFlow transforms traditional command-line file operations into an easy-to-use web interface. It combines Python file handling with a Streamlit dashboard to make common file operations more accessible.

## Features

- **Dashboard:** View file statistics, including file count, storage usage, and the latest modification information.
- **Create Files:** Create new text files from the interface.
- **Read Files:** Select and view existing files.
- **Update Files:** Append content to files or overwrite existing content.
- **Rename Files:** Rename files through the interface.
- **Delete Files:** Remove selected files with a dedicated delete action.
- **Workspace Management:** Store application-managed files in a dedicated workspace directory.
- **Input Validation:** Validate filenames to help prevent ordinary filename inputs from accessing paths outside the managed workspace.
- **Interactive UI:** Navigate between file operations using Streamlit's sidebar and dashboard layout.

## Tech Stack

- **Language:** Python
- **UI Framework:** Streamlit
- **File Handling:** Python `pathlib`
- **Version Control:** Git and GitHub

## Project Structure

```text
fileflow-streamlit-file-manager/
├── app.py
├── main.py
├── README.md
└── workspace/
    └── Hello world.py
```

- `app.py` — Streamlit user interface and file management features.
- `main.py` — Original Python command-line implementation.
- `workspace/` — Directory for application-managed files.
- `README.md` — Project documentation.

## Getting Started

### Prerequisites

- Python 3.10 or later recommended
- pip
- Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone https://github.com/AnanyaK-arch12/fileflow-streamlit-file-manager.git
cd fileflow-streamlit-file-manager
```

### 2. Install Streamlit

```bash
python -m pip install streamlit
```

### 3. Run the application

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL in your terminal. Open that URL in your browser to use FileFlow.

## How It Works

1. Launch the application.
2. Navigate through the sidebar to choose a file operation.
3. Enter a filename and any required content.
4. Create, read, update, rename, or delete files using the interface.
5. View the dashboard to monitor workspace file statistics.

## Learning Outcomes

This project provided practical experience with:

- Python file input/output operations
- Filesystem paths using `pathlib`
- Building interactive applications with Streamlit
- Organizing Python application code
- Validating user input
- Using Git and GitHub for version control and project publishing

## Future Improvements

- Add automated unit tests for file operations.
- Add file type and size restrictions.
- Improve error handling and user feedback.
- Add search, sorting, and file previews.
- Add deployment so the application can be accessed online.
- Introduce authentication and access controls if the application is deployed for multiple users.

## Author

**Ananya K.**

GitHub: [@AnanyaK-arch12](https://github.com/AnanyaK-arch12)

---

*Built as a Python project to practice file handling, interactive UI development, and version control.*
