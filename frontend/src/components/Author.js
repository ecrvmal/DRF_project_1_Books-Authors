import React from "react"


const AuthorItem = ({author}) => {    // for single user

    return (
        <tr>
            <td>
                {author.first_name}
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
            <tr>
                <th First name />
            </tr>
            <tr>
                <th Last name />
            </tr>
            <tr>
                <th Birthday year />
            </tr>
            {authors.map((author) => <AuthorItem author={author} /> )}

        </table>
    )
}

export default AuthorList