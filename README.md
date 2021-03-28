# Viewing Party

# Skills Assessed

Solving problems with...

- Conditional logic
- Lists
- Dictionaries
- Nested loops
- Nested data structures

# Goal

You and your friends enjoy watching things together online. Of course, everyone has seen different things, has different favorites, and different things they want to watch.

You've been using a spreadsheet to compare everyone's watched list, favorites list, and watchlist, but it's been getting too cumbersome. In order to find things you've watched and your friends haven't watched, or things that your friends have watched and yo haven't watched, you have to comb through the spreadsheet. You know that there are different ways we can get that information: we can use Python!

For this project, you will be given some data structure that represents the things you've watched, favorited, and want to watch. The directions below will lead you to create a series of functions. These functions will modify the data, and implement features like adding and removing things between different lists. Other features include creating recommendations!

# One-Time Project Setup

Follow these directions once, a the beginning of your project:

1. Navigate to your projects folder named `projects`

```bash
$ cd ~/Developer/projects
```

2. In Github click on the "Fork" button in github and fork the repository to your Github account.  This will make a copy of the project in your github account.

![Fork Button](images/fork.png)

3. "Clone" (download a copy of this project) into your projects folder. This command makes a new folder called `viewing-party`, and then puts the project into this new folder.  Make sure you are cloning from your copy of the project and not the class version (ada-cX).

```bash
$ git clone ...
```

Use `ls` to confirm there's a new project folder

4. Move your location into this project folder

```bash
$ cd viewing-party
```

5. Create a virtual environment named `venv` for this project:

```bash
$ python3 - m venv venv
```

6. Activate this environment:

```bash
$ source venv/bin/activate
```

Verify that you're in a python3 virtual environment by running:

- `$ python - -version` should output a Python 3 version
- `$ pip - -version` should output that it is working with Python 3

6. Install dependencies once at the beginning of this project with

```bash
# Must be in activated virtual environment
$ pip install - r requirements.txt
```

Summary of one-time project setup:

- [] `cd` into your `projects` folder
- [] Clone the project onto your machine
- [] `cd` into the `viewing-party` folder
- [] Create the virtual environment `venv`
- [] Activate the virtual environment `venv`
- [] Install the dependencies with `pip`

# Project Development Workflow

1. When you want to begin work on this project, ensure that your virtual environment is activated:

```bash
$ source venv/bin/activate
```

2. Find the test file that contains the test you want to run. Ensure that the test(s) you want to run isn't skipped.

   - Check the `tests` folder, and find the test file you want to run
    - In that test file, read through each test case
    - Remove all lines that contain `@ pytest.mark.skip()`

3. Run the tests!

```bash
# Must be in activated virtual environment
$ pytest
```

4. Focus on the top test failure. Read through the test failure, and understand why the failure is happening. Confirm your findings with a classmate.

5. Make a plan to fix the test failure.

6. Write code to fix the test failure.

7. Re-run the tests.

8. Repeat steps 5-7 until that test passes!

9. Repeats steps 4-8 until you have finished all tests in the file.

10. Begin using the test file of the next wave!

11. When you are finished working for the day, deactivate your environment with deactivate or closing the Terminal tab/window

```bash
$ deactivate
```

# Details About How to Run Tests

Run all unskipped tests that exist in this project with:

```bash
# Must be in activated virtual environment
$ pytest
```

If you want to see any `print` statements print to the console, add `- s` to the end of any `pytest` command:

```bash
# Must be in activated virtual environment
$ pytest - s
```

If you want to run all unskipped tests that exist in one file, use:

```bash
# Must be in activated virtual environment
$ pytest tests/test_file_name.py
```

... where `test_file_name.py` is replaced with the correct test file name.

# Project Write-Up: How to Complete and Submit

The goal of this project is to write code in `main.py` so that as many of the tests pass as possible.

To complete this project, use the above workflow and follow these steps:

1. Start with making the tests in `test_wave_01.py` pass.
1. Review your code in `main.py` and see if there are ways you can make the code more readable.
1. Then, work on making the tests in `test_wave_02.py` pass.
1. Review your code in `main.py`
1. Repeat on all test files until submission time.

At submission time, no matter where you are, submit the project via Learn.

# Project Directions

This project is designed such that one could puzzle together how to implement this project without many directions. Being able to read tests to understand what is expected of our program is a skill that needs to be developed
programmers often take years to develop this skill competently.

When our test failures leave us confused and stuck, let's use the detailed project requirements below.

# Wave 1

1. The first four tests are about a `create_movie()` function.

In `main.py`, there should be a function named `create_movie`. This function should...

- take three parameters: `title`, `genre`, `rating`
- If those there attributes are truthy, then return a dictionary. This dictionary should...
   - Have three key-value pairs, with specific keys
    - The three keys should be `"title"`, `"genre"`, and `"rating"`
    - The values of these key-value pairs should be appropriate values
