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

/*
                 users - iterable list object
                 map takes users from object one-by-one > user
                 we route the user to UserItem
                 for those objects from list where  user == user
                 (user) передается в функцию (user)
                 UserItem User - вызывает верхнюю функцию с параметром
*/

