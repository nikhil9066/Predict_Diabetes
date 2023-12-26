import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(e.stderr.strip())
        raise

# Define your commands
commands = [
    'echo Creating and Deploying pods',
    'kubectl apply -f flask-app-deployment.yaml',
    'kubectl apply -f flask-app-service.yaml',
    'kubectl get pods'
]

# Run each command
for command in commands:
    output = run_command(command)
    print(output)
