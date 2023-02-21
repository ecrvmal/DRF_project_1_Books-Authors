import React from 'react';
import axios from 'axios'
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'    // from User.js

class App extends React.Component {


    constructor(props)  {           //    constructor props - set settings
        super(props)                // re-define parent settings
        this.state = {              // state (variables)  of App component
        'users':[]
        }
    }

       componentDidMount(){                    // монтирует данные на нашу страницу
        const users = [                     // список словарей прилетит из backend
            {
            'first_name': "Fedor",
            'last_name' : "Dostoevskiy",
            "birthday_year" : 1821,
                },
            {
            'first_name': "Aleksander",
            'last_name' : "Grin",
            "birthday_year" : 1881,
                },
        ]                                  // получаем двнные, записываем в users

        this.setState(                                    // создаем состояние объекта
            {
                'users':users
            }
        )
    }

    render() {
        return (
            <div>
//            Main App

             < UserList users={this.state.users} />
            </div>
        );
    }
}

export default App;
