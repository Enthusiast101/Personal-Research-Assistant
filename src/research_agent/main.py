import subprocess

from research_agent.llm.server import initiate_server
from research_agent.llm.model import generate_response


if __name__ == "__main__":
    process = initiate_server()

    try:
        print(generate_response("Hello World"))
        process.wait()

    except KeyboardInterrupt:
        print("\nStopping llama-server...", flush=True)
        process.terminate()
        process.wait()

    
