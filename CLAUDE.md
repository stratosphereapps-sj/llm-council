# LLM Council - Project Context

## Project Overview

LLM Council is a multi-agent AI discussion system where multiple AI agents collaborate to analyze topics through structured reasoning. The system uses Google's Gemini 3 Flash Preview model to power all agents, running entirely through Google's Generative AI API.

### Purpose
- Enable structured, multi-perspective analysis of complex topics
- Demonstrate agent-based reasoning with specialized roles
- Provide transparent, step-by-step AI decision making
- Store and track discussion history for reference

---

## Architecture

### System Flow
1. **User Input** → Topic submitted through Streamlit UI
2. **Generator Agent** → Frames the problem clearly
3. **Analyst Agent** → Breaks down and analyzes the problem
4. **Critic Agent** → Challenges assumptions and identifies gaps
5. **Summarizer Agent** → Synthesizes insights into balanced conclusion
6. **Database Storage** → All responses saved to SQLite for history

### Agent Roles

| Agent | Model | Purpose |
|-------|-------|---------|
| **Generator** | gemini-3-flash-preview | Transform user topic into well-defined problem statement |
| **Analyst** | gemini-3-flash-preview | Analyze problem logically, identify factors and trade-offs |
| **Critic** | gemini-3-flash-preview | Challenge assumptions, expose gaps, provide counterpoints |
| **Summarizer** | gemini-3-flash-preview (Chairman) | Synthesize discussion into balanced conclusion |

---

## Project Structure

```
llm-council/
├── agents/                      # Agent implementations
│   ├── base_agent.py           # Base class for all agents
│   ├── generate_agent.py       # Problem framing agent
│   ├── analyst.py              # Analysis agent
│   ├── critic.py               # Critique agent
│   └── summarizer.py           # Synthesis agent
├── db/                         # Database layer
│   └── council.py              # SQLite database functions
├── data/                       # Data storage
│   └── conversations/          # Conversation history (gitignored)
├── app.py                      # Streamlit UI application
├── council_runner.py           # Agent orchestration logic
├── ollama_client.py            # Gemini API client (legacy name)
├── config.py                   # Centralized configuration
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variable template
├── .env                       # API keys (gitignored)
└── CLAUDE.md                  # This file
```

---

## Setup Instructions

### Prerequisites
- Python 3.10+
- Google Gemini API key
- ~6-8 GB RAM recommended

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/stratosphereapps-sj/llm-council.git
   cd llm-council
   ```

2. **Install dependencies**
   ```bash
   pip install --break-system-packages -r requirements.txt
   ```
   Or with virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```
   Get API key from: https://aistudio.google.com/app/apikey

4. **Run the application**
   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   streamlit run app.py
   ```

---

## Configuration

### Environment Variables (.env)
- `GEMINI_API_KEY` - Google Gemini API key (required)

### Config File (config.py)

**Models Configuration:**
```python
COUNCIL_MODELS = [
    "gemini-3-flash-preview",  # Generator
    "gemini-3-flash-preview",  # Analyst
    "gemini-3-flash-preview",  # Critic
    "gemini-3-flash-preview",  # (unused slot)
]

CHAIRMAN_MODEL = "gemini-3-flash-preview"  # Summarizer
```

**API Configuration:**
```python
GEMINI_API_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"
DATA_DIR = "data/conversations"
```

---

## Key Components

### 1. Gemini API Client (ollama_client.py)
**Purpose:** Interface with Google's Generative AI API

**Request Format:**
```python
{
    "contents": [{
        "parts": [{"text": "prompt"}]
    }]
}
```

**Response Parsing:**
```python
data["candidates"][0]["content"]["parts"][0]["text"]
```

**Headers:**
- `x-goog-api-key`: API key authentication
- `Content-Type`: application/json

### 2. Base Agent (agents/base_agent.py)
**Purpose:** Shared logic for all agents

**Features:**
- Model assignment from config
- Prompt construction with role-specific instructions
- API query execution
- Response handling

### 3. Council Runner (council_runner.py)
**Purpose:** Orchestrate agent execution

**Flow:**
```python
input → Generator → Analyst → Critic → Summarizer → results
         |            |          |          |
         ↓            ↓          ↓          ↓
      Save to DB  Save to DB Save to DB Save to DB
```

### 4. Database Layer (db/council.py)
**Purpose:** Persist discussion history

**Schema:**
```sql
CREATE TABLE responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_name TEXT,
    input_text TEXT,
    output_text TEXT,
    timestamp TEXT
)
```

**Functions:**
- `init_db()` - Initialize database and create tables
- `save_response()` - Store agent responses
- `get_connection()` - SQLite connection manager

### 5. Streamlit UI (app.py)
**Purpose:** User interface for council discussions

**Features:**
- Topic input text area
- Run council button
- Expandable agent response cards
- Session state management

---

## Dependencies

### Production Dependencies
```
streamlit>=1.28.0      # Web UI framework
requests>=2.31.0       # HTTP client for API calls
python-dotenv>=1.0.0   # Environment variable management
```

### Runtime Requirements
- Python 3.10+
- Internet connection (for Gemini API)
- Web browser (for Streamlit UI)

---

## API Integration

### Google Gemini API

**Endpoint Pattern:**
```
POST {GEMINI_API_BASE_URL}/{model}:generateContent
```

**Example Request:**
```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [{"text": "Your prompt here"}]
    }]
  }'
