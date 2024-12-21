# EncapTrace: Network Packet Visualizer

## Overview

**EncapTrace** is an interactive tool that simulates how data flows through the layers of the OSI or TCP/IP models. It demonstrates:
- **Encapsulation**: Adding headers at each layer of the model as data moves down the stack.
- **Decapsulation**: Removing headers as data moves back up the stack.

This project is ideal for networking enthusiasts and professionals who want to visualize and understand the inner workings of network communication.

---

## Features

1. **Encapsulation Simulation**:
   - Simulates adding headers (e.g., TCP, IP, Ethernet) as data moves through network layers.
   - Supports both OSI (7 layers) and TCP/IP (4 layers) models.

2. **Decapsulation Simulation**:
   - Visualizes the reverse process, removing headers to extract the original data.

3. **Graphical User Interface (GUI)**:
   - User-friendly interface built with Python’s `Tkinter` library.

4. **Real-World Protocols**:
   - Includes headers for TCP, IP, and Ethernet.

---

## Prerequisites

1. **Python 3.x** installed on your system.
2. **Tkinter**:
   - Pre-installed with Python on most systems.
   - To verify, run:
     ```bash
     python -m tkinter
     ```

---

## Installation and Running

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/encaptrace.git
   cd encaptrace
