import React from "react"
import {Link} from "react-router-dom"


const BookItem = ({book, deleteBook}) => {    // for single user

    return (
        <tr>
            <td>
                {book.id}
            </td>
            <td>
                {book.name}
            </td>
            <td>
                {book.authors}
            </td>
            <td>
            <button onClick={()=> deleteBook(book.id)}type='button'>Delete</button>
            </td>
        </tr>
    )
}


const BookList = ({books, deleteBook}) => {    // for list of users
     console.log('Book.js')
    console.log(books)
    return (
        <div>
            <table>
               <th>
                    Book ID
                </th>
                <th>
                    Book name
                </th>
                <th>
                    Authors
                </th>

                {books.map((book) => <BookItem book={book} deleteBook={deleteBook} /> )}

            </table>

            {/* <Link to='/books/create'>Create</Link>   */}
                <a href='/books/create'>Create</a>

        </div>
    )
}

export default BookList