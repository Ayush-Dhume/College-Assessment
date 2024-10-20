class DecisionTree:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def traverse(self, node):
        if isinstance(node, dict):
            question = list(node.keys())[0]
            answer = input(question + " (Yes/No): ")
            next_node = node[question][answer]
            return self.traverse(next_node)
        else:
            return node


K_Base = {
    "Is the computer powering on?": {
        "Yes": {
            "Is there a beeping sound?": {
                "Yes": "Check the RAM and CPU",
                "No": {
                    "Is the display showing any output?": {
                        "Yes": "Check the display connections and settings",
                        "No": "Check the power supply and motherboard"
                    }
                }
            }
        },
        "No": "Check the power supply and cables"
    }
}

tree = DecisionTree(K_Base)

result = tree.traverse(K_Base)

print("\nRecommendation:", result)