<div align="center">

File Type Identifier & Malware Hint Scanner 🕵️‍♂️🔍

A Python tool to identify a file's true type by reading its magic bytes and scan for potential malware indicators.

</div>

🌟 Overview

This tool is designed to help cybersecurity enthusiasts, developers, and analysts quickly verify file integrity. It goes beyond simple file extensions by analyzing the file's header (magic bytes) to determine its actual type. It also flags suspicious characteristics, such as mismatched extensions, which can be an indicator of a disguised malicious file.

Add a screenshot or GIF of your application in action.

✨ Key Features

🔍 Magic Byte Analysis: Accurately detects a file's type, ignoring the extension.

⚠️ Mismatch Detection: Flags files where the extension doesn't match the true file type.

** laajiro File Support**: Supports a wide range of common file types like .exe, .dll, .jpg, .png, .pdf, .zip, and more.

🔑 Hash Computation: Optionally computes MD5 and SHA256 hashes for further analysis or verification on platforms like VirusTotal.

🖥️ User-Friendly Interface: Built with Streamlit for an easy-to-use web interface.

🛠️ Tech Stack

Language: Python 3.x

Core Libraries: os, hashlib, struct

Web Framework: streamlit

🚀 Getting Started

Follow these steps to get the project up and running on your local machine.

Prerequisites

Python 3.7 or newer

Git

Installation & Usage

Clone the Repository:

git clone [https://github.com/Asura-Lord/File-Type-Identifier.git](https://github.com/Asura-Lord/File-Type-Identifier.git)
cd File-Type-Identifier


Create and Activate a Virtual Environment:

On Windows:

python -m venv .venv
.\.venv\Scripts\activate


On macOS/Linux:

python3 -m venv .venv
source .venv/bin/activate


Install Dependencies:

pip install -r requirements.txt


Run the Application:

streamlit run app.py


Your browser should open with the application running!

🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License

This project is distributed under the MIT License. See LICENSE for more information.

<div align="center">
Made with ❤️ by Asura-Lord
</div>
