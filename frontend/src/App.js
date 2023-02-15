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


        axios.get('http://127.0.0.1:8000/api/users/').then(response => {
            this.setState(                                        // создаем состояние объекта
                {
                    'users': response.data

                }
                )
            }
            ).catch(error => console.log(error))
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
