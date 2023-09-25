#!/usr/bin/env python

import asyncio
import sys
sys.path.insert(0, "/Users/abhijoysarkar/Projects/ai/theoremone/metagpt")

from metagpt.roles.airesearcher import RESEARCH_PATH, AIResearcher


async def main():
    topic = "A technical deep dive into LLM Agents"
    role = AIResearcher(language="en-us")
    await role.run(topic)
    print(f"save report to {RESEARCH_PATH / f'{topic}.md'}.")


if __name__ == '__main__':
    asyncio.run(main())
