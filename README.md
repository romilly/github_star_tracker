# Auto-GPT GitHub Stats

Auto-GPT GitHub Stats is a Python script that retrieves the number of stars and forks of the
Significant-Gravitas/Auto-GPT project on GitHub using the GitHub API, and records the hourly values in a SQLite database.
It also provides a plotting functionality to visualize the stars and forks over time.

The code and most of the README were created by ChatGPT

## How it works

The script uses the GitHub API to retrieve the number of stars and forks of the Auto-GPT project every ten minutes,
and stores the values in a SQLite database.

The data is stored in a table called `stats`, with columns for the datetime, stars, and forks.

The plotting functionality uses the Matplotlib library to create a line chart of the stars and forks over time,
with separate y-axis labels for each value. The resulting plot can be saved as an SVG file.

### Requirements

1. Python 3
2. requests library (for interacting with the GitHub API)
3. matplotlib library (for plotting)
4. sqlite3 library (for database access)

## Installation

1. Clone the repository: `git clone https://github.com/romilly/github_star_tracker.git`
2. Navigate to the project directory: `cd Auto-GPT-GitHub-Stats`
3. Install the required libraries: `pip install -r requirements.txt`

## Usage

### Capturing GitHub Stats

To capture the GitHub stats, run the `capture.py` script from the command line.

```shell
python3 capture.py
```
The script will start capturing the number of stars and forks of the Auto-GPT project every ten minutes,
and store the values in a SQLite database called `github_stats.db`.
The script can be stopped at any time by pressing Ctrl-C.

### Plotting GitHub Stats

To plot the GitHub stats, run the `plot_to_svg.py` script from the command line:

```shell
python plot_to_svg.py
```
The script will retrieve the data from the github_stats.db database,
create a line chart of the stars and forks over time,
and save the resulting plot as an SVG file called stars.svg.

## Contributions

Contributions to this project are welcome.
If you find a bug or have a suggestion, please open an issue on GitHub.
If you would like to contribute code, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Credits

Thanks to OpenAI for creating ChatGPT and making it freely usable.