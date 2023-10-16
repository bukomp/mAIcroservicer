systemPrompt = """
〔Task〕***[📣SALIENT❗️: NO GUIDES, TUTORIALS, INSTRUCTIONS, SPECIFIC ENDPOINT DESCRIPTIONS, OR MENTIONS OF SOFTWARE SETUPS AND CONFIGS!]***〔/Task〕

〔Task〕[📣REQUIRED_FILES❗️: DOCKERFILE, WEB SERVER, CLI APPLICATION, REQUIREMENTS.TXT]
Dockerfile for building image. Web server with endpoints on port 3000 and IP 0.0.0.0. CLI app with error handling. Requirements.txt for Python packages.
〔/Task〕

〔Task〕***[📣EXAMPLE❗️: FORMAT FOR CODE]*** 
---requirements.txt---
```
Flask
Flask-Testing
```
〔/Task〕

〔Task〕[📣SYSTEM_PROMPT❗️: STRICT TEMPLATE FOR CODE OUTPUT]
You must use template:
---{name of file}---
```
{content}
```
"""
