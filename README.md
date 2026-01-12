# LinkedIn Post Generator

This tool analyzes the posts of a LinkedIn influencer and helps create new posts in the same writing style. It leverages past posts to extract key topics and uses them as guidance for generating new content.

---

## Features

* **Analyze past LinkedIn posts**: Extract topics, language, length, and tags from existing posts.
* **Few-shot guided post generation**: Use past posts related to a specific topic, language, and length to guide a language model for generating new posts.
* **Customizable outputs**: Select topic, length, language (English or Hinglish), and generate posts in the influencer’s style.

---

## How It Works

### Stage 1: Post Collection & Metadata Extraction

* Feed past LinkedIn posts (JSON format) into the system.
* Extract metadata such as:

  * Topic / Tags
  * Language (English or Hinglish)
  * Length (Short, Medium, Long)

### Stage 2: Post Generation

* Choose topic, language, and length for a new post.
* The system uses examples of past posts with similar attributes to guide the language model.
* Generates a new post that matches the influencer’s style.

---

## Setup Instructions

1. **Get API Key**
   Obtain an API key from [Groq Console](https://console.groq.com/keys) and set it in your `.env` file:

   ```env
   GROQ_API_KEY=<your_api_key_here>
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**

   ```bash
   streamlit run main.py
   ```

---

## Usage

1. Upload past LinkedIn posts (JSON format).
2. The tool will automatically extract topics, length, language, and tags.
3. Select:

   * **Topic**
   * **Length** (Short, Medium, Long)
   * **Language** (English/Hinglish)
4. Click **Generate** to create a new post in the same style.

---

## Technical Details

* **Language Model**: Uses an LLM (via `llm_helper`) for generating posts.
* **Few-shot Learning**: Uses 1–2 example posts for style guidance.
* **Data Handling**: Processes JSON of past posts, extracts metadata using Python & Pandas.

---

## Directory Structure

```
linkedin_post_generator/
│
├── data/                     # Raw and processed posts
├── linkedin_post_generator/  # Main project code
│   ├── few_shot.py           # Few-shot post filtering and metadata
│   ├── preprocessor.py       # Metadata extraction from raw posts
│   ├── main.py               # Streamlit app
│   └── llm_helper.py         # Language model integration
├── requirements.txt          # Dependencies
└── .env                      # API key configuration
```

---

## Notes

* Language:

  * **English**: Fully English post.
  * **Hinglish**: Mix of Hindi and English, but written in English script.
* Maximum of **2 example posts** are used for few-shot guidance per new post.
* Ensure your `processed_post.json` is up-to-date for accurate few-shot learning.

---
