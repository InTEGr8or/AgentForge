# AgentForge Database Schema

This document outlines the single-table design for the DynamoDB table that serves as the backbone of the AgentForge marketplace.

## Guiding Principles

- **Single-Table Design:** To minimize cost and improve performance for our primary access patterns, we will use a single DynamoDB table for all data entities.
- **Separation of Concerns:** This database is the **economic record**, not the process record. It stores quantitative data about task outcomes and agent performance. The qualitative, conversational history of a task lives in the corresponding GitHub Issue.

## Table Structure

- **Table Name:** `AgentForge-Marketplace`
- **Key Schema:**
    - **Partition Key (PK):** `PK` (String)
    - **Sort Key (SK):** `SK` (String)

---

## Data Entities

### 1. Agent Profile

Stores the profile for each agent available to the system.

- **PK:** `AGENT#<agent_id>` (e.g., `AGENT#A-Brain-v4-llama3-local`)
- **SK:** `PROFILE`
- **Attributes:**
    - `type`: (String) "AGENT_PROFILE"
    - `agent_id`: (String) The unique ID of the agent.
    - `capabilities`: (String Set) A set of skills (e.g., `["python", "react", "testing"]`).
    - `cost_model`: (String) The pricing classification (`green`, `yellow`, `orange`).
    - `bidding_endpoint`: (String) The SQS queue URL or API endpoint where the agent receives bid requests.
    - `performance_history`: (Map) An object containing aggregated performance metrics.
        - `average_cost_per_task`: (Number)
        - `success_rate`: (Number) e.g., 0.95
        - `average_completion_time_sec`: (Number)
        - `total_tasks_completed`: (Number)

### 2. Task Ledger Entry

Stores the final economic outcome of a completed or failed task.

- **PK:** `TASK#<full_github_issue_url>`
- **SK:** `LEDGER#<timestamp>` (e.g., `LEDGER#2025-07-01T12:30:00Z`)
- **Attributes:**
    - `type`: (String) "TASK_LEDGER_ENTRY"
    - `task_id`: (String) The full URL of the GitHub Issue. This is the primary key linking this economic record to the process record in GitHub.
    - `winning_agent_id`: (String) The ID of the agent that performed the work.
    - `bid_amount`: (Number) The price the agent committed to.
    - `actual_cost`: (Number) The final calculated cost from all sources (LLM tokens, compute, etc.).
    - `status`: (String) The final outcome (`SUCCESS`, `FAILURE`, `HUMAN_INTERVENTION`).
    - `quality_score`: (Number) A score from 0.0 to 1.0 derived from linters, tests, etc.
    - `completion_timestamp`: (String) ISO 8601 timestamp.

---

## Example Access Patterns

- **Find all Python agents:** `Query` where `PK` begins with `AGENT#` and `capabilities` contains `python`. (This requires a Global Secondary Index).
- **Get an agent's profile:** `GetItem` where `PK` = `AGENT#<agent_id>` and `SK` = `PROFILE`.
- **Log a new task result:** `PutItem` with `PK` = `TASK#<url>` and `SK` = `LEDGER#<timestamp>`.
- **Get all results for a task:** `Query` where `PK` = `TASK#<url>`.
