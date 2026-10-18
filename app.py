
from pathlib import Path
from datetime import datetime
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="FileFlow | File Manager",
    page_icon="📁",
    layout="wide"
)

# Keep app files inside this folder
DATA_DIR = Path(__file__).parent / "workspace"
DATA_DIR.mkdir(exist_ok=True)


def safe_path(filename):
    filename = filename.strip()

    if not filename:
        raise ValueError("Please enter a file name.")

    if Path(filename).name != filename or filename in {".", ".."}:
        raise ValueError("Enter a file name only, not a folder path.")

    return DATA_DIR / filename


def get_files():
    return sorted(
        [p for p in DATA_DIR.iterdir() if p.is_file()],
        key=lambda p: p.name.lower()
    )


def format_size(size):
    if size < 1024:
        return f"{size} B"
    elif size < 1024 ** 2:
        return f"{size / 1024:.1f} KB"
    return f"{size / (1024 ** 2):.1f} MB"


# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 0%, #e8eaff, transparent 30%),
        #f7f8fc;
}

[data-testid="stSidebar"] {
    background: #111827;
}

[data-testid="stSidebar"] * {
    color: #eef2ff;
}

.hero {
    padding: 35px;
    border-radius: 24px;
    color: white;
    background: linear-gradient(
        120deg, #171e38, #4338ca, #0f766e
    );
    box-shadow: 0 15px 40px rgba(35, 42, 95, 0.18);
    margin-bottom: 25px;
}

.hero h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 42px;
    color: white;
    margin-bottom: 8px;
}

.hero p {
    color: #e0e7ff;
    font-size: 16px;
}

.eyebrow {
    text-transform: uppercase;
    letter-spacing: 3px;
    font-size: 12px;
    color: #c7d2fe;
    font-weight: 700;
}

.metric {
    background: white;
    padding: 22px;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.04);
    min-height: 105px;
}

.metric-label {
    color: #667085;
    font-size: 14px;
}

.metric-value {
    font-size: 29px;
    font-weight: 700;
    color: #172033;
    margin-top: 8px;
    overflow-wrap: anywhere;
}

.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 24px;
    font-weight: 700;
    color: #172033;
    margin: 15px 0 5px;
}

div[data-testid="stForm"],
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 16px;
}

.stButton button,
.stDownloadButton button,
.stFormSubmitButton button {
    border-radius: 10px;
    font-weight: 600;
    min-height: 43px;
}

#MainMenu, footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("# 📁 FileFlow")
    st.caption("Your personal file workspace")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "Overview",
            "Create File",
            "Read File",
            "Update File",
            "Delete File"
        ]
    )

    st.divider()
    st.markdown("### 🔐 Workspace")
    st.caption(
        "Your app-managed files are stored in the "
        "workspace folder beside app.py."
    )
    st.caption("Built with Python + Streamlit")


# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <div class="eyebrow">PYTHON • PATHLIB • STREAMLIT</div>
    <h1>File management, made simple.</h1>
    <p>
        Create, read, edit, rename and delete files
        from one clean dashboard.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- DASHBOARD STATISTICS ----------------
files = get_files()
total_size = sum(p.stat().st_size for p in files)

