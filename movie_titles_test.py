import movie_titles
import pytest
from unittest import mock


@pytest.fixture(scope='module')
def movie_response():
    yield \
        {'page': 1,
         'per_page': 13,
         'total': 13,
         'total_pages': 1,
         'data': [
             {'Title': 'Italian Spiderman', 'Year': 2007,
              'imdbID': 'tt2705436'},
             {'Title': 'Superman, Spiderman or Batman', 'Year': 2011,
              'imdbID': 'tt2084949'},
             {'Title': 'Spiderman', 'Year': 1990, 'imdbID': 'tt0100669'},
             {'Title': 'Spiderman', 'Year': 2010, 'imdbID': 'tt1785572'},
             {'Title': ('Fighting, Flying and Driving: The Stunts of '
                        'Spiderman 3'),
              'Year': 2007, 'imdbID': 'tt1132238'},
             {'Title': 'Spiderman and Grandma', 'Year': 2009,
              'imdbID': 'tt1433184'},
             {'Title': 'The Amazing Spiderman T4 Premiere Special',
              'Year': 2012, 'imdbID': 'tt2233044'},
             {'Title': 'Amazing Spiderman Syndrome', 'Year': 2012,
              'imdbID': 'tt2586634'},
             {'Title': "Hollywood's Master Storytellers: Spiderman Live",
              'Year': 2006, 'imdbID': 'tt2158533'},
             {'Title': 'Spiderman 5', 'Year': 2008, 'imdbID': 'tt3696826'},
             {'Title': 'They Call Me Spiderman', 'Year': 2016,
              'imdbID': 'tt5861236'},
             {'Title': 'The Death of Spiderman', 'Year': 2015,
              'imdbID': 'tt5921428'},
             {'Title': 'Spiderman in Cannes', 'Year': 2016,
              'imdbID': 'tt5978586'}
          ]
         }


@pytest.fixture(scope='module')
def empty_response():
    yield \
        {'page': 1,
         'per_page': 10,
         'total': 10,
         'total_pages': 1,
         'data': []}


def test_fetch_and_display_movie_titles__success(movie_response: dict):
    response_mock = mock.Mock()
    response_mock.status = 200
    response_mock.json = mock.MagicMock(return_value=movie_response)
    with mock.patch('requests.get', return_value=response_mock) as mock_request:
        expected = [
            'Amazing Spiderman Syndrome',
            'Fighting, Flying and Driving: The Stunts of Spiderman 3',
            'Hollywood\'s Master Storytellers: Spiderman Live',
            'Italian Spiderman', 'Spiderman', 'Spiderman', 'Spiderman 5',
            'Spiderman and Grandma', 'Spiderman in Cannes',
            'Superman, Spiderman or Batman',
            'The Amazing Spiderman T4 Premiere Special',
            'The Death of Spiderman', 'They Call Me Spiderman']
        actual = movie_titles.fetch_and_display_movie_titles('Spiderman')
        assert expected == actual
        assert mock_request.call_count == 1


def test_fetch_and_display_movie_titles__error_status():
    response_mock = mock.Mock()
    response_mock.status = 400
    with mock.patch('requests.get', return_value=response_mock) as mock_request:
        assert movie_titles.fetch_and_display_movie_titles('Spiderman') == []
        assert mock_request.call_count == 1


def test_fetch_and_display_movie_titles__empty_response(empty_response: dict):
    response_mock = mock.Mock()
    response_mock.status = 200
    response_mock.json = mock.MagicMock(return_value=empty_response)
    with mock.patch('requests.get', return_value=response_mock) as mock_request:
        assert movie_titles.fetch_and_display_movie_titles('Spiderman') == []
        assert mock_request.call_count == 1
