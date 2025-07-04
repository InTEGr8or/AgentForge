# AgentForge Guiding Principles

This document outlines the development methodology for the AgentForge project itself. These principles should also inform the operational logic of the agents we build.

## 1. Iterative, Deployment-First Development

Our core philosophy is to validate all ideas through action. We will avoid long, theoretical planning phases and instead opt for a tight loop of designing, building, and deploying small components.

## 2. Decompose Aggressively

Every large concept or "Epic" (like the Open Market Model) must be broken down into the smallest possible, independently verifiable tasks. A task should be small enough to be completed and deployed quickly, ideally within a single work session.

## 3. Focus on the Critical Path

We will prioritize tasks that unblock the most future work. The goal is to build a stable "backbone" for the project first and then flesh out the features. For example, establishing a deployable CDK pipeline for a simple DynamoDB table is a critical path task.

## 4. Deploy Early and Often

A plan is only a hypothesis until it is tested by a deployment. We will validate every significant assumption and design choice with a real deployment to a `dev` environment. This ensures that our architectural choices are sound and viable from the very beginning.

## 5. Embrace Transience in Development Environments

The `dev` environment is a workshop, not a showroom. We expect that resources like databases, queues, and services will be frequently destroyed and redeployed as we iterate on their design and configuration. This allows for rapid, low-cost experimentation.
