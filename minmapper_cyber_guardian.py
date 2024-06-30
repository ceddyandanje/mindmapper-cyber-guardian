from graphviz import Digraph

# Create a Digraph object with layout settings for a more compact, square structure
dot = Digraph(engine='neato')
dot.attr(size="10,10", ratio="fill")

# Game Concept
dot.node('A', 'Game Concept')
dot.node('A1', 'Objective')
dot.node('A2', 'Key Features')
dot.node('A3', 'Target Audience')
dot.edge('A', 'A1')
dot.edge('A', 'A2')
dot.edge('A', 'A3')

# Story and Characters
dot.node('B', 'Story and Characters')
dot.node('B1', 'Main Storyline')
dot.node('B2', 'Subplots')
dot.node('B3', 'Characters')
dot.edge('B', 'B1')
dot.edge('B', 'B2')
dot.edge('B', 'B3')

dot.node('B3a', 'Protagonist')
dot.node('B3b', 'Antagonists')
dot.node('B3c', 'Supporting Characters')
dot.edge('B3', 'B3a')
dot.edge('B3', 'B3b')
dot.edge('B3', 'B3c')

# Hacking Techniques
dot.node('C', 'Hacking Techniques')
dot.node('C1', 'Network Scanning')
dot.node('C2', 'Vulnerability Exploitation')
dot.node('C3', 'Social Engineering')
dot.node('C4', 'Password Cracking')
dot.node('C5', 'Wi-Fi Hacking')
dot.node('C6', 'Malware Analysis')
dot.edge('C', 'C1')
dot.edge('C', 'C2')
dot.edge('C', 'C3')
dot.edge('C', 'C4')
dot.edge('C', 'C5')
dot.edge('C', 'C6')

# Mini-Games/Challenges
dot.node('D', 'Mini-Games/Challenges')
dot.node('D1', 'Capture the Flag (CTF)')
dot.node('D2', 'Code Breaking')
dot.node('D3', 'Intrusion Detection')
dot.node('D4', 'Forensics')
dot.edge('D', 'D1')
dot.edge('D', 'D2')
dot.edge('D', 'D3')
dot.edge('D', 'D4')

# Skill Progression
dot.node('E', 'Skill Progression')
dot.node('E1', 'Skill Tree')
dot.node('E2', 'Tools and Software')
dot.edge('E', 'E1')
dot.edge('E', 'E2')

# Multiplayer Mode
dot.node('F', 'Multiplayer Mode')
dot.node('F1', 'Co-op Missions')
dot.node('F2', 'PvP Challenges')
dot.edge('F', 'F1')
dot.edge('F', 'F2')

# Realistic Environments
dot.node('G', 'Realistic Environments')
dot.node('G1', 'Simulated Networks')
dot.node('G2', 'Realistic Scenarios')
dot.edge('G', 'G1')
dot.edge('G', 'G2')

# Educational Aspect
dot.node('H', 'Educational Aspect')
dot.node('H1', 'Tutorials and Guides')
dot.node('H2', 'Quiz Challenges')
dot.edge('H', 'H1')
dot.edge('H', 'H2')

# Development Roadmap
dot.node('I', 'Development Roadmap')
dot.node('I1', 'Milestones')
dot.node('I2', 'Tasks and Deadlines')
dot.edge('I', 'I1')
dot.edge('I', 'I2')

# Testing and Feedback
dot.node('J', 'Testing and Feedback')
dot.node('J1', 'Beta Testing')
dot.node('J2', 'Bug Tracking')
dot.node('J3', 'Feature Requests')
dot.edge('J', 'J1')
dot.edge('J', 'J2')
dot.edge('J', 'J3')

# Marketing and Launch
dot.node('K', 'Marketing and Launch')
dot.node('K1', 'Marketing Strategy')
dot.node('K2', 'Promotional Materials')
dot.node('K3', 'Launch Event')
dot.edge('K', 'K1')
dot.edge('K', 'K2')
dot.edge('K', 'K3')

# Connect related nodes to show relationships
dot.edge('A', 'B')  # Game Concept to Story and Characters
dot.edge('A', 'C')  # Game Concept to Hacking Techniques
dot.edge('A', 'D')  # Game Concept to Mini-Games/Challenges
dot.edge('A', 'E')  # Game Concept to Skill Progression
dot.edge('A', 'F')  # Game Concept to Multiplayer Mode
dot.edge('A', 'G')  # Game Concept to Realistic Environments
dot.edge('A', 'H')  # Game Concept to Educational Aspect
dot.edge('A', 'I')  # Game Concept to Development Roadmap
dot.edge('A', 'J')  # Game Concept to Testing and Feedback
dot.edge('A', 'K')  # Game Concept to Marketing and Launch

dot.edge('B', 'C')  # Story and Characters to Hacking Techniques
dot.edge('B', 'D')  # Story and Characters to Mini-Games/Challenges
dot.edge('B', 'E')  # Story and Characters to Skill Progression

dot.edge('C', 'D')  # Hacking Techniques to Mini-Games/Challenges
dot.edge('C', 'E')  # Hacking Techniques to Skill Progression
dot.edge('C', 'F')  # Hacking Techniques to Multiplayer Mode
dot.edge('C', 'G')  # Hacking Techniques to Realistic Environments
dot.edge('C', 'H')  # Hacking Techniques to Educational Aspect

dot.edge('D', 'E')  # Mini-Games/Challenges to Skill Progression
dot.edge('D', 'F')  # Mini-Games/Challenges to Multiplayer Mode

dot.edge('E', 'F')  # Skill Progression to Multiplayer Mode
dot.edge('E', 'G')  # Skill Progression to Realistic Environments
dot.edge('E', 'H')  # Skill Progression to Educational Aspect

dot.edge('F', 'G')  # Multiplayer Mode to Realistic Environments

dot.edge('I', 'J')  # Development Roadmap to Testing and Feedback
dot.edge('I', 'K')  # Development Roadmap to Marketing and Launch

dot.edge('J', 'K')  # Testing and Feedback to Marketing and Launch

# Render the mindmap
dot.render('/mnt/data/cyber_guardian_mindmap_connected', format='png')
