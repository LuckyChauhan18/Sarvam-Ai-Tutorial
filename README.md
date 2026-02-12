# 🚀 Sarvam AI Tutorial

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Sarvam AI](https://img.shields.io/badge/API-Sarvam%20AI-orange.svg)](https://www.sarvam.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive collection of tutorials and scripts demonstrating the power of **Sarvam AI** for Indic languages. This project covers Voice (TTS/STT), Vision, and Translation capabilities.

---

## 🌟 Features

- 🗣️ **Text-to-Speech (Bulbul)**: High-quality Hindi speech generation.
- 🎤 **Speech-to-Text (Saarika)**: Accurate transcription for Indian languages.
- 🖼️ **Document Intelligence**: Extract insights from documents and images.
- 🌐 **Translation**: seamless translation between English and multiple Indic languages.
- 💬 **Indic Chat**: LLM-powered chat optimized for Indian context.

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8 or higher.
- A Sarvam AI API Subscription Key.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/LuckyChauhan18/Sarvam-Ai-Tutorial.git
   cd Sarvam-Ai-Tutorial
   ```

2. **Install dependencies**:
   ```bash
   pip install sarvamai python-dotenv
   ```

### 🔑 Configuration

Create a `.env` file in the root directory and add your API key:

```env
SARVAM_API_KEY=your_api_subscription_key_here
```

---

## 🚀 Usage Examples

### 1. Indic Chat (LLM)
Query the model for information or creative tasks.
```python
# Run sarvamM.py
python sarvamM.py
```

### 2. Text-to-Speech
Convert Hindi text into high-quality audio.
```python
# Run Speech_reco.py
python Speech_reco.py
```

### 3. Speech-to-Text
Transcribe audio files (wav) into text.
```python
# Run sarika_model.py
python sarika_model.py
```

### 4. Document Intelligence (Vision)
Process PDF documents and extract structured content.
```python
# Run sarvam_Vision.py
python sarvam_Vision.py
```

### 5. Translation
Translate text between Indic languages and English.
```python
# Run sarvam_translate.py (Hindi -> English)
# Run translation.py (Hindi -> Marathi)
```

---

## 📂 Project Structure

```text
.
├── .env                # API Keys (Git ignored)
├── .gitignore          # Files to ignore in Git
├── README.md           # Project documentation
├── sarvamM.py          # Chat Completions demo
├── Speech_reco.py      # Text-to-Speech demo
├── sarika_model.py     # Speech-to-Text demo
├── sarvam_Vision.py    # Document Intelligence demo
├── sarvam_translate.py # HINDI -> ENGLISH translation
└── translation.py      # HINDI -> MARATHI translation
```

---

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙌 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---


