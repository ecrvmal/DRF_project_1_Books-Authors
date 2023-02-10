import React from "react"


const UserItem = ({user}) => {    // for single user

    return (
        <tr>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.birthday_year}
            </td>
        </tr>
    )
}


const UserList = ({users}) => {    // for list of users
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
            {users.map((user) => <UserItem user={user} /> )}

        </table>
    )
}

export default UserList

/*
                 users - iterable list object
                 map takes users from object one-by-one > user
                 we route the user to UserItem
                 for those objects from list where  user == user
                 (user) передается в функцию (user)
                 UserItem User - вызывает верхнюю функцию с параметром
*/

