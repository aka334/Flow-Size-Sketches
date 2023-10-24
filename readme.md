# Project 3: Implementation of Flow-Size Sketches

This project provides implementations for three flow estimation techniques: **CountMin**, **Counter Sketch**, and **Active Counter**.

## Techniques and Specifications:

### 1. CountMin

- **Input**:
    1. File: `project3input.txt` with the following structure:
        - First line: Number `n` of flows.
        - Next `n` lines: Each contains a flow id (source address) and the number of packets in the flow.
    2. Number of counter arrays, `k` (demo value: 3).
    3. Number of counters in each array, `w` (demo value: 3000).

- **Function**: Records the sizes of all flows, queries for estimated sizes, and computes the average error of all flows.

- **Output** (`countmin.txt`):
    1. First line: Average error among all flows.
    2. Next 100 lines: Flows of the largest estimated sizes, including flow id, estimated size, and true size.

### 2. Counter Sketch
- **Input**:
    1. File: `project3input.txt` (same structure as for CountMin).
    2. Number of counter arrays, `k` (demo value: 3).
    3. Number of counters in each array, `w` (demo value: 3000).

- **Function**: Records sizes of all flows using the Counter Sketch method, queries for estimated sizes, and computes average error.

- **Output** (`countersketch.txt`):
    1. First line: Average error among all flows.
    2. Next 100 lines: Flows of the largest estimated sizes, with flow id, estimated size, and true size.

### 3. Active Counter
- **Input**: A single active counter of 32 bits. The number part of the counter uses 16 bits, and the exponent part also uses 16 bits.
- **Function**: Probabilistically increases the active counter by one for 1,000,000 times.
- **Output** (`activecount.txt`): Final value of the active counter in decimal format.
## How to Run:
### Dependencies:
- Python 3.x
### Execution:
1. **CountMin**:
    ```bash
    python3 countmin.py
    ```
2. **Counter Sketch**:
    ```bash
    python3 countersketch.py
    ```
3. **Active Counter**:
    ```bash
    python3 active_count.py
    ```
## Additional Notes:
The implementations were developed following specific specifications detailing the functionalities and objectives of each technique.
