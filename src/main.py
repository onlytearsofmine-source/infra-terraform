import os
import sys
import logging
from pathlib import Path

# Set up logging configuration
logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

def initialize_infra():
    try:
        # Import required Terraform modules
        import terraform
        from terraform import Terraform
    except ImportError as e:
        logging.error(f"Failed to import Terraform module: {str(e)}")
        sys.exit(1)

    # Define the Terraform working directory
    tf_dir = Path(os.getcwd()) / 'terraform'

    # Initialize the Terraform working directory
    if not tf_dir.exists():
        logging.info(f"Creating Terraform directory: {tf_dir}")
        tf_dir.mkdir(parents=True)

    return tf_dir

def apply_infra(tf_dir):
    try:
        # Initialize Terraform
        tf = Terraform(working_dir=str(tf_dir))

        # Apply the Terraform configuration
        logging.info("Applying Terraform configuration...")
        tf.apply()
    except Exception as e:
        logging.error(f"Failed to apply Terraform configuration: {str(e)}")

def destroy_infra(tf_dir):
    try:
        # Initialize Terraform
        tf = Terraform(working_dir=str(tf_dir))

        # Destroy the Terraform configuration
        logging.info("Destroying Terraform configuration...")
        tf.destroy()
    except Exception as e:
        logging.error(f"Failed to destroy Terraform configuration: {str(e)}")

def main():
    tf_dir = initialize_infra()

    # Parse command-line arguments
    if len(sys.argv) != 2:
        logging.error("Invalid command-line arguments. Usage: python main.py <apply|destroy>")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'apply':
        apply_infra(tf_dir)
    elif command == 'destroy':
        destroy_infra(tf_dir)
    else:
        logging.error(f"Invalid command: {command}. Usage: python main.py <apply|destroy>")

if __name__ == '__main__':
    main()