import React from "react"
import {Link} from "react-router-dom";


const AuthorItem = ({author}) => {    // for single user

    return (
        <tr>
            <td>
             {/*   {author.first_name}  */}
             <Link to={`/author/${author.id}`}> {author.first_name}</Link>
            </td>
            <td>
                {author.last_name}
            </td>
            <td>
                {author.birthday_year}
            </td>
        </tr>
    )
}


const AuthorList = ({authors}) => {    // for list of users
    return (
        <table>
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                Birthday year
            </th>
            {authors.map((author) => <AuthorItem author={author} /> )}

        </table>
    )
}

export default AuthorList