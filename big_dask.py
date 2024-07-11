import argparse
import dask
import dask.array as da
import dask.bag as db
import dask.distributed
from sympy import factorint

# Function to read numbers from a file and return them as a Dask Bag
def read_numbers(file_path):
    with open(file_path, 'r') as f:
        numbers = f.readlines()
    numbers = [int(number.strip()) for number in numbers]
    return db.from_sequence(numbers, npartitions=10)

# Function to factorize a number
def factorize_number(number):
    return factorint(number)

# Function to process numbers (example task: factorization)
def process_numbers(numbers):
    return numbers.map(factorize_number)

# Main function to set up Dask, parse arguments, and run the application
def main(args):
    # Setup Dask client with threading support
    client = dask.distributed.Client(
        threads_per_worker=4,  # Adjusted to use more threads per worker
        n_workers=4,
        processes=False  # Ensure that we use threads, not processes
    )

    # Display the Dask dashboard URL
    print(f"Dask dashboard available at: {client.dashboard_link}")

    # Read numbers from the file
    numbers = read_numbers(args.file)
    
    # Process numbers (factorization in this case)
    result = process_numbers(numbers)
    
    # Compute the result and return it
    computed_result = result.compute(scheduler='threads')
    
    # Print the results
    for number, factors in zip(numbers.compute(), computed_result):
        print(f"Number: {number}, Factors: {factors}")
    
    # Keep the Dask client running to allow UI access
    client.close()

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process very large numbers from a file.")
    parser.add_argument("file", type=str, help="Path to the input .txt file containing large numbers.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Run the main funct
    main(args)
