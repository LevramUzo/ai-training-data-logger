# 🤖 AI Training Data Logger

A command-line tool that simulates a **human annotation pipeline** for AI training data — built as part of the CS50P File I/O module.

---

## 💡 Why This Project?

This project is inspired by **RLHF (Reinforcement Learning from Human Feedback)** — the technique used to align AI models like ChatGPT and Claude with human preferences.

The RLHF pipeline works like this:

```
Human Annotators → Rate AI Responses → Train Reward Model → Guide AI with PPO
```

This tool simulates the **first step** of that pipeline: collecting and storing human-rated prompt/response pairs in a structured format ready for downstream model training.

I previously built a [full RLHF pipeline](https://github.com/LevramUzo) (SFT → Reward Modelling → PPO on KubeFlow Pipelines), so this project connects directly to real-world AI engineering practice.

---

## ✨ Features

- 📝 Log prompt/response pairs interactively via CLI
- ⭐ Rate each response on a scale of 1–5 (simulating human preference labeling)
- 💾 Save all entries to a structured **CSV file** (`training_data.csv`)
- 📊 Export a full dataset **summary to JSON** (`training_summary.json`) including:
  - Average rating
  - Rating distribution (1–5)
  - Per-annotator breakdown
- 🔒 Safe file handling — no data lost on re-runs (append mode)
- ✅ Input validation — handles bad input gracefully without crashing

---

## 🚀 How to Run

**Requirements:** Python 3.6+

```bash
git clone https://github.com/LevramUzo/ai-training-data-logger.git
cd ai-training-data-logger
python data-logger.py
```

---

## 🖥️ Sample Session

```
🤖 AI Training Data Logger
==========================

Options:
  1. Log a new prompt/response pair
  2. View all logged entries
  3. Export summary to JSON
  4. Exit

Choose an option (1-4): 1

--- Log New Entry ---
Prompt: What is reinforcement learning?
Response: It is a type of ML where an agent learns by interacting with an environment using rewards and penalties.
Rate this response (1 = poor, 5 = excellent): 5
Annotator name (or press Enter for 'anonymous'): Marvellous

✅ Entry #1 logged successfully.
```

**Sample JSON export (`training_summary.json`):**

```json
{
    "export_timestamp": "2026-04-25 10:00:00",
    "total_entries": 2,
    "average_rating": 4.5,
    "rating_distribution": {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 1,
        "5": 1
    },
    "annotators": {
        "Marvellous": 2
    }
}
```

---

## 🛠️ Tech Used

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| `csv` module | Reading and writing structured data |
| `json` module | Exporting dataset summaries |
| `datetime` module | Timestamping entries |
| `sys` module | Clean program exit with status codes |

---

## 📁 Files

```
ai-training-data-logger/
├── data-logger.py        # Main program
├── training_data.csv     # Generated on first log entry
├── training_summary.json # Generated on export
└── README.md
```

---

## 🔗 Related Projects

- **RLHF Pipeline** — Full SFT → Reward Model → PPO implementation on KubeFlow
- **Computer Vision Object Detection** — RF-DETR Nano on custom dataset (88.5% precision)

---

## 👨‍💻 Author

**Marvellous .U. Opara**  
BSc Industrial Physics | Aspiring AI Engineer  
[GitHub](https://github.com/LevramUzo) • [LinkedIn](https://linkedin.com/in/marvellous-opara-0816b0385) • oparamarvellous456@gmail.com
