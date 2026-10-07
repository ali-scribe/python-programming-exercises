# Python Mania

A collection of Python practice exercises and beginner projects I completed while following CodeWithHarry's 10-hour Python tutorial. The repository is organized by the chapter folders used for my exercises, with each script focusing on a small concept or problem.

## What I practiced

- Writing functions and using parameters, return values, and recursion
- Working with strings, lists, loops, conditionals, and user input
- Converting values and formatting output
- Reading, writing, copying, and appending to text files
- Handling exceptions with `try` / `except`
- Defining classes and using objects, inheritance, properties, static methods, and special methods
- Applying `filter()` and `reduce()` to collections
- Using Python's standard library and external packages in small projects

## Repository contents

| Folder | What's inside |
| --- | --- |
| `Chapter 8 PS` | Function practice: comparisons, temperature and unit conversions, recursion, patterns, and list/string operations |
| `Chapter 9 PS` | File-handling exercises: searching text, generating multiplication tables, updating a high score, replacing text, and copying files |
| `Chapter 10 PS` | Object-oriented programming exercises using classes such as `Programmer`, `Calculator`, and `Train` |
| `Chapter 11 PS` | Loop and pattern problems, factorial and multiplication tables, plus inheritance, properties, static methods, vectors, and operator overloading |
| `Chapter 12 PS` | Exception handling, list iteration with indexes, multiplication tables, and appending results to a file |
| `Chapter 13 PS` | Practice with input and output, string/list formatting, `filter()`, and `reduce()` |
| `Project 1` | A command-line Snake, Water, Gun game against the computer |
| `Project 2` | A number-guessing game with higher/lower hints and an attempt counter |
| `Mega Project 1 - Jarvis` | A voice-controlled assistant that responds to a wake word, opens websites and news, and looks up songs in a small music library |

## Running the scripts

Install Python 3, then run an individual script from its folder. For example, in PowerShell:

```powershell
cd "Project 1"
python main.py
```

To run another script, replace the folder and filename with the exercise you want to try. Some exercises read or write text files using relative paths, so run them from their own folder to ensure those files are found in the expected location. Several programs also prompt for input in the terminal.

### Running Jarvis

The Jarvis project uses `SpeechRecognition`, `pyttsx3`, and `PyAudio` in addition to Python's standard library. Install these dependencies in your Python environment, make a working microphone available, and ensure you have an internet connection for speech recognition. Then run `main.py` from the `Mega Project 1 - Jarvis` folder. The project currently does not include a dependency/requirements file.

## Notes

These are learning exercises and small projects, not a single installable application. Some scripts create or update local text files as part of their demonstrations.

The exercises are my practice work based on CodeWithHarry's Python tutorial; this repository is an independent learning project and is not affiliated with CodeWithHarry.
