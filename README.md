# 🚀 Agentic AI Python SDK – Hands‑On Playground

Welcome to my personal sandbox for exploring **agentic AI development** using the **OpenAI Agents Python SDK**.  
This repo is built as a learning space where I experiment with different agent patterns, tools, and workflows—heavily inspired by the official examples in:

**openai-agents-python/examples/agent_patterns/README.md**  
https://github.com/openai/openai-agents-python

If you're curious about how to build autonomous, tool‑using, multi‑step AI agents in Python, this repo is a great place to start.

---

## 🎯 Goals of This Repo

- Get hands‑on experience with the Agentic AI Python SDK  
- Understand and implement common agent patterns  
- Experiment with tools, memory, planning, and multi‑step reasoning  
- Use **uv** for fast, modern Python environment management and execution  
- Build a foundation for future agentic projects  

---

## 📁 Repository Structure

.
├── src/  
│   ├── basic_agent.py  
│   ├── tool_use_agent.py  
│   ├── multi_step_agent.py  
│   └── ...  
├── README.md  
├── pyproject.toml  
└── uv.lock  

Each script in `src/` corresponds to a specific agent pattern or concept.

---

## ⚙️ Setup & Installation (using uv)

### ✅ Prerequisites
- Python 3.10+
- `uv` installed (`pip install uv`)

### ✅ Install dependencies
uv sync

### ✅ Run any example
uv run src/basic_agent.py

---

## 🔑 Environment Variables

Make sure to set your OpenAI API key:

export OPENAI_API_KEY="your-key-here"

Or create a `.env` file:

OPENAI_API_KEY=your-key-here

---

## 🧠 What You’ll Learn Here

### ✅ Basic Agent Setup
- Creating an agent  
- Running simple tasks  
- Understanding the agent lifecycle  

### ✅ Tool‑Using Agents
- Defining tools  
- Letting agents call Python functions  
- Handling tool responses  

### ✅ Multi‑Step Reasoning
- Agents that plan, reflect, and iterate  
- Breaking down complex tasks  

### ✅ Patterns from the Official Examples
- Re‑implementing and customizing patterns from the OpenAI Agents repo  

---

## 🧪 Running Experiments

Feel free to tweak the agent prompts, add tools, or modify the reasoning loops.  
This repo is intentionally lightweight so you can experiment freely.

Some ideas:
- Add a file‑reading tool  
- Build a planning agent  
- Create a multi‑agent workflow  
- Try long‑running tasks with memory  

---

## 📚 References

- OpenAI Agents Python SDK: https://github.com/openai/openai-agents-python

---

## 🌟 Future Plans

- Add more advanced agent patterns  
- Integrate external APIs as tools  
- Explore agent evaluation and debugging  
- Build a small real‑world agentic application  
