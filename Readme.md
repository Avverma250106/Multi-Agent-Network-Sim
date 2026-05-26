Multi-Agent Autonomous Network Simulator
A research-oriented autonomous network simulation platform built completely in Python.
Features
Adaptive routing
Congestion-aware traffic engineering
Tick-based network simulation
Queue-based packet scheduling
QoS & priority traffic handling
Dynamic packet drops and congestion propagation
Telemetry and performance metrics
Current Capabilities
Graph-based network topology
Stateful packet lifecycle tracking
Queue backlog simulation
Asynchronous packet scheduling
Priority-aware packet routing
Delivery/drop ratio tracking
Queue delay analytics
Tech Stack
Python
NetworkX
Heap-based priority queues
Planned Features
Weighted Fair Queueing (WFQ)
Real-time visualization dashboard
Socket-based distributed agents
Reinforcement learning routing
Self-healing infrastructure
MLOps integration
Run The Project
Bash
git clone <repo-url>
cd multi-agent-network

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

python main.py
Vision
The long-term goal is to evolve this project into a research-grade autonomous networking simulator capable of supporting:
intelligent traffic engineering,
distributed coordination,
RL-driven routing,
and self-healing network infrastructure.
Author
Aksh Verma