import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))

# Prompt user to enter scores
scores = []
num_nodes = int(input("Enter the number of nodes: "))
for i in range(num_nodes):
    score = int(input(f"Enter score for node {i}: "))
    scores.append(score)

# Calculate tree depth
treeDepth = math.log(len(scores), 2)

# Display optimal value
print("The optimal value is:", end=" ")
print(minimax(0, 0, True, scores, treeDepth))
