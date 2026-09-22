<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&height=220&section=header&text=GIT%20LEARNING&fontSize=48&fontColor=ffffff&fontAlignY=38&desc=From%20Fundamentals%20to%20Internals&descAlignY=58&descSize=18&color=gradient&customColorList=12,20,30,2"
    width="100%"
  />

</p>
<p align="center">
  <b>Network Connection Monitor</b>
</p>


# Network Connection Monitor

A Python-based TCP connection monitoring project focused on connection tracking, logging, basic traffic analysis, and security-oriented detection.

This project is built as a practical learning project and is continuously developed alongside the author's progress in Python, networking, Linux, and cybersecurity.

---

## Project Status

**Active Development**

This project is intentionally not considered a finished or production-ready application.

The current implementation represents the author's current understanding of Python networking and security concepts. As new concepts are learned, the project will be continuously improved, refactored, and extended.

Future updates may include:

* Code refactoring and better project architecture
* Improved connection management
* More advanced logging
* Better statistics and traffic analysis
* Additional security detection mechanisms
* Improved error handling
* Better concurrency management
* More structured configuration
* Additional networking and security features

The goal is for this project to evolve together with the author's technical knowledge.

> The more concepts I learn, the more this project will grow, change, and improve.

---

## Overview

Network Connection Monitor is an educational TCP monitoring application written in Python.

The project started as a simple TCP server and gradually evolved into a connection monitoring system capable of tracking clients, recording connection information, calculating statistics, detecting repeated connections from the same IP address, and handling multiple clients using threading.

The project is intentionally developed incrementally rather than being designed as a complete system from the beginning.

---

## Current Features

* TCP server and client communication
* Connection ID generation
* Client IP and port tracking
* Connection date and time tracking
* Connection status tracking
* Connection duration calculation
* Connection history
* Connection search by ID
* Persistent connection logging
* Connection statistics
* Unique IP analysis
* IP connection counting
* Basic suspicious IP detection
* Security alert messages
* Multi-client support using Python threading

---

## Current Architecture

The current version is intentionally kept simple while the project is still evolving.

```text
network-connection-monitor/
│
├── server.py
├── client.py
├── log.txt
├── README.md
└── .gitignore
```

As the project grows, the codebase will gradually be refactored into a more modular architecture.

---

## Connection Lifecycle

```text
Client
   |
   v
Connection Accepted
   |
   v
Connection ID Generated
   |
   v
Connection Recorded
   |
   v
Active
   |
   v
Data Exchange
   |
   v
Connection Closed
   |
   v
Duration Calculated
   |
   v
Record Updated
   |
   v
Log Written
```

---

## Technologies

* Python
* Socket Programming
* TCP
* `socket`
* `threading`
* `datetime`
* `time`
* File I/O

---

## Running the Project

Start the server:

```bash
python server.py
```

Then run the client in another terminal:

```bash
python client.py
```

Multiple clients can be connected to the server simultaneously.

---

## Security Detection

The current implementation includes a basic detection mechanism for identifying IP addresses that establish an unusually high number of connections.

This mechanism is intentionally simple and exists primarily to demonstrate fundamental security monitoring concepts.

It is not intended to replace a production IDS, IPS, firewall, or network monitoring platform.

---

## Learning Objectives

This project is being developed to gain practical experience with:

* Python networking
* TCP communication
* Socket programming
* Client-server architecture
* Concurrent connections
* Threading
* Logging
* Data structures
* Connection lifecycle management
* Basic security monitoring
* Network-oriented programming
* Code refactoring and software architecture

---

## Future Development

This project will continue to evolve as new concepts are learned.

The development process is intentionally incremental:

```text
Learn
  |
  v
Implement
  |
  v
Test
  |
  v
Understand
  |
  v
Refactor
  |
  v
Extend
  |
  +---------> Learn More
```

The architecture, functionality, and implementation may change significantly over time as the project develops.

---

## Purpose

The primary purpose of this project is practical learning.

Rather than building the entire application from the beginning, the project is developed step by step. Each new feature is introduced as a way to apply newly learned concepts in Python, networking, Linux, and cybersecurity.

This repository therefore represents not only the application itself, but also the progression of the development and learning process behind it.

<p align="center">

  <img
    src="https://capsule-render.vercel.app/api?type=waving&height=140&section=footer&text=LEARN%20%E2%80%A2%20PRACTICE%20%E2%80%A2%20BREAK%20%E2%80%A2%20FIX&fontSize=22&fontColor=ffffff&fontAlignY=65&color=gradient&customColorList=12,20,30,2"
    width="100%"
  />

</p>


