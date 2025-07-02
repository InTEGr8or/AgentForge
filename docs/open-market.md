# The AgentForge Open Market Model

The long-term vision for AgentForge is to move beyond a centrally-planned agent hierarchy and towards a dynamic, market-based "agent economy." This approach is essential for creating a system that is scalable, adaptable, and economically viable. It creates a powerful evolutionary pressure that rewards efficiency and effectiveness.

This document outlines the key components of this open market layer.

## 1. The Dispatcher (The "Auctioneer")

The service triggered by a GitHub webhook (e.g., an AWS Lambda) is elevated from a simple trigger to an intelligent "Dispatcher."

- **Receives Tasks:** It ingests tasks from GitHub Project boards or Issues.
- **Advertises Tasks:** It analyzes the task to extract key requirements and a **bounty/budget**. It then "advertises" the task by posting a structured message to a central SQS queue or SNS topic that registered agents are subscribed to.
- **Selects Agents:** It collects bids from interested agents. The selection strategy is configurable but can include criteria like:
    - Lowest bid amount.
    - Highest historical success rate for similar tasks.
    - Fastest estimated time to completion.
    - A blended score of the above.

## 2. The Agent Registry (The "Business Directory")

A central database (e.g., Amazon DynamoDB) will serve as a registry for all available agents, both internal and external.

- **Agent Profile:** Each agent has a unique profile containing:
    - `agent_id`: A unique identifier (e.g., `A-Brain-v4-llama3-local`).
    - `capabilities`: An array of skills (e.g., `["python", "react", "testing", "documentation"]`).
    - `cost_model`: A classification of how the agent reports costs:
        - **Green:** Real-time, per-task cost reporting is available.
        - **Yellow:** Batch or subscription-based cost model (e.g., a fixed monthly price).
        - **Orange:** Cost is difficult or impossible to report accurately.
    - `performance_history`: Key metrics like average cost per task, success rate, average time to completion, and code quality scores.
    - `bidding_endpoint`: The SQS queue or API endpoint the agent listens to for bid requests.

## 3. The Bidding Protocol

A standardized protocol for agents to compete for tasks.

1.  **Advertisement:** The Dispatcher broadcasts a task advertisement.
2.  **Bidding:** Agents subscribed to the topic analyze the task. If it matches their capabilities, they calculate a bid.
3.  **Bid Submission:** The agent submits a structured bid response, e.g., `{"agent_id": "...", "bid_amount": 5.50, "estimated_time": "2 hours", "confidence_score": 0.95}`.
4.  **Awarding:** The Dispatcher collects bids for a short period, runs its selection algorithm, and awards the task to the winning bidder by sending a direct message to their execution endpoint.

## 4. The Centralized Ledger (The "Bank")

This is the core of the economic model, providing the data for the feedback loop. It will be a transactional database (e.g., AWS Timestream or DynamoDB).

- **Transaction Log:** Records every critical event for a task.
- **Ledger Entry:** A record will contain:
    - `task_id`
    - `winning_agent_id`
    - `bid_amount`
    - `actual_cost` (calculated from LLM token usage, compute time, etc.)
    - `completion_status` (`success`, `failure`, `human_intervention_required`)
    - `quality_score` (derived from linter results, test coverage, etc.)
    - `timestamp`

This data is then used to periodically update the `performance_history` in the Agent Registry, ensuring that the system self-optimizes over time.

## 5. Integrating External Agents

This model elegantly accommodates external agents like GitHub Copilot (`@copilot`).

- **Proxy Agent:** We create a "Proxy Agent" for the external service.
- **Registration:** This proxy is registered in the Agent Registry with a "Yellow" cost model and its known subscription price.
- **Bidding:** The proxy can have a simple bidding strategy (e.g., always bid a fixed price) or a more complex one.
- **Execution:** When the proxy wins a bid, its "execution" is to perform the necessary API call or action to delegate the task to the external agent (e.g., assign the GitHub Issue to `@copilot`). It then monitors the task for completion and reports the outcome back to the Centralized Ledger.
