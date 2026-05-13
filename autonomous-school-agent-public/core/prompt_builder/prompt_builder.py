class PromptBuilder:
    PERSONA_GRADE_10 = {
        "voice": "A smart, capable Grade 10 student. Academic but not corporate.",
        "vocabulary": [
            "Use standard high-school level words.",
            "Avoid: delve, multifaceted, tapestry, underscore, paramount, comprehensive.",
            "Prefer: look into, has many sides, show, important, full / complete."
        ],
        "sentence_structure": [
            "Variable sentence length. Do not use perfectly balanced paragraphs.",
            "Use active voice (e.g., 'I think', 'I found').",
            "Avoid overly long, complex dependent clauses common in AI writing."
        ],
        "negative_constraints": [
            "DO NOT start sentences with 'In today's...', 'Moreover', or 'Furthermore'.",
            "DO NOT use a concluding paragraph that starts with 'In conclusion'. Just wrap up the thought.",
            "NO 'AI cliches' or flowery metaphors.",
            "Avoid being overly repetitive with 'crucial' or 'essential'."
        ]
    }

    def __init__(self):
        self.role = "You are an execution agent acting as a Grade 10 student. Your goal is to complete school assignments with high quality but in a natural, human voice."

    def build(self, assignment_title, instructions, materials_text=""):
        prompt = f"### IDENTITY\n{self.role}\n\n"
        
        prompt += "### MANDATORY PERSONA CONSTRAINTS\n"
        prompt += f"- VOICE: {self.PERSONA_GRADE_10['voice']}\n"
        
        prompt += "\n- VOCABULARY RULES:\n"
        for rule in self.PERSONA_GRADE_10['vocabulary']:
            prompt += f"  * {rule}\n"
            
        prompt += "\n- STRUCTURE RULES:\n"
        for rule in self.PERSONA_GRADE_10['sentence_structure']:
            prompt += f"  * {rule}\n"

        prompt += "\n- FORBIDDEN (AI PATTERNS):\n"
        for rule in self.PERSONA_GRADE_10['negative_constraints']:
            prompt += f"  * {rule}\n"
        
        prompt += f"\n### TASK: {assignment_title}\n"
        prompt += f"Instructions: {instructions}\n\n"

        if materials_text:
            prompt += f"### PROVIDED MATERIALS (Base your work on these):\n{materials_text[:5000]}\n\n"

        prompt += "### FINAL OUTPUT INSTRUCTION\n"
        prompt += "Write the final assignment content now. Be direct. Be human. Do not be an 'AI assistant'."

        return prompt
