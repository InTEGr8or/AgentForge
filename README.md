# AgentForge

## Vision

AgentForge is a multi-agent AI software engineering system designed to automate the development lifecycle using a hierarchical, "Society of Mind" architecture. It leverages standard DevOps tools and practices to manage and execute software development tasks with a high degree of autonomy and security.

## Core Architecture

The system is composed of three primary layers, analogous to Minsky's A-Brain, B-Brain, and C-Brain model.

### C-Brain: The Architect
- **Role:** High-level project management and planning.
- **Responsibilities:**
    - Ingests high-level goals from sources like GitHub Project boards.
    - Creates comprehensive project plans, including functional specifications, integration tests, architectural diagrams, and Gherkin specs.
    - Breaks down the project into logical, high-level tasks for the B-Brain.

### B-Brain: The Engineer
- **Role:** System design and task decomposition.
- **Responsibilities:**
    - Takes architectural plans from the C-Brain.
    - Designs the file structure, data flows, and class/module hierarchies.
    - Defines the specific function signatures and their cross-cutting concerns.
    - Generates highly-structured, Pydantic-defined tasks for the A-Brain.

### A-Brain: The Coder
- **Role:** Code implementation.
- **Responsibilities:**
    - Executes small, well-defined coding tasks based on the precise specifications from the B-Brain.
    - Writes, modifies, and tests individual functions or code blocks.
    - Ensures adherence to project-specific linting and coding standards.
    - Operates within a secure, isolated environment with its own Git identity.

## Technology and Workflow

The AgentForge ecosystem is designed as a dynamic marketplace that promotes efficiency and cost-effectiveness. For a detailed breakdown of this economic model, see the [Open Market Model documentation](./docs/open-market.md).

### 1. Task Initiation & Bidding
- **Task Creation:** A new task is created by adding an Issue or moving a card on a **GitHub Project board**. The task description should include a **bounty** (the maximum price the project is willing to pay).
- **Dispatcher & Auctioneer:** A **GitHub Action** triggers a central "Dispatcher" service (e.g., AWS Lambda). This service formally advertises the task to all registered agents.
- **Bidding:** Agents (both internal and external proxies) analyze the task and submit bids based on their capabilities, cost models, and performance history. The Dispatcher selects the winning agent based on an optimization strategy (e.g., lowest cost, highest success probability).

### 2. Orchestration & Agent Hierarchy
- **Orchestration Framework:** **CrewAI** is used to manage the high-level, process-oriented workflow *within* a task, especially for complex projects requiring the A/B/C-Brain hierarchy.
- **Agent Hierarchy:**
    - **C-Brain (Architect):** Handles high-level planning and specification.
    - **B-Brain (Engineer):** Designs the system and decomposes the work.
    - **A-Brain (Coder):** Implements the specific code.

### 3. Communication & Execution
- **Structured Communication:** Agents communicate using structured **Pydantic** models passed through a message queue system (**Amazon SQS**). This ensures clear, predictable instructions.
- **Execution Environment:** Each agent runs in a portable **Docker container**, deployed as a serverless task on **AWS ECS with Fargate**. The entire infrastructure is managed via the **AWS CDK (IaC)**.

### 4. Economic Model & Optimization
- **Agent Registry:** A central registry (e.g., DynamoDB) stores profiles for all available agents, including their capabilities, cost models (e.g., real-time, batch), and performance metrics.
- **Centralized Ledger:** A transaction log records the full lifecycle of each task: the winning bid, the actual cost (e.g., LLM tokens, compute time), completion status, and quality scores.
- **Feedback Loop:** This ledger data continuously updates the Agent Registry, creating an evolutionary pressure where more efficient and effective agents are more likely to win future tasks.

### 5. Code & Security
- **Standard Tooling:** Agents interact with codebases using standard **Git** operations.
- **Secure Identities:** Each agent has its own GitHub account and fine-grained permissions managed through **IAM roles** and **GitHub branch protection rules**.
- **Quality Gates:** Code reviews and pull request approvals are enforced as part of the workflow, separating development from verification.
