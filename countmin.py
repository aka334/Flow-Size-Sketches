import hashlib
import sys

def hash_functions(k, w):
    hash_funcs = []
    for _ in range(k):
        seed = hashlib.sha256(str(_).encode('utf-8')).hexdigest()
        hash_funcs.append(lambda x, seed=seed: int(hashlib.sha256((str(x) + seed).encode('utf-8')).hexdigest(), 16) % w)
    return hash_funcs

def count_min(file_path, k, w):
    with open(file_path, 'r') as f:
        n = int(f.readline().strip())
        flows = [tuple(line.strip().split()) for line in f.readlines()]
        
    counters = [[0] * w for _ in range(k)]
    hash_funcs = hash_functions(k, w)
    
    for flow_id, count in flows:
        count = int(count)
        for i in range(k):
            counters[i][hash_funcs[i](flow_id)] += count
    
    estimated_sizes = {}
    true_sizes = {flow_id: 0 for flow_id, _ in flows}
    
    for flow_id, count in flows:
        count = int(count)
        true_sizes[flow_id] += count
        if flow_id not in estimated_sizes:
            estimates = [counters[i][hash_funcs[i](flow_id)] for i in range(k)]
            estimated_sizes[flow_id] = min(estimates)
    
    errors = [abs(estimated_sizes[flow_id] - true_sizes[flow_id]) for flow_id, _ in flows]

    avg_error = sum(errors) / len(errors)
    top_estimated_flows = sorted(estimated_sizes.items(), key=lambda x: x[1], reverse=True)[:100]
    
    with open("countmin.txt", "w") as f:
        f.write(str(avg_error) + "\n")
        for flow_id, estimated_size in top_estimated_flows:
            f.write(f"{flow_id} {estimated_size} {true_sizes[flow_id]}\n")
    
if __name__ == "__main__":
    file_path = 'project3input.txt'
    k = 3  # number of counter arrays
    w = 3000  # number of counters in each array
    
    count_min(file_path, k, w)
