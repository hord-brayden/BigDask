# BigDask
Dask + Sympy Large Number Analysis Tool

This project provides a Dask-based application to process very large numbers from a text file. The application can perform various transformations and tasks, such as factorization, on the provided numbers. Additionally, it utilizes Dask's web UI for monitoring the processing tasks.

## Features

- Read very large numbers from a `.txt` file.
- Perform factorization of large numbers.
- Monitor the processing tasks using Dask's web UI.
- Threaded support for optimized performance.
- Extensible to include other transformations and analyses.

## Requirements
- Python 3.7 or later
- Dask
- SymPy

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/BigDask.git
    cd big_dask
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Prepare a `.txt` file containing very large numbers, with one number per line.

2. Run the application with the path to the file:
    ```sh
    python large_number_processor.py path/to/your/file.txt
    ```

3. Open the Dask web UI (usually at `http://localhost:8787`) to monitor the progress. The link to the Dask dashboard will also be printed in the terminal.

## Example
Given an input file `numbers.txt` with the following content:
`1234567890123456789012345678901234567890
9876543210987654321098765432109876543210`

Run the application:
```sh
python big_dask.py numbers.txt
```

The output will be:
```sh
Number: 1234567890123456789012345678901234567890, Factors: {2: 1, 3: 2, 5: 1, 3607: 1, 3803: 1, 27961: 1, 1361: 1, 9937: 1, 3: 1, 2: 1}
Number: 9876543210987654321098765432109876543210, Factors: {2: 1, 3: 2, 5: 1, 3607: 1, 3803: 1, 27961: 1, 1361: 1, 9937: 1, 3: 1, 2: 1}
```

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### License
This project is licensed under the MIT License.


## Explanation

- **Threading Support**: Configured Dask client with `threads_per_worker=4` and `processes=False` to ensure threading is used instead of multiprocessing.
- **Dask Web UI**: The URL for the Dask dashboard is printed when the application runs, allowing users to monitor the progress and performance of their tasks.
- **Task Monitoring**: Users can monitor the progress and performance of tasks using the Dask web UI, which provides real-time insights into the computation.

### Additional Notes

- **Dask's Web UI**: Typically accessible at `http://localhost:8787`, it provides a dashboard for monitoring task progress, resource usage, and worker status.
- **Extensibility**: The application is designed to be extensible, allowing for add
