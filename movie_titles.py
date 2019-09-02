"""Handles the implementation of movie titles."""

import argparse
import requests
import sys
import typing


MOVIE_TITLE_URI = ('https://jsonmock.hackerrank.com/api/movies/search/?Title={}'
                   '&page={}')


def fetch_and_display_movie_titles(title: str) -> typing.List[str]:
    """Returns a sorted list of movie titles."""
    movie_titles = []
    current_page_number = 1
    max_page_number = -1
    while True:
        response = requests.get(
            MOVIE_TITLE_URI.format(title, current_page_number))
        if response.status != 200:
            break
        movie_titles_dict = response.json()
        movie_data_list = movie_titles_dict.get('data', [])
        if not movie_data_list:
            break
        movie_titles.extend([movie_dict.get('Title', '')
                             for movie_dict in movie_data_list])

        max_page_number = max(max_page_number,
                              movie_titles_dict.get('total_pages'))
        current_page_number += 1
        if current_page_number > max_page_number:
            break
    return sorted(movie_titles)


if __name__ == '__main__':  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument('--title',
                        help='Name of the movie to be searched',
                        required=True)
    arguments = parser.parse_args(sys.argv[1:])
    print(fetch_and_display_movie_titles(arguments.title))
