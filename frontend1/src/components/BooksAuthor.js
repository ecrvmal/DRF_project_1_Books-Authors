import React from "react"
import {useParams} from "react-router-dom";


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


const BookListAuthors = ({books, authors}) => {    // for list of users
     console.log('BookAuthors.js')
    console.log(books)
        console.log(authors)
            let {id} = useParams()
    console.log(id)
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

export default BookListAuthors