- If `title` is falsy, `genre` is falsy, or `rating` is falsy, this function should return `None`

2. The next test is about a `add_to_watched()` function.

In `main.py`, there should be a function named `add_to_watched`. This function should...

- take two parameters: `user_data`, `movie`
   - the value of `user_data` will be a dictionary with a key `"watched"`, and a value `[]`
       - This represents that the user has no movies in their watched list
    - the value of `movie` will be a dictionary in this format:
        - ```python
           {
                "title": "Title A",
              "genre": "Horror",
              "rating": 3.5
            }
            ```
- add the `movie` to the `"watched"` list inside of `user_data`
- return the `user_data`

3. The next test is about a `add_to_watchlist()` function.

In `main.py`, there should be a function named `add_to_watchlist`. This function should...

- take two parameters: `user_data`, `movie`
   - the value of `user_data` will be a dictionary with a key `"watchlist"`, and a value `[]`
       - This represents that the user has no movies in their watchlist
    - the value of `movie` will be a dictionary in this format:
        - ```python
           {
                "title": "Title A",
              "genre": "Horror",
              "rating": 3.5
            }
            ```
- add the `movie` to the `"watchlist"` list inside of `user_data`
- return the `user_data`

4. There are three tests about a `watch_movie()` function.

In `main.py`, there should be a function named `watch_movie`. This function should...

- take two parameters: `user_data`, `title`
   - the value of `user_data` will be a dictionary with a `"watchlist"` and a `"watched"`
       - This represents that the user has a watchlist and a list of watched movies
    - the value of `title` will be a string
       - This represents the title of the movie the user has watched
- If the title is in a movie in the user's watchlist:
    - remove that movie from the watchlist
    - add that movie to watched
    - return the `user_data`
- If the title is not a movie in the user's watchlist:
    - return the `user_data`

# Wave 2

1. The first two tests are about a `get_watched_avg_rating()` function.

In `main.py`, there should be a function named `get_watched_avg_rating`. This function should...

- take one parameter: `user_data`
   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries
       - This represents that the user has a list of watched movies
- Calculate the average rating of all movies in the watched list
   - The average rating of an empty watched list is `0.0`
- return the average rating

2. The next two tests are about a `get_most_watched_genre()` function.

In `main.py`, there should be a function named `get_most_watched_genre`. This function should...

- take one parameter: `user_data`
   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries. Each movie dictionary has a key `"genre"`.
       - This represents that the user has a list of watched movies. Each watched movie has a genre.
        - The values of `"genre"` is a string.
- Determine which genre is most frequently occurring in the watched list
- return the genre that is the most frequently watched

# Wave 3

1. The first two tests are about a `get_unique_watched()` function.

In `main.py`, there should be a function named `get_unique_watched`. This function should...

- take one parameter: `user_data`
   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
       - This represents that the user has a list of watched movies and a list of friends
        - The value of `"friends"` is a list
        - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
        - Each movie dictionary has a `"title"`.
- Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
- Return a list of dictionaries, that represents a list of movies

2. The next three tests are about a `get_friends_unique_watched()` function.

In `main.py`, there should be a function named `get_friends_unique_watched`. This function should...

- take one parameter: `user_data`
   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
       - This represents that the user has a list of watched movies and a list of friends
        - The value of `"friends"` is a list
        - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
        - Each movie dictionary has a `"title"`.
- Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
- Return a list of dictionaries, that represents a list of movies

# Wave 4

1. There are two tests about a `get_available_recs` function

Create a function named `get_available_recs`

- takes one parameter: `user_data`
   - `user_data` will have a field `"subscriptions"`. The value of `"subscriptions"` is a list of strings
       - This represents the names of streaming services that the user has access to
        - each friend in `"friends"` has a watched list. Each movie in the watched list has a `"host"`, which a string that says what streaming service it's hosted on
- Determine a list of recommended movies. A movie should be added to this list if and only if:
    - The user has not watched it
    - At least one of the user's friends has watched
    - The `"host"` of the movie is a service that is in the user's `"subscriptions"`
- Return the list of recommended movies

# Wave 5

1. There are four tests about a `get_new_rec_by_genre` function

Create a function named `get_new_rec_by_genre`

- takes one parameter: `user_data`
- Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
    - The user has not watched it
    - At least one of the user's friends has watched
    - The `"genre"` of the movie is the same as the user's most frequent genre
- Return the list of recommended movies

1. There is also one test about a `get_rec_from_favorites` function

Create a function named `get_rec_from_favorites`

- takes one parameter: `user_data`
   - `user_data` will have a field `"favorites"`. The value of `"favorites"` is a list of movie dictionaries
       - This represents the user's favorite movies
- Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
    - The movie is in the user's `"favorites"`
    - None of the user's friends have watched it
- Return the list of recommended movies
