# Custom Ransomware Simulation 🔐

<p align="center">
  <img src="https://github.com/CodeWithTanim/README-MANAGER/blob/main/Custom-Ransomware-Simulation.jpeg" alt="Ransomware Simulation Banner" style="max-width: 100%; height: auto; width: 400px;">
</p>

<h1 align="center">🧑‍💻 Custom Ransomware Simulation ⚠️</h1>
<p align="center">
  <b>Internship Project for <a href="http://codectechnologies.in/">Codec Technologies</a><br>
  <b>A safe, educational simulation of ransomware encryption & decryption!</b> 🔒<br>
  Demonstrates AES-based file encryption in a controlled sandbox environment.<br>
  <sub>Tech Stack: Python, pyAesCrypt, Logging</sub>
</p>

---

### 🧠 Introduction

Developed as part of my internship with **Codec Technologies**, the **Custom Ransomware Simulation** is a project designed to **demonstrate ransomware-like behavior in a safe sandbox**.  
It showcases how ransomware encrypts and decrypts files, with proper logging and key handling, without putting real system files at risk.

---

### 📦 Features

- 🔑 **Key Generation** – Secure random key creation saved in `key.key`
- 🔒 **File Encryption** – Encrypts sandbox files with AES-256
- 🔓 **File Decryption** – Decrypt files using the same key
- 🗂️ **Sandbox Environment** – Works only on test files (no risk to your system)
- 📜 **Logging** – Tracks every action in `simulation.log`
- 🧪 **Unit Tests** – Includes test cases for safe verification

---

### 🛠️ Technologies Used

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/pyAesCrypt-FFCC00?style=for-the-badge" alt="pyAesCrypt">
  <img src="https://img.shields.io/badge/Logging-000000?style=for-the-badge&logo=logstash&logoColor=white" alt="Logging">
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest">
</p>

---

### 🚀 How to Run the Project?

#### ✅ Prerequisites:
- Python 3.8+
- Virtual environment recommended

#### 🛠️ Setup:
```bash
# Clone and setup
git clone https://github.com/CodeWithTanim/Custom-Ransomware-Simulation.git
cd Custom-Ransomware-Simulation
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Linux/macOS

# Install requirements
pip install -r requirements.txt

# Run the app
python src/main.py
````

---

### 🗂️ Project Structure

```
Custom-Ransomware-Simulation/
│
├── README.md                  ← Project documentation
├── requirements.txt           ← Python dependencies
│
├── docs/                      ← Documentation & Screenshots
│   ├── project_overview.md
│   ├── encryption_demo.md
│   └── screenshots/
│       ├── encrypt_demo.png
│       └── decrypt_demo.png
│
├── src/                       ← Source Code
│   ├── main.py                ← Main program
│   ├── encryptor.py           ← Encryption logic
│   ├── decryptor.py           ← Decryption logic
│   └── utils.py               ← Key generation & logging
│
├── tests/                     ← Unit Tests
│   ├── test_encryptor.py
│   ├── test_decryptor.py
│   └── test_utils.py
│
└── sandbox/                   ← Safe testing folder
    ├── sample_text.txt
    └── sample_files/
        └── sample1.txt
```

---

### 🌟 Key Learnings (Internship)

* Understood ransomware workflow (key, encrypt, decrypt)
* Implemented AES-256 encryption in Python using `pyAesCrypt`
* Practiced secure coding with logging and sandboxing
* Gained hands-on with project structure & testing
* Learned professional GitHub documentation

---

### ✍️ Developer

> [MD SAMIUR RAHMAN TANIM](https://github.com/CodeWithTanim)
> Intern at [Codec Technologies](http://codectechnologies.in/)
> 🔗 [GitHub](https://github.com/CodeWithTanim) | [LinkedIn](https://www.linkedin.com/in/CodeWithTanim)

---

### 📜 Acknowledgments

* Thanks to [Codec Technologies](http://codectechnologies.in/) for the internship opportunity
* Python & pyAesCrypt community for excellent documentation

---

### 🤝 Contribute

Pull requests are welcome! Found bugs or improvements? Fork the repo and submit a PR.

---

### 📡 Connect With Me:

<p align="left">
  <a href="https://fb.com/CodeWithTanim" target="blank"><img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="Facebook" height="30" width="40" /></a>
  <a href="https://instagram.com/CodeWithTanim" target="blank"><img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram" height="30" width="40" /></a>
  <a href="https://www.youtube.com/@CodeWithTanim" target="blank"><img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="YouTube" height="30" width="40" /></a>
</p>

