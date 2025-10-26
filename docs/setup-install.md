## ⚙️ **Setup & Installation**

### **Prerequisites**

Before you begin, ensure you have the following installed:

* **Python 3.11+**
* **pip** (latest version recommended)
* **virtualenv** (optional but highly recommended)
* **Git**
* Access to an **OpenAI-compatible LLM API key** (or local inference model)

---

### **1. Clone the Repository**

```bash
git clone https://github.com/<your-username>/empathy-engine.git
cd empathy-engine
```

---

### **2. Create and Activate a Virtual Environment**

#### 🪟 On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 On macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

You can customize the dependencies later, but a minimal starting `requirements.txt` might look like this:

```
openai
transformers
torch
pandas
numpy
scikit-learn
flask
fastapi
uvicorn
pytest
python-dotenv
```

---

### **4. Set Up Environment Variables**

Create a `.env` file in the project root directory (based on `.env.example`):

```bash
cp .env.example .env
```

Then open `.env` and set your values:

```
OPENAI_API_KEY=your_api_key_here
DEBUG=True
LOG_LEVEL=info
```

---

### **5. Run the Empathy Engine**

Start the main system loop:

```bash
python main.py
```

Or, if you’re using the API interface:

```bash
uvicorn interface.api.endpoints:app --reload
```

---

### **6. Run Tests**

To ensure everything is working:

```bash
pytest
```

---

### **7. Optional Developer Tools**

To improve your development experience:

```bash
pip install black isort mypy
```

Then format your code:

```bash
black .
isort .
```

---

### ✅ **You’re Ready**

Once setup completes, the engine will initialize its **Core Cognitive Loop** and load the base empathy model.
From here, you can begin fine-tuning emotional mappings, integrating with interfaces, or connecting to your own dialogue system.
