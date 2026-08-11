# Collaborative Multi-Agent AI System

A local AI-powered collaborative multi-agent system built with Python, Ollama, and Gemma 3.

The project demonstrates how multiple specialized AI agents can work together to solve a user request through planning, implementation, review, and iterative improvement.

The entire AI workflow runs locally on your computer using Ollama, so no paid API key is required.



## Project Overview

Traditional LLM applications usually rely on a single model call to answer a request.

This project uses multiple specialized agents:

- Coordinator Agent
- Planner Agent
- Developer Agent
- Reviewer Agent

Each agent has a specific responsibility and collaborates with the other agents to complete the user's request.

The Reviewer Agent can evaluate the Developer's solution and request improvements when necessary.



## Architecture

```text
                 USER REQUEST
                       |
                       v
              COORDINATOR AGENT
                       |
                       v
                PLANNER AGENT
                       |
                 Creates Plan
                       |
                       v
               DEVELOPER AGENT
                       |
             Creates Implementation
                       |
                       v
                REVIEWER AGENT
                       |
              Reviews the Solution
                       |
             +---------+---------+
             |                   |
             |                   |
      STATUS: APPROVED   STATUS: NEEDS IMPROVEMENT
             |                   |
             |                   v
             |            DEVELOPER AGENT
             |                   |
             |             Revises Solution
             |                   |
             |                   v
             |            REVIEWER AGENT
             |                   |
             +---------<---------+
                       |
                       v
                  FINAL RESULT

Agents
Coordinator Agent

The Coordinator Agent controls the complete workflow.

Responsibilities:

Receives the user's task
Sends the request to the Planner Agent
Sends the plan to the Developer Agent
Sends the developer solution to the Reviewer Agent
Handles the review feedback loop
Returns the final result
Planner Agent

The Planner Agent analyzes the user's request and creates a structured development plan.

Responsibilities:

Understand the user request
Break the request into smaller tasks
Identify implementation requirements
Identify edge cases
Produce instructions for the Developer Agent
Developer Agent

The Developer Agent receives the Planner Agent's plan and generates the implementation.

Responsibilities:

Understand the development plan
Generate Python code
Handle edge cases
Improve code quality
Revise the solution based on reviewer feedback

Reviewer Agent

The Reviewer Agent performs a technical review of the Developer Agent's solution.

It evaluates:

Correctness
Code quality
Error handling
Bugs
Missing edge cases

Maintainability

The Reviewer Agent returns one of two statuses:

STATUS: APPROVED

or

STATUS: NEEDS IMPROVEMENT

If improvements are required, the Coordinator sends the review feedback back to the Developer Agent.

Technologies Used
Python
Ollama
Gemma 3
Requests
Git
GitHub
VS Code

Why Ollama?

Ollama allows Large Language Models to run locally.

Benefits:

No paid API required
No API key required
Local inference
Easy model management
Simple local REST API
Useful for experimenting with AI agents

The application communicates with Ollama using:

http://localhost:11434/api/generate

Project Structure
collaborative-multi-agent-system/
│
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── coordinator.py
│   │   ├── planner.py
│   │   ├── developer.py
│   │   └── reviewer.py
│   │
│   └── main.py
│
├── .gitignore
├── README.md
└── requirements.txt

Prerequisites

Before running the project, install:

Python 3
Git
Ollama
VS Code or another code editor
Installation

1. Clone the repository
git clone https://github.com/pavanreddy-kpr/collaborative-multi-agent-system.git

Move into the project directory:

cd collaborative-multi-agent-system

2. Create a Python virtual environment

On macOS or Linux:

python3 -m venv venv

Activate it:

source venv/bin/activate

3. Install Python dependencies
pip install -r requirements.txt
Ollama Setup

Install Ollama on your machine.

After installing, verify:

ollama --version

Download and run Gemma 3:

ollama run gemma3

The first run downloads the model.

Once the model has been downloaded, you can exit the Ollama chat with:

/bye

Ollama will continue to make the model available locally.

Run the Multi-Agent System

Make sure your Python virtual environment is active.

Run:

python3 src/main.py

You will see:

==================================================
      COLLABORATIVE MULTI-AGENT SYSTEM
==================================================

Enter your task:

Example request:

Create a Python student management system that can add, view, update, and delete students using CSV storage

Example Workflow
User submits a task

        ↓

Coordinator Agent receives task

        ↓

Planner Agent creates development plan

        ↓

Developer Agent generates implementation

        ↓

Reviewer Agent evaluates implementation

        ↓

If approved:

STATUS: APPROVED

        ↓

Final result


If improvements are required:

STATUS: NEEDS IMPROVEMENT

        ↓

Developer Agent receives reviewer feedback

        ↓

Developer Agent improves solution

        ↓

Reviewer Agent reviews again

Example Reviewer Output
Correctness:
The implementation satisfies the core requirements.

Code Quality:
The solution is well structured and readable.

Missing Edge Cases:
Additional validation should be added for malformed CSV data.

Suggestions:
Improve exception handling and input validation.

STATUS: NEEDS IMPROVEMENT

The Coordinator can then send this feedback back to the Developer Agent automatically.

Key Features
Multi-agent AI architecture
Specialized AI agents
Local LLM inference
Planner-to-developer collaboration
Automated AI code review
Reviewer feedback loop
Iterative solution improvement
No paid AI API required
Modular Python architecture
GitHub-ready project structure

Current Workflow
User
  |
  v
Coordinator
  |
  v
Planner
  |
  v
Developer
  |
  v
Reviewer
  |
  +---- APPROVED ----------> Final Result
  |
  +---- NEEDS IMPROVEMENT
             |
             v
         Developer
             |
             v
         Reviewer

Future Improvements

Future versions of this project can include:

LangGraph orchestration
Research Agent
Testing Agent
Security Agent
Memory Agent
Tool-using agents
Web search capabilities
Persistent conversation memory
Streamlit web interface
FastAPI backend
SQLite or PostgreSQL storage
Docker support
Automated unit testing
Logging and monitoring
Multiple local LLM support
Agent performance metrics
Future Architecture
                       USER
                         |
                         v
                   COORDINATOR
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
       PLANNER       RESEARCHER      ANALYST
          |              |              |
          +--------------+--------------+
                         |
                         v
                    DEVELOPER
                         |
                         v
                      TESTER
                         |
                         v
                     REVIEWER
                         |
                  +------+------+
                  |             |
               APPROVED      REVISE
                  |             |
                  |             v
                  |         DEVELOPER
                  |             |
                  +-------------+
                         |
                         v
                    FINAL RESULT
Learning Objectives

This project demonstrates concepts including:

Generative AI
Large Language Models
Multi-agent systems
Agent orchestration
Prompt engineering
Local LLM deployment
AI code generation
AI code review
Feedback loops
Modular software architecture
Security

Do not commit secrets or API keys to GitHub.

The .gitignore file excludes:

venv/
__pycache__/
*.pyc
.env
.DS_Store

Since this project uses Ollama locally, no cloud AI API key is required.

Author

Pavan Reddy

GitHub:

pavanreddy-kpr

License

This project is intended for learning, experimentation, and portfolio demonstration.


After pasting it into `README.md`, press **Command + S**.

Then update GitHub:

```bash
git status
git add README.md
git commit -m "Add professional project documentation"
git push