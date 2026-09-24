<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=180&section=header&text=Network%20Connection%20Monitor&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=35" />
</p>

<p align="center">
  A Python-based TCP connection monitoring project focused on connection tracking, logging, analysis, visualization, and basic security detection.
</p>

---

## Project Status

**Active Development**

This project is continuously evolving alongside the author's progress in Python, Linux, networking, and cybersecurity.

The current implementation is not considered a final or production-ready version. The project is intentionally developed step by step, and its architecture and functionality will change as new concepts are learned and applied.

As the project develops, existing code will be regularly reviewed, refactored, improved, and extended.

> The more I learn, the more this project will evolve.

---

## Overview

Network Connection Monitor is an educational TCP connection monitoring application written in Python.

The project started as a simple TCP server and gradually evolved into a connection monitoring system capable of tracking clients, recording connection information, calculating statistics, detecting repeated connections from the same IP address, handling multiple clients using threading, and visualizing connection data.

The project is intentionally developed incrementally rather than being designed as a complete system from the beginning.

Each new feature is introduced to apply concepts learned during the development process and to improve the overall understanding of Python networking, data processing, visualization, and security.

---

## Current Features

* TCP server and client communication
* Connection ID generation
* Client IP and port tracking
* Server port tracking
* Connection date and time tracking
* Connection status tracking
* Connection duration calculation
* Connection history
* Connection search by ID
* Persistent connection logging
* Separate dashboard data logging
* Connection statistics
* Unique IP analysis
* IP connection counting
* Basic suspicious IP detection
* Security alert messages
* Multi-client support using Python threading
* Connection duration visualization
* Bar chart based connection monitoring
* Connection duration labels on charts

---

## Current Architecture

The current version intentionally uses a simple structure while the project is still evolving.

```text
network-connection-monitor/

├── server.py
├── client.py
├── dashboard.py
├── README.md
└── .gitignore
```

Runtime log files are generated inside the `logs/` directory and are excluded from version control.

The architecture will be gradually refactored as the project grows.

For example, connection management, security detection, statistics, logging, and dashboard functionality may eventually be separated into dedicated modules.

This refactoring will happen incrementally rather than all at once.

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

   |

   v

Dashboard Data Updated
```

---

## Security Monitoring

The current implementation includes a basic detection mechanism for identifying IP addresses that establish an unusually high number of connections.

When an IP exceeds the configured connection threshold, the system generates a security alert.

This feature is intentionally simple and is currently used to practice fundamental concepts such as:

* Connection analysis
* IP-based detection
* Threshold-based monitoring
* Security alerts
* Network activity observation

The detection logic will become more advanced as the project develops.

---

## Statistics

The current monitoring system provides basic connection statistics, including:

* Total connections
* Active connections
* Disconnected connections
* Unique IP addresses
* Average connection duration
* Number of connections per IP

These statistics are currently calculated from the connection records maintained by the server.

---

## Logging

The project currently uses separate JSON files for different logging purposes.

### Connection History

The main connection log stores connection events and records the lifecycle of each connection.

It contains information such as:

* Connection ID
* Client IP
* Client port
* Connection date
* Connection time
* Exit time
* Connection status
* Connection duration

The main connection log may contain both the initial active record and the final updated record.

### Dashboard Data

A separate JSON log is maintained specifically for the dashboard.

```text
logs/
├── connections.json
└── connections_for_dashboard.json
```

`connections_for_dashboard.json` contains the finalized connection records used by `dashboard.py`.

This separation allows the dashboard to work with completed connection records without having to process the intermediate active records.

Runtime log files are excluded from version control and are not intended to be committed to the repository.

---

## Dashboard

The project now includes an initial graphical dashboard implemented with Python and Matplotlib.

The current dashboard focuses on visualizing connection duration.

The chart uses:

* X-axis: Connection identifier
* Y-axis: Connection duration in seconds
* Each bar: One connection
* Bar height: Duration of the connection
* Label above each bar: Exact connection duration

A simplified representation of the current visualization is:

```text
Duration (seconds)

30 |                 █
   |                 █
20 |        █        █
   |        █        █
10 |   █    █        █
   |   █    █        █
 0 +-------------------------
    Connection 1
             Connection 2
                      Connection 3
```

The dashboard currently reads its data from:

```text
logs/connections_for_dashboard.json
```

The visualization is intentionally kept simple at this stage. More advanced dashboard functionality will be introduced gradually as the project develops.

---

## Multi-Client Support

The server currently supports multiple simultaneous clients using Python's `threading` module.

Each accepted client connection is handled by a separate thread, allowing the server to continue accepting new connections while existing clients remain connected.

This feature was introduced as part of the project's progression from a sequential TCP server toward a more realistic network monitoring architecture.

---

## Technologies

* Python
* Socket Programming
* TCP
* Client-Server Architecture
* `socket`
* `threading`
* `datetime`
* `time`
* JSON
* File I/O
* Matplotlib
* Git

---

## Running the Project

Clone the repository:

```bash
git clone git@github.com:Morez-Momeni/Network-Connection-Monitor.git
```

Enter the project directory:

```bash
cd Network-Connection-Monitor
```

Start the server:

```bash
python server.py
```

Open another terminal and start the client:

```bash
python client.py
```

Multiple clients can be connected to the server simultaneously.

To view the connection duration dashboard:

```bash
python dashboard.py
```

The dashboard reads finalized connection data from the dashboard-specific JSON log.

---

## Example

A connection may produce information similar to:

```text
====================

Connection#1

====================

IP:127.0.0.1

Port:52341

ServerPort:5000

Date:22-09-2026

Time:23:10:42

====================
```

After the connection is closed, the system calculates its duration and updates the final connection record.

The finalized record can then be used by the dashboard for visualization.

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
* JSON data handling
* Data structures
* Connection lifecycle management
* Network activity analysis
* Data visualization
* Basic security monitoring
* Code refactoring
* Software architecture

---

## Development Philosophy

This project follows a learning-driven development approach.

Instead of trying to design and implement the final architecture from the beginning, the project grows alongside the author's knowledge.

The development cycle is:

```text
Learn

  |

  v

Understand

  |

  v

Implement

  |

  v

Test

  |

  v

Analyze

  |

  v

Visualize

  |

  v

Refactor

  |

  v

Extend

  |

  +------------> Learn More
```

As new concepts are learned, they will be applied to the project where appropriate.

This means that the codebase, architecture, and features are expected to change over time.

---

## Future Development

Planned improvements may include:

* Modular project architecture
* Improved connection management
* Better logging architecture
* Structured log formats
* Improved error handling
* More advanced IP analysis
* Additional security detection mechanisms
* Better concurrency management
* Configuration management
* Improved statistics and reporting
* Real-time dashboard updates
* Additional connection visualizations
* More detailed network activity analysis
* Additional networking and security features

These features will be implemented gradually as the project develops.

---

## Disclaimer

This project is developed for educational purposes.

It is intended to demonstrate fundamental concepts related to Python networking, TCP communication, connection monitoring, logging, concurrency, data visualization, and basic security detection.

It is not intended to replace production-grade network monitoring systems, IDS/IPS solutions, firewalls, or other professional security infrastructure.

---

## Purpose

The primary purpose of this project is practical learning.

Rather than building the entire application at once, the project is developed step by step. Each new feature provides an opportunity to apply newly learned concepts in Python, Linux, networking, and cybersecurity.

The repository therefore represents both the development of a network monitoring application and the progression of the learning process behind it.

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=120&section=footer" />
</p>