latest = max(
    files,
    key=lambda p: p.stat().st_mtime,
    default=None
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric">
        <div class="metric-label">📄 Total Files</div>
        <div class="metric-value">{len(files)}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric">
        <div class="metric-label">💾 Storage Used</div>
        <div class="metric-value">{format_size(total_size)}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    latest_name = latest.name if latest else "No files yet"

    st.markdown(f"""
    <div class="metric">
        <div class="metric-label">🕒 Latest Modified</div>
        <div class="metric-value" style="font-size:18px">
            {latest_name}
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")


# ---------------- OVERVIEW ----------------
if page == "Overview":

    left, right = st.columns([1.4, 1], gap="large")

    with left:
        st.markdown(
            '<div class="section-title">Your Workspace</div>',
            unsafe_allow_html=True
        )
        st.caption("Browse the files managed by this application.")

        if not files:
            st.info(
                "Your workspace is empty. Select Create File "
                "in the sidebar to add your first file."
            )

        for file in files:
            stat = file.stat()

            modified = datetime.fromtimestamp(
                stat.st_mtime
            ).strftime("%d %b %Y, %I:%M %p")

            preview = file.read_text(
                encoding="utf-8",
                errors="replace"
            ).replace("\n", " ")

            preview = preview[:90]
            if len(file.read_text(encoding="utf-8", errors="replace")) > 90:
                preview += "..."

            with st.container(border=True):
                st.markdown(f"### 📄 {file.name}")
                st.caption(preview or "Empty file")
                st.caption(
                    f"{format_size(stat.st_size)} • {modified}"
                )

    with right:
        st.markdown(
            '<div class="section-title">Quick Actions</div>',
            unsafe_allow_html=True
        )
        st.caption("Manage your files with a few clicks.")

        st.markdown("**＋ Create new files**")
        st.markdown("**⌕ Read saved content**")
        st.markdown("**✏️ Update or rename files**")
        st.markdown("**🗑️ Delete unwanted files**")

        st.info("Tip: Try creating a file named notes.txt")


# ---------------- CREATE FILE ----------------
elif page == "Create File":

    st.markdown(
        '<div class="section-title">✨ Create a New File</div>',
        unsafe_allow_html=True
    )
    st.caption("Enter a file name and write its initial content.")

    with st.form("create_form"):
        filename = st.text_input(
            "File Name",
            placeholder="e.g. notes.txt"
        )

        content = st.text_area(
            "File Content",
            placeholder="Start writing here...",
            height=220
        )

        submit = st.form_submit_button(
            "＋ Create File",
            type="primary",
            use_container_width=True
        )

    if submit:
        try:
            path = safe_path(filename)

            if path.exists():
                st.error("A file with this name already exists.")
            else:
                path.write_text(content, encoding="utf-8")
                st.success(f"File '{path.name}' created successfully!")
                st.rerun()

        except (ValueError, OSError) as error:
            st.error(str(error))


# ---------------- READ FILE ----------------
elif page == "Read File":

    st.markdown(
        '<div class="section-title">🔎 Read a File</div>',
        unsafe_allow_html=True
    )

    if not files:
        st.info("No files found. Create a file first.")

    else:
        names = [p.name for p in files]
        selected = st.selectbox("Select a file", names)
        path = safe_path(selected)

        try:
            content = path.read_text(
                encoding="utf-8",
                errors="replace"
            )

            st.caption(
                f"{len(content):,} characters • "
                f"{format_size(path.stat().st_size)}"
            )

            st.text_area(
                "File Contents",
                value=content,
                height=320,
                disabled=True
            )

            st.download_button(
                "⬇ Download File",
                data=content,
                file_name=path.name,
                mime="text/plain",
                use_container_width=True
            )

        except OSError as error:
            st.error(f"Could not read file: {error}")


# ---------------- UPDATE FILE ----------------
elif page == "Update File":

    st.markdown(
        '<div class="section-title">✏️ Update a File</div>',
        unsafe_allow_html=True
    )
    st.caption("Append content, overwrite content or rename a file.")

    if not files:
        st.info("No files found. Create a file first.")

    else:
        names = [p.name for p in files]
        selected = st.selectbox("Select a file", names)
        path = safe_path(selected)

        operation = st.radio(
            "Choose Operation",
            [
                "Append Content",
                "Overwrite Content",
                "Rename File"
            ],
            horizontal=True
        )

        if operation in ["Append Content", "Overwrite Content"]:

            with st.form("update_form"):
                new_content = st.text_area(
                    "Content",
                    placeholder="Enter your text here...",
                    height=200
                )

                submit = st.form_submit_button(
                    operation,
                    type="primary",
                    use_container_width=True
                )

            if submit:
                try:
                    if operation == "Append Content":
                        with path.open("a", encoding="utf-8") as file:
                            if path.stat().st_size > 0 and new_content:
                                file.write("\n")
                            file.write(new_content)

                        st.success("Content appended successfully!")

                    else:
                        path.write_text(
                            new_content,
                            encoding="utf-8"
                        )
                        st.success("File overwritten successfully!")

                    st.rerun()

                except OSError as error:
                    st.error(str(error))

        else:
            with st.form("rename_form"):
                new_name = st.text_input(
                    "New File Name",
                    value=path.name
                )

                submit = st.form_submit_button(
                    "↪ Rename File",
                    type="primary",
                    use_container_width=True
                )

            if submit:
                try:
                    new_path = safe_path(new_name)

                    if new_path == path:
                        st.warning("This is already the file name.")

                    elif new_path.exists():
                        st.error("A file with this name already exists.")

                    else:
                        path.rename(new_path)
                        st.success(
                            f"Renamed successfully to {new_path.name}!"
                        )
                        st.rerun()

                except (ValueError, OSError) as error:
                    st.error(str(error))


# ---------------- DELETE FILE ----------------
elif page == "Delete File":

    st.markdown(
        '<div class="section-title">🗑️ Delete a File</div>',
        unsafe_allow_html=True
    )
    st.caption("Select a file and confirm before deleting it.")

    if not files:
        st.info("No files found. Create a file first.")

    else:
        names = [p.name for p in files]
        selected = st.selectbox("Select a file to delete", names)
        path = safe_path(selected)

        st.warning(
            f"Selected: {path.name} "
            f"({format_size(path.stat().st_size)})"
        )

        confirm = st.checkbox(
            "I understand this file will be permanently deleted."
        )

        if st.button(
            "🗑️ Delete Selected File",
            type="primary",
            disabled=not confirm,
            use_container_width=True
        ):
            try:
                path.unlink()
                st.success("File deleted successfully!")
                st.rerun()

            except OSError as error:
                st.error(str(error))


# ---------------- FOOTER ----------------
st.divider()
st.caption(
    "FileFlow • Built with Python, pathlib and Streamlit"
)
