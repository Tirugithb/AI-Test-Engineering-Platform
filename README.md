# 🤖 TestGen AI

## AI-Powered Multi-Agent Test Engineering Platform

---

# 🚀 Overview

**TestGen AI** is an AI-powered Multi-Agent Test Engineering Platform that transforms natural language requirements into software engineering artifacts. The platform intelligently classifies user requests and routes them to specialized AI agents to generate high-quality deliverables for QA, Automation, API Testing, Database Design, Architecture, DevOps, Code Generation, and Document Analysis.

The objective of **TestGen AI** is to accelerate software delivery by reducing manual effort in test engineering and documentation while improving consistency, productivity, and software quality.


# Architecture

# TestGen AI - Multi-Agent Architecture

                                    👤 USER
                                       │
                                       ▼
        ┌──────────────────────────────────────────────────┐
        │          🤖 TestGen AI (Streamlit UI)           │
        │  • Prompt Input                                 │
        │  • File Upload                                  │
        │  • Chat Interface                               │
        └──────────────────────────────────────────────────┘
                                       │
                                       ▼
        ┌──────────────────────────────────────────────────┐
        │             🧠 Artifact Classifier              │
        │     Detects Request Type / Artifact Type        │
        └──────────────────────────────────────────────────┘
                                       │
                                       ▼
        ┌──────────────────────────────────────────────────┐
        │              🎯 Orchestrator Agent              │
        │   Selects and Invokes the Appropriate Agent     │
        └──────────────────────────────────────────────────┘
                                       │
        ───────────────────────────────┼──────────────────────────────
                                       │
      ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
      │Requirement│ │   QA     │ │   API    │ │Automation│ │ Database │
      │   Agent   │ │  Agent   │ │  Agent   │ │  Agent   │ │  Agent   │
      └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘

      ┌──────────┐ ┌──────────┐ ┌────────────────┐ ┌──────────┐
      │Architecture││ DevOps  │ │Code Generation│ │ Document │
      │   Agent    ││  Agent  │ │     Agent      │ │  Agent   │
      └──────────┘ └──────────┘ └────────────────┘ └──────────┘
                                       │
                                       │
                     (Only the Selected Agent Executes)
                                       │
                                       ▼
        ┌──────────────────────────────────────────────────┐
        │          📝 Prompt Engineering Layer             │
        │  Builds Specialized Prompt for Selected Agent    │
        └──────────────────────────────────────────────────┘
                                       │
                                       ▼
        ┌──────────────────────────────────────────────────┐
        │             🔷 Google Gemini LLM                │
        │      AI Processing & Content Generation          │
        └──────────────────────────────────────────────────┘
                                       │
                                       ▼
        ┌──────────────────────────────────────────────────┐
        │              📦 Generated Artifact              │
        │ BRD │ Test Cases │ SQL │ DevOps │ Code │ Docs   │
        └──────────────────────────────────────────────────┘
                                       │
                                       ▼
        ┌──────────────────────────────────────────────────┐
        │           🖥️ Streamlit Response UI              │
        │  • Result Display                               │
        │  • Response Time                                │
        │  • Metrics                                      │
        │  • Chat History                                 │
        └──────────────────────────────────────────────────┘
                                       │
                                       ▼
                                    👤 USER


**This architecture is accurate because**
* User submits a prompt.
* Streamlit UI collects the prompt and optional uploaded document.
* Artifact Classifier determines the artifact type (qa, devops, database_sql, architecture, etc.).
* Orchestrator Agent routes the request.
* Only one specialized agent executes for that request.
* That agent performs prompt engineering and prepares the final prompt.*
* The prompt is sent to Google Gemini.
* Gemini generates the artifact.
* The result is returned to the Streamlit UI, which displays the output and metrics to the user.

# Key Features

* Multi-Agent AI Architecture
* Business Requirement Document (BRD) Generation
* Test Case Generation
* API Test Case Generation
* Selenium Automation Script Generation
* SQL Queries & Database Design Generation
* Software & Cloud Architecture Generation
* DevOps Artifact Generation (Dockerfile, CI/CD, etc.)
* Code Generation & Design Pattern Solutions
* Document Summarization
* Functional Requirement Extraction
* Response Time Tracking
* Chat History Management
* Regression-Tested Platform


