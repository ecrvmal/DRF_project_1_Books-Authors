import React from "react"


const BookItem = ({book}) => {    // for single user

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
        </tr>
    )
}


const BookList = ({books}) => {    // for list of users
     console.log('Book.js')
    console.log(books)
    return (
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

            {books.map((book) => <BookItem book={book} /> )}

        </table>
    )
}

export default BookList