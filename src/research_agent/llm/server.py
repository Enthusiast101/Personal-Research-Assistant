import subprocess
import time
import requests
from research_agent.config.settings import HOST, PORT, MODEL


def initiate_server():
    command = [
        "llama",
        "serve",
        "-hf",
        MODEL,
        "--host",
        HOST,
        "--port",
        str(PORT),
    ]

    print("Starting llama-server...", flush=True)
    print("Command:", " ".join(command), flush=True)

    process = subprocess.Popen(
        command,
        stdout=None,
        stderr=None,
    )

    print(f"Waiting for llama-server at http://{HOST}:{PORT}...", flush=True)

    while True:
        if process.poll() is not None:
            raise RuntimeError(
                f"llama-server exited with code {process.returncode}"
            )

        try:
            response = requests.get(
                f"http://{HOST}:{PORT}/health",
                timeout=1,
            )

            if response.status_code == 200:
                print("llama-server is ready.", flush=True)
                return process

        except requests.exceptions.RequestException:
            pass

        time.sleep(0.5)

    return 


if __name__ == "__main__":
    process = initiate_server()

    try:
        process.wait()

    except KeyboardInterrupt:
        print("\nStopping llama-server...", flush=True)
        process.terminate()
        process.wait()