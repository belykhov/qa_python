import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        'book_name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Мультфильмы'],
            ['Что делать, если ваш кот хочет вас убить', 'Ужасы']
        ]
    )
    def test_set_book_genre_add_two_books(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize(
        'book_name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Мультфильмы'],
        ]
    )
    def test_get_book_genre_get_one_book_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre_get_cartoon_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Унесенные призраками')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Унесенные призраками', 'Мультфильмы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert len(collector.get_books_with_specific_genre('Мультфильмы')) == 1

    @pytest.mark.parametrize(
        'book_name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Мультфильмы'],
            ['Что делать, если ваш кот хочет вас убить', 'Ужасы'],
            ['Унесенные призраками', 'Мультфильмы']
        ]
    )
    def test_get_books_genre_three_books(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_genre() == collector.books_genre

    def test_get_books_for_children_get_allowed_book(self):
        collector = BooksCollector()
        collector.add_new_book('Унесенные призраками')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Унесенные призраками', 'Мультфильмы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_book_genre((collector.get_books_for_children())[0]) in collector.genre

    def test_add_book_in_favorites_one_book(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert (collector.favorites[0]) == book_name

    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert collector.favorites == []

    def test_get_list_of_favorites_books_get_list(self):
        collector = BooksCollector()
        collector.add_new_book('Унесенные призраками')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Унесенные призраками')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_list_of_favorites_books()) == 2
