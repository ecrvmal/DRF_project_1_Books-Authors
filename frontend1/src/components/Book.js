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
    return (
        <table>
           <tr>
                <th Book ID />
            </tr>
            <tr>
                <th Book name/>
            </tr>
            <tr>
                <th Authors/>
            </tr>

            {books.map((book) => <BookItem book={book} /> )}

        </table>
    )
}

export default BookList