# Multi-Agent Architecture

TestGen AI consists of multiple specialized AI agents coordinated by an intelligent Orchestrator.

## Available Agents

* Requirement Agent
* QA Agent
* API Agent
* Automation Agent
* Database Agent
* Architecture Agent
* DevOps Agent
* Code Generation Agent
* Document Agent

## Core Components

* Artifact Classifier
* Orchestrator Agent
* Streamlit User Interface
* LLM Integration
* Document Processing Engine

---

# Technology Stack

## Programming Language

* Python

## Framework

* Streamlit

## Artificial Intelligence

* Google Gemini
* Prompt Engineering
* Multi-Agent Architecture

## Testing

* QA Engineering
* Automation Engineering

## Version Control

* Git
* GitHub



# Installation

## Prerequisites

Make sure the following are installed:

* Python 3.10 or above
* Git
* pip


## Clone the Repository

bash
git clone https://github.com/<your-github-username>/TestGen-AI.git



## Navigate to the Project

bash
cd TestGen-AI


## Install Dependencies

bash
pip install -r requirements.txt


## Run the Application

bash
streamlit run app.py


## Access the Application

Open your browser and navigate to:

http://localhost:8501


You can now start generating software engineering artifacts using natural language prompts.


# Project Structure

TestGen-AI/

│── agents/
│── prompts/
│── utils/
│── ui/
│── docs/
│── architecture/
│── prototype/
│── roadmap/
│── tests/
│── screenshots/
│── logs/
│── requirements.txt
│── README.md
│── LICENSE


# Example Prompts

## Requirement Engineering

* Generate BRD for Hospital Management System

## QA

* Generate Test Cases for Login Screen

## API

* Generate API Test Cases for Login API

## Automation

* Generate Selenium Automation Script for Login Page

## Database

* Generate ER Diagram for Banking System

## Architecture

* Generate Microservices Architecture for E-commerce

## DevOps

* Generate Dockerfile for FastAPI Application

## Code Generation

* Generate Python Singleton Design Pattern

## Document Analysis

* Summarize the uploaded document

* Extract functional requirements from the uploaded document


# Supported Artifacts

| Artifact                          | Supported |
| --------------------------------- | --------- |
| BRD                               | ✅         |
| Test Cases                        | ✅         |
| API Test Cases                    | ✅         |
| Selenium Automation Scripts       | ✅         |
| SQL Queries                       | ✅         |
| ER Diagrams                       | ✅         |
| Architecture Documents            | ✅         |
| DevOps Artifacts                  | ✅         |
| Code Generation                   | ✅         |
| Document Summary                  | ✅         |
| Functional Requirement Extraction | ✅         |


# Regression Testing

The platform has been validated through regression testing covering all supported agents.

| Module                | Status |
| --------------------- | ------ |
| Requirement Agent     | ✅ Pass |
| QA Agent              | ✅ Pass |
| API Agent             | ✅ Pass |
| Automation Agent      | ✅ Pass |
| Database Agent        | ✅ Pass |
| Architecture Agent    | ✅ Pass |
| DevOps Agent          | ✅ Pass |
| Code Generation Agent | ✅ Pass |
| Document Agent        | ✅ Pass |

## Regression Result

* **Total Test Cases:** 10
* **Passed:** 10
* **Failed:** 0
* **Pass Percentage:** **100%**

---

# Project Highlights

* Multi-Agent AI Architecture
* Intelligent Artifact Classification
* Dynamic Agent Routing
* Streamlit-Based Interactive UI
* Document Processing Capability
* Response Time Tracking
* Regression Tested
* 10/10 Test Cases Passed


# Future Roadmap

## Phase 1

* Professional GitHub Documentation
* Architecture Diagram
* UI Enhancements

## Phase 2

* PDF Export
* DOCX Export
* Enhanced Logging
* Analytics Dashboard

## Phase 3

* Cloud Deployment
* Docker Support
* CI/CD Integration

## Phase 4

* Enterprise Multi-Agent Ecosystem
* Advanced Knowledge Base
* Autonomous Test Engineering Assistant

---

# License

This project is licensed under the MIT License.


# Vision

> **Accelerating Software Quality Engineering through Intelligent Multi-Agent AI Automation.**
