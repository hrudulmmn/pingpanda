# PingPanda 🐼

<p align="center">
  <img src="img/url-status-checker-logo.png" alt="PingPanda logo" width="180">
</p>

<p align="center">
  <strong>A fast, friendly command-line URL status checker.</strong>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.10%2B-blue.svg" alt="Python 3.10+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License"></a>
</p>

PingPanda checks one URL or a list of URLs and groups the results by HTTP status class. It is a small command-line tool for developers, students, and anyone who wants a quick overview of whether a set of websites is reachable, redirecting, or returning an error.

PingPanda started as [Status Checker](https://github.com/BLACK-SCORP10/url-status-checker) by **BLACK-SCORP10** and was later enhanced by **matteocapricci**. The original authors are credited in the program banner and in the [LICENSE](LICENSE) file. The project is maintained for the **FOSSSoC-S1** contribution season.

## Preview

<p align="center">
  <img src="img/demo.png" alt="PingPanda checking a list of URLs in a terminal" width="720">
</p>

## Features

- Check a single URL or a list of URLs from a text file.
- Use asynchronous HTTP requests for list checks.
- Follow redirects and show the final destination.
- Display the HTTP status, response time, and resolved IP address for each URL.
- Organise results into status-class sections: 1xx, 2xx, 3xx, 4xx, 5xx, and invalid.
- Colour-coded terminal output with a progress bar for list runs.
- Save the report to a text file.
- Print a summary line at the end of every run.
- Simple command-line interface with built-in help.

## Tech Stack

| Area | Technology |
|---|---|
| Language | Python 3.10+ |
| HTTP client | httpx |
| Terminal output | colorama, tqdm |
| Command line | argparse |
| Testing | pytest, pytest-asyncio |
| Continuous integration | GitHub Actions |

## Project Structure

```text
url-status-checker.py    Entry point for the command-line tool
pingpanda/
├── __init__.py          Package exports
├── constants.py         Banner, colours, and status groups
├── models.py            Data model for a checked URL
├── network.py           URL preparation, address lookup, and checks
├── report.py            Grouping, formatting, and saving results
└── cli.py               Argument parsing and application flow
tests/                   Test suite (no external network access)
.github/                 CI workflow and issue/PR templates
img/                     Logo and demo image
```

## Prerequisites

- **Python 3.10 or newer**
- **pip**
- **Git** (to clone the repository)
- Network access to the URLs you want to check

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/PingPanda.git
   cd PingPanda
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Linux and macOS:

   ```bash
   source .venv/bin/activate
   ```

   Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install the runtime dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   For development and for running the test suite, install the development
   dependencies instead:

   ```bash
   pip install -r requirements-dev.txt
   ```

## Running the Application

Check a single URL:

```bash
python url-status-checker.py -d https://example.com
```

Check a list of URLs:

```bash
python url-status-checker.py -l urls.txt
```

Save the report to a file:

```bash
python url-status-checker.py -l urls.txt -o results.txt
```

Show the built-in help:

```bash
python url-status-checker.py --help
```

A list file contains one URL per line:

```text
https://example.com
https://github.com
https://python.org
```

### Command-line options

| Option | Description |
|---|---|
| `-d`, `--domain` | Check a single URL or domain |
| `-l`, `--list` | Check every URL in a text file, one per line |
| `-o`, `--output` | Save the report to a file |
| `-v`, `--version` | Show version information |
| `-h`, `--help` | Show the help text |

Provide one input source, either `-d` or `-l`, for each run.

### Report format

Every checked URL becomes one line of the report:

```text
[Status: 200] [Time: 123.456 ms] [IP: 93.184.216.34:443] https://example.com [Redirect: None]
```

| Field | Meaning |
|---|---|
| `Status` | HTTP status code of the response, or `Invalid` when the URL could not be reached |
| `Time` | Response time in milliseconds |
| `IP` | Resolved address and port of the host |
| `URL` | The URL that was checked |
| `Redirect` | Final URL and its address when the server redirected, `None` otherwise |

Results are grouped under headings such as `2XX`, `4XX`, and `INVALID`. The run
ends with a summary line:

```text
Checked: 3 | 1xx: 0 | 2xx: 2 | 3xx: 0 | 4xx: 1 | 5xx: 0 | Failed: 0
```

The `-o` option writes the report to a file without the colours.

### Periodic checks

On systems that provide the `watch` command, the tool can be run repeatedly:

```bash
watch -n 72000 python url-status-checker.py -l urls.txt
```

## Development

Run the whole test suite:

```bash
python -m pytest
```

Run a single test file or a single test:

```bash
python -m pytest tests/test_cli.py
python -m pytest tests/test_cli.py::test_version_option_prints_a_version
```

The suite does not use the public internet. HTTP responses are simulated, and a
temporary server on `localhost` is used where a real socket is needed.

## Contributing

Contributions of all sizes are welcome: bug reports, documentation
improvements, tests, and new features.

1. **Fork** the repository on GitHub.
2. **Clone your fork** and create a branch:

   ```bash
   git clone https://github.com/<your-username>/PingPanda.git
   cd PingPanda
   git checkout -b fix/short-description
   ```

3. **Make your change.** Keep the pull request focused on a single issue, and
   add or update tests when the behaviour changes.
4. **Commit** with a clear message:

   ```bash
   git add .
   git commit -m "Add a test for the report summary"
   ```

5. **Push** the branch and open a pull request against `main`. Link the issue
   it resolves in the pull request description.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for the full setup and review
workflow, and follow the [Code of Conduct](CODE_OF_CONDUCT.md). If you are new
to the project, look for issues labelled `good first issue`.

## Development Standards

- Follow the style of the existing code: 4 spaces, small functions, and clear
  names.
- Add a test for every bug fix and for new behaviour.
- Keep pull requests small and limited to one issue.
- Update the README when a change affects users.
- Do not commit local artifacts such as `.venv`, `__pycache__`, or report files.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file
for details.

## Acknowledgements

- **BLACK-SCORP10** for creating the original Status Checker.
- **matteocapricci** for the earlier enhancements.
- The FOSSSoC-S1 organisers and all contributors who help maintain PingPanda.