```

**Response Structure:**
```json
{
  "candidates": [{
    "content": {
      "parts": [{
        "text": "AI generated response"
      }]
    }
  }]
}
```

---

## Development Workflow

### Making Changes

1. **Modify code** in relevant files
2. **Test locally** with `streamlit run app.py`
3. **Stage changes** with `git add <files>`
4. **Commit** with descriptive message
5. **Push** to GitHub repository

### Git Configuration
```bash
git config user.email "council@llm-council.local"
git config user.name "LLM Council Developer"
```

### Common Commands
```bash
# Run the app
streamlit run app.py

# Check git status
git status

# View logs
git log --oneline -10

# Push changes
git add .
git commit -m "Description of changes"
git push origin master
```

---

## Agent Prompt Structure

Each agent receives a prompt with:
1. **Identity** - "You are {agent_name}"
2. **Role description** - Agent-specific instructions
3. **Rules** - What NOT to do
4. **Requirements** - What MUST be done
5. **Output format** - Structured response template
6. **Input context** - Previous agent's output

**Example:**
```
You are Analyst.

Role:
Analyze the problem strictly based on the input provided.

Rules:
- You MUST rely entirely on the provided input
- Do NOT introduce new topics
[...]

========== INPUT ==========
{previous_agent_output}
===========================

Your response:
```

---

## Data Flow

### Request Flow
```
User → Streamlit UI → Council Runner → Agents → Gemini API
                           ↓
                      Database (SQLite)
```

### Response Flow
```
Gemini API → Agent → Council Runner → Streamlit UI
                ↓
           Database (SQLite)
```

### State Management
- **Session state** - Streamlit manages UI state
- **Database** - Persistent storage of all discussions
- **Config** - Centralized configuration loaded at runtime

---

## Security & Privacy

### Protected Information
- `.env` file (contains API keys) - **gitignored**
- `data/conversations/*` (user discussions) - **gitignored**
- SQLite database files (`*.db`) - **gitignored**

### API Key Management
- Stored in `.env` file
- Loaded via `python-dotenv`
- Never committed to version control
- Validated at runtime before API calls

---

## Error Handling

### API Errors
```python
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file")

response.raise_for_status()  # Raises HTTPError for bad responses
```

### Common Issues

**Issue:** `GEMINI_API_KEY not found`
**Solution:** Create `.env` file with valid API key

**Issue:** `command not found: streamlit`
**Solution:** Add `~/.local/bin` to PATH or activate venv

**Issue:** API rate limiting
**Solution:** Wait and retry, or upgrade API tier

---

## Testing

### Manual Testing
1. Run app: `streamlit run app.py`
2. Enter test topic: "Should AI be used in school grading?"
3. Click "Run Council"
4. Verify all 4 agents respond
5. Check database: `sqlite3 db/council.db "SELECT * FROM responses;"`

### Test Topics
- "Impact of AI on modern education"
- "Is a four-day work week viable?"
- "Should social media be regulated?"

---

## Future Enhancements

### Potential Improvements
- [ ] Add more specialized agent roles
- [ ] Implement different models per agent
- [ ] Add conversation history viewer
- [ ] Enable user feedback on responses
- [ ] Support for multi-turn discussions
- [ ] Export discussions to PDF/Markdown
- [ ] Add streaming responses for real-time updates
- [ ] Implement rate limiting and retry logic
- [ ] Add cost tracking for API usage

---

## Migration History

### Ollama → Gemini API (Latest)
- **Date:** 2026-02-05
- **Reason:** Replace local Ollama with cloud-based Gemini API
- **Changes:**
  - Updated `ollama_client.py` to use Gemini API format
  - Created `config.py` for centralized configuration
  - Changed model from `gemma3:4b` to `gemini-3-flash-preview`
  - Updated authentication to use `x-goog-api-key` header
  - Modified response parsing for Gemini format

---

## Contact & Resources

### Documentation
- Gemini API: https://ai.google.dev/docs
- Streamlit: https://docs.streamlit.io
- Python dotenv: https://pypi.org/project/python-dotenv/

### Repository
- GitHub: https://github.com/stratosphereapps-sj/llm-council

### Getting Help
- Open issues on GitHub repository
- Check error logs in terminal
- Verify `.env` configuration
- Review Gemini API documentation

---

## Quick Reference

### Environment Setup
```bash
export PATH="$HOME/.local/bin:$PATH"
cd /home/coder/llm-council
```

### Run Application
```bash
streamlit run app.py
```

### Database Inspection
```bash
sqlite3 db/council.db
.tables
.schema responses
SELECT * FROM responses ORDER BY id DESC LIMIT 5;
```

### Git Operations
```bash
git status
git add .
git commit -m "Description"
git push origin master
```

---

**Last Updated:** 2026-02-05
**Version:** 1.0 (Gemini API)
**Status:** Production Ready
