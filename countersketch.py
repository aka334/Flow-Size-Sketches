import hashlib
import random

def hash_func(seed, key, mod_val):
    """Generate hash value for a key."""
    return int(hashlib.sha256((str(seed) + str(key)).encode()).hexdigest(), 16) % mod_val

def sign_hash_func(seed, key):
    """Generate -1 or 1 based on the hash of a key."""
    return 1 if hashlib.sha256((str(seed) + str(key)).encode()).hexdigest()[0] in "0123456789" else -1

def record(flow_id, num_packets, counters, k, w):
    """Record the flow in the Counter Sketch."""
    for i in range(k):
        index = hash_func(i, flow_id, w)
        counters[i][index] += num_packets * sign_hash_func(i, flow_id)

def query(flow_id, counters, k, w):
    """Query the estimated size of the flow from Counter Sketch."""
    estimates = []
    for i in range(k):
        index = hash_func(i, flow_id, w)
        estimates.append(counters[i][index] * sign_hash_func(i, flow_id))
    return median(estimates)

def median(lst):
    """Compute the median of a list."""
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2

def main():
    # Read input
    with open('project3input.txt', 'r') as file:
        n = int(file.readline().strip())
        flows = [list(map(str, line.strip().split())) for line in file.readlines()]
    
    k = 3
    w = 3000
    
    # Initialize counter arrays
    counters = [[0] * w for _ in range(k)]
    
    # Record all flows in Counter Sketch
    for flow_id, num_packets in flows:
        record(flow_id, int(num_packets), counters, k, w)
    
    # Query for estimated sizes and compute errors
    estimates = {}
    errors = []
    for flow_id, true_size in flows:
        true_size = int(true_size)
        est_size = query(flow_id, counters, k, w)
        errors.append(abs(est_size - true_size))
        estimates[flow_id] = (est_size, true_size)
    
    # Compute average error
    avg_error = sum(errors) / n
    
    # Sort flows based on estimated sizes
    top_flows = sorted(estimates.items(), key=lambda x: x[1][0], reverse=True)[:100]
    
   # Write to countersketch.txt
    with open('countersketch.txt', 'w') as output_file:
        output_file.write(str(avg_error) + '\n')
        for flow_id, (est_size, true_size) in top_flows:
            output_file.write(f"{flow_id} {est_size} {true_size}\n")

if __name__ == "__main__":
    main()
