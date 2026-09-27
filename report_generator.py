from datetime import datetime

def generate_report(player_id, message, detected_words):

    report = f"""
GAMEGUARD AI - TOXICITY REPORT
================================

Player ID      : {player_id}
Date & Time    : {datetime.now()}

Chat Message   : {message}

Detected Words : {", ".join(detected_words)}

Status         : TOXIC CONTENT DETECTED
Action         : Message flagged for moderation

================================
"""

    with open("toxicity_report.txt", "a") as file:
        file.write(report)

    